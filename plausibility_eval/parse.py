"""Turn a model reply into the {"changes": [...], "notes": [...]} structure, or report why not.

Tolerant to code fences, leading prose and <think>...</think> blocks; strict about the shape.
Returns (parsed, None) or (None, error_string). A None result is a *format failure*, which the
grader reports separately and never counts as bias.
"""
from __future__ import annotations

import json
import re

_THINK = re.compile(r"<think>.*?</think>", re.DOTALL)
_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)


def _candidates(text: str):
    text = _THINK.sub("", text).strip()
    for m in _FENCE.finditer(text):
        yield m.group(1).strip()
    yield text
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end > start:
        yield text[start:end + 1]


def _as_str(v) -> str | None:
    if v is None:
        return None
    if isinstance(v, bool):
        return str(v).lower()
    if isinstance(v, (int, float)):
        return repr(v) if isinstance(v, float) else str(v)
    return str(v)


def parse_response(text: str) -> tuple[dict | None, str | None]:
    last_err = "no JSON object found"
    for cand in _candidates(text or ""):
        try:
            obj = json.loads(cand)
        except json.JSONDecodeError as e:
            last_err = f"JSON decode error: {e.msg}"
            continue
        if not isinstance(obj, dict):
            last_err = "top level is not an object"
            continue
        changes = obj.get("changes", [])
        notes = obj.get("notes", [])
        if not isinstance(changes, list) or not isinstance(notes, list):
            last_err = "'changes' and 'notes' must be lists"
            continue
        out_changes, out_notes = [], []
        ok = True
        for ch in changes:
            if not isinstance(ch, dict) or "cell_id" not in ch or "new" not in ch:
                ok, last_err = False, "a change lacks cell_id or new"
                break
            out_changes.append({
                "cell_id": str(ch["cell_id"]),
                "old": _as_str(ch.get("old")),
                "new": _as_str(ch.get("new")),
                "reason": _as_str(ch.get("reason")) or "",
                "quote": _as_str(ch.get("quote")),
            })
        if not ok:
            continue
        for n in notes:
            if not isinstance(n, dict) or "cell_id" not in n:
                ok, last_err = False, "a note lacks cell_id"
                break
            out_notes.append({"cell_id": str(n["cell_id"]), "note": _as_str(n.get("note")) or ""})
        if not ok:
            continue
        return {"changes": out_changes, "notes": out_notes}, None
    return None, last_err
