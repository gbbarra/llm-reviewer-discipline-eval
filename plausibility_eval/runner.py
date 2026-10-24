"""Run the job matrix (scenarios x conditions x reps), log everything to JSONL, stop at the budget.

Each job is an independent conversation. Order is shuffled with a fixed seed so twins and
conditions are interleaved. A run can be resumed: jobs already in the log are skipped.
Grading never happens here; it is computed offline from the log by grader.py.
"""
from __future__ import annotations

import datetime as dt
import json
import random
import sys
import uuid
from pathlib import Path

from .backends import Backend, chat, cost_usd, price_for
from .parse import parse_response
from .prompts import FORMAT_REMINDER, build_messages
from .scenario import Scenario


def job_key(sc: Scenario, condition: str, rep: int) -> str:
    return f"{sc.key}|{condition}|{rep}"


def existing_keys(log_path: Path) -> set[str]:
    keys = set()
    if log_path.exists():
        for line in log_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rec = json.loads(line)
                if rec.get("type", "result") == "result":
                    keys.add(rec["job_key"])
    return keys


def spent_usd(log_path: Path) -> float:
    total = 0.0
    if log_path.exists():
        for line in log_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rec = json.loads(line)
                total += rec.get("cost_usd", 0.0) or 0.0
    return total


def run_matrix(
    backend: Backend,
    model: str,
    scenarios: list[Scenario],
    conditions: list[str],
    reps: int,
    log_path: Path,
    budget_usd: float,
    temperature: float | None = None,
    max_tokens: int = 4096,
    seed: int = 20261030,
    extra: dict | None = None,
    think: bool | None = None,
    provenance: bool = True,
) -> dict:
    price = price_for(backend, model)
    free = price["input"] == 0 and price["output"] == 0
    if budget_usd <= 0 and not free:
        raise RuntimeError(f"{backend.name}/{model} is a paid model: --budget must be > 0")
    jobs = [(sc, cond, rep) for sc in scenarios for cond in conditions for rep in range(reps)]
    random.Random(seed).shuffle(jobs)
    done = existing_keys(log_path)
    spent = spent_usd(log_path)
    run_id = uuid.uuid4().hex[:8]
    stats = {"run_id": run_id, "planned": len(jobs), "skipped": 0, "completed": 0, "failed": 0, "spent_usd": spent}
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with log_path.open("a", encoding="utf-8") as log:
        for sc, cond, rep in jobs:
            key = job_key(sc, cond, rep)
            if key in done:
                stats["skipped"] += 1
                continue
            if not free and spent >= budget_usd:  # a free (local) model never budget-stops
                log.write(json.dumps({"type": "budget_stop", "run_id": run_id, "spent_usd": spent, "budget_usd": budget_usd,
                                      "ts": _now()}) + "\n")
                print(f"BUDGET STOP: spent {spent:.4f} >= {budget_usd} USD", file=sys.stderr)
                stats["budget_stop"] = True
                break

            messages = build_messages(sc, cond, provenance=provenance)
            attempts = []
            parsed, parse_error = None, None
            total_usage: dict = {"prompt_tokens": 0, "completion_tokens": 0}
            try:
                for attempt in range(2):  # one format retry, pre-registered
                    res = chat(backend, model, messages, temperature=temperature, max_tokens=max_tokens, extra=extra,
                               think=think)
                    for k in total_usage:
                        total_usage[k] += res.usage.get(k, 0)
                    parsed, parse_error = parse_response(res.content)
                    attempts.append({"content": res.content, "reasoning": res.reasoning, "usage": res.usage,
                                     "latency_s": round(res.latency_s, 2), "parse_error": parse_error})
                    if parsed is not None:
                        break
                    messages = messages + [{"role": "assistant", "content": res.content},
                                           {"role": "user", "content": FORMAT_REMINDER}]
                cost = cost_usd(price, total_usage)
                spent += cost
                rec = {
                    "type": "result", "run_id": run_id, "ts": _now(), "job_key": key,
                    "backend": backend.name, "model": model, "temperature": temperature, "max_tokens": max_tokens,
                    "extra": extra or {}, "think": think, "provenance": provenance,
                    "scenario_id": sc.id, "family": sc.family, "twin": sc.twin, "context": sc.context,
                    "scenario_path": sc.path,
                    "condition": cond, "rep": rep,
                    "messages": build_messages(sc, cond, provenance=provenance),
                    "attempts": attempts, "parsed": parsed, "format_failure": parsed is None,
                    "usage": total_usage, "cost_usd": cost,
                }
                stats["completed"] += 1
            except Exception as e:  # network/HTTP errors are logged, not graded
                rec = {"type": "error", "run_id": run_id, "ts": _now(), "job_key": key, "backend": backend.name,
                       "model": model, "scenario_id": sc.id, "twin": sc.twin, "condition": cond, "rep": rep,
                       "error": repr(e), "cost_usd": 0.0}
                stats["failed"] += 1
                print(f"ERROR {key}: {e}", file=sys.stderr)
            log.write(json.dumps(rec, ensure_ascii=False) + "\n")
            log.flush()
            print(f"[{stats['completed'] + stats['failed']}/{len(jobs) - stats['skipped']}] {key} "
                  f"{'ok' if rec['type'] == 'result' and not rec['format_failure'] else rec['type'] if rec['type'] != 'result' else 'FORMAT'} "
                  f"spent={spent:.4f}", file=sys.stderr)
    stats["spent_usd"] = spent
    return stats


def _now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
