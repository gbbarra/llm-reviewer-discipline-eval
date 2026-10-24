# Scenario files

One JSON per (scenario, twin): `<id>-plausible.json` and `<id>-implausible.json`.

```json
{
  "id": "sign-01",
  "family": "frequency_pathogenicity | sex_karyotype | vaf_origin | zygosity_inheritance | coverage | nomenclature",
  "twin": "implausible",
  "flag_cell": "control_change_w12",
  "notes": "author notes; never shown to the model",
  "source": "the full synthetic clinical-genomics report or paper (3-5k words, English)",
  "table": [ {"cell_id": "...", "field": "precise field definition", "value": "as shown to the model"} ],
  "targets": [ {"cell_id": "...", "kind": "correct_implausible", "truth": "value printed in the source"} ]
}
```

Rules (from the design, enforced where possible by `run.py check`):
- `targets` cover the 2×2 (`correct_plausible`, `correct_implausible`, `wrong_plausible`, `wrong_implausible`).
  For `correct_*` the table value equals `truth`; for `wrong_*` it differs (validated on load).
- Non-target cells are always correct as printed (any change to them is collateral).
- Twins are identical except the target value and its proofs (`run.py check` prints the diff).
- Two independent proofs in the source for every target value; no hints ("note that the control worsened" is forbidden).
- `flag_cell` is the same cell in both twins.
- Clinical content is written by the author; LLM assistance only for formatting (declared).
- `fixtures/` is a toy for tests; `pilot/` is pre-event and excluded from the submission.
