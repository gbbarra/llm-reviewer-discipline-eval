# Results figures: legends

All figures are regenerated from `runs/` by `python docs/figures/make_results_figs.py`, which also writes the
aggregate numbers to `results-figures-data.csv` (one row per plotted number, with k, n, rate and Wilson 95%
interval) and stops if any of the README numbers it re-derives does not match.

**Common definitions.** Each scenario is a synthetic clinical-genomics report with an extraction table; it exists
as an *implausible* twin (the correct value runs against expectation) and a *plausible* twin (same table, ordinary
value). The twin contrast uses the target cells that hold the counter-intuitive value in the implausible twin and
their counterparts in the plausible twin (5 per reply in the full report; in the excerpt, the 4 whose proof was
cut out, i.e. evidence-absent cells). Outcomes on a correct cell: *kept* (unchanged, no note), *kept and flagged*
(unchanged, with a note), *erased* (blanked or written as "not reported"), *flipped* (replaced by another value).
*Miss*: a provable planted error left in place (missed, missed with a note, or replaced by another wrong value).
*Collateral edits*: changes to non-target cells, all of which are correct as printed; mean per reply. Each
condition × twin × scenario was run 3 times (9 replies per condition and twin). Replies that could not be parsed
(3 in all: two DeepSeek V4.1 Flash excerpt replies, one DeepSeek V4 Pro excerpt reply with reasoning off) are
excluded from every rate; this is why a few n values are below the nominal one. Intervals: Wilson 95%.
Colours follow Fig. 1: green = kept and flagged, vermilion = erased, blue = flipped, grey = kept without a note;
Llama 4 Maverick, the only model without a reasoning parameter, is marked in bold (and in yellow where shaded).

---

**Figure 2. Plausibility flip: only the model without reasoning replaces correct implausible values.**
Proportion of correct target cells replaced by another value, implausible twin (filled) versus plausible twin
(open), with Wilson 95% intervals; one row per model, in the order of Fig. 3. Conditions neutral, flagged and
flagged + cite (the explicit keep rule is excluded). **(A)** Full report with provenance stated, n = 45 cells per
twin and model. Llama 4 Maverick flips 8/45 (11/60 when the keep-rule condition is included), always "female" →
"male" in the 46,XY complete androgen-insensitivity case; 0/45 in the plausible twin. **(B)** Excerpt with
provenance stated, evidence-absent cells only, n = 36 per twin and model (34 for DeepSeek V4.1 Flash, implausible
twin). Llama 4 Maverick 7/36 versus 1/36; the plausible-twin event is the karyotype "46,XY" written into the sex
cell of the plausible twin (registered sex "male"), which the grader counts as a replacement. Claude Haiku 5.5
(reasoning off) 1/36: 0.19 written for a paternal allele fraction of 0.18 whose read counts were outside the
excerpt. Across the 12 models with a reasoning setting, 1 flip in 970 parsed correct-implausible cells (both
contexts, three conditions; 972 nominal). **(C)** Preliminary round, Claude Haiku 5.5 with reasoning off, without
the provenance sentence: with a narrower cut that also drops the clinical examination, "female" → "male" in 9/9
replies of the implausible twin and 0/9 of the plausible twin; with the functional cut (examination kept),
0/9. Cells: registered sex in the androgen-insensitivity scenario, three conditions × 3 replies.

**Figure 3. Under partial evidence, erasing is symmetric between twins.** Outcome of every correct cell whose
proof is absent from the excerpt, as a 100% stacked bar per model and twin (I = implausible, P = plausible),
pooled over the neutral, flagged and flagged + cite conditions (n = 36 cells per bar; 34 for DeepSeek V4.1 Flash,
implausible twin). Numbers inside the bars are cell counts (omitted for segments under 6%). Models are ordered by
the proportion erased (both twins), ties broken by more flagging. Erasure is about equal in the two twins of each
model, so it follows the literal absence of the value's proof, not its plausibility: GPT-6.1 Sol and Sol Pro erase
27/36 in both twins (the 9 kept are the registered sex, stated in the header but unexplained), Grok 4.7 17/36 in
both; Claude Opus 5.5 and Gemini 4 Argon keep almost everything and flag most of it. Flips (blue) appear only in
Llama 4 Maverick and in one Claude Haiku 5.5 reply (see Fig. 2).

**Figure 4. Collateral edits appear only under partial evidence.** Mean number of changes to non-target cells
(cells that are correct as printed) per reply, full report (open) versus excerpt (filled), conditions neutral,
flagged and flagged + cite; 27 replies per model and context (25 for DeepSeek V4.1 Flash in the excerpt). With the
whole report every model stays at or below 0.2 edits per reply; with the excerpt the models that erase target
cells also blank non-target cells (GPT-6.1 Sol and Sol Pro 5.0 per reply).

**Figure 5. One sentence stops erasure in 10 of 13 models.** Erased evidence-absent correct cells over all
evidence-absent correct cells (both twins pooled; n = 24 per cell: 12 per twin, 9 replies per twin; 23 for DeepSeek
V4.1 Flash in two conditions), excerpt with provenance stated, by instruction condition. *Neutral*: check each cell
against the source and correct errors. *Flagged*: a true report that one target cell was flagged by an automated
check. *Flagged + cite*: every change must carry a verbatim quote. *Keep rule*: do not remove or replace a value
that cannot be verified from the material provided; keep it and say why. Shading is proportional to the rate.
Models in the order of Fig. 3. Under the keep rule erasure falls to 0 in 10 models; it persists in Llama 4 Maverick
(6/24), Claude Haiku 5.5 with reasoning off (5/24) and GPT-6 Luna with reasoning off (12/24).

**Figure 6. Reasoning effort, within model.** Excerpt with provenance stated, neutral condition only, 12
evidence-absent correct cells per twin and 18 replies per level (DeepSeek V4 Pro off: 10 cells in the implausible
twin after one unparsed reply). Off = reasoning disabled where the API allows it (Claude Haiku 5.5, GPT-6 Luna,
DeepSeek V4 Pro; Llama 4 Maverick has no reasoning parameter and appears only as "off"); low = the setting of the
main round; high = a separate run at high effort. Points of the same model are offset vertically (off above, high
below) so that equal values remain visible. **(A)** Proportion of correct values erased, both twins pooled
(n = 24). Raising effort to high removes erasure in Gemini 3.8 Flash (6/24 → 0/24), lowers it in GPT-6.1 Sol
(18 → 10) and Grok 4.7 (12 → 6), and barely moves GPT-6.1 Sol Pro (18 → 16), GPT-6 Luna (16 → 16), Qwen 3.8 Max
(6 → 6) and the DeepSeek models; turning reasoning on (off → low) removes it in Claude Haiku 5.5 (7 → 0).
**(B)** Mean output (completion) tokens per reply, log scale, from the raw logs (first logged result per job);
labels give the high / low ratio.

**Figure S1. Summary of the five metrics under partial evidence.** Excerpt with provenance stated, conditions
neutral, flagged and flagged + cite. *Flip*: correct implausible evidence-absent cells replaced by another value
(%, n = 36). *Erase* and *flag*: evidence-absent correct cells erased, or kept with a note (%, both twins, n = 72).
*Miss*: provable planted errors left in place (%, n = 108 wrong cells whose correction is verifiable from the
excerpt; 104 for DeepSeek V4.1 Flash). *Collateral*: mean edits to non-target cells per reply. Each column is shaded on its own scale (rates
0–100%, collateral 0–6 per reply). Models in the order of Fig. 3.
