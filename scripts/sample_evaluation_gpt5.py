#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sample_evaluation_gpt5.py
-------------------------
Sample evaluation script for running a GPT-5-style ReAct solver on ToolMATH
with gold tools plus top-K distractors from a prebuilt distractor file.

- Deterministic sampling with random seed 42 (stable across runs/models)
- Optional flag --no-gold-tools to evaluate with distractors ONLY (gold tools removed).
  Useful for “no-gold” ablations / stress tests:
    python scripts/sample_evaluation_gpt5.py ... --no-gold-tools
  (Any distractor that accidentally shares a name with a gold tool
   is filtered out to avoid leakage.)
- Duplicate-call guard & cache reuse
- Robust retries for chat calls
- Records which tools were used per problem
- Prints verification-style breakdown and coverage metrics at the end

Usage example
-------------
export OPENAI_API_KEY=...      # or set OPENAI_BASE_URL + dummy keys for vLLM
python scripts/sample_evaluation_gpt5.py \
  --distractors-json data/distractors_by_level.json \
  --tools-dir data/function_ToolMATH \
  --level 1 \
  --k 100 \
  --num-examples 200 \
  --no-gold-tools \
  --out results/sample_evaluation_gpt5_l1_k100_nogold.json
"""

from __future__ import annotations
import argparse, ast, hashlib, json, os, random, re, textwrap, time
from pathlib import Path
from typing import Any, Dict, List, Tuple, Optional
import types
import importlib.util
import math as _math
import json as _json
from collections import defaultdict
import multiprocessing as mp

from datasets import load_dataset
import openai
from openai import (
    APIError, RateLimitError, APIConnectionError, APITimeoutError,
    BadRequestError, AuthenticationError,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
RESULTS_DIR = REPO_ROOT / "results"

# ─────────────────────────── CLI ────────────────────────────
P = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
P.add_argument("--distractors-json", type=str,
               default=str(DATA_DIR / "distractors_by_level.json"),
               help="Per-problem dict with {problem, gold_tools, distractors:{level1..5}}")
P.add_argument("--tools-dir", type=str, default=str(DATA_DIR / "function_ToolMATH"),
               help="Directory containing the Python tool implementations referenced by the selected split.")
P.add_argument("--split", type=str, default="train", help="HF split for problem+solution")
P.add_argument("--level", type=int, default=1, choices=[1,2,3,4,5],
               help="distractor difficulty level to use (1..5)")
P.add_argument("--k", type=int, default=100, help="top-K distractors to add (from the pre-ranked 100)")
P.add_argument("--num-examples", type=int, default=None, help="limit number of problems")
P.add_argument("--model", type=str, default="gpt-5", help="solver model")
P.add_argument("--judge-model", type=str, default="gpt-4o-mini", help="grading model")
P.add_argument("--out", type=str,
               default=str(RESULTS_DIR / "sample_evaluation_gpt5.json"),
               help="final merged pretty JSON output")
P.add_argument("--live-ndjson", type=str, default=None, help="optional live JSONL")
P.add_argument("--num-workers", type=int, default=1)
P.add_argument("--api-key-vars", type=str, default="OPENAI_API_KEY",
               help="comma-separated env var names for OpenAI API keys (one per worker ideally)")
P.add_argument("--sleep", type=float, default=0.7)
P.add_argument("--no-gold-tools", action="store_true", help="If set, remove all gold tools; provide only distractors.")
P.add_argument("--max-retries", type=int, default=5)
P.add_argument("--retry-backoff", type=float, default=0.8)
args = P.parse_args()
if args.live_ndjson is None:
    args.live_ndjson = str(Path(args.out).with_suffix(".ndjson"))

# ───────────────────────── regex & prompts ──────────────────────────
ANS_RE = re.compile(r"^ANSWER\s*:\s*(.+)$", re.M)
ACT_RE = re.compile(r"^Action\s*:\s*({.*})\s*$", re.M)

SYS_SOLVER = textwrap.dedent("""\
    You are an expert competition-math solver.
    For every turn output *exactly one* line beginning with “Thought: …”.
    If you need a tool, follow IMMEDIATELY with ONE line:
    Action: { "name": "<tool>", "arguments": { … } }
    Then WAIT for the Observation line before thinking again.
    Never call a tool with the same arguments twice – reuse the prior Observation.
    If you have already called a tool with the same name and identical arguments, DO NOT call it again; reuse the cached Observation verbatim and move forward.
    Finish with:
    ANSWER: <numeric answer>""")

SYS_JUDGE = textwrap.dedent("""\
    You are an automated grader for math-contest problems.
    Reply YES if the student's answer is fully correct, otherwise reply NO.
    Reply with ONLY YES or NO.""")

# ───────────────────── file resolution & import ─────────────────────
def _resolve_tool_path(file_field: str, tools_dir: Path, override_functions_dir: Optional[Path]) -> Path:
    cand = Path(file_field)
    if cand.is_absolute() and cand.exists():
        return cand
    cand2 = (tools_dir / file_field).resolve()
    if cand2.exists():
        return cand2
    if override_functions_dir:
        cand3 = (override_functions_dir / file_field).resolve()
        if cand3.exists():
            return cand3
    cand4 = (tools_dir / "function_total" / file_field).resolve()
    if cand4.exists():
        return cand4
    if not file_field.endswith(".py"):
        return _resolve_tool_path(file_field + ".py", tools_dir, override_functions_dir)
    raise FileNotFoundError(f"Cannot locate tool file for: {file_field}")

_module_cache: Dict[Path, types.ModuleType] = {}

def _import_module_from_path(py_path: Path) -> types.ModuleType:
    if py_path in _module_cache:
        return _module_cache[py_path]
    mod_name = "toolmod_" + hashlib.sha1(str(py_path).encode("utf-8")).hexdigest()
    spec = importlib.util.spec_from_file_location(mod_name, py_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not create spec for {py_path}")
    module = importlib.util.module_from_spec(spec)
    module.__dict__.setdefault("math", _math)
    spec.loader.exec_module(module)
    _module_cache[py_path] = module
    return module

def _load_callable(t: Dict[str, Any], tools_dir: Path, override_functions_dir: Optional[Path]) -> Any:
    if "_impl" in t:
        return t["_impl"]
    file_field = t.get("function")
    if not isinstance(file_field, str):
        raise TypeError(f"tool['function'] must be a filename string; got {type(file_field)}")
    py_path = _resolve_tool_path(file_field, tools_dir, override_functions_dir)
    module = _import_module_from_path(py_path)
    fn_name = t.get("name")
    if not isinstance(fn_name, str) or not fn_name:
        raise ValueError("tool['name'] must be a non-empty string")
    try:
        fn = getattr(module, fn_name)
    except AttributeError:
        raise AttributeError(
            f"Function '{fn_name}' not found in module '{py_path.name}'. "
            f"Ensure the file defines: def {fn_name}(...):"
        )
    t["_impl"] = fn
    return fn

def run_tool(t: Dict[str, Any], kwargs: Dict[str, Any],
             tools_dir: Path, override_functions_dir: Optional[Path]) -> Any:
    fn = _load_callable(t, tools_dir, override_functions_dir)
    return fn(**(kwargs or {}))

def strip_impl(t: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in t.items() if k != "_impl"}

# ────────────────────── canonical cache key helpers ─────────────────────
MAX_DUP_OBS = 2

def _canon_args(obj):
    if isinstance(obj, dict):
        return {k: _canon_args(obj[k]) for k in sorted(obj)}
    if isinstance(obj, (list, tuple)):
        return [_canon_args(x) for x in obj]
    if isinstance(obj, float) and obj.is_integer():
        return int(obj)
    return obj

def _key_for_call(name: str, args: dict) -> tuple[str, str]:
    canon = _canon_args(args or {})
    return (name, _json.dumps(canon, separators=(",", ":"), sort_keys=True))

# ───────────────────────── Retryable OpenAI calls ─────────────────────────
def _sleep_with_jitter(base: float, attempt: int):
    delay = base * (2 ** attempt) * (0.75 + random.random() * 0.5)
    time.sleep(delay)

def _format_error(err: Exception) -> str:
    code = getattr(err, "status_code", None)
    body = getattr(err, "body", None)
    if code is not None:
        return f"{type(err).__name__}(status={code}, body={body})"
    return f"{type(err).__name__}({err})"

def safe_chat(client: openai.Client, *, model: str, messages: List[dict],
              temperature: float = 0.0, max_retries: int = 5, backoff: float = 0.8):
    last_err: Optional[str] = None
    # gpt-5 on chat.completions may reject non-default temperature values.
    is_gpt5_family = model.strip().lower().startswith("gpt-5")
    for attempt in range(max_retries + 1):
        try:
            req = {"model": model, "messages": messages}
            if not is_gpt5_family:
                req["temperature"] = temperature
            return client.chat.completions.create(**req)
        except (RateLimitError, APIConnectionError, APITimeoutError, APIError) as e:
            last_err = _format_error(e)
            if attempt >= max_retries:
                print(f"[safe_chat] model={model} failed after retries: {last_err}", flush=True)
                return None
            _sleep_with_jitter(backoff, attempt)
        except (BadRequestError, AuthenticationError) as e:
            last_err = _format_error(e)
            print(f"[safe_chat] model={model} non-retryable: {last_err}", flush=True)
            return None
        except Exception as e:
            last_err = _format_error(e)
            if attempt >= max_retries:
                print(f"[safe_chat] model={model} unexpected failure: {last_err}", flush=True)
                return None
            _sleep_with_jitter(backoff, attempt)

def llm_grade(client: openai.Client, ans: str, official: str, judge_model: str,
              max_retries: int, backoff: float) -> bool:
    judge_msgs = [
        {"role": "system", "content": SYS_JUDGE},
        {"role": "user",
         "content": f"Official solution:\n{official}\n\nStudent answer:\n{ans}\n\nIs the student's answer correct?"}
    ]
    rsp = safe_chat(client, model=judge_model, messages=judge_msgs,
                    temperature=0, max_retries=max_retries, backoff=backoff)
    if rsp is None:
        return False
    content = (rsp.choices[0].message.content or "").strip().upper()
    return content.startswith("YES")

# ───────────────────────── writer (live NDJSON) ─────────────────────────
def writer_entry(live_path: str, q: mp.Queue):
    p = Path(live_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(p, "a", encoding="utf-8") as f:
            while True:
                item = q.get()
                if item is None or (isinstance(item, dict) and item.get("type") == "STOP"):
                    break
                if isinstance(item, dict) and item.get("type") == "result":
                    rec = item["data"]
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    f.flush()
                    os.fsync(f.fileno())
    except Exception as e:
        print(f"[writer] ERROR (continuing): {e}", flush=True)

# ───────────────────────── tool assembly (gold + top-K distractors) ─────────────────────────
def normalize_problem(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()

def dedup_tools_keep_gold_first(golds: List[dict], decoys: List[dict]) -> List[dict]:
    out: List[dict] = []
    seen_names = set()
    # gold first
    for t in golds:
        if t["name"] not in seen_names:
            out.append(t); seen_names.add(t["name"])
    # then distractors but skip name collisions
    for t in decoys:
        if t["name"] not in seen_names:
            out.append(t); seen_names.add(t["name"])
    return out

def pick_topk(record: dict, level: int, k: int) -> List[dict]:
    levels = record.get("distractors", {})
    key = {1:"level1", 2:"level2", 3:"level3", 4:"level4", 5:"level5"}[level]
    lst = levels.get(key, [])[:100]  # the precomputed 100
    return lst[:max(0, k)]

# ───────────────────────── worker main loop ─────────────────────────
def worker_run(shard_id: int,
               api_key: str,
               jobs: List[Dict[str, Any]],
               tools_dir_str: str,
               override_functions_dir_str: Optional[str],
               out_part_path: str,
               sleep_time: float,
               solve_model: str,
               judge_model: str,
               max_retries: int,
               retry_backoff: float,
               live_q: Optional[mp.Queue] = None):

    prefix = f"[W{shard_id}]"
    print(f"{prefix} Starting with {len(jobs)} problems.", flush=True)

    client = openai.Client(api_key=api_key)
    tools_dir = Path(tools_dir_str)
    override_functions_dir = Path(override_functions_dir_str).resolve() if override_functions_dir_str else None

    results: List[Dict[str, Any]] = []
    call_cache: Dict[Tuple[str, str], Any] = {}
    correct = total = 0
    stats = {
        "correct_with_tools": 0,
        "correct_no_tools": 0,
        "wrong_nonnull_with_tools": 0,
        "wrong_nonnull_no_tools": 0,
        "wrong_null_answer": 0,
    }

    def save_part():
        try:
            Path(out_part_path).parent.mkdir(parents=True, exist_ok=True)
            Path(out_part_path).write_text(json.dumps(results, indent=2), encoding="utf-8")
        except Exception as e:
            print(f"{prefix} WARN: could not write part file ({e})", flush=True)

    for idx, job in enumerate(jobs, 1):
        try:
            prob = job["problem"]
            sol  = job["solution"]
            tools = job["tools"]

            used_tool_names = set()  # ← track unique tool names used for coverage

            # header to show only summary info
            tb_view = [{k: t[k] for k in ("name", "description", "inputs")} for t in tools]
            header  = f"Here are the available tools:\n```json\n{json.dumps(tb_view, indent=2)}\n```"

            msgs  = [{"role": "system", "content": SYS_SOLVER},
                     {"role": "user",   "content": header},
                     {"role": "user",   "content": prob}]
            turns: List[Dict[str, Any]] = []
            idle, answered = 0, False

            used_tools = False
            num_tool_actions = 0
            dup_counts = defaultdict(int)

            print(f"{prefix} 🔢  Problem {idx}/{len(jobs)}", flush=True)

            for _ in range(16):
                rsp = safe_chat(client, model=solve_model, messages=msgs,
                                temperature=0, max_retries=max_retries, backoff=retry_backoff)
                if rsp is None:
                    note = "Observation: ERROR – LLM request failed repeatedly; skipping this problem."
                    msgs.append({"role": "user", "content": note})
                    turns.append({"role": "user", "content": note})
                    break

                msg  = rsp.choices[0].message
                text = msg.content or ""
                if hasattr(msg, "model_dump"):
                    turns.append(msg.model_dump())
                else:
                    turns.append({"role": "assistant", "content": text})

                m = ACT_RE.search(text)
                if m:
                    raw = m.group(1)
                    try:
                        call = json.loads(raw)
                    except json.JSONDecodeError:
                        try:
                            call = ast.literal_eval(raw)
                        except Exception as e:
                            err = f"Observation: ERROR – malformed Action JSON ({e})."
                            msgs += [{"role": "user", "content": err}]
                            turns.append({"role": "user", "content": err}); time.sleep(sleep_time)
                            idle += 1
                            if idle >= 2:
                                remind = ("Reminder – output exactly one Thought line and don’t "
                                          "repeat an identical tool call; use the cached Observation instead.")
                                msgs += [{"role": "user", "content": remind}]
                                turns.append({"role": "user", "content": remind}); idle = 0
                            continue

                    if not isinstance(call, dict) or "name" not in call:
                        err = ("Observation: ERROR – Action must be a JSON object with "
                               '"name" and "arguments" keys.')
                        msgs += [{"role": "user", "content": err}]
                        turns.append({"role": "user", "content": err}); time.sleep(sleep_time)
                        idle += 1
                        if idle >= 2:
                            remind = ("Reminder – output exactly one Thought line and don’t "
                                      "repeat an identical tool call; use the cached Observation instead.")
                            msgs += [{"role": "user", "content": remind}]
                            turns.append({"role": "user", "content": remind}); idle = 0
                        continue

                    args_dict = call.get("arguments", {}) or {}
                    key = _key_for_call(call["name"], args_dict)
                    dup_counts[key] += 1

                    if key in call_cache:
                        obs = call_cache[key]
                        if dup_counts[key] == 1:
                            note = f"Observation (cached): {obs}"
                        elif dup_counts[key] <= MAX_DUP_OBS:
                            note = (f"Observation (cached-duplicate #{dup_counts[key]}): {obs}\n"
                                    f"Reminder: You've already called {call['name']} with the same arguments. "
                                    "Do not call it again; reuse this Observation and move forward.")
                        else:
                            note = (f"Observation (cached-duplicate #{dup_counts[key]}): {obs}\n"
                                    "STOP: Identical Action detected repeatedly. Further identical Actions "
                                    "will be ignored. Proceed to the next reasoning step or output ANSWER.")

                        idle += 1
                        msgs += [{"role": "user", "content": note}]
                        turns.append({"role": "user", "content": note}); time.sleep(sleep_time)
                        if idle >= 2:
                            remind = ("Reminder – output exactly one Thought line and don’t "
                                      "repeat an identical tool call; use the cached Observation instead.")
                            msgs += [{"role": "user", "content": remind}]
                            turns.append({"role": "user", "content": remind}); idle = 0
                        continue
                    else:
                        try:
                            tool = next(t for t in tools if t["name"] == call["name"])
                            used_tool_names.add(tool["name"])  # ← mark this tool as used
                            obs  = run_tool(tool, args_dict, tools_dir, override_functions_dir)
                            num_tool_actions += 1
                            used_tools = True
                        except StopIteration:
                            obs = f"ERROR: tool '{call['name']}' not found among provided tools."
                        except Exception as e:
                            obs = f"ERROR: {e}"

                        call_cache[key] = obs
                        note = f"Observation ({call['name']}, {_json.dumps(_canon_args(args_dict), separators=(',',':'), sort_keys=True)}): {obs}"
                        msgs += [{"role": "user", "content": note}]
                        turns.append({"role": "user", "content": note}); time.sleep(sleep_time)
                        idle = 0
                        continue

                m = ANS_RE.search(text)
                if m:
                    answered  = True
                    model_ans = m.group(1).strip()
                    is_corr   = llm_grade(client, model_ans, sol, judge_model,
                                          max_retries=max_retries, backoff=retry_backoff)
                    correct  += bool(is_corr)
                    total    += 1

                    if is_corr and used_tools:
                        bucket = "correct_with_tools"; stats[bucket] += 1
                    elif is_corr and not used_tools:
                        bucket = "correct_no_tools"; stats[bucket] += 1
                    elif (not is_corr) and used_tools:
                        bucket = "wrong_nonnull_with_tools"; stats[bucket] += 1
                    else:
                        bucket = "wrong_nonnull_no_tools"; stats[bucket] += 1

                    print(f"{prefix}    Finished {'✅' if is_corr else '❌'} ({bucket})", flush=True)

                    record = {
                        "problem": prob, "solution": sol,
                        "model_answer": model_ans, "is_correct": bool(is_corr),
                        "used_tools": used_tools, "num_tool_actions": num_tool_actions,
                        "used_tool_names": sorted(used_tool_names),  # ← NEW
                        "tools": [strip_impl(t) for t in tools],
                        "turns": turns
                    }
                    results.append(record)
                    save_part()
                    if live_q is not None:
                        try:
                            live_q.put({"type": "result", "data": record})
                        except Exception:
                            pass
                    break

                # no progress → nudge
                idle += 1
                if idle == 2:
                    remind = ("Reminder – output exactly one Thought line and don’t "
                              "repeat an identical tool call; use the cached Observation instead.")
                    msgs += [{"role": "user", "content": remind}]
                    turns.append({"role": "user", "content": remind}); idle = 0
                else:
                    msgs += [{"role": "assistant", "content": text}]
                time.sleep(sleep_time)

            if not answered:
                total += 1
                stats["wrong_null_answer"] += 1
                print(f"{prefix}    Finished ❌ (no valid ANSWER line)", flush=True)
                record = {
                    "problem": prob, "solution": sol,
                    "model_answer": None, "is_correct": False,
                    "used_tools": used_tools, "num_tool_actions": num_tool_actions,
                    "used_tool_names": sorted(used_tool_names),  # ← NEW
                    "tools": [strip_impl(t) for t in tools],
                    "turns": turns
                }
                results.append(record)
                save_part()
                if live_q is not None:
                    try:
                        live_q.put({"type": "result", "data": record})
                    except Exception:
                        pass

        except Exception as e:
            print(f"{prefix} ERROR (problem-level, continuing): {e}", flush=True)
            record = {
                "problem": job.get("problem",""),
                "solution": job.get("solution",""),
                "model_answer": None, "is_correct": False,
                "used_tools": False, "num_tool_actions": 0,
                "used_tool_names": [],  # ← NEW
                "tools": [strip_impl(t) for t in job.get("tools", [])],
                "turns": [{"role": "system", "content": f"ERROR: {e}"}]
            }
            results.append(record)
            save_part()
            if live_q is not None:
                try:
                    live_q.put({"type": "result", "data": record})
                except Exception:
                    pass

    return {
        "correct_with_tools": stats["correct_with_tools"],
        "correct_no_tools": stats["correct_no_tools"],
        "wrong_nonnull_with_tools": stats["wrong_nonnull_with_tools"],
        "wrong_nonnull_no_tools": stats["wrong_nonnull_no_tools"],
        "wrong_null_answer": stats["wrong_null_answer"],
        "correct": correct,
        "total": total,
        "out_part_path": out_part_path,
    }

# ───────────────────────── parent main ─────────────────────────
def _worker_entry(shard_id, api_key, chunk, tools_dir_str, override_functions_dir_str,
                  out_part_path, sleep_time, solve_model, judge_model,
                  max_retries, retry_backoff, conn, live_q):
    try:
        ret = worker_run(shard_id, api_key, chunk, tools_dir_str, override_functions_dir_str,
                         out_part_path, sleep_time, solve_model, judge_model,
                         max_retries, retry_backoff, live_q)
        conn.send(ret)
    except Exception as e:
        conn.send({
            "correct_with_tools": 0, "correct_no_tools": 0,
            "wrong_nonnull_with_tools": 0, "wrong_nonnull_no_tools": 0,
            "wrong_null_answer": 0, "correct": 0, "total": 0,
            "out_part_path": out_part_path,
        })
        print(f"[W{shard_id}] ERROR (worker-level): {e}", flush=True)
    finally:
        conn.close()

def main():
    rand = random.Random(42)

    # Load distractors per problem
    DIST = json.loads(Path(args.distractors_json).read_text(encoding="utf-8"))
    # Build problem->record mapping
    by_prob: Dict[str, dict] = {normalize_problem(r["problem"]): r for r in DIST}

    # Load HF to retrieve official solution text
    print("📚  Loading MATH dataset …", flush=True)
    ds = load_dataset("qwedsacf/competition_math", split=args.split)
    SOLN = {normalize_problem(r["problem"]): r["solution"] for r in ds}

    # Build job list from validated problems only (those appearing in DIST)
    problems = list(by_prob.keys())
    rand.shuffle(problems)
    if args.num_examples is not None:
        problems = problems[:args.num_examples]

    level = args.level
    k = args.k

    mode_str = "NO-GOLD (distractors only)" if args.no_gold_tools else "GOLD+DISTRACTORS"
    print(f"⚙️  Mode: {mode_str} | Level={level} | K={k}", flush=True)

    jobs_all: List[Dict[str, Any]] = []
    for pnorm in problems:
        rec = by_prob[pnorm]
        gold = rec.get("gold_tools", [])
        decoys = pick_topk(rec, level, k)
        if args.no_gold_tools:
            gold_names = {t.get("name") for t in gold}
            # filter any distractor that collides with a gold name (paranoia)
            decoys = [t for t in decoys if t.get("name") not in gold_names]
            tools = dedup_tools_keep_gold_first([], decoys)
        else:
            tools = dedup_tools_keep_gold_first(gold, decoys)

        prob_text = rec["problem"]
        solution  = SOLN.get(pnorm, "")  # empty if not found

        jobs_all.append({
            "problem": prob_text,
            "solution": solution,
            "tools": tools,
            # helpful metadata for later analysis
            "no_gold_tools": bool(args.no_gold_tools),
            "gold_tool_names": sorted({t.get("name") for t in gold}),
            "provided_tool_names": sorted({t.get("name") for t in tools}),
        })

    # Keys & workers
    var_names = [v.strip() for v in (args.api_key_vars or "").split(",") if v.strip()]
    keys = [os.environ.get(v) for v in var_names]
    keys = [k for k in keys if k]
    if not keys:
        raise SystemExit("No API keys found. Set them in env vars named by --api-key-vars.")
    num_workers = min(args.num_workers, len(keys), max(1, len(jobs_all)))
    if num_workers < args.num_workers:
        print(f"⚠️  Reducing workers to {num_workers} (limited by keys/jobs).", flush=True)

    # Shard jobs
    chunks: List[List[Dict[str, Any]]] = [[] for _ in range(num_workers)]
    for i, job in enumerate(jobs_all):
        chunks[i % num_workers].append(job)

    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    live_path = Path(args.live_ndjson).resolve() if args.live_ndjson else None

    ctx = mp.get_context("spawn")

    # Start writer
    live_q = None
    writer_proc = None
    if live_path is not None:
        live_q = ctx.Queue(maxsize=1000)
        writer_proc = ctx.Process(target=writer_entry, args=(str(live_path), live_q))
        writer_proc.daemon = False
        writer_proc.start()
        print(f"🟢 Live NDJSON appending to: {live_path}", flush=True)

    # Pipes for worker stats
    parent_conns = []
    procs = []
    for i in range(num_workers):
        api_key = keys[i % len(keys)]
        out_part = f"{str(out_path)}.part{i+1}.json"
        parent_conn, child_conn = ctx.Pipe(False)
        parent_conns.append(parent_conn)
        p = ctx.Process(
            target=_worker_entry,
            args=(i+1, api_key, chunks[i], args.tools_dir, None,
                  out_part, args.sleep, args.model, args.judge_model,
                  args.max_retries, args.retry_backoff, child_conn, live_q)
        )
        p.daemon = False
        p.start()
        procs.append(p)
        child_conn.close()

    # Aggregate stats
    merged_parts = []
    for pc in parent_conns:
        _ = pc.recv()  # we recompute final stats from merged 'full' below
        pc.close()
        merged_parts.append(f"{str(out_path)}.part{len(merged_parts)+1}.json")

    for p in procs:
        p.join()

    # Stop writer
    if writer_proc is not None and live_q is not None:
        try:
            live_q.put({"type": "STOP"})
            writer_proc.join()
        except Exception:
            pass

    # Merge into final pretty JSON
    full: List[Dict[str, Any]] = []
    used_live = False
    if live_path is not None and live_path.exists():
        try:
            with open(live_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    full.append(json.loads(line))
            used_live = True
        except Exception as e:
            print(f"⚠️  Could not read live NDJSON '{live_path}': {e}. Falling back to parts.", flush=True)

    if not used_live:
        # collect all .part*.json that were written
        for part_path in sorted(out_path.parent.glob(out_path.name + ".part*.json")):
            try:
                part_data = json.loads(Path(part_path).read_text(encoding="utf-8"))
                full.extend(part_data)
            except Exception as e:
                print(f"⚠️  Could not read part '{part_path}': {e}", flush=True)

    Path(out_path).write_text(json.dumps(full, indent=2), encoding="utf-8")

    # ───────── Detailed breakdown & coverage (verification-style) ─────────
    total = len(full)
    corr = sum(1 for r in full if r.get("is_correct"))
    wrong = total - corr
    acc = 100.0 * corr / max(total, 1)

    # Buckets
    correct_with_tools = sum(1 for r in full if r.get("is_correct") and r.get("used_tools"))
    correct_no_tools   = sum(1 for r in full if r.get("is_correct") and not r.get("used_tools"))
    wrong_nonnull_with_tools = sum(1 for r in full if (not r.get("is_correct")) and (r.get("model_answer") is not None) and r.get("used_tools"))
    wrong_nonnull_no_tools   = sum(1 for r in full if (not r.get("is_correct")) and (r.get("model_answer") is not None) and (not r.get("used_tools")))
    wrong_null_answer        = sum(1 for r in full if r.get("model_answer") is None)

    # Coverage
    problems_with_tools = sum(1 for r in full if len(r.get("tools", [])) > 0)
    problems_used_any   = sum(1 for r in full if len(r.get("used_tool_names", [])) > 0)

    # Per-instance coverage
    total_tool_instances = sum(len(r.get("tools", [])) for r in full)
    instances_used       = 0
    for r in full:
        if not r.get("tools"):
            continue
        tool_names = {t.get("name") for t in r["tools"]}
        used_names = set(r.get("used_tool_names", []))
        instances_used += len(tool_names & used_names)

    cov_pct = (100.0 * instances_used / max(total_tool_instances, 1)) if total_tool_instances else 0.0

    # Average per-problem coverage (only problems with ≥1 tool)
    per_prob_cov = []
    for r in full:
        tools = r.get("tools", [])
        if not tools:
            continue
        tool_names = {t.get("name") for t in tools}
        used_names = set(r.get("used_tool_names", []))
        per_prob_cov.append(100.0 * len(tool_names & used_names) / max(len(tool_names), 1))
    avg_cov = sum(per_prob_cov) / max(len(per_prob_cov), 1) if per_prob_cov else 0.0

    # Pretty print
    def pct(x, d):
        return f"{x} ({100.0 * x / max(d,1):.1f}%)"

    print("\nBreakdown (merged):")
    print(f"  ✓ Correct (total)              : {pct(corr, total)}")
    print(f"    • Correct w/ tools           : {pct(correct_with_tools, total)}")
    print(f"    • Correct w/o tools          : {pct(correct_no_tools, total)}")
    print(f"  ✗ Wrong (total)                : {pct(wrong, total)}")
    print(f"    • Wrong (non-null w/ tools)  : {pct(wrong_nonnull_with_tools, total)}")
    print(f"    • Wrong (non-null w/o tools) : {pct(wrong_nonnull_no_tools, total)}")
    print(f"    • Wrong (null answer)        : {wrong_null_answer}")

    print(f"\nProblems in file (with ≥1 extracted tool): {problems_with_tools}")
    if problems_with_tools:
        print(f"  • Problems that used ≥1 tool at least once : "
              f"{problems_used_any} ({100.0 * problems_used_any / problems_with_tools:.2f}%)")

    print("\nPer-instance coverage (counts each tool listed per problem):")
    print(f"  • Extracted tool instances total          : {total_tool_instances}")
    print(f"  • Instances used ≥1 time                  : {instances_used}")
    print(f"  • Coverage                                : {cov_pct:.2f}%")
    print(f"\nAverage per-problem coverage                : {avg_cov:.2f}%")

    print(f"\nFinal Accuracy : {acc:.2f}%  (correct / total = {corr}/{total})")
    print(f"📝  Full log saved to {out_path}", flush=True)
    if live_path is not None:
        print(f"🟢  Live NDJSON was written to {live_path}", flush=True)

if __name__ == "__main__":
    main()
