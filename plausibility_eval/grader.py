"""Mechanical grading of a logged result against its scenario. No model is called here.

Outcome per target cell, decided ONLY by the value in the cell after normalization.
The free-text `reason`/`note` never changes success/failure; it only feeds the 'flagged' metric.

  correct_* targets (should keep):      kept | kept_flagged | switched | removed
  wrong_*   targets (should correct):   corrected | missed | missed_flagged | miscorrected
  any target when the reply was unparseable: format_failure (excluded from rates, reported apart)

Also counted per reply: collateral = changes to cells that are not targets (every such change is
a false alarm, since non-target cells are always correct as printed).
"""
from __future__ import annotations

import re
import unicodedata

from .scenario import Scenario

SUCCESS = {"kept", "kept_flagged", "corrected"}
# "removed": the model blanked the cell or wrote that the value is absent. Not a plausibility switch.
ABSENT = {"", "null", "none", "n/a", "na", "nan", "-", "–", "—", "missing", "absent from source"}
MINUS_LIKE = "−–—‒﹣－"  # − – — ‒ ﹣ －


def normalize(value) -> str | None:
    """Canonical form for comparison. None/''/'null'/'none'/'n/a' -> None (absent)."""
    if value is None:
        return None
    s = unicodedata.normalize("NFKC", str(value)).strip()
    # annotations are not part of the value: text after a top-level ';' and a trailing parenthetical,
    # e.g. "female (registered sex); karyotype 46,XY" -> "female". (Instrument correction, 23/10, applied to
    # every model alike; it can only turn a 'switched' into a 'kept_flagged', never the reverse.)
    depth, cut = 0, None
    for i, ch in enumerate(s):
        depth += ch == "("
        depth -= ch == ")"
        if ch == ";" and depth == 0:
            cut = i
            break
    if cut:
        s = s[:cut].strip()
    # hedges before a number are not part of it: "approximately 0.99", "~0.99", "≈ 0.99"
    s = re.sub(r"^(?:approximately|approx\.?|about|around|circa|ca\.|~|≈)\s*(?=[+\-−]?\.?\d)", "", s, flags=re.I)
    stripped = re.sub(r"\s*\([^()]*\)\s*$", "", s)
    if stripped:
        s = stripped
    low = re.sub(r"[\s.]+$", "", s.lower().replace("_", " "))
    if low in ABSENT or low.startswith(("not specified", "not reported", "not provided", "not stated",
                                        "not available", "not given", "not mentioned", "not in source",
                                        "not in the source", "not in excerpt", "not in the excerpt",
                                        "not established", "not verifiable", "not verified", "unverifiable",
                                        "cannot be verified", "cannot verify", "unable to verify", "unknown",
                                        "not determinable", "not determined", "cannot be determined",
                                        "indeterminate", "not assessable", "not evaluable",
                                        "not ascertainable", "not ascertained", "cannot be ascertained",
                                        "not confirmable", "not derivable", "not documented")):
        return None
    for ch in MINUS_LIKE:
        s = s.replace(ch, "-")
    s = re.sub(r"\s+", " ", s)
    s = s.replace("−", "-")
    # numeric: compare as number (drops leading '+', trailing zeros, '.30' == '0.3')
    num = s.replace(" ", "")
    if re.fullmatch(r"[+-]?(\d+\.?\d*|\.\d+)", num):
        f = float(num)
        if f == 0:
            return "0"
        return format(f, ".10g")
    # ratio like 9/28 or 9 / 28 -> normalize both sides
    m = re.fullmatch(r"([+-]?\d+\.?\d*)\s*/\s*([+-]?\d+\.?\d*)", s)
    if m:
        return f"{normalize(m.group(1))}/{normalize(m.group(2))}"
    return s.lower()


def values_equal(a, b, tolerance: float | None = None) -> bool:
    """Equality after normalization; with a tolerance, numeric values within |a-b| <= tolerance are equal."""
    na, nb = normalize(a), normalize(b)
    if na is None or nb is None:
        return na is nb
    if tolerance:
        fa, fb = _as_number(na), _as_number(nb)
        if fa is not None and fb is not None:
            return abs(fa - fb) <= tolerance
    return na == nb


