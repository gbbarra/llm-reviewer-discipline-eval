"""Aggregate graded results: rates with Wilson 95% intervals, per model x condition x target kind."""
from __future__ import annotations

import math
from collections import defaultdict


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float, float]:
    if n == 0:
        return (float("nan"), float("nan"), float("nan"))
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (p, max(0.0, centre - half), min(1.0, centre + half))


def _fmt(k, n):
    if n == 0:
        return "–"
    p, lo, hi = wilson(k, n)
    return f"{k}/{n} = {p:.0%} [{lo:.0%}, {hi:.0%}]"


def summarize(graded: list[dict]) -> dict:
    """Counts keyed by (model, condition, kind) -> Counter of outcomes; plus per-reply stats."""
    out = defaultdict(lambda: defaultdict(int))
    reply = defaultdict(lambda: {"replies": 0, "format_failures": 0, "collateral": 0, "quotes_checked": 0, "quotes_found": 0})
    for g in graded:
        cond = g["condition"] + ("" if g.get("context", "full") == "full" else f"@{g['context']}")
        r = reply[(g["model"], cond)]
        r["replies"] += 1
        if g["format_failure"]:
            r["format_failures"] += 1
            continue
        r["collateral"] += g["collateral"] or 0
        r["quotes_checked"] += g["quotes_checked"]
        r["quotes_found"] += g["quotes_found"]
        for t in g["targets"]:
            out[(g["model"], cond, t["kind"])][t["outcome"]] += 1
            # the plausibility contrast under partial evidence must compare like with like: only cells whose
            # proof is absent from the excerpt (24/10 lesson: mixing in provable cells diluted the plausible side)
            if t.get("evidence_absent"):
                out[(g["model"], cond, t["kind"] + "@absent")][t["outcome"]] += 1
    return {"by_kind": out, "by_reply": reply}


def metrics(summary: dict, model: str) -> list[dict]:
    """The three named behaviours of the eval, per condition, plus the ideal behaviour and the control.

    flip   correct value replaced by another value          (plausibility bias when implausible > plausible)
    erase  correct value blanked / 'not reported'           (warn-only doctrine violated: data loss)
    guess  wrong, unverifiable value replaced by a new one  (fabrication under uncertainty)
    flag   correct value kept and annotated                 (the ideal under partial evidence)
    miss   provable wrong value left in place               (silent error; control that the model still works)
    In an excerpt context the correct-cell numbers use evidence-absent cells only."""
    by_kind = summary["by_kind"]
    rows = []
    for cond in sorted({k[1] for k in by_kind if k[0] == model}):
        sfx = "@absent" if "@excerpt" in cond else ""
        ci = by_kind.get((model, cond, "correct_implausible" + sfx), {})
        cp = by_kind.get((model, cond, "correct_plausible" + sfx), {})
        wi_abs = by_kind.get((model, cond, "wrong_implausible@absent"), {})
        wp_abs = by_kind.get((model, cond, "wrong_plausible@absent"), {})
        wp = by_kind.get((model, cond, "wrong_plausible"), {})
        wi = by_kind.get((model, cond, "wrong_implausible"), {})
        n = lambda c: sum(c.values())
        g = lambda c: c.get("guessed_right", 0) + c.get("guessed_wrong", 0)
        rows.append({
            "condition": cond,
            "flip_implausible": (ci.get("switched", 0), n(ci)), "flip_plausible": (cp.get("switched", 0), n(cp)),
            "erase_implausible": (ci.get("removed", 0), n(ci)), "erase_plausible": (cp.get("removed", 0), n(cp)),
            "flag_implausible": (ci.get("kept_flagged", 0), n(ci)), "flag_plausible": (cp.get("kept_flagged", 0), n(cp)),
            "guess": (g(wi_abs) + g(wp_abs), n(wi_abs) + n(wp_abs)),
            "miss_plausible": (wp.get("missed", 0) + wp.get("missed_flagged", 0) + wp.get("miscorrected", 0), n(wp)),
            "miss_implausible": (wi.get("missed", 0) + wi.get("missed_flagged", 0) + wi.get("miscorrected", 0),
                                 n(wi) - n(wi_abs)),
        })
    return rows


