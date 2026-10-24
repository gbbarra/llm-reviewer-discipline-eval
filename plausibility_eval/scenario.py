"""Scenario files: one JSON per (scenario, twin).

A scenario is a synthetic trial report plus an extraction table shown to the model.
`targets` tell the grader what each target cell really is; the model never sees them.

Target kinds (the 2x2 design):
  correct_plausible    printed value is correct and looks normal      -> model should keep
  correct_implausible  printed value is correct but looks wrong       -> model should keep
  wrong_plausible      printed value is wrong but looks normal        -> model should correct
  wrong_implausible    printed value is wrong and looks wrong         -> model should correct
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

KINDS = ("correct_plausible", "correct_implausible", "wrong_plausible", "wrong_implausible")
TWINS = ("plausible", "implausible")


@dataclass
class Cell:
    cell_id: str
    field: str
    value: str


@dataclass
class Target:
    cell_id: str
    kind: str
    truth: str  # the value printed in the source (what a faithful reviewer ends with)
    tolerance: float | None = None  # absolute numeric tolerance, for values the reviewer must compute (e.g. 41/228)


@dataclass
class Scenario:
    id: str
    family: str
    twin: str
    source: str
    table: list[Cell]
    targets: list[Target]
    flag_cell: str | None = None
    notes: str = ""
    path: str = ""
    context: str = "full"  # "full": whole report; "excerpt": proofs of the correct targets are outside the text
    evidence_absent: list[str] | None = None  # cell_ids whose proofs are not in the excerpt (documentation)

    def cell(self, cell_id: str) -> Cell | None:
        return next((c for c in self.table if c.cell_id == cell_id), None)

    def target(self, cell_id: str) -> Target | None:
        return next((t for t in self.targets if t.cell_id == cell_id), None)

    @property
    def key(self) -> str:
        return f"{self.id}/{self.twin}" + ("" if self.context == "full" else f"/{self.context}")


class ScenarioError(ValueError):
    pass


def load_scenario(path: str | Path) -> Scenario:
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    try:
        sc = Scenario(
            id=data["id"],
            family=data["family"],
            twin=data["twin"],
            source=data["source"],
            table=[Cell(**c) for c in data["table"]],
            targets=[Target(**t) for t in data["targets"]],
            flag_cell=data.get("flag_cell"),
            notes=data.get("notes", ""),
            path=str(path),
            context=data.get("context", "full"),
            evidence_absent=data.get("evidence_absent"),
        )
    except (KeyError, TypeError) as e:
        raise ScenarioError(f"{path}: malformed scenario ({e})") from e
    _validate(sc)
    return sc


def _validate(sc: Scenario) -> None:
    from .grader import values_equal  # local import: grader also imports this module

    ids = [c.cell_id for c in sc.table]
    if len(ids) != len(set(ids)):
        raise ScenarioError(f"{sc.key}: duplicate cell_id in table")
    if sc.twin not in TWINS:
        raise ScenarioError(f"{sc.key}: twin must be one of {TWINS}")
    if not sc.targets:
        raise ScenarioError(f"{sc.key}: no targets")
    for t in sc.targets:
        if t.kind not in KINDS:
            raise ScenarioError(f"{sc.key}: target {t.cell_id} has unknown kind {t.kind!r}")
        cell = sc.cell(t.cell_id)
        if cell is None:
            raise ScenarioError(f"{sc.key}: target {t.cell_id} is not in the table")
        same = values_equal(cell.value, t.truth, t.tolerance)
        if t.kind.startswith("correct") and not same:
            raise ScenarioError(f"{sc.key}: {t.cell_id} is 'correct' but table value {cell.value!r} != truth {t.truth!r}")
        if t.kind.startswith("wrong") and same:
            raise ScenarioError(f"{sc.key}: {t.cell_id} is 'wrong' but table value equals truth {t.truth!r}")
    if sc.flag_cell is not None and sc.cell(sc.flag_cell) is None:
        raise ScenarioError(f"{sc.key}: flag_cell {sc.flag_cell!r} is not in the table")
    if sc.context not in ("full", "excerpt"):
        raise ScenarioError(f"{sc.key}: context must be 'full' or 'excerpt'")
    for cid in sc.evidence_absent or []:
        if sc.cell(cid) is None:
            raise ScenarioError(f"{sc.key}: evidence_absent cell {cid!r} is not in the table")


def load_dir(path: str | Path) -> list[Scenario]:
    files = sorted(Path(path).glob("*.json"))
    if not files:
        raise ScenarioError(f"no scenario files in {path}")
    return [load_scenario(f) for f in files]


def twin_diff(a: Scenario, b: Scenario) -> list[str]:
    """Lines that differ between the two twins' sources, for the identical-twins check."""
    import difflib

    return [
        line
        for line in difflib.unified_diff(a.source.splitlines(), b.source.splitlines(), lineterm="", n=0)
        if line.startswith(("+", "-")) and not line.startswith(("+++", "---"))
    ]
