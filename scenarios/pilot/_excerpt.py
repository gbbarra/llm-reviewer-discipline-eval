"""Cut a full synthetic report down to the excerpt a retrieval-based reviewer would see.

Functional rule (fixed on 24/10, before any final scenario is written): the excerpt keeps what is
IDENTIFICATION, METHOD and RAW DATA (title block, PATIENT, CLINICAL INDICATION with exam and laboratory
values, the variant block with read counts, METHODS); it drops what is INTERPRETATION, CONFIRMATION,
DISCUSSION, RECOMMENDATIONS and LIMITATIONS (and the RESULT SUMMARY, which is interpretation in short).
That is where the proofs of the correct-but-implausible targets live. Planted wrong cells stay provable
from the raw data.
"""
from __future__ import annotations

import re

HEADING = re.compile(r"^[A-Z][A-Z ,()\-/]+$")
KEEP = ("PATIENT", "CLINICAL INDICATION", "VARIANT REPORTED", "VARIANTS REPORTED", "METHODS")


def excerpt(source: str, keep: tuple[str, ...] = KEEP) -> str:
    blocks: list[tuple[str, list[str]]] = [("", [])]
    for line in source.strip().splitlines():
        if HEADING.match(line.strip()):
            blocks.append((line.strip(), [line]))
        else:
            blocks[-1][1].append(line)
    out: list[str] = []
    first_titled = next((i for i, (h, _) in enumerate(blocks) if h), None)
    for i, (heading, lines) in enumerate(blocks):
        # the report's title block (first heading: "CLINICAL EXOME SEQUENCING REPORT ...") is always kept
        if heading == "" or heading in keep or i == first_titled:
            out.extend(lines)
            out.append("")
    text = "\n".join(out).strip() + "\n"
    # the closing disclaimer is the last paragraph of the full report; keep it in the excerpt too
    tail = source.strip().split("\n\n")[-1]
    if tail.startswith("This is a synthetic report") and tail not in text:
        text += "\n" + tail + "\n"
    return text


def write_pair(HERE, data: dict, scenario_id: str, twin: str, evidence_absent: list[str], note: str) -> None:
    """Write <id>-<twin>.json (full) in HERE and <id>-<twin>-excerpt.json in HERE/../pilot-excerpt."""
    import json

    out = HERE / f"{scenario_id}-{twin}.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {out.name}: {len(data['source'].split())} words, {len(data['table'])} cells")

    ex = dict(data)
    ex["context"] = "excerpt"
    ex["evidence_absent"] = evidence_absent
    ex["source"] = excerpt(data["source"])
    ex["notes"] = data["notes"] + " EXCERPT variant (step 2, 'editing without evidence'): " + note
    exdir = HERE.parent / "pilot-excerpt"
    exdir.mkdir(exist_ok=True)
    out2 = exdir / f"{scenario_id}-{twin}-excerpt.json"
    out2.write_text(json.dumps(ex, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote pilot-excerpt/{out2.name}: {len(ex['source'].split())} words")
