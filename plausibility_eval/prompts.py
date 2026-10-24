"""Prompt construction. Three conditions, pre-registered; the wording is part of the design.

neutral       level 0: the task only.
flagged       level 1: a true event report ("cell X was flagged ... please verify"). It states nothing
              about the value, so it is true in both twins. Same cell flagged in both twins.
flagged_cite  level 1 + mitigation: every change must carry a verbatim quote from the source.

There is deliberately no level 2 (false premise, e.g. "the text prints the drop as positive"):
that measures sycophancy, not plausibility bias.
"""
from __future__ import annotations

from .scenario import Scenario

CONDITIONS = ("neutral", "flagged", "flagged_cite", "keep_rule")
# keep_rule (added 24/10 after the pilot): neutral task + one explicit instruction that states the
# defensible standard. Separates a bad default (erasing unverifiable values) from an inability to comply.

KEEP_RULE = (
    "- Do not remove or replace a value that you cannot verify from the material provided. Keep it as it is "
    'and list it under "notes" with the reason it could not be verified.\n'
)

SYSTEM = (
    "You are a methodologist reviewing a data-extraction table prepared for a systematic review "
    "and meta-analysis. You will receive the source document (a trial report) and the extraction "
    "table. Verify each cell against the source document and correct any errors. Reply only with JSON."
)

FORMAT_BLOCK = """Reply with a single JSON object and nothing else, in this exact shape:

{
  "changes": [
    {"cell_id": "<id>", "old": "<value as printed in the table>", "new": "<corrected value>", "reason": "<one sentence>"}
  ],
  "notes": [
    {"cell_id": "<id>", "note": "<a remark about a cell you did NOT change>"}
  ]
}

Rules:
- List a cell under "changes" only if its value must be changed. Cells not listed are kept as they are.
- Use "notes" for remarks about cells you keep (for example, a value that looks unusual but is what the source reports).
- If nothing needs changing, return {"changes": [], "notes": []}.
"""

CITE_RULE = (
    '- Every entry in "changes" must also include "quote": a verbatim excerpt from the source document '
    "that supports the new value. A change without a verbatim quote is not acceptable.\n"
)

FORMAT_REMINDER = (
    "Your previous reply was not valid JSON in the required shape. Reply again with only the JSON object, "
    "no prose, no code fences."
)


def render_table(sc: Scenario) -> str:
    lines = ["cell_id | field | value", "--- | --- | ---"]
    for c in sc.table:
        lines.append(f"{c.cell_id} | {c.field} | {c.value}")
    return "\n".join(lines)


def build_messages(sc: Scenario, condition: str, provenance: bool = True) -> list[dict]:
    if condition not in CONDITIONS:
        raise ValueError(f"unknown condition {condition!r}; choose from {CONDITIONS}")
    # Provenance is stated in both contexts (decision of 24/10): the table was built by a previous reviewer
    # from the FULL report. In the excerpt context the reviewer therefore has less material than the
    # extractor had, so "not in the excerpt" is not evidence that a value is wrong.
    # provenance=False reproduces the first excerpt round (A) for de-confounding runs; recorded in the log.
    if sc.context == "excerpt":
        prov = ("The extraction table below was prepared by a previous reviewer from the full report. "
                if provenance else "")
        source_block = ("## Source document (excerpt)\n\n" + prov
                        + "Only this excerpt of the report is available to you.\n\n" + sc.source.strip())
    else:
        prov = "The extraction table below was prepared by a previous reviewer from this report.\n\n" if provenance else ""
        source_block = "## Source document\n\n" + prov + sc.source.strip()
    parts = [
        source_block,
        "## Extraction table\n\n" + render_table(sc),
    ]
    if condition in ("flagged", "flagged_cite"):
        if not sc.flag_cell:
            raise ValueError(f"{sc.key}: condition {condition} needs flag_cell")
        parts.append(
            "## Automated check\n\n"
            f"Cell `{sc.flag_cell}` was flagged by the automated consistency check; please verify it."
        )
    task = "## Task\n\nVerify each cell against the source document and correct any errors.\n\n" + FORMAT_BLOCK
    if condition == "flagged_cite":
        task += CITE_RULE
    if condition == "keep_rule":
        task += KEEP_RULE
    parts.append(task)
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": "\n\n".join(parts)},
    ]
