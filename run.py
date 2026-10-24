"""Command line.

  python run.py check   scenarios/pilot                 validate scenarios, show twin diffs
  python run.py run     --backend ollama --model gemma4:12b --scenarios scenarios/pilot \
                        --conditions neutral,flagged,flagged_cite --reps 3 --budget 0 --out runs/pilot-gemma12.jsonl
  python run.py grade   runs/pilot-gemma12.jsonl        grade offline -> runs/pilot-gemma12.graded.jsonl
  python run.py report  runs/*.graded.jsonl             aggregate tables with Wilson intervals
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from plausibility_eval.backends import load_backend
from plausibility_eval.grader import grade
from plausibility_eval.prompts import CONDITIONS
from plausibility_eval.report import render, summarize
from plausibility_eval.runner import run_matrix
from plausibility_eval.scenario import load_dir, load_scenario, twin_diff


def cmd_check(a):
    scs = load_dir(a.scenarios)
    by_id = {}
    for sc in scs:
        by_id.setdefault((sc.id, sc.context), {})[sc.twin] = sc
        print(f"OK  {sc.key:40s} family={sc.family:12s} cells={len(sc.table):3d} words={len(sc.source.split()):5d} targets="
              + ",".join(f"{t.cell_id}:{t.kind}" for t in sc.targets)
              + (f"  evidence_absent={','.join(sc.evidence_absent)}" if sc.evidence_absent else ""))
    for sid, twins in by_id.items():
        if set(twins) != {"plausible", "implausible"}:
            print(f"WARN {sid}: missing twin ({sorted(twins)})")
            continue
        diff = twin_diff(twins["plausible"], twins["implausible"])
        print(f"\n--- twin diff {sid} ({len(diff)} changed lines; must be only the target value and its proofs)")
        for line in diff:
            print("   ", line)


def cmd_run(a):
    backend = load_backend(a.backend)
    scs = load_dir(a.scenarios)
    conds = [c.strip() for c in a.conditions.split(",")]
    bad = [c for c in conds if c not in CONDITIONS]
    if bad:
        sys.exit(f"unknown conditions {bad}; choose from {CONDITIONS}")
    extra = json.loads(a.extra) if a.extra else None
    think = {"on": True, "off": False, "default": None}[a.think]
    stats = run_matrix(backend, a.model, scs, conds, a.reps, Path(a.out), a.budget,
                       temperature=a.temperature, max_tokens=a.max_tokens, seed=a.seed, extra=extra, think=think,
                       provenance=not a.no_provenance)
    print(json.dumps(stats, indent=2))


def cmd_grade(a):
    for log in a.logs:
        log = Path(log)
        out = log.with_suffix(".graded.jsonl")
        cache: dict[str, object] = {}
        n, seen, dups = 0, set(), 0
        with out.open("w", encoding="utf-8") as fo:
            for line in log.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                rec = json.loads(line)
                if rec.get("type", "result") != "result":
                    continue
                if rec["job_key"] in seen:  # two runs appended to the same log concurrently: first result wins
                    dups += 1
                    continue
                seen.add(rec["job_key"])
                sc = cache.get(rec["scenario_path"]) or cache.setdefault(rec["scenario_path"], load_scenario(rec["scenario_path"]))
                fo.write(json.dumps(grade(rec, sc), ensure_ascii=False) + "\n")
                n += 1
        print(f"graded {n} results -> {out}" + (f" (skipped {dups} duplicate job keys)" if dups else ""))


def cmd_report(a):
    graded = []
    for p in a.graded:
        for line in Path(p).read_text(encoding="utf-8").splitlines():
            if line.strip():
                graded.append(json.loads(line))
    print(render(summarize(graded)))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check"); c.add_argument("scenarios"); c.set_defaults(fn=cmd_check)

    r = sub.add_parser("run")
    r.add_argument("--backend", required=True)
    r.add_argument("--model", required=True)
    r.add_argument("--scenarios", required=True)
    r.add_argument("--conditions", default=",".join(CONDITIONS))
    r.add_argument("--reps", type=int, default=3)
    r.add_argument("--budget", type=float, required=True,
                   help="USD ceiling for this log file, CUMULATIVE over everything already in it (0 for Ollama); "
                        "when appending a new condition to an existing log, add the new allowance to the spend already logged")
    r.add_argument("--out", required=True)
    r.add_argument("--temperature", type=float, default=None, help="omit to use the provider default; record it")
    r.add_argument("--max-tokens", type=int, default=4096)
    r.add_argument("--no-provenance", action="store_true",
                   help="omit the 'table was prepared from the full report' sentence (de-confounding runs only)")
    r.add_argument("--think", choices=["on", "off", "default"], default="default",
                   help="Ollama native API only: hidden reasoning on/off (recorded in the log)")
    r.add_argument("--seed", type=int, default=20261030)
    r.add_argument("--extra", default=None, help='JSON merged into the request body, e.g. {"reasoning":{"effort":"low"}}')
    r.set_defaults(fn=cmd_run)

    g = sub.add_parser("grade"); g.add_argument("logs", nargs="+"); g.set_defaults(fn=cmd_grade)
    t = sub.add_parser("report"); t.add_argument("graded", nargs="+"); t.set_defaults(fn=cmd_report)

    a = p.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()
