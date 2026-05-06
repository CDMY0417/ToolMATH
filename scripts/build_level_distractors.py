#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_level_distractors.py
--------------------------
Build 100 distractor functions per difficulty level (1..5) for every problem,
using a ToolMATH-format JSON file as the global tool pool.

Defaults are relative to the public repository layout:
  --tool-json       data/ToolMATH.json
  --split           train  (HuggingFace 'qwedsacf/competition_math' for category/type)
Output:
  --out             data/distractors_by_level.json
Embeddings cache (optional):
  --emb-cache       data/emb_cache.jsonl

Levels:
  L1: random from pool EXCLUDING same-category
  L2: pure random from pool
  L3: random from pool ONLY same-category
  L4: rank by OpenAI embeddings (max cosine vs any gold tool) → top 100
  L5: rank by keyword overlap desc, then L4 similarity desc → top 100

Notes:
- Pool = filtered gold tools (across all problems).
- For each problem, we exclude that problem’s own tools from the candidate pool.
- Sequences are length 100. If a candidate pool is small, we sample/cycle with replacement.
- Reproducible randomness (seed=42).
"""

from __future__ import annotations
import argparse, json, math, os, re, hashlib, random, sys, tempfile
from pathlib import Path
from typing import Dict, List, Tuple, Optional

from datasets import load_dataset
from openai import OpenAI

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"

# ────────────────────────────── CLI & defaults ──────────────────────────────

DEF_TOOL_JSON = DATA_DIR / "ToolMATH.json"
DEF_OUT       = DATA_DIR / "distractors_by_level.json"
DEF_EMB_CACHE = DATA_DIR / "emb_cache.jsonl"

HF_DATASET = "qwedsacf/competition_math"
EMB_MODEL  = "text-embedding-3-large"
RAND_SEED  = 42

ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
ap.add_argument("--tool-json", "--filtered-tools", dest="tool_json", default=DEF_TOOL_JSON, type=Path,
                help="ToolMATH-format JSON file used both as the gold set and the distractor pool.")
ap.add_argument("--split", default="train", help="HF split to read 'type' (category).")
ap.add_argument("--out",   default=DEF_OUT, type=Path, help="Output JSON file.")
ap.add_argument("--emb-cache", default=DEF_EMB_CACHE, type=Path, help="Embedding cache JSONL.")
ap.add_argument("--max-problems", type=int, default=None, help="Optional cap for quick tests.")
ap.add_argument("--keywords-extra", type=str, default="", help="Comma-separated extra keywords for L5.")
ap.add_argument("--checkpoint-every", type=int, default=25,
                help="Write checkpoint to --out every N newly processed problems.")
ap.add_argument("--resume", action="store_true", default=True,
                help="Resume from existing --out JSON if present.")
ap.add_argument("--no-resume", dest="resume", action="store_false",
                help="Ignore existing --out and rebuild from scratch.")
ap.add_argument("--out-alias", type=Path, default=None,
                help="Optional secondary JSON path updated together with --out at each checkpoint.")
args = ap.parse_args()

rand = random.Random(RAND_SEED)
client = OpenAI()  # uses $OPENAI_API_KEY

# ────────────────────────────── helpers: normalize ───────────────────────────

_WS_RE = re.compile(r"\s+")
WORD_RE = re.compile(r"[a-zA-Z]+")

def norm_text(s: str) -> str:
    return _WS_RE.sub(" ", (s or "")).strip()

def tool_uid(t: dict) -> str:
    key = (t.get("name","") + "||" + t.get("description","") + "||" + str(t.get("function","")))
    return hashlib.sha1(key.encode("utf-8")).hexdigest()

def text_for_embed(t: dict) -> str:
    return f"{t.get('name','')}\n{t.get('description','')}"

# ────────────────────────────── load dataset/type ────────────────────────────

print("⤵  Loading MATH dataset (for 'type' categories)…", file=sys.stderr)
ds = load_dataset(HF_DATASET, split=args.split)
PROB_TYPE: Dict[str, str] = {norm_text(r.get("problem","")): (r.get("type") or "Unknown")
                             for r in ds}

# ────────────────────────────── load filtered tools ──────────────────────────

print("⤵  Loading tool JSON (also used as distractor pool)…", file=sys.stderr)
FILTERED_TOOLS: List[dict] = json.loads(args.tool_json.read_text(encoding="utf-8"))

# Group gold-by-problem from filtered set (these are the gold tools per problem)
GOLD_BY_PROB: Dict[str, List[dict]] = {}
for t in FILTERED_TOOLS:
    sp = norm_text(t.get("source_problem",""))
    GOLD_BY_PROB.setdefault(sp, []).append(t)

# Map problem → category for tools
def tool_category(t: dict) -> str:
    return PROB_TYPE.get(norm_text(t.get("source_problem","")), "Unknown")

# ────────────────────────────── keywords for L5 ─────────────────────────────

BASE_KEYWORDS = {
    "divisor","factor","prime","composite","gcd","lcm","mod","modulo","remainder","congruent",
    "polynomial","root","zero","factorization","equation","system","inequality",
    "line","slope","intercept","midpoint","distance","circle","radius","diameter","area","perimeter",
    "triangle","angle","quadrilateral","polygon","similar","congruent","parallel","perpendicular",
    "probability","combinatorics","binomial","permutation","combination","expected","variance",
    "sequence","series","sum","product","fraction","ratio","proportion",
    "matrix","determinant","eigenvalue","vector","dot","cross",
    "log","exponential","power","square","cube","root","radical",
    "diophantine","integral","derivative","limit",
}
if args.keywords_extra:
    for k in args.keywords_extra.split(","):
        k = k.strip().lower()
        if k:
            BASE_KEYWORDS.add(k)

def extract_keywords(t: dict) -> set:
    text = f"{t.get('name','')} {t.get('description','')}".lower()
    toks = WORD_RE.findall(text)
    return {w for w in toks if w in BASE_KEYWORDS}

# ────────────────────────────── embedding cache ──────────────────────────────

def load_emb_cache(path: Path) -> Dict[str, List[float]]:
    cache = {}
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                if not line: continue
                try:
                    obj = json.loads(line)
                    cache[obj["id"]] = obj["vec"]
                except Exception:
                    pass
    return cache

def append_to_cache(path: Path, items: List[Tuple[str, List[float]]]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        for tid, vec in items:
            f.write(json.dumps({"id": tid, "vec": vec}) + "\n")

EMB_CACHE: Dict[str, List[float]] = load_emb_cache(args.emb_cache)

def embed_texts(ids: List[str], texts: List[str]) -> Dict[str, List[float]]:
    out: Dict[str, List[float]] = {}
    need_ids, need_texts = [], []
    for tid, tx in zip(ids, texts):
        if tid in EMB_CACHE:
            out[tid] = EMB_CACHE[tid]
        else:
            need_ids.append(tid); need_texts.append(tx)
    # batch misses
    BATCH = 128
    new_entries: List[Tuple[str, List[float]]] = []
    for i in range(0, len(need_texts), BATCH):
        chunk_ids  = need_ids[i:i+BATCH]
        chunk_text = need_texts[i:i+BATCH]
        if not chunk_text: continue
        resp = client.embeddings.create(model=EMB_MODEL, input=chunk_text)
        for cid, ed in zip(chunk_ids, resp.data):
            v = ed.embedding
            out[cid] = v
            EMB_CACHE[cid] = v
            new_entries.append((cid, v))
    if new_entries:
        append_to_cache(args.emb_cache, new_entries)
    return out

def vnorm(v: List[float]) -> List[float]:
    s = math.sqrt(sum(x*x for x in v)) or 1.0
    return [x/s for x in v]

def cos(a: List[float], b: List[float]) -> float:
    return float(sum(x*y for x,y in zip(a,b)))

def write_json_atomic(path: Path, payload: List[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", dir=str(path.parent), prefix=path.name + ".", suffix=".tmp", delete=False, encoding="utf-8") as tf:
        tmp = Path(tf.name)
        json.dump(payload, tf, indent=2)
    os.replace(tmp, path)

def checkpoint_write(records_by_problem: Dict[str, dict], ordered_problems: List[str], out_path: Path, out_alias: Optional[Path]) -> int:
    payload = [records_by_problem[p] for p in ordered_problems if p in records_by_problem]
    write_json_atomic(out_path, payload)
    if out_alias:
        write_json_atomic(out_alias, payload)
    return len(payload)

# ────────────────────────────── pool helpers ────────────────────────────────

# Build pool index by problem (from filtered tools)
POOL_BY_PROB: Dict[str, List[dict]] = {}
for t in FILTERED_TOOLS:
    POOL_BY_PROB.setdefault(norm_text(t.get("source_problem","")), []).append(t)

POOL_FLAT = list(FILTERED_TOOLS)

def pool_excluding_problem(problem_text: str) -> List[dict]:
    pnorm = norm_text(problem_text)
    excl = set(tool_uid(t) for t in POOL_BY_PROB.get(pnorm, []))
    return [t for t in POOL_FLAT if tool_uid(t) not in excl]

def pool_same_category(problem_text: str) -> List[dict]:
    cat = PROB_TYPE.get(norm_text(problem_text), "Unknown")
    pnorm = norm_text(problem_text)
    return [t for t in POOL_FLAT
            if tool_category(t) == cat and norm_text(t.get("source_problem","")) != pnorm]

def pool_diff_category(problem_text: str) -> List[dict]:
    cat = PROB_TYPE.get(norm_text(problem_text), "Unknown")
    pnorm = norm_text(problem_text)
    return [t for t in POOL_FLAT
            if tool_category(t) != cat and norm_text(t.get("source_problem","")) != pnorm]

# ────────────────────────────── sampling helpers ────────────────────────────

def sample_sequence(pool: List[dict], n: int, fallback: Optional[List[dict]] = None) -> List[dict]:
    """
    Return a sequence of length n.
      - If pool has >= n → sample without replacement.
      - Else → sample with replacement.
      - If pool is empty and fallback is provided → sample from fallback.
      - If both empty → return [].
    """
    src = pool if pool else (fallback or [])
    if not src:
        return []
    if len(src) >= n:
        return rand.sample(src, n)
    seq = list(src)
    while len(seq) < n:
        seq.append(rand.choice(src))
    return seq[:n]

def cycle_to_n(lst: List[dict], n: int, fallback: Optional[List[dict]] = None) -> List[dict]:
    """Cycle a ranked list to reach length n; fallback if empty."""
    if not lst:
        return sample_sequence(fallback or [], n)
    out, i = [], 0
    while len(out) < n:
        out.append(lst[i % len(lst)])
        i += 1
    return out[:n]

# ────────────────────────────── main loop ───────────────────────────────────

problems = list(GOLD_BY_PROB.keys())
if args.max_problems:
    problems = problems[:args.max_problems]

records_by_problem: Dict[str, dict] = {}
if args.resume and args.out.exists():
    try:
        existing = json.loads(args.out.read_text(encoding="utf-8"))
        if isinstance(existing, list):
            for rec in existing:
                p = norm_text(rec.get("problem", ""))
                if p:
                    records_by_problem[p] = rec
            print(f"↻ Resume enabled: loaded {len(records_by_problem)} existing records from {args.out}", file=sys.stderr)
    except Exception as e:
        print(f"⚠ Failed to read existing --out for resume ({e}); starting fresh.", file=sys.stderr)

print(f"🔧 Building 5×100 distractors for {len(problems)} problems…", file=sys.stderr)
if records_by_problem:
    print(f"⏩ Skipping {sum(1 for p in problems if p in records_by_problem)}/{len(problems)} already-completed problems", file=sys.stderr)

processed_new = 0
for i, prob_text in enumerate(problems, 1):
    if prob_text in records_by_problem:
        if i % 25 == 0:
            print(f"  …{i}/{len(problems)} (resumed skip)", file=sys.stderr)
        continue

    gold_tools = GOLD_BY_PROB[prob_text]
    cat = PROB_TYPE.get(prob_text, "Unknown")

    # Candidate pools (all from FILTERED_TOOLS, excluding current problem's tools)
    pool_all_excl = pool_excluding_problem(prob_text)
    pool_same      = pool_same_category(prob_text)
    pool_diff      = pool_diff_category(prob_text)

    # Levels 1–3 (ensure length=100 with fallback to pool_all_excl)
    L1 = sample_sequence(pool_diff, 100, fallback=pool_all_excl)   # exclude same-category
    L2 = sample_sequence(pool_all_excl, 100)                       # pure random
    L3 = sample_sequence(pool_same, 100, fallback=pool_all_excl)   # same-category only

    # Embeddings for L4/L5
    gold_ids   = [f"G::{tool_uid(t)}" for t in gold_tools]
    gold_texts = [text_for_embed(t)     for t in gold_tools]
    gold_emb_map = embed_texts(gold_ids, gold_texts)
    gold_vecs  = [vnorm(gold_emb_map[gid]) for gid in gold_ids]

    cand_ids   = [f"C::{tool_uid(t)}" for t in pool_all_excl]
    cand_texts = [text_for_embed(t) for t in pool_all_excl]
    cand_vecs_map = embed_texts(cand_ids, cand_texts)

    # L4 ranking: max similarity vs any gold vector
    sims = []
    for t, cid in zip(pool_all_excl, cand_ids):
        v = vnorm(cand_vecs_map[cid])
        smax = max((cos(v, g) for g in gold_vecs), default=0.0)
        sims.append((smax, t))
    sims.sort(key=lambda x: x[0], reverse=True)
    L4_ranked = [t for _, t in sims]
    L4 = cycle_to_n(L4_ranked, 100, fallback=pool_all_excl)

    # L5 ranking: keyword-overlap DESC, then L4 similarity DESC
    gold_kw_union = set()
    for gt in gold_tools:
        gold_kw_union |= extract_keywords(gt)
    L5_pairs = []
    for (smax, t) in sims:
        overlap = len(gold_kw_union & extract_keywords(t))
        L5_pairs.append((overlap, smax, t))
    L5_pairs.sort(key=lambda x: (x[0], x[1]), reverse=True)
    L5_ranked = [t for _,__,t in L5_pairs]
    L5 = cycle_to_n(L5_ranked, 100, fallback=pool_all_excl)

    rec = {
        "problem": prob_text,
        "type": cat,
        "gold_tools": gold_tools,
        "distractors": {
            "level1": L1,
            "level2": L2,
            "level3": L3,
            "level4": L4,
            "level5": L5
        }
    }
    records_by_problem[prob_text] = rec
    processed_new += 1

    if args.checkpoint_every > 0 and (processed_new % args.checkpoint_every == 0):
        written = checkpoint_write(records_by_problem, problems, args.out, args.out_alias)
        print(f"💾 Checkpointed {written} records to {args.out}", file=sys.stderr)
        if args.out_alias:
            print(f"💾 Updated alias: {args.out_alias}", file=sys.stderr)

    if i % 25 == 0:
        print(f"  …{i}/{len(problems)}", file=sys.stderr)

# ────────────────────────────── write output ────────────────────────────────

args.out.parent.mkdir(parents=True, exist_ok=True)
total_written = checkpoint_write(records_by_problem, problems, args.out, args.out_alias)
print(f"✅ Wrote {total_written} problems × 5 levels → {args.out}")
if args.out_alias:
    print(f"✅ Updated alias → {args.out_alias}")
