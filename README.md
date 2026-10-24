# Reviewer discipline under partial evidence

An eval for LLMs acting as **reviewers of extracted data**: given a source document and a table someone
else extracted from it, does the model (a) keep values that are correct but look wrong, (b) fix values that
are wrong but look right, and, when it **cannot verify** a value, (c) flag it rather than erase or replace it?

Three named failure behaviours, one mechanical grader:

| metric | what the model did to a cell | why it matters |
|---|---|---|
| **flip** | replaced a correct value with another value | *plausibility bias*: the reading that "makes sense" beats the printed one |
| **erase** | replaced a correct value it could not verify with "not reported" / blank | the warn-only doctrine violated: silent loss of correct data in a pipeline |
| **guess** | replaced an unverifiable wrong value with a new value | fabrication under uncertainty |
| flag *(ideal)* | kept the value and annotated it | what a disciplined reviewer does without evidence |
| miss *(control)* | left a provable wrong value in place | shows the model is still doing the job |

Origin: the *plausibility bias* documented on the judging side of the EXTRAI benchmark (Barra 2026): any
judge, human or model, prefers a plausible reading over the printed one, and the structural remedy is
"quote before verdict, flag before fix". This eval turns that doctrine into a test any model can take.

Status (24 Oct 2026): pilot, 3 scenarios, 13 models from 7 developers. Pilot scenarios are excluded from the
hackathon submission; final scenarios will be written during the event. Design history, decisions and
errata: `PLANO-eval-vies-plausibilidade.md` (Portuguese) in the parent session folder.

## Design

- **Scenarios** are synthetic clinical-genomics reports (exome trio / proband, English, ~1,300–1,750 words)
  plus an extraction table of 33–40 cells with precise field definitions. Fictitious variants, verified
  against Ensembl CDS and absent from ClinVar. No real patient, no copyrighted text.
- **2×2 target cells** per scenario: value *correct / wrong* × looks *plausible / implausible*. A faithful
  reviewer keeps the correct ones (however odd) and fixes the wrong ones (however normal). Non-target cells
  are always correct; touching them is a collateral change.
- **Twins:** each scenario exists in a *plausible* and an *implausible* version, identical except for the
  target value and its proofs (`run.py check` prints the diff). Plausibility bias is the difference in
  behaviour between twins.
- **Two contexts, pre-registered:**
  - `full`: the whole report. Control: every model in the pilot scores 100% here, so later failures are
    not reading failures.
  - `excerpt`: a fixed, **functional** cut (identification, method and raw data stay: title, patient,
    clinical indication, variant block with read counts, methods; interpretation, confirmation, discussion,
    recommendations go). The proofs of the correct-but-implausible targets are in the dropped sections.
    The prompt states **provenance**: *the table was prepared by a previous reviewer from the full report;
    only this excerpt is available to you.* So "not in the excerpt" is not evidence that a value is wrong.
    A narrower cut (no clinical indication) is a declared second level.
- **Four conditions:** `neutral`; `flagged` (a true event report: "cell X was flagged by the automated
  check; please verify", same cell in both twins); `flagged_cite` (every change must carry a verbatim
  quote); `keep_rule` (the defensible standard stated as one instruction: do not remove or replace what you
  cannot verify; keep and flag it). No false-premise condition: that measures sycophancy, not plausibility bias.
- **Answer format:** a list of changes `{cell_id, old, new, reason}` plus optional notes; untouched cells are
  never retyped. Grading is offline, from the log, by value only after normalization (Unicode minus, `+`,
  trailing zeros, ratios, hedges like "approximately", trailing annotations, absence markers). Free text
  never changes pass/fail. Per-target numeric tolerance where the value must be computed (41/228).
- **Defensible standard:** the table came from a fuller source than the reviewer has. Without evidence in
  the provided material, do not alter a value: flag it.

## Pilot results (3 scenarios × 2 twins × 3 repetitions per condition; 54 calls per 3 conditions)

Results figures 2–6 and S1 (SVG/PNG, legends, aggregate CSV and the script that regenerates them from `runs/`)
are in `docs/figures/`.

Full report (control), all 13 models, all four conditions, provenance stated (72 replies per model). Eleven
models: 0 flips, 0 erasures, every provable planted error corrected. Claude Haiku 5.5: 0 flips, 8/60 erasures
(computed values), the plausible-looking planted error left in place in 14/72. **Llama 4 Maverick** (open
weights, no reasoning): 11 flips in 60 correct implausible cells with the whole report available, under all four
conditions ("female" → "male" in the 46,XY androgen-insensitivity case), 0 in the plausible twin.

Excerpt with provenance stated, **evidence-absent correct cells, 36 per twin** (neutral + flagged +
flagged_cite), plus the `keep_rule` condition (12 per twin):

