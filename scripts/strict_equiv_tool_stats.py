#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
strict_equiv_tool_stats.py
--------------------------
Estimate, for each ToolMATH gold tool, how many other tools are strictly
equivalent distractors.

This script is repo-relative and can be used for either ToolMATH or ToolMATHHard
by changing --tool-json and --tools-dir.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import os
import random
import re
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import numpy as np
from openai import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    NotFoundError,
    OpenAI,
    PermissionDeniedError,
    RateLimitError,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"

DEFAULT_TOOL_JSON = DATA_DIR / "ToolMATH.json"
DEFAULT_TOOLS_DIR = DATA_DIR / "function_ToolMATH"
DEFAULT_OUT_JSON = DATA_DIR / "strict_equiv_tool_stats.json"
DEFAULT_OUT_CSV = DATA_DIR / "strict_equiv_tool_stats.csv"
DEFAULT_EMB_CACHE = DATA_DIR / "strict_equiv_tool_stats_emb_cache.jsonl"
DEFAULT_PAIR_CACHE = DATA_DIR / "strict_equiv_tool_stats_pair_cache.jsonl"
EMB_MODEL = "text-embedding-3-large"

SYS_JUDGE = (
    "You are a strict tool-equivalence judge. "
    "Return YES only if Tool A and Tool B are strictly the same tool in meaning. "
    "Strictly the same means all of the following hold: "
    "(1) they implement the same mathematical operation / behavior, "
    "(2) their input type signatures are the same up to parameter renaming and parameter order changes, "
    "(3) their output type is the same, and "
    "(4) for corresponding valid inputs they produce the same kind of result. "
    "Different formulas, different tasks, different return kinds, or different input type requirements mean NO. "
    "Parameter order may differ and still be YES. "
    "Respond with ONLY YES or NO."
)

WORD_RE = re.compile(r"\s+")


def normalize_ws(s: str) -> str:
    return WORD_RE.sub(" ", s or "").strip()


def tool_uid(t: Dict[str, Any]) -> str:
    raw = "||".join([
        t.get("name", ""),
        t.get("description", ""),
        json.dumps(t.get("inputs", {}), sort_keys=True),
        t.get("function", ""),
    ])
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def sleep_with_jitter(base: float, attempt: int) -> None:
    delay = base * (2 ** attempt) * (0.75 + random.random() * 0.5)
    time.sleep(min(delay, 8.0))


def safe_chat(client: OpenAI, *, model: str, messages: List[dict], temperature: Optional[float], max_retries: int, backoff: float):
    for attempt in range(max_retries + 1):
        try:
            req: Dict[str, Any] = {"model": model, "messages": messages}
            if temperature is not None:
                req["temperature"] = temperature
            return client.chat.completions.create(**req)
        except (RateLimitError, APIConnectionError, APITimeoutError, APIError):
            if attempt >= max_retries:
                return None
            sleep_with_jitter(backoff, attempt)
        except (BadRequestError, AuthenticationError, PermissionDeniedError, NotFoundError):
            return None
        except Exception:
            if attempt >= max_retries:
                return None
            sleep_with_jitter(backoff, attempt)


def safe_embed(client: OpenAI, *, model: str, texts: List[str], max_retries: int, backoff: float):
    for attempt in range(max_retries + 1):
        try:
            return client.embeddings.create(model=model, input=texts)
        except (RateLimitError, APIConnectionError, APITimeoutError, APIError):
            if attempt >= max_retries:
                return None
            sleep_with_jitter(backoff, attempt)
        except (BadRequestError, AuthenticationError, PermissionDeniedError, NotFoundError):
            return None
        except Exception:
            if attempt >= max_retries:
                return None
            sleep_with_jitter(backoff, attempt)


def extract_return_annotation(py_path: Path, fn_name: str) -> str:
    try:
        src = py_path.read_text(encoding="utf-8")
        tree = ast.parse(src, filename=str(py_path))
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name == fn_name:
                if node.returns is None:
                    return "<missing>"
                try:
                    return ast.unparse(node.returns)
                except Exception:
                    return "<annotated>"
    except Exception:
        return "<parse_error>"
    return "<missing>"


