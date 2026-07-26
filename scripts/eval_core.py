#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
eval_core.py
------------
Shared ReAct evaluation core for ToolMATH / ToolMATHHard with prebuilt distractors.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import importlib.util
import json
import math as _math
import multiprocessing as mp
import os
import random
import re
import textwrap
import time
import types
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import openai
from openai import (
    APIConnectionError,
    APIError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    RateLimitError,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
RESULTS_DIR = REPO_ROOT / "results"

ANS_RE = re.compile(r"^ANSWER\s*:\s*(.+)$", re.M)
ACT_RE = re.compile(r"^Action\s*:\s*({.*})\s*$", re.M)
MAX_DUP_OBS = 2

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

_module_cache: Dict[Path, types.ModuleType] = {}


def normalize_problem(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def strip_impl(t: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in t.items() if k != "_impl"}


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


def run_tool(t: Dict[str, Any], kwargs: Dict[str, Any], tools_dir: Path, override_functions_dir: Optional[Path]) -> Any:
    fn = _load_callable(t, tools_dir, override_functions_dir)
    return fn(**(kwargs or {}))


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
    return (name, json.dumps(canon, separators=(",", ":"), sort_keys=True))


def _sleep_with_jitter(base: float, attempt: int):
    delay = base * (2 ** attempt) * (0.75 + random.random() * 0.5)
    time.sleep(delay)


def _format_error(err: Exception) -> str:
    code = getattr(err, "status_code", None)
    body = getattr(err, "body", None)
    if code is not None:
        return f"{type(err).__name__}(status={code}, body={body})"
    return f"{type(err).__name__}({err})"


def safe_chat(client: openai.Client, *, model: str, messages: List[dict], temperature: float = 0.0, max_retries: int = 5, backoff: float = 0.8):
    last_err: Optional[str] = None
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


def llm_grade(client: openai.Client, ans: str, official: str, judge_model: str, max_retries: int, backoff: float) -> bool:
    judge_msgs = [
        {"role": "system", "content": SYS_JUDGE},
        {"role": "user", "content": f"Official solution:\n{official}\n\nStudent answer:\n{ans}\n\nIs the student's answer correct?"},
    ]
    rsp = safe_chat(client, model=judge_model, messages=judge_msgs, temperature=0, max_retries=max_retries, backoff=backoff)
    if rsp is None:
        return False
    content = (rsp.choices[0].message.content or "").strip().upper()
    return content.startswith("YES")


def writer_entry(live_path: str, q: mp.Queue):
    p = Path(live_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        with p.open("a", encoding="utf-8") as f:
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


def dedup_tools_keep_gold_first(golds: List[dict], decoys: List[dict]) -> List[dict]:
    out: List[dict] = []
    seen_names = set()
    for t in golds:
        if t["name"] not in seen_names:
            out.append(t)
            seen_names.add(t["name"])
    for t in decoys:
        if t["name"] not in seen_names:
            out.append(t)
            seen_names.add(t["name"])
    return out


def pick_topk(record: dict, level: int, k: int) -> List[dict]:
    levels = record.get("distractors", {})
    key = {1: "level1", 2: "level2", 3: "level3", 4: "level4", 5: "level5"}[level]
    lst = levels.get(key, [])[:100]
    return lst[:max(0, k)]


def load_solution_map(tool_json_path: Path) -> Dict[str, str]:
    data = json.loads(tool_json_path.read_text(encoding="utf-8"))
    out: Dict[str, str] = {}
    for r in data:
        if not isinstance(r, dict):
            continue
        prob = normalize_problem(r.get("source_problem", "") or r.get("problem", ""))
        sol = r.get("source_solution", "") or r.get("solution", "")
        if prob and sol and prob not in out:
            out[prob] = sol
    return out


def worker_run(
    shard_id: int,
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
    live_q: Optional[mp.Queue] = None,
):
    prefix = f"[W{shard_id}]"
    print(f"{prefix} Starting with {len(jobs)} problems.", flush=True)

    client = openai.Client(api_key=api_key)
    tools_dir = Path(tools_dir_str)
    override_functions_dir = Path(override_functions_dir_str).resolve() if override_functions_dir_str else None

    results: List[Dict[str, Any]] = []
    call_cache: Dict[Tuple[str, str], Any] = {}

    def save_part():
        try:
            Path(out_part_path).parent.mkdir(parents=True, exist_ok=True)
            Path(out_part_path).write_text(json.dumps(results, indent=2), encoding="utf-8")
        except Exception as e:
            print(f"{prefix} WARN: could not write part file ({e})", flush=True)

    for idx, job in enumerate(jobs, 1):
        try:
            prob = job["problem"]
            sol = job["solution"]
            tools = job["tools"]
            used_tool_names = set()

            tb_view = [{k: t[k] for k in ("name", "description", "inputs")} for t in tools]
            header = f"Here are the available tools:\n```json\n{json.dumps(tb_view, indent=2)}\n```"

            msgs = [{"role": "system", "content": SYS_SOLVER}, {"role": "user", "content": header}, {"role": "user", "content": prob}]
            turns: List[Dict[str, Any]] = []
            idle, answered = 0, False
            used_tools = False
            num_tool_actions = 0
            dup_counts = defaultdict(int)

            print(f"{prefix} 🔢  Problem {idx}/{len(jobs)}", flush=True)

            for _ in range(16):
                rsp = safe_chat(client, model=solve_model, messages=msgs, temperature=0, max_retries=max_retries, backoff=retry_backoff)
                if rsp is None:
                    note = "Observation: ERROR – LLM request failed repeatedly; skipping this problem."
                    msgs.append({"role": "user", "content": note})
                    turns.append({"role": "user", "content": note})
                    break

                msg = rsp.choices[0].message
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
                            turns.append({"role": "user", "content": err})
                            time.sleep(sleep_time)
                            idle += 1
                            if idle >= 2:
                                remind = "Reminder – output exactly one Thought line and don’t repeat an identical tool call; use the cached Observation instead."
                                msgs += [{"role": "user", "content": remind}]
                                turns.append({"role": "user", "content": remind})
                                idle = 0
                            continue

                    if not isinstance(call, dict) or "name" not in call:
                        err = 'Observation: ERROR – Action must be a JSON object with "name" and "arguments" keys.'
                        msgs += [{"role": "user", "content": err}]
                        turns.append({"role": "user", "content": err})
                        time.sleep(sleep_time)
                        idle += 1
                        if idle >= 2:
                            remind = "Reminder – output exactly one Thought line and don’t repeat an identical tool call; use the cached Observation instead."
                            msgs += [{"role": "user", "content": remind}]
                            turns.append({"role": "user", "content": remind})
                            idle = 0
                        continue

                    args_dict = call.get("arguments", {}) or {}
                    key = _key_for_call(call["name"], args_dict)
                    dup_counts[key] += 1

                    if key in call_cache:
                        obs = call_cache[key]
                        if dup_counts[key] == 1:
                            note = f"Observation (cached): {obs}"
                        elif dup_counts[key] <= MAX_DUP_OBS:
                            note = (
                                f"Observation (cached-duplicate #{dup_counts[key]}): {obs}\n"
                                f"Reminder: You've already called {call['name']} with the same arguments. "
                                "Do not call it again; reuse this Observation and move forward."
                            )
                        else:
                            note = (
                                f"Observation (cached-duplicate #{dup_counts[key]}): {obs}\n"
                                "STOP: Identical Action detected repeatedly. Further identical Actions "
                                "will be ignored. Proceed to the next reasoning step or output ANSWER."
                            )
                        idle += 1
                        msgs += [{"role": "user", "content": note}]
                        turns.append({"role": "user", "content": note})
                        time.sleep(sleep_time)
                        if idle >= 2:
                            remind = "Reminder – output exactly one Thought line and don’t repeat an identical tool call; use the cached Observation instead."
                            msgs += [{"role": "user", "content": remind}]
                            turns.append({"role": "user", "content": remind})
                            idle = 0
                        continue

                    try:
                        tool = next(t for t in tools if t["name"] == call["name"])
                        used_tool_names.add(tool["name"])
                        obs = run_tool(tool, args_dict, tools_dir, override_functions_dir)
                        num_tool_actions += 1
                        used_tools = True
                    except StopIteration:
                        obs = f"ERROR: tool '{call['name']}' not found among provided tools."
                    except Exception as e:
                        obs = f"ERROR: {e}"

                    call_cache[key] = obs
                    note = f"Observation ({call['name']}, {json.dumps(_canon_args(args_dict), separators=(',',':'), sort_keys=True)}): {obs}"
                    msgs += [{"role": "user", "content": note}]
                    turns.append({"role": "user", "content": note})
                    time.sleep(sleep_time)
                    idle = 0
                    continue

                m = ANS_RE.search(text)
                if m:
                    answered = True
                    model_ans = m.group(1).strip()
                    is_corr = llm_grade(client, model_ans, sol, judge_model, max_retries=max_retries, backoff=retry_backoff)
                    record = {
                        "problem": prob,
                        "solution": sol,
                        "model_answer": model_ans,
                        "is_correct": bool(is_corr),
                        "used_tools": used_tools,
                        "num_tool_actions": num_tool_actions,
                        "used_tool_names": sorted(used_tool_names),
                        "tools": [strip_impl(t) for t in tools],
                        "turns": turns,
                    }
                    results.append(record)
                    save_part()
                    if live_q is not None:
                        try:
                            live_q.put({"type": "result", "data": record})
                        except Exception:
                            pass
                    break

                idle += 1
                if idle == 2:
                    remind = "Reminder – output exactly one Thought line and don’t repeat an identical tool call; use the cached Observation instead."
                    msgs += [{"role": "user", "content": remind}]
                    turns.append({"role": "user", "content": remind})
                    idle = 0
                else:
                    msgs += [{"role": "assistant", "content": text}]
                time.sleep(sleep_time)

            if not answered:
                record = {
                    "problem": prob,
                    "solution": sol,
                    "model_answer": None,
                    "is_correct": False,
                    "used_tools": used_tools,
                    "num_tool_actions": num_tool_actions,
                    "used_tool_names": sorted(used_tool_names),
                    "tools": [strip_impl(t) for t in tools],
                    "turns": turns,
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
                "problem": job.get("problem", ""),
                "solution": job.get("solution", ""),
                "model_answer": None,
                "is_correct": False,
                "used_tools": False,
                "num_tool_actions": 0,
                "used_tool_names": [],
                "tools": [strip_impl(t) for t in job.get("tools", [])],
                "turns": [{"role": "system", "content": f"ERROR: {e}"}],
            }
            results.append(record)
            save_part()
            if live_q is not None:
                try:
                    live_q.put({"type": "result", "data": record})
                except Exception:
                    pass


def _worker_entry(shard_id, api_key, chunk, tools_dir_str, override_functions_dir_str, out_part_path, sleep_time, solve_model, judge_model, max_retries, retry_backoff, conn, live_q):
    try:
        worker_run(shard_id, api_key, chunk, tools_dir_str, override_functions_dir_str, out_part_path, sleep_time, solve_model, judge_model, max_retries, retry_backoff, live_q)
        conn.send({"ok": True})
    except Exception as e:
        conn.send({"ok": False, "error": str(e)})
        print(f"[W{shard_id}] ERROR (worker-level): {e}", flush=True)
    finally:
        conn.close()


def build_arg_parser(default_model: str, default_out: str) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--distractors-json", type=str, default=str(DATA_DIR / "distractors_by_level.json"),
                   help="Per-problem dict with {problem, gold_tools, distractors:{level1..5}}")
    p.add_argument("--tool-json", type=str, default=str(DATA_DIR / "ToolMATH.json"),
                   help="Tool metadata JSON used to source official problem/solution text.")
    p.add_argument("--tools-dir", type=str, default=str(DATA_DIR / "function_ToolMATH"),
                   help="Directory containing the Python tool implementations referenced by the selected split.")
    p.add_argument("--level", type=int, default=1, choices=[1, 2, 3, 4, 5],
                   help="distractor difficulty level to use (1..5)")
    p.add_argument("--k", type=int, default=0, help="top-K distractors to add (from the pre-ranked 100)")
    p.add_argument("--num-examples", type=int, default=None, help="limit number of problems")
    p.add_argument("--model", type=str, default=default_model, help="solver model")
    p.add_argument("--judge-model", type=str, default="gpt-4o-mini", help="grading model")
    p.add_argument("--out", type=str, default=default_out, help="final merged pretty JSON output")
    p.add_argument("--live-ndjson", type=str, default=None, help="optional live JSONL")
    p.add_argument("--num-workers", type=int, default=1)
    p.add_argument("--api-key-vars", type=str, default="OPENAI_API_KEY",
                   help="comma-separated env var names for OpenAI-compatible API keys")
    p.add_argument("--sleep", type=float, default=0.7)
    p.add_argument("--no-gold-tools", action="store_true", help="If set, remove all gold tools; provide only distractors.")
    p.add_argument("--max-retries", type=int, default=5)
    p.add_argument("--retry-backoff", type=float, default=0.8)
    return p


def run(default_model: str, default_out_name: str) -> None:
    parser = build_arg_parser(default_model, str(RESULTS_DIR / default_out_name))
    args = parser.parse_args()
    if args.live_ndjson is None:
        args.live_ndjson = str(Path(args.out).with_suffix(".ndjson"))

    rand = random.Random(42)
    dist = json.loads(Path(args.distractors_json).read_text(encoding="utf-8"))
    by_prob: Dict[str, dict] = {normalize_problem(r["problem"]): r for r in dist}
    soln = load_solution_map(Path(args.tool_json))

    problems = [p for p in by_prob.keys() if p in soln]
    rand.shuffle(problems)
    if args.num_examples is not None:
        problems = problems[:args.num_examples]

    mode_str = "NO-GOLD (distractors only)" if args.no_gold_tools else "GOLD+DISTRACTORS"
    print(f"⚙️  Mode: {mode_str} | Level={args.level} | K={args.k}", flush=True)
    print(f"📦 Problems available after joining distractors and tool JSON: {len(problems)}", flush=True)

    jobs_all: List[Dict[str, Any]] = []
    for pnorm in problems:
        rec = by_prob[pnorm]
        gold = rec.get("gold_tools", [])
        decoys = pick_topk(rec, args.level, args.k)
        if args.no_gold_tools:
            gold_names = {t.get("name") for t in gold}
            decoys = [t for t in decoys if t.get("name") not in gold_names]
            tools = dedup_tools_keep_gold_first([], decoys)
        else:
            tools = dedup_tools_keep_gold_first(gold, decoys)
        jobs_all.append({
            "problem": rec["problem"],
            "solution": soln.get(pnorm, ""),
            "tools": tools,
        })

    var_names = [v.strip() for v in (args.api_key_vars or "").split(",") if v.strip()]
    keys = [os.environ.get(v) for v in var_names if os.environ.get(v)]
    if not keys:
        raise SystemExit("No API keys found. Set them in env vars named by --api-key-vars.")
    num_workers = min(args.num_workers, len(keys), max(1, len(jobs_all)))

    chunks: List[List[Dict[str, Any]]] = [[] for _ in range(num_workers)]
    for i, job in enumerate(jobs_all):
        chunks[i % num_workers].append(job)

    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    live_path = Path(args.live_ndjson).resolve() if args.live_ndjson else None

    ctx = mp.get_context("spawn")
    live_q = None
    writer_proc = None
    if live_path is not None:
        live_q = ctx.Queue(maxsize=1000)
        writer_proc = ctx.Process(target=writer_entry, args=(str(live_path), live_q))
        writer_proc.daemon = False
        writer_proc.start()

    parent_conns = []
    procs = []
    for i in range(num_workers):
        api_key = keys[i % len(keys)]
        out_part = f"{str(out_path)}.part{i+1}.json"
        parent_conn, child_conn = ctx.Pipe(False)
        parent_conns.append(parent_conn)
        p = ctx.Process(
            target=_worker_entry,
            args=(i + 1, api_key, chunks[i], args.tools_dir, None, out_part, args.sleep, args.model, args.judge_model, args.max_retries, args.retry_backoff, child_conn, live_q),
        )
        p.daemon = False
        p.start()
        procs.append(p)
        child_conn.close()

    for pc in parent_conns:
        _ = pc.recv()
        pc.close()
    for p in procs:
        p.join()

    if writer_proc is not None and live_q is not None:
        try:
            live_q.put({"type": "STOP"})
            writer_proc.join()
        except Exception:
            pass

    full: List[Dict[str, Any]] = []
    used_live = False
    if live_path is not None and live_path.exists():
        try:
            with live_path.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        full.append(json.loads(line))
            used_live = True
        except Exception as e:
            print(f"⚠️  Could not read live NDJSON '{live_path}': {e}. Falling back to parts.", flush=True)

    if not used_live:
        for part_path in sorted(out_path.parent.glob(out_path.name + ".part*.json")):
            try:
                full.extend(json.loads(part_path.read_text(encoding="utf-8")))
            except Exception as e:
                print(f"⚠️  Could not read part '{part_path}': {e}", flush=True)

    out_path.write_text(json.dumps(full, indent=2), encoding="utf-8")

    total = len(full)
    corr = sum(1 for r in full if r.get("is_correct"))
    acc = 100.0 * corr / max(total, 1)
    print(f"\nFinal Accuracy : {acc:.2f}%  (correct / total = {corr}/{total})")
    print(f"📝  Full log saved to {out_path}", flush=True)
    if live_path is not None:
        print(f"🟢  Live NDJSON was written to {live_path}", flush=True)