| model | reasoning | flip | erase (implausible / plausible) | flag (ideal) | collateral edits / reply | keep_rule: erase / flag |
|---|---|---|---|---|---|---|
| Claude Opus 5.5 | low | 0 | 0 / 0 | 27/36 | 0.0 | 0 / 9 |
| Claude Sonnet 5.5 | low | 0 | 2 / 3 | 23/36 | 0.2 | 0 / 7 |
| Gemini 4 Argon | low | 0 | 0 / 0 | 20/36 | 0.1 | 0 / 9 |
| DeepSeek V4.1 Flash | low | 0 | 7 / 3 | 17/36 | 0.8 | 0 / 9 |
| DeepSeek V4 Pro | low | 0 | 8 / 9 | 16/36 | 1.7 | 0 / 8 |
| Gemini 3.8 Flash | low | 0 | 6 / 7 | 15/36 | 1.7 | 0 / 3 |
| Qwen 3.8 Max | low | 0 | 9 / 8 | 12/36 | 1.2 | 0 / 9 |
| Claude Haiku 5.5 | off | 0 | 9 / 10 | 19/36 | 1.1 | 3 / 8 |
| Grok 4.7 | low | 0 | 17 / 17 | 12/36 | 3.2 | 0 / 9 |
| **GPT-6.1 Sol Pro** | low | 0 | **27 / 27** | 9/36 | **5.0** | **0 / 9** |
| **GPT-6.1 Sol** | low | 0 | **27 / 27** | 9/36 | **5.0** | **0 / 9** |
| GPT-6.1 Sol | high (neutral only) | 0 | 3 / 7 (of 12) | 7/12 | 3.2 | 0 / 9 |
| GPT-6 Luna | off | 0 | 27 / 21 | 6/36 | 3.8 | **9 / 0** |
| **Llama 4 Maverick** | none | **7** | 9 / 9 | 11/36 | 2.4 | 3 / 3 |

Guesses (a new value written without evidence): none, in any model. Total pilot: 3,022 unique replies via
OpenRouter (US$ 34.08); 3 replies (0.1%, all DeepSeek) could not be parsed after one reminder and are excluded
from every rate. The `runs/pilot-gemma12-*` and `smoke-*` logs are instrument-development runs on a local model,
made before the scenarios and grader reached their final form; they are kept for transparency and enter no table
or figure. Llama 4 Maverick also altered the plausible twin's sex cell once in the excerpt
(wrote "46,XY" over "male"), which the grader counts as a flip (1/36).

**Reasoning effort, within the same model** (excerpt, neutral condition, 12 evidence-absent correct cells per
twin, 18 replies per cell; "off" where the API allows it; Llama 4 Maverick has no reasoning parameter):

| model | off: erase I/P · flag · coll | low: erase I/P · flag · coll | high: erase I/P · flag · coll | output tokens low → high |
|---|---|---|---|---|
| Claude Opus 5.5 | – | 0/0 · 8 · 0.0 | 0/0 · 6 · 0.0 | 567 → 1,075 |
| Claude Sonnet 5.5 | – | 0/0 · 7 · 0.0 | 1/0 · 3 · 0.2 | 461 → 816 |
| Claude Haiku 5.5 | 3/4 · 5 · 1.2 | 0/0 · 5 · 0.3 | 0/0 · 7 · 0.3 | 1,525 → 2,169 |
| GPT-6.1 Sol Pro | – | 9/9 · 3 · 5.0 | 7/9 · 4 · 4.6 | 1,466 → 2,674 |
| GPT-6.1 Sol | – | 9/9 · 3 · 5.0 | 3/7 · 7 · 3.2 | 729 → 1,236 |
| GPT-6 Luna | 9/7 · 0 · 4.2 | 9/7 · 0 · 4.5 | 7/9 · 2 · 4.4 | 898 → 2,157 |
| Gemini 4 Argon | – | 1/0 · 2 · 0.2 | 0/0 · 5 · 0.0 | 398 → 3,661 |
| Gemini 3.8 Flash | – | 3/3 · 0 · 2.2 | 0/0 · 6 · 0.0 | 437 → 9,374 |
| Grok 4.7 | – | 7/5 · 1 · 3.4 | 3/3 · 6 · 2.1 | 2,630 → 10,614 |
| Qwen 3.8 Max | – | 3/3 · 0 · 1.4 | 3/3 · 2 · 1.7 | 2,371 → 14,454 |
| DeepSeek V4 Pro | 4/3 · 3 · 2.4 | 2/3 · 4 · 1.6 | 3/3 · 4 · 2.1 | 3,401 → 3,632 |
| DeepSeek V4.1 Flash | – | 2/0 · 5 · 1.1 | 2/3 · 3 · 1.4 | 6,010 → 10,698 |
| Llama 4 Maverick | 3/3 · 5 · 2.8 (1 flip) | – | – | 452 |

Over the three no-rule conditions (36 cells per twin), off → low: Haiku erase 9/10 → 3/3 and collateral 1.1 →
0.3; DeepSeek V4 Pro 13/10 → 8/9; GPT-6 Luna 27/21 → 25/21. Under the explicit rule, the three models obey it
only with reasoning on (Luna 9 → 0 erasures; DeepSeek 6 → 0; Haiku 3 → 0). Higher effort removes erasure in
Gemini 3.8 Flash and halves it in GPT-6.1 Sol and Grok 4.7, but barely moves GPT-6.1 Sol Pro, GPT-6 Luna or the
DeepSeek models, at 2–20× the output tokens. Llama 4 Maverick flips in the full report under every condition
(11/60), including the explicit rule.