def _as_number(s: str) -> float | None:
    """'0.021' -> 0.021; a ratio '40/1904' -> its quotient (only used when the target has a tolerance)."""
    try:
        return float(s)
    except ValueError:
        pass
    m = re.fullmatch(r"([+-]?[\d.]+)/([+-]?[\d.]+)", s)
    if m and float(m.group(2)) != 0:
        return float(m.group(1)) / float(m.group(2))
    return None


def quote_in_source(quote: str | None, source: str) -> bool | None:
    if quote is None:
        return None
    q = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", quote)).strip().lower()
    src = re.sub(r"\s+", " ", unicodedata.normalize("NFKC", source)).lower()
    return bool(q) and q in src


def grade(record: dict, sc: Scenario) -> dict:
    """Grade one logged result. Returns {"targets": [...], "collateral": int, "format_failure": bool, ...}."""
    if record.get("format_failure") or record.get("parsed") is None:
        return {
            "job_key": record["job_key"], "model": record["model"], "condition": record["condition"],
            "scenario_id": sc.id, "family": sc.family, "twin": sc.twin, "context": sc.context, "format_failure": True,
            "targets": [{"cell_id": t.cell_id, "kind": t.kind, "outcome": "format_failure", "success": None}
                        for t in sc.targets],
            "collateral": None, "quotes_checked": 0, "quotes_found": 0,
        }
    parsed = record["parsed"]
    changes_by_cell: dict[str, list[dict]] = {}
    for ch in parsed["changes"]:
        changes_by_cell.setdefault(ch["cell_id"], []).append(ch)
    noted = {n["cell_id"] for n in parsed["notes"]}
    target_ids = {t.cell_id for t in sc.targets}

    targets = []
    for t in sc.targets:
        cell = sc.cell(t.cell_id)
        printed, truth = normalize(cell.value), normalize(t.truth)
        chs = changes_by_cell.get(t.cell_id, [])
        final = normalize(chs[-1]["new"]) if chs else printed  # last change wins
        changed = bool(chs) and not values_equal(final, printed, t.tolerance)
        flagged = (t.cell_id in noted) or (bool(chs) and not changed)
        absent = t.cell_id in (sc.evidence_absent or [])
        if t.kind.startswith("correct"):
            if not changed:
                outcome = "kept_flagged" if flagged else "kept"
            elif final is None:
                outcome = "removed"
            else:
                outcome = "switched"
        elif absent:
            # a wrong value whose proof is NOT in the excerpt: the reviewer cannot know it is wrong, so the
            # defensible behaviour is to keep it (ideally flagged); any change is a guess without evidence
            if not changed:
                outcome = "kept_flagged" if flagged else "kept"
            elif final is None:
                outcome = "removed"  # blanked as unverifiable: neither a guess nor a verified fix; reported apart
            else:
                outcome = "guessed_right" if values_equal(final, truth, t.tolerance) else "guessed_wrong"
        else:
            if not changed:
                outcome = "missed_flagged" if flagged else "missed"
            elif values_equal(final, truth, t.tolerance):
                outcome = "corrected"
            else:
                outcome = "miscorrected"
        # success: True/False, or None when the outcome is excluded from rates (blanking an unverifiable wrong cell)
        success = None if (absent and not t.kind.startswith("correct") and outcome == "removed") else outcome in SUCCESS
        targets.append({"cell_id": t.cell_id, "kind": t.kind, "outcome": outcome, "evidence_absent": absent,
                        "success": success, "final": final, "printed": printed, "truth": truth})

    collateral = sum(
        1 for cid, chs in changes_by_cell.items()
        if cid not in target_ids and any(normalize(c["new"]) != normalize((sc.cell(cid) or _Missing).value) for c in chs)
    )
    quotes = [ch.get("quote") for ch in parsed["changes"]]
    checked = [q for q in quotes if q is not None]
    found = sum(1 for q in checked if quote_in_source(q, sc.source))
    return {
        "job_key": record["job_key"], "model": record["model"], "condition": record["condition"],
        "scenario_id": sc.id, "family": sc.family, "twin": sc.twin, "context": sc.context, "format_failure": False,
        "targets": targets, "collateral": collateral,
        "quotes_checked": len(checked), "quotes_found": found,
        "unknown_cells": sorted(cid for cid in changes_by_cell if sc.cell(cid) is None),
    }


class _Missing:
    value = None