def canonical_input_signature(inputs: Dict[str, Any]) -> Tuple[str, ...]:
    return tuple(sorted(str(v) for v in (inputs or {}).values()))


def block_key(tool: Dict[str, Any]) -> Tuple[Tuple[str, ...], str]:
    return canonical_input_signature(tool.get("inputs", {})), tool.get("_return_type", "<missing>")


def embedding_text(tool: Dict[str, Any]) -> str:
    sig = ", ".join(canonical_input_signature(tool.get("inputs", {})))
    return "\n".join([
        f"name: {tool.get('name', '')}",
        f"description: {normalize_ws(tool.get('description', ''))}",
        f"input_types: [{sig}]",
        f"return_type: {tool.get('_return_type', '<missing>')}",
    ])


def load_jsonl_cache(path: Path) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    if not path.exists():
        return out
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            key = obj.get("id")
            if key:
                out[key] = obj
    return out


def append_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def pair_id(uid_a: str, uid_b: str) -> str:
    a, b = sorted([uid_a, uid_b])
    return f"{a}::{b}"


def judge_prompt(a: Dict[str, Any], b: Dict[str, Any]) -> str:
    payload = {
        "tool_a": {
            "name": a["name"],
            "description": a["description"],
            "inputs": a["inputs"],
            "input_type_multiset": list(canonical_input_signature(a["inputs"])),
            "return_type": a["_return_type"],
        },
        "tool_b": {
            "name": b["name"],
            "description": b["description"],
            "inputs": b["inputs"],
            "input_type_multiset": list(canonical_input_signature(b["inputs"])),
            "return_type": b["_return_type"],
        },
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def parse_yes_no(text: str) -> Optional[bool]:
    text = (text or "").strip().upper()
    if text.startswith("YES"):
        return True
    if text.startswith("NO"):
        return False
    return None


def embed_all_tools(client: OpenAI, tools: List[Dict[str, Any]], cache_path: Path, batch_size: int, max_retries: int, backoff: float) -> Dict[str, np.ndarray]:
    cache = load_jsonl_cache(cache_path)
    out: Dict[str, np.ndarray] = {}
    missing: List[Dict[str, Any]] = []
    for t in tools:
        uid = t["_uid"]
        row = cache.get(uid)
        if row and "vec" in row:
            out[uid] = np.asarray(row["vec"], dtype=np.float32)
        else:
            missing.append(t)

    new_rows: List[Dict[str, Any]] = []
    for i in range(0, len(missing), batch_size):
        chunk = missing[i:i + batch_size]
        texts = [embedding_text(t) for t in chunk]
        rsp = safe_embed(client, model=EMB_MODEL, texts=texts, max_retries=max_retries, backoff=backoff)
        if rsp is None:
            raise RuntimeError(f"Embedding request failed for batch starting at {i}")
        for t, item in zip(chunk, rsp.data):
            out[t["_uid"]] = np.asarray(item.embedding, dtype=np.float32)
            new_rows.append({"id": t["_uid"], "vec": item.embedding})
        if new_rows:
            append_jsonl(cache_path, new_rows)
            new_rows = []
    return out


def find_candidate_pairs(tools: List[Dict[str, Any]], emb_map: Dict[str, np.ndarray], sim_threshold: float, chunk_size: int) -> List[Tuple[int, int, float]]:
    by_block: Dict[Tuple[Tuple[str, ...], str], List[int]] = defaultdict(list)
    for idx, t in enumerate(tools):
        by_block[block_key(t)].append(idx)

    pairs: List[Tuple[int, int, float]] = []
    for indices in by_block.values():
        if len(indices) < 2:
            continue
        mat = np.stack([emb_map[tools[i]["_uid"]] for i in indices], axis=0)
        norms = np.linalg.norm(mat, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        mat = mat / norms
        n = len(indices)
        for start in range(0, n, chunk_size):
            stop = min(start + chunk_size, n)
            sims = mat[start:stop] @ mat.T
            for local_i, row in enumerate(sims):
                i = start + local_i
                row[: i + 1] = -1.0
                hits = np.where(row >= sim_threshold)[0]
                for j in hits.tolist():
                    pairs.append((indices[i], indices[j], float(row[j])))
    return pairs


def judge_pairs(client: OpenAI, tools: List[Dict[str, Any]], candidates: List[Tuple[int, int, float]], pair_cache_path: Path, judge_model: str, max_retries: int, backoff: float) -> Dict[str, Dict[str, Any]]:
    cache = load_jsonl_cache(pair_cache_path)
    out: Dict[str, Dict[str, Any]] = {}
    pending: List[Dict[str, Any]] = []
    temp = None if judge_model.startswith("gpt-5") else 0.0

    for i, j, sim in candidates:
        a = tools[i]
        b = tools[j]
        pid = pair_id(a["_uid"], b["_uid"])
        if pid in cache:
            out[pid] = cache[pid]
            continue
        rsp = safe_chat(
            client,
            model=judge_model,
            messages=[{"role": "system", "content": SYS_JUDGE}, {"role": "user", "content": judge_prompt(a, b)}],
            temperature=temp,
            max_retries=max_retries,
            backoff=backoff,
        )
        raw = "" if rsp is None else (rsp.choices[0].message.content or "").strip()
        verdict = parse_yes_no(raw)
        row = {
            "id": pid,
            "uid_a": a["_uid"],
            "uid_b": b["_uid"],
            "name_a": a["name"],
            "name_b": b["name"],
            "function_a": a["function"],
            "function_b": b["function"],
            "similarity": sim,
            "strict_equivalent": verdict,
            "judge_model": judge_model,
            "raw_response": raw,
        }
        out[pid] = row
        pending.append(row)
        if len(pending) >= 100:
            append_jsonl(pair_cache_path, pending)
            pending = []
    if pending:
        append_jsonl(pair_cache_path, pending)
    return out


def summarize(tools: List[Dict[str, Any]], candidates: List[Tuple[int, int, float]], judged: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    per_tool_matches: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    num_true_pairs = 0
    for i, j, sim in candidates:
        a = tools[i]
        b = tools[j]
        row = judged[pair_id(a["_uid"], b["_uid"])]
        if row.get("strict_equivalent") is not True:
            continue
        num_true_pairs += 1
        per_tool_matches[a["_uid"]].append({"uid": b["_uid"], "name": b["name"], "function": b["function"], "similarity": sim})
        per_tool_matches[b["_uid"]].append({"uid": a["_uid"], "name": a["name"], "function": a["function"], "similarity": sim})

    tool_rows: List[Dict[str, Any]] = []
    hist = Counter()
    max_count = 0
    nonzero = 0
    total_counts = 0
    for idx, t in enumerate(tools):
        matches = sorted(per_tool_matches.get(t["_uid"], []), key=lambda x: (-x["similarity"], x["name"], x["function"]))
        cnt = len(matches)
        hist[cnt] += 1
        max_count = max(max_count, cnt)
        total_counts += cnt
        if cnt > 0:
            nonzero += 1
        tool_rows.append({
            "tool_index": idx,
            "uid": t["_uid"],
            "name": t["name"],
            "function": t["function"],
            "type": t.get("type"),
            "inputs": t.get("inputs", {}),
            "return_type": t.get("_return_type", "<missing>"),
            "strict_equiv_count": cnt,
            "strict_equiv_tools": matches,
        })
    return {
        "summary": {
            "num_tools": len(tools),
            "num_candidate_pairs": len(candidates),
            "num_strict_equiv_pairs": num_true_pairs,
            "num_tools_with_at_least_one_equiv": nonzero,
            "mean_equiv_count_per_tool": (total_counts / len(tools)) if tools else 0.0,
            "max_equiv_count_for_a_tool": max_count,
            "equiv_count_histogram": {str(k): v for k, v in sorted(hist.items())},
        },
        "tools": tool_rows,
    }


def write_csv(path: Path, tool_rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["tool_index", "uid", "name", "function", "type", "return_type", "strict_equiv_count"])
        for row in tool_rows:
            w.writerow([row["tool_index"], row["uid"], row["name"], row["function"], row.get("type"), row.get("return_type"), row["strict_equiv_count"]])


def main() -> None:
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    ap.add_argument("--tool-json", default=DEFAULT_TOOL_JSON, type=Path)
    ap.add_argument("--tools-dir", default=DEFAULT_TOOLS_DIR, type=Path)
    ap.add_argument("--out-json", default=DEFAULT_OUT_JSON, type=Path)
    ap.add_argument("--out-csv", default=DEFAULT_OUT_CSV, type=Path)
    ap.add_argument("--emb-cache", default=DEFAULT_EMB_CACHE, type=Path)
    ap.add_argument("--pair-cache", default=DEFAULT_PAIR_CACHE, type=Path)
    ap.add_argument("--judge-model", default="gpt-5")
    ap.add_argument("--sim-threshold", type=float, default=0.985)
    ap.add_argument("--embed-batch-size", type=int, default=128)
    ap.add_argument("--sim-chunk-size", type=int, default=256)
    ap.add_argument("--max-tools", type=int, default=None)
    ap.add_argument("--max-retries", type=int, default=5)
    ap.add_argument("--retry-backoff", type=float, default=0.8)
    args = ap.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set.")

    raw_tools = json.loads(args.tool_json.read_text(encoding="utf-8"))
    if args.max_tools is not None:
        raw_tools = raw_tools[:args.max_tools]

    tools: List[Dict[str, Any]] = []
    for t in raw_tools:
        tt = dict(t)
        tt["_uid"] = tool_uid(tt)
        tt["_return_type"] = extract_return_annotation(args.tools_dir / tt["function"], tt["name"])
        tools.append(tt)

    print(f"Loaded {len(tools)} tools", flush=True)
    client = OpenAI()
    emb_map = embed_all_tools(client, tools, args.emb_cache, args.embed_batch_size, args.max_retries, args.retry_backoff)
    print(f"Embedded {len(emb_map)} tools", flush=True)
    candidates = find_candidate_pairs(tools, emb_map, args.sim_threshold, args.sim_chunk_size)
    print(f"Candidate pairs above threshold {args.sim_threshold}: {len(candidates)}", flush=True)
    judged = judge_pairs(client, tools, candidates, args.pair_cache, args.judge_model, args.max_retries, args.retry_backoff)
    print(f"Judged candidate pairs: {len(judged)}", flush=True)

    result = summarize(tools, candidates, judged)
    result["config"] = {
        "tool_json": str(args.tool_json),
        "tools_dir": str(args.tools_dir),
        "judge_model": args.judge_model,
        "embedding_model": EMB_MODEL,
        "sim_threshold": args.sim_threshold,
        "max_tools": args.max_tools,
    }
    result["cache_paths"] = {
        "emb_cache": str(args.emb_cache),
        "pair_cache": str(args.pair_cache),
    }

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(args.out_csv, result["tools"])

    s = result["summary"]
    print("Summary:", flush=True)
    print(f"  num_tools: {s['num_tools']}", flush=True)
    print(f"  num_candidate_pairs: {s['num_candidate_pairs']}", flush=True)
    print(f"  num_strict_equiv_pairs: {s['num_strict_equiv_pairs']}", flush=True)
    print(f"  num_tools_with_at_least_one_equiv: {s['num_tools_with_at_least_one_equiv']}", flush=True)
    print(f"  mean_equiv_count_per_tool: {s['mean_equiv_count_per_tool']:.4f}", flush=True)
    print(f"  max_equiv_count_for_a_tool: {s['max_equiv_count_for_a_tool']}", flush=True)
    print(f"  out_json: {args.out_json}", flush=True)
    print(f"  out_csv: {args.out_csv}", flush=True)


if __name__ == "__main__":
    main()