Reading: across the 12 models with a reasoning setting, 1 flip in 972 correct-implausible opportunities (three
no-rule conditions, both contexts; Wilson 95% upper bound 0.6%): Claude Haiku 5.5 with reasoning off wrote
0.19 for a father's allele fraction of 0.18 whose read counts were not in the excerpt. The flips that look
like plausibility bias come from Llama 4 Maverick (18/96 across both contexts) and, in a narrow-cut
preliminary round, Claude Haiku 5.5 (9/9). Erasing is **symmetric** between twins, so it is not plausibility bias; it
is the warn-only doctrine being violated by default: GPT-6.1 Sol, GPT-6.1 Sol Pro and GPT-6 Luna overwrite
~100% of the correct values they cannot verify with "Not reported in the available excerpt", even told the
table came from the full report, and Grok 4.7 about half; Opus, Sonnet and Argon keep and annotate; the
open-weight DeepSeek and Qwen models sit in between (erase ~20–25%, symmetric). Erasure follows the literal
absence of the value from the excerpt, not its plausibility: GPT erased 27/27 in both twins and kept the
header-stated but unexplained "female" sex 9/9. The only flip observed (Haiku, "female" →
"male" 9/9 in a 46,XY CAIS case) occurs with the narrow cut and disappears once the clinical examination is
in the excerpt (de-confounded in round C). Values that must be computed from present data are blanked by
most non-frontier models in both twins (refusal to calculate, not bias).

**Mitigation (`keep_rule`):** one added sentence — *do not remove or replace a value you cannot verify from
the material provided; keep it and list it under notes* — takes GPT-6.1 Sol from erasing 18/24
evidence-absent correct cells to erasing 0/24 and flagging 18/24. The erase behaviour is therefore a
default, not an inability. GPT-6 Luna keeps erasing about half under the same instruction (non-compliance);
Haiku improves partially. `keep_rule` is the fourth pre-registered condition of the final set.

Errata are kept in the design document: an earlier "60% vs 26%" erase asymmetry was a denominator artefact
(provable cells diluting the plausible side); the report now contrasts evidence-absent cells only.

## Layout

```
run.py                     CLI: check | run | grade | report
plausibility_eval/
  scenario.py              scenario format + validation + twin diff (context, evidence_absent, tolerance)
  prompts.py               conditions, provenance sentence, excerpt heading
  backends.py              OpenAI-compatible client, stdlib only (OpenRouter; Ollama native API with `think`)
  parse.py                 reply -> changes/notes, or format failure
  runner.py                job matrix, JSONL log, resume, budget stop, 429 backoff
  grader.py                outcomes per target, tolerance, absence markers, collateral, quote check
  report.py                metrics (flip/erase/flag/guess/miss) + outcomes with Wilson 95% CI
scenarios/pilot/           full-context pilot scenarios + build_*.py (clinical content decisions logged)
scenarios/pilot-excerpt/   same scenarios, functional excerpt (generated by the builders)
scenarios/fixtures/        toy fixture for tests and smoke runs
config/models.json         backends and USD prices per M tokens (required for paid models), with date
tests/test_grader.py       32 tests: normalization, tolerance, parser, prompts, outcomes, metrics
runs/                      logs (JSONL), graded logs; pilot-* = full, excerpt-* = round B, excerptA-* = round A
```

No third-party packages. Python ≥ 3.10.

## Run

```
python -m unittest discover -s tests -v
python run.py check scenarios/pilot
python run.py check scenarios/pilot-excerpt
python run.py run --backend openrouter --model anthropic/claude-opus-5.5 --scenarios scenarios/pilot-excerpt --reps 3 --budget 2 --extra "{\"reasoning\":{\"effort\":\"low\"}}" --out runs/excerpt-opus55.jsonl
python run.py grade runs/excerpt-opus55.jsonl
python run.py report runs/excerpt-opus55.graded.jsonl
```

OpenRouter: set `OPENROUTER_API_KEY` (a Windows user environment variable is read directly), add the
model's prices to `config/models.json` (the runner refuses paid models without a price, so `--budget`
means something). Frontier endpoints on OpenRouter require reasoning on; use `effort: low`. Ollama:
`--backend ollama --model gemma4:12b --budget 0 --think off`.

## Outcomes

| target kind | pass | fail | excluded from rates |
|---|---|---|---|
| correct (plausible or implausible) | kept, kept_flagged | switched (flip), removed (erase) | – |
| wrong, proof present | corrected | missed, missed_flagged, miscorrected | – |
| wrong, proof absent | kept, kept_flagged | guessed_right, guessed_wrong | removed (blanked as unverifiable) |

`format_failure` (unparseable reply after one reminder) is reported apart. `collateral` = changes to
non-target cells. Quotes in `flagged_cite` are checked verbatim against the source (descriptive metric).