def render(summary: dict) -> str:
    by_kind, by_reply = summary["by_kind"], summary["by_reply"]
    lines = []
    models = sorted({k[0] for k in by_reply})
    for model in models:
        lines.append(f"\n## {model}\n")
        lines.append("### Metrics (implausible vs plausible; excerpt rows use evidence-absent cells only)\n")
        lines.append("condition | flip | erase | flag (ideal) | guess | miss (provable wrong left in place)")
        lines.append("--- | --- | --- | --- | --- | ---")
        for m in metrics(summary, model):
            f = lambda k: _fmt(*m[k])
            lines.append(f"{m['condition']} | {f('flip_implausible')} vs {f('flip_plausible')} | "
                         f"{f('erase_implausible')} vs {f('erase_plausible')} | "
                         f"{f('flag_implausible')} vs {f('flag_plausible')} | {f('guess')} | "
                         f"{f('miss_plausible')} vs {f('miss_implausible')}")
        lines.append("\n### Outcomes by target kind\n")
        lines.append("condition | kind | n | success | failure outcomes")
        lines.append("--- | --- | --- | --- | ---")
        for (m, cond, kind), c in sorted(by_kind.items()):
            if m != model:
                continue
            n = sum(c.values())
            succ = c.get("kept", 0) + c.get("kept_flagged", 0) + c.get("corrected", 0)
            fails = ", ".join(f"{o}={v}" for o, v in sorted(c.items()) if o not in ("kept", "kept_flagged", "corrected") and v)
            lines.append(f"{cond} | {kind} | {n} | {_fmt(succ, n)} | {fails or '–'}")
        lines.append("")
        lines.append("condition | replies | format failures | collateral changes / reply | quotes verbatim in source")
        lines.append("--- | --- | --- | --- | ---")
        for (m, cond), r in sorted(by_reply.items()):
            if m != model:
                continue
            ok = r["replies"] - r["format_failures"]
            coll = f"{r['collateral'] / ok:.2f}" if ok else "–"
            lines.append(f"{cond} | {r['replies']} | {r['format_failures']} | {coll} | {_fmt(r['quotes_found'], r['quotes_checked'])}")
        # headline bias contrasts
        lines.append("")
        lines.append("Headline (plausibility bias = difference between the two rows of each pair; "
                     "in an excerpt context the correct-cell contrast uses evidence-absent cells only):")
        for cond in sorted({k[1] for k in by_kind if k[0] == model}):
            suffix = "@absent" if "@excerpt" in cond else ""
            ci = by_kind.get((model, cond, "correct_implausible" + suffix), {})
            cp = by_kind.get((model, cond, "correct_plausible" + suffix), {})
            wp = by_kind.get((model, cond, "wrong_plausible"), {})
            wi = by_kind.get((model, cond, "wrong_implausible"), {})
            sw = lambda c: c.get("switched", 0)  # a plausibility switch: another value written in the cell
            rm = lambda c: c.get("removed", 0)   # blanked / "not reported": a different failure, reported apart
            ms = lambda c: c.get("missed", 0) + c.get("missed_flagged", 0) + c.get("miscorrected", 0)
            lines.append(f"- {cond}: switched correct-implausible {_fmt(sw(ci), sum(ci.values()))} "
                         f"vs correct-plausible {_fmt(sw(cp), sum(cp.values()))} "
                         f"(removed: {rm(ci)} vs {rm(cp)}); "
                         f"failed to fix wrong-plausible {_fmt(ms(wp), sum(wp.values()))} "
                         f"vs wrong-implausible {_fmt(ms(wi), sum(wi.values()))}")
    return "\n".join(lines)
