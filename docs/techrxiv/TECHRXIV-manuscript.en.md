# Discipline of language models reviewing data extracted from genomic reports under full and partial evidence: plausibility bias, erasure, and the effect of a keep rule

**Short title:** Language-model reviewers under partial evidence

**Gustavo Barcelos Barra**¹

¹ Base by Base, Brasília, DF, Brazil. ORCID 0000-0002-2136-3471.

**Correspondence:** Gustavo Barcelos Barra, gustavo@basebybase.com

**Keywords:** large language models; data extraction; automated review; clinical genomics; plausibility bias; context faithfulness; prompt engineering; data safety

**Subject (TechRxiv):** Computing and Processing; Bioengineering

**Code, scenarios, prompts, logs, and data:** https://github.com/gbbarra/llm-reviewer-discipline-eval

---

## Abstract

**Background.** Large language models (LLMs) are used as reviewers of tables extracted by an earlier step of a pipeline. In this role, the model must keep correct values even when they look wrong, correct errors, and, when it cannot verify a value, flag it instead of erasing it. We found no studies that measure these three behaviours separately.

**Methods.** Thirteen models from seven developers reviewed tables of 33 to 40 cells extracted from three synthetic clinical exome reports. Each report has an identical twin in which the correct target value is counterintuitive (implausible twin) or common (plausible twin), plus planted plausible and implausible errors. The models received the full report or an excerpt without the sections that prove the counterintuitive values, with a statement that the table had been prepared from the full report. Four instructions (neutral, true alert, mandatory citation, keep rule) and three levels of reasoning effort were compared. A mechanical grader classified each cell as kept, kept and flagged, erased, flipped, corrected, or not corrected. A total of 3,019 responses were analysed.

**Results.** In the 12 models with a reasoning parameter, correct counterintuitive values were flipped in 1 of 970 cells (0.1%; 95% CI 0.02% to 0.58%). Llama 4 Maverick, without reasoning, flipped 8 of 45 in the full report and 7 of 36 in the excerpt, always "female" to "male" in a 46,XY patient with androgen insensitivity. Without the proof in the excerpt, the models diverged: Claude Opus 5.5 and Gemini 4 Argon kept almost everything and flagged it; GPT-6.1 Sol and Sol Pro erased 27 of 36 cells in each twin and changed on average 5.0 non-target cells per response. Erasure was equal in the two twins, which indicates a reaction to the literal absence of the text, not to plausibility. A keep sentence brought erasure to zero in 10 of the 13 models; raising reasoning effort cost 1.1 to 21.5 times more tokens and reduced erasure in only three models.

**Conclusions.** In models with reasoning, the risk is not the flipping of atypical values but the erasure of correct values under partial evidence. This behaviour is a default of some models and disappears with an explicit keep instruction.

---

## Introduction

Data extraction from documents is an error-prone step in systematic reviews and in clinical records. In systematic reviews, single extraction by humans generates more errors than double extraction, and methodological reviews estimate relevant error frequencies even with trained extractors [1,2]. Large language models (LLMs) have come to be evaluated as extractors in this context, with high accuracy on simple fields and errors concentrated in numerical values and in fields that require interpretation [3–5]. A common response to these errors is to add a second step, in which a model reviews the table produced by the first, in the pattern known as "LLM as a judge" [6,7].

The reviewer role creates two distinct risks. The first is plausibility bias: the reviewer replaces a correct but counterintuitive value with a value that seems more likely to it. Language models show content effects on reasoning tasks, with performance that depends on whether the statement is plausible, and tend to agree with premises presented by the user, including false premises in a medical context [8–12]. In clinical genomics, correct values often contradict expectation: a rare pathogenic variant can have a high allele frequency in a population isolate, a patient with a female phenotype can have a 46,XY karyotype, and a variant thought to be de novo can be mosaic in one of the parents [13–15].

The second risk arises when the reviewer does not have access to the whole document. In real pipelines, the table travels with an excerpt of the document, a summary, or a methods block, not with the full text. Faced with a correct value whose proof is not in the excerpt, the reviewer may treat the absence as evidence of error and replace the value with a missing-value marker. The literature on context faithfulness and on abstention describes what the model does when the answer is not in the material provided, from the standpoint of the unanswerable question or of the conflict between context and prior knowledge [16–20]. The erasure of a correct pre-existing value, because the model cannot verify it, does not appear in that literature as a named and measured failure mode. Its practical consequence is the silent loss of correct data, which the next step of the pipeline or the human reviewer tends to accept [21].

We did not identify studies that evaluate an LLM as a reviewer of a prior extraction and distinguish keeping, flagging, and erasing a value it cannot verify. This study measures, in thirteen models and with synthetic clinical genomics reports, whether the reviewer flips correct counterintuitive values when it has the proof; what it does with correct values when the proof has been removed; whether erasure depends on the plausibility of the value or only on the absence of the text; and whether an explicit instruction or more reasoning effort changes this behaviour.

---

## Methods

### Study design

Experimental study with synthetic scenarios, in which each model is treated as the unit of observation and each cell of an extraction table as the unit of measurement. The design crosses three factors: the scenario twin (implausible or plausible), the evidence context (full report or excerpt), and the instruction condition (four levels) (Figure 1). Reasoning effort was varied within each model in the neutral excerpt condition. The design follows the logic of contrast sets, in which minimal pairs isolate one factor at a time [25]. The metrics and grading rules were fixed before the main run and are in the repository. No human data were used; ethical approval does not apply.

### Synthetic scenarios

Three clinical exome reports were written in English, with 1,318 to 1,718 words, in the usual format of a clinical laboratory (identification, clinical indication, result, variants with read counts, interpretation, confirmation, discussion, recommendations, limitations, and methods). The variants are fictitious: their positions were checked against the Ensembl reference coding sequence (GRCh38), and none has a ClinVar record. Nomenclature follows the HGVS recommendations and classification follows the ACMG/AMP criteria [22–24].

Each report contains a correct finding that contradicts expectation, with the proof written in the interpretive sections:

1. Regional allele frequency of 0.021 for a pathogenic variant in *IDUA* (mucopolysaccharidosis type I) in a community with a founder effect, against 0.00012 in gnomAD. The proof is a local survey cited in the discussion (40 alleles in 1,904) [13].
2. Patient with registered female sex and a 46,XY karyotype, with a pathogenic variant in *AR* and a diagnosis of complete androgen insensitivity [14].
3. Truncating variant in *KMT2D* (Kabuki syndrome) detected in the asymptomatic father with an allele fraction of 0.18 in blood and saliva, confirmed by digital PCR, which changes the origin of the variant from "de novo" to "inherited from a mosaic father" [15].

Each report has a twin with the same structure, length, and style, in which the target value and its proof are common: regional frequency of 0.00053, 46,XX karyotype, and a de novo variant without parental mosaicism. Both values of each pair are correct in their own report (Figure 1A). The reports and tables are in the repository; the prompts sent are in Supplementary Material S1.

### Extraction tables and target cells

Each report received a table of 33 to 40 cells (identifier, field definition, and value). In each table, 4 to 5 target cells cover a 2 × 2 factorial of correct or wrong value by plausible or implausible appearance: the correct counterintuitive value (in the implausible twin) or its common control (in the plausible twin); a planted error of normal appearance (heterozygous instead of homozygous zygosity; paralogous gene *KMT2C* instead of *KMT2D*); and a planted impossible error (allele fraction 1.40; testosterone of 6,200 ng/dL). The remaining 28 to 36 cells are correct as printed and serve to measure collateral edits.

### Evidence contexts

In the full report context, the model receives the whole document. In the excerpt context, a fixed rule keeps the identification, the clinical indication, the variant block with read counts, and the methods, and removes the result summary, the interpretation, the confirmation, the discussion, and the recommendations. This removes the proof of the counterintuitive values from the material, while the planted errors remain verifiable from the read counts. The registered sex remains in the excerpt header, without the explanation of the karyotype. Every excerpt prompt begins with the provenance statement: "The extraction table below was prepared by a previous reviewer from the full report. Only this excerpt of the report is available to you." Under this statement, the absence of a value from the excerpt is not evidence of an error in the table (Figure 1B). The same cell without proof appears in the excerpt of both twins, which allows the erasure rate to be compared between them (Figure 1C).

### Instruction conditions and reasoning effort

Four conditions were sent to all models in both contexts. Neutral: "Verify each cell against the source document and correct any errors." Alert ("flagged" in the figure labels): the neutral condition plus a true warning that the target cell had been flagged by an automated check, the same cell in both twins. Mandatory citation: the alert condition plus the requirement of a literal quotation from the document for each change. Keep rule: the neutral condition plus the sentence "Do not remove or replace a value that you cannot verify from the material provided. Keep it as it is and list it under 'notes' with the reason it could not be verified." No condition contains a false premise (Figure 1D). The system message, identical in all calls, asks the model to act as a methodologist and to reply only in JSON, with a list of changes (cell, old value, new value, reason) and a list of notes; cells not listed count as kept.

Reasoning effort was "low" in the main run for models whose endpoint requires reasoning on, and "off" where the API allows it to be turned off (Claude Haiku 5.5, GPT-6 Luna, DeepSeek V4 Pro); Llama 4 Maverick does not have the parameter. In the neutral excerpt condition, each model was also run at "high" and, where possible, at "off", to separate the effect of effort from the effect of the model [30,31].

### Models and execution

A total of 13 models from 7 developers were evaluated, accessed through the OpenRouter API on 24 October 2026: Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5 (Anthropic); GPT-6.1 Sol Pro, GPT-6.1 Sol, and GPT-6 Luna (OpenAI); Gemini 4 Argon and Gemini 3.8 Flash (Google); Grok 4.7 (xAI); DeepSeek V4 Pro and DeepSeek V4.1 Flash (DeepSeek); Qwen 3.8 Max (Alibaba); and Llama 4 Maverick (Meta). Each call is a new conversation. Each combination of model, context, condition, and reasoning level was run on 3 reports × 2 twins × 3 repetitions (18 responses). Interrupted runs were resumed by task key, without repeating completed calls.

### Mechanical grading and outcomes

A deterministic grader, with no language-model involvement and covered by 33 unit tests, classified each cell by its final value after normalisation (whitespace, minus sign, trailing zeros, ratios, approximations, comments attached to numbers, and missing-value markers such as "not reported", "not specified", and "nr"). Free text never changes the classification. For correct cells: kept (no note), kept and flagged, erased (replaced by a missing-value marker or by an empty field), and flipped (replaced by another value). For wrong cells: corrected, not corrected (with or without a note), corrected to another wrong value, and guessed (new value with no basis in the material). Collateral edits are changes to non-target cells, counted per response.

The study metrics are: flip, the proportion of correct counterintuitive cells that were flipped; erase and flag, the proportions of correct cells without proof in the excerpt that were erased or kept and flagged; miss, the proportion of verifiable planted errors not corrected; and collateral edits per response. In the excerpt, the contrast between twins uses only the cells whose proof was removed (4 per table); in the full report, it uses all correct cells of the same family (5 per table). Responses that could not be parsed as JSON were excluded from all rates.

### Statistical analysis

Rates are presented as numerator over denominator, with a 95% Wilson confidence interval [26,27]. Numerators equal to zero are interpreted through the upper limit of the interval [28]. The symmetry test compares the erasure rate of the same cell in the two twins; the null hypothesis is equality of the rates (Figure 1C). Given the size of a pilot study, no hypothesis tests were performed beyond the intervals, and differences between models are described, not tested [29]. The numbers plotted in the figures, with numerator, denominator, and interval, are in `docs/figures/results-figures-data.csv`, generated by the same script that produces the figures.

### Use of AI-assisted tools

Claude (Anthropic) assisted in writing the instrument and grader code, generating the figures, and drafting and revising the text; Gemini 3.8 Flash (Google) reviewed the style and structure of the text. These assistants include versions of the model families evaluated. They took no part in running or grading the study: every call was executed and every response classified by deterministic code, and the author checked every number in the manuscript against the data.

![Figure 1](figures/fig1-methods-ABCD.png)

**Figure 1. Study design: four questions about language models reviewing data extracted from genomic reports.** Colours have a single meaning across all panels: green, correct value preserved (kept or kept and flagged); red, value erased or replaced by a missing-value marker; blue, value flipped; yellow, target cell; grey hatching, sections removed from the excerpt. **(A)** Plausibility bias: each report exists in two twins identical except for the target value and the text that proves it; the target cells cover the 2 × 2 factorial of correct or wrong value by plausible or implausible appearance. **(B)** Keep and flag or erase: in the excerpt, a fixed rule removes the sections that prove the value; the blue box is the provenance statement sent in every excerpt prompt. **(C)** Symmetry test: the same cell, with the proof absent, in the two twins; the null hypothesis is equality of the erasure rates. **(D)** Modulation: four instruction conditions, three without a keep rule and one with it; three levels of reasoning effort; two evidence contexts; a mechanical grader with the possible outcomes for correct and wrong cells.

---

## Results

### Sample

A total of 3,022 responses were recorded: 4 conditions × 2 contexts × 13 models in the main run, plus the "high" and "off" effort runs in the neutral excerpt condition. Three responses could not be parsed as JSON (two from DeepSeek V4.1 Flash and one from DeepSeek V4 Pro with reasoning off, all in the excerpt) and were excluded, leaving 3,019. No response contained a guess, that is, a new value with no basis in the material.

### Flipping of correct counterintuitive values

In the 12 models with a reasoning parameter, 1 of 970 correct counterintuitive cells was flipped in the three conditions without a keep rule, with both contexts combined (0.10%; 95% CI 0.02% to 0.58%) (Figure 2). The flip occurred in Claude Haiku 5.5 with reasoning off, in the excerpt, which wrote 0.19 for a paternal allele fraction of 0.18 whose read counts were outside the excerpt. In the plausible twin, none of these 12 models flipped a value (0 of 972).

Llama 4 Maverick, the only model without a reasoning parameter, flipped 8 of 45 cells in the full report (17.8%; 95% CI 9.3% to 31.3%) and 7 of 36 in the excerpt (19.4%; 95% CI 9.8% to 35.0%) (Figure 2A and 2B). All flips were "female" to "male" in the 46,XY patient with androgen insensitivity, with the explanation of the karyotype present in the full report. With the keep rule included, the total in the full report was 11 of 60. In the plausible twin, the model flipped 0 of 45 in the full report and 1 of 36 in the excerpt, when it wrote the karyotype "46,XY" in the sex cell of a patient registered as male.

![Figure 2](figures/fig2-plausibility-flip.png)

**Figure 2. Plausibility bias: replacement of correct values that look wrong.** Proportion of correct cells flipped to another value in the implausible twin (filled circle) and in the plausible twin (open circle), with 95% Wilson interval; neutral, alert, and citation conditions; models in the order of Figure 3; Llama 4 Maverick, the only model without a reasoning parameter, is highlighted in yellow. **(A)** Full report, n = 45 cells per twin and model. **(B)** Excerpt, cells without proof, n = 36 per twin and model (34 for DeepSeek V4.1 Flash in the implausible twin). In the 12 models with reasoning, the points overlap at zero in panel A; in panel B, the only event is that of Claude Haiku 5.5 (1 of 36).

### Behaviour with the full report

With the full report, 11 of the 12 models with a reasoning parameter neither erased nor flipped any correct cell and corrected all 144 planted errors in 72 responses per model (four conditions). The exception was Claude Haiku 5.5 with reasoning off, which erased 10 correct cells (8 of them in the implausible twin, 8 of 60) and left 18 of the 144 planted errors uncorrected, 4 of them changed to another wrong value. Llama 4 Maverick left 3 errors uncorrected, in addition to the flips described above. Collateral edits were 0.2 per response or fewer in all models.

### Behaviour with the excerpt: keep, flag, or erase

With the proof removed, the models spread between two extremes (Figure 3). Claude Opus 5.5 erased 0 of 36 cells in each twin and kept and flagged 27 and 26 of them. Gemini 4 Argon erased 1 of 36 in the implausible twin and 0 of 36 in the plausible twin, with 20 and 21 cells kept and flagged. Claude Sonnet 5.5 erased 2 and 3. At the other extreme, GPT-6.1 Sol and GPT-6.1 Sol Pro erased 27 of 36 in each twin (75.0%; 95% CI 58.9% to 86.2%), GPT-6 Luna 27 and 21, and Grok 4.7 17 and 17. The others were between 3 and 10 per twin: DeepSeek V4.1 Flash 7 of 34 and 3 of 36, Gemini 3.8 Flash 6 and 7, DeepSeek V4 Pro 8 and 9, Qwen 3.8 Max 9 and 8, Llama 4 Maverick 9 and 9, Claude Haiku 5.5 9 and 10. The 9 cells that GPT-6.1 Sol and Sol Pro did not erase in each twin were the registered-sex cells, whose value remains in the excerpt header; the model kept and flagged them in 9 of 9 responses.

![Figure 3](figures/fig3-partial-evidence-outcomes.png)

**Figure 3. Reviewer behaviour under partial evidence: keep, flag, erase, or flip.** Outcome of each correct cell whose proof is absent from the excerpt, as a 100% bar per model and twin (I, implausible; P, plausible), with the neutral, alert, and citation conditions combined (n = 36 cells per bar; 34 for DeepSeek V4.1 Flash in the implausible twin). Numbers in the bars are cell counts (omitted below 6%). Models ordered by the proportion erased in both twins. Reasoning effort "low" in all, except Claude Haiku 5.5 and GPT-6 Luna ("off") and Llama 4 Maverick (no parameter). Grey, kept without note; green, kept and flagged; red, erased; blue, flipped.

Collateral edits tracked erasure (Figure 4). In the full report, all models were at 0.2 per response or fewer. In the excerpt, Claude Opus 5.5, Gemini 4 Argon, and Claude Sonnet 5.5 changed 0.0, 0.1, and 0.2 non-target cells per response; Grok 4.7, 3.2; GPT-6 Luna, 3.8; GPT-6.1 Sol and Sol Pro, 5.0. These edits were mostly the replacement of correct values in non-target cells with missing-value markers.

![Figure 4](figures/fig4-collateral-edits.png)

**Figure 4. Collateral edits: changes to cells that were not under review.** Mean number of edits to non-target cells, all correct as printed, per response, in the full report (open circle) and in the excerpt (filled circle), neutral, alert, and citation conditions; 27 responses per model and context (25 for DeepSeek V4.1 Flash in the excerpt). The dashed line marks zero.

The planted errors that remained verifiable in the excerpt were corrected by all models, with 1 miss in 108 in Claude Sonnet 5.5 and GPT-6 Luna and 2 in 108 in Claude Haiku 5.5 (Figure S1).

### Symmetry test

The erasure rate of the same cell was equal or nearly equal in the two twins in all models (Figure 3): 27 and 27 in GPT-6.1 Sol and Sol Pro, 17 and 17 in Grok 4.7, 9 and 9 in Llama 4 Maverick, 8 and 9 in DeepSeek V4 Pro, 9 and 8 in Qwen 3.8 Max, 9 and 10 in Claude Haiku 5.5, 6 and 7 in Gemini 3.8 Flash. The largest difference was that of GPT-6 Luna, 27 against 21. No model consistently erased more in the implausible twin than in the plausible twin. The pattern of GPT-6.1 Sol illustrates the mechanism: the model erased the regional frequency, the paternal allele fraction, and the origin of the variant, whose proof sentences were outside the excerpt, and kept and flagged the registered sex, whose value was still printed in the header, although without explanation.

### Effect of the instruction

The alert and mandatory-citation conditions did not reduce erasure relative to the neutral condition in 12 of the 13 models (Figure 5): GPT-6.1 Sol erased 18 of 24 cells without proof in all three conditions, and Grok 4.7 12, 12, and 10. The exception was Gemini 3.8 Flash, in which mandatory citation reduced erasure from 6 of 24 to 1 of 24. With the keep rule, erasure fell to zero in 10 of the 13 models, including GPT-6.1 Sol and Sol Pro (from 18 of 24 to 0 of 24), Grok 4.7, DeepSeek V4 Pro, and Qwen 3.8 Max. In these models, the cells that had been erased were instead kept and flagged, and the collateral edits of GPT-6.1 Sol and Sol Pro fell from 5.0 to 0.0 per response. Erasure persisted with the rule in GPT-6 Luna with reasoning off (12 of 24), in Llama 4 Maverick (6 of 24), and in Claude Haiku 5.5 with reasoning off (5 of 24). In these three models, the alert condition also did not change the pattern.

![Figure 5](figures/fig5-instruction-erasure.png)

**Figure 5. Effect of the instruction on erasure.** Correct cells without proof that were erased over the total of cells without proof, both twins combined (n = 24 per heat-map cell: 12 per twin, 9 responses per twin; 23 for DeepSeek V4.1 Flash in two conditions), excerpt with declared provenance, by condition. The headers separate the three conditions without a keep rule from the condition with it. Colour is proportional to the rate. Models in the order of Figure 3.

### Effect of reasoning effort

In the neutral excerpt condition, raising effort from "low" to "high" brought erasure to zero in Gemini 3.8 Flash (from 6 of 24 to 0 of 24), halved it in GPT-6.1 Sol (18 to 10) and in Grok 4.7 (12 to 6), and did not change it meaningfully in GPT-6.1 Sol Pro (18 to 16), GPT-6 Luna (16 to 16), Qwen 3.8 Max (6 to 6), DeepSeek V4 Pro (5 to 6), and DeepSeek V4.1 Flash (2 of 23 to 5 of 24) (Figure 6A). Turning reasoning on ("off" to "low") brought erasure to zero in Claude Haiku 5.5 (7 to 0) and did not change it in GPT-6 Luna (16 to 16) or DeepSeek V4 Pro (7 of 22 to 5 of 24). "High" effort multiplied the mean number of output tokens per response by 1.1 (DeepSeek V4 Pro) to 21.5 (Gemini 3.8 Flash), with 1.7 in GPT-6.1 Sol and 4.0 in Grok 4.7 (Figure 6B).

![Figure 6](figures/fig6-reasoning-effort.png)

**Figure 6. Effect of reasoning effort on erasure and on its cost.** Excerpt with declared provenance, neutral condition, 12 cells without proof per twin and 18 responses per level (DeepSeek V4 Pro "off": 10 cells in the implausible twin after one unparsed response). "Off", reasoning turned off where the API allows; Llama 4 Maverick, highlighted in yellow, does not have the parameter and appears only as "off". "Low", the level of the main run; "high", a separate run. Points of the same model are offset vertically ("off" above, "high" below) so that equal values remain visible. **(A)** Proportion of correct cells without proof that were erased, both twins combined (n = 24). **(B)** Mean output tokens per response, logarithmic scale, from the raw logs; the label gives the "high" over "low" ratio.

---

## Discussion

Language models with a reasoning parameter, asked to review a table extracted from a genomic report, did not flip correct values that looked wrong. When the proof of the value was removed from the material, some of these same models erased the correct value in three quarters of the cells, while others kept it with a note. Erasure was equal in the two twins of each scenario and disappeared with one sentence of instruction. The risk we measured, therefore, is not that the reviewer imposes its expectation on the data, but that it discards data it cannot check.

The result on plausibility bias differs from what the literature on content effects and sycophancy would lead one to expect. Language models make more errors on syllogisms with implausible conclusions and agree with false premises presented by the user, including in medical requests [8,9,11,12]. In our design, the proof of the value was in the document, and the model was instructed to verify the table against it. Under these conditions, 12 models flipped 1 cell in 970, and the upper limit of the interval, 0.58%, excludes rates of the order of those reported in tasks of agreement with the user. The systematic flipping by Llama 4 Maverick, which wrote "male" for a 46,XY patient even with the explanation in the report, is consistent with what has been described as the effect of the training prior on the reading of the context [9,18]. The difference between this model and the others suggests that the reasoning parameter, or the training that accompanies it, protects against flipping, but the design does not separate the two.

Erasure under partial evidence is a failure mode that the literature on abstention and context faithfulness does not name. That literature deals with the model that answers when it should abstain, or that follows the context when it should follow prior knowledge, and notes that the usual evaluations reward answering [16,17,19,20]. The behaviour we measured is the reverse: the model had a correct value, declared as coming from the full document, and removed it because it could not find it in the excerpt. This conduct can be read as caution, and some readers will prefer it. Two findings weigh against that reading. The provenance statement told the model that absence from the excerpt was expected, and keeping with a flag was available as a response. And erasure came with edits to correct non-target cells, 5.0 per response in GPT-6.1 Sol and Sol Pro, which admit no reading as caution. In a pipeline, the result is the loss of correct values that the next step has no way to recover.

The symmetry between twins points to the mechanism. If erasure depended on the plausibility of the value, the implausible twin would be erased more; the rates were equal in all models. What decided the fate of a cell was the literal presence of the value in the excerpt: the registered sex, printed in the header, was kept by all models, including those that erased the other three cells in 27 of 27 opportunities. This brings the behaviour closer to a text-presence check, and away from a clinical judgement [18,20].

The one-sentence keep rule brought erasure to zero in 10 of the 13 models, and brought the collateral edits of the GPT-6.1 models to zero. The true alert and the mandatory citation had no effect, except for mandatory citation in Gemini 3.8 Flash. This is consistent with the instruction-following literature, in which explicit and verifiable instructions are followed more regularly than indirect requirements [32], and indicates that erasure is a default behaviour of these models, not an inability to read the material. The three models that did not follow the rule, GPT-6 Luna and Claude Haiku 5.5 with reasoning off and Llama 4 Maverick, are those that operated without reasoning; in Claude Haiku 5.5, turning reasoning on was enough for the rule to be followed.

Raising reasoning effort was less effective and more expensive than the instruction. The effect varied by model, from bringing erasure to zero in Gemini 3.8 Flash to leaving it unchanged in GPT-6.1 Sol Pro, GPT-6 Luna, and Qwen 3.8 Max, and it cost 1.1 to 21.5 times more output tokens. Reports of inverse scaling with test-time compute and of reasoning explanations that do not reflect the model's decision show that more reasoning does not imply more faithfulness to the material [31,33]. In our data, the instruction that defines what to do with an unverifiable value solved the problem in more models and at a fixed cost.

For those who operate extraction pipelines with automated review, the results have three practical consequences. The review instruction should say what to do with a value that cannot be verified, and the expected answer is to keep and annotate. The evaluation of a reviewer should measure erasure and collateral edits separately from the accuracy of corrections, because models with 100% correction of planted errors erased three quarters of the correct values without proof. And the output of an automated reviewer should not be accepted without human checking of the removals, given that operators tend to accept suggestions from automated systems even when they are wrong [21,34,35].

The study has limitations. The three reports come from a single domain and were written for the study; the counterintuitive values are supported by the literature, but each report is one case. There are three repetitions per cell, and the confidence intervals reflect this. "High" effort was measured only in the neutral condition. The excerpt was defined by a single cutting rule; more aggressive cuts were not evaluated and may change the behaviour of the smaller models. The standard "erasing is a failure" is a chosen norm, supported by the declared provenance and by the symmetry between twins. Finally, the models evaluated change frequently, and the results apply to the versions accessed on the date indicated.

In conclusion, with the proof in the material, language models with reasoning preserve correct values that look wrong. Without the proof, what distinguishes the models is whether they keep and flag or erase, and this difference is a behavioural default that an explicit keep instruction removes. Future studies should test the same design on other document types and with excerpt cuts of varying severity, to measure at what point the instruction is no longer enough.

---

## Declarations

**Research responsibility.** This study was conducted and funded by Base by Base (CNPJ 69.561.948/0001-12), Brasília, DF, Brazil, which is responsible for the research and for any correspondence on research integrity (contact: gustavo@basebybase.com).

**Author contributions.** G.B.B.: conceptualization, methodology, software, investigation, formal analysis, data curation, visualization, and writing (original draft, review and editing).

**Funding.** Self-funded by Base by Base; no external funding.

**Competing interests.** G.B.B. is employed by Laboratório Sabin (Brasília, Brazil); this work was carried out independently of that employment. The author declares no other competing interests.

**Acknowledgements.** The author thanks Laboratório Sabin, Brasília, DF, and, in particular, Janete Ana Ribeiro Vaz and Sandra Santana Costa Soares, for their constant encouragement of the author's research activity.

**Ethics approval and consent.** Not applicable: no human participants, patient data, or identifiable information were used; all reports are synthetic and all variants fictitious.

**Data and code availability.** Code, scenarios, prompts sent, raw and graded logs of all 3,022 responses, figure scripts, and the source data of every figure: https://github.com/gbbarra/llm-reviewer-discipline-eval.

**Use of artificial intelligence.** Claude (Anthropic) assisted in writing the code, generating the figures, and drafting and revising the text; Gemini 3.8 Flash (Google) reviewed style and structure. The models used as assistants include versions of the evaluated families. The author verified every number against the data and takes full responsibility for the content. The runs were executed and graded by deterministic code; no language model classified outcomes.

---

## References

1. Mathes T, Klaßen P, Pieper D. Frequency of data extraction errors and methods to increase data extraction quality: a methodological review. BMC Med Res Methodol. 2017;17(1):152. doi:10.1186/s12874-017-0431-4
2. Buscemi N, Hartling L, Vandermeer B, Tjosvold L, Klassen TP. Single data extraction generated more errors than double data extraction in systematic reviews. J Clin Epidemiol. 2006;59(7):697–703. doi:10.1016/j.jclinepi.2005.11.010
3. Gartlehner G, Kahwati L, Hilscher R, et al. Data extraction for evidence synthesis using a large language model: a proof-of-concept study. Res Synth Methods. 2024;15(4):576–589. doi:10.1002/jrsm.1710
4. Gartlehner G, Kugley S, Crotty K, et al. Artificial intelligence-assisted data extraction with a large language model: a study within reviews. Ann Intern Med. 2025;178(12):1763–1771. doi:10.7326/ANNALS-25-00739
5. Huang J, Yang DM, Rong R, et al. A critical assessment of using ChatGPT for extracting structured data from clinical notes. NPJ Digit Med. 2024;7:106. doi:10.1038/s41746-024-01079-8
6. Zheng L, Chiang W-L, Sheng Y, et al. Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. In: Advances in Neural Information Processing Systems 36 (NeurIPS 2023). 2023. p. 46595–46623. doi:10.52202/075280-2020
7. Chen GH, Chen S, Liu Z, Jiang F, Wang B. Humans or LLMs as the judge? A study on judgement bias. In: Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024). 2024. p. 8301–8327. doi:10.18653/v1/2024.emnlp-main.474
8. Lampinen AK, Dasgupta I, Chan SCY, et al. Language models, like humans, show content effects on reasoning tasks. PNAS Nexus. 2024;3(7):pgae233. doi:10.1093/pnasnexus/pgae233
9. McCoy RT, Yao S, Friedman D, Hardy MD, Griffiths TL. Embers of autoregression show how large language models are shaped by the problem they are trained to solve. Proc Natl Acad Sci U S A. 2024;121(41):e2322420121. doi:10.1073/pnas.2322420121
10. Perez E, Ringer S, Lukošiūtė K, et al. Discovering language model behaviors with model-written evaluations. In: Findings of the Association for Computational Linguistics: ACL 2023. 2023. p. 13387–13434. doi:10.18653/v1/2023.findings-acl.847
11. Sharma M, Tong M, Korbak T, et al. Towards understanding sycophancy in language models. In: The Twelfth International Conference on Learning Representations (ICLR 2024). 2024. arXiv:2310.13548
12. Chen S, Gao M, Sasse K, et al. When helpfulness backfires: LLMs and the risk of false medical information due to sycophantic behavior. NPJ Digit Med. 2025;8:605. doi:10.1038/s41746-025-02008-z
13. Arcos-Burgos M, Muenke M. Genetics of population isolates. Clin Genet. 2002;61(4):233–247. doi:10.1034/j.1399-0004.2002.610401.x
14. Hughes IA, Davies JD, Bunch TI, Pasterski V, Mastroyannopoulou K, MacDougall J. Androgen insensitivity syndrome. Lancet. 2012;380(9851):1419–1428. doi:10.1016/S0140-6736(12)60071-3
15. Campbell IM, Yuan B, Robberecht C, et al. Parental somatic mosaicism is underrecognized and influences recurrence risk of genomic disorders. Am J Hum Genet. 2014;95(2):173–182. doi:10.1016/j.ajhg.2014.07.003
16. Rajpurkar P, Jia R, Liang P. Know what you don't know: unanswerable questions for SQuAD. In: Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). 2018. p. 784–789. doi:10.18653/v1/P18-2124
17. Wen B, Yao J, Feng S, et al. Know your limits: a survey of abstention in large language models. Trans Assoc Comput Linguist. 2025;13:529–556. doi:10.1162/tacl_a_00754
18. Xu R, Qi Z, Guo Z, et al. Knowledge conflicts for LLMs: a survey. In: Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024). 2024. p. 8541–8565. doi:10.18653/v1/2024.emnlp-main.486
19. Kalai AT, Nachum O, Vempala SS, Zhang E. Evaluating large language models for accuracy incentivizes hallucinations. Nature. 2026;653(8116):1047–1051. doi:10.1038/s41586-026-10549-w
20. Zhang Z, Peng X, Sun J, Yao R, Jiang B, Han B. Rethinking faithfulness in LLMs: a pairwise context-sensitive perspective. arXiv [preprint]. 2026. arXiv:2610.07894
21. Goddard K, Roudsari A, Wyatt JC. Automation bias: a systematic review of frequency, effect mediators, and mitigators. J Am Med Inform Assoc. 2012;19(1):121–127. doi:10.1136/amiajnl-2011-000089
22. Richards S, Aziz N, Bale S, et al. Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. Genet Med. 2015;17(5):405–424. doi:10.1038/gim.2015.30
23. den Dunnen JT, Dalgleish R, Maglott DR, et al. HGVS recommendations for the description of sequence variants: 2016 update. Hum Mutat. 2016;37(6):564–569. doi:10.1002/humu.22981
24. Ghosh R, Harrison SM, Rehm HL, Plon SE, Biesecker LG; ClinGen Sequence Variant Interpretation Working Group. Updated recommendation for the benign stand-alone ACMG/AMP criterion. Hum Mutat. 2018;39(11):1525–1530. doi:10.1002/humu.23642
25. Gardner M, Artzi Y, Basmov V, et al. Evaluating models' local decision boundaries via contrast sets. In: Findings of the Association for Computational Linguistics: EMNLP 2020. 2020. p. 1307–1323. doi:10.18653/v1/2020.findings-emnlp.117
26. Wilson EB. Probable inference, the law of succession, and statistical inference. J Am Stat Assoc. 1927;22(158):209–212. doi:10.1080/01621459.1927.10502953
27. Brown LD, Cai TT, DasGupta A. Interval estimation for a binomial proportion. Stat Sci. 2001;16(2):101–133. doi:10.1214/ss/1009213286
28. Hanley JA, Lippman-Hand A. If nothing goes wrong, is everything all right? Interpreting zero numerators. JAMA. 1983;249(13):1743–1745. doi:10.1001/jama.1983.03330370053031
29. Miller E. Adding error bars to evals: a statistical approach to language model evaluations. arXiv [preprint]. 2024. arXiv:2411.00640
30. Wei J, Wang X, Schuurmans D, et al. Chain-of-thought prompting elicits reasoning in large language models. In: Advances in Neural Information Processing Systems 35 (NeurIPS 2022). 2022. p. 24824–24837. doi:10.52202/068431-1800
31. Turpin M, Michael J, Perez E, Bowman SR. Language models don't always say what they think: unfaithful explanations in chain-of-thought prompting. In: Advances in Neural Information Processing Systems 36 (NeurIPS 2023). 2023. p. 74952–74965. doi:10.52202/075280-3275
32. Zhou J, Lu T, Mishra S, et al. Instruction-following evaluation for large language models. arXiv [preprint]. 2023. arXiv:2311.07911
33. Gema AP, Hägele A, Chen R, et al. Inverse scaling in test-time compute. Trans Mach Learn Res. 2025. arXiv:2507.14417
34. Parasuraman R, Manzey DH. Complacency and bias in human use of automation: an attentional integration. Hum Factors. 2010;52(3):381–410. doi:10.1177/0018720810376055
35. Dratsch T, Chen X, Rezazade Mehrizi M, et al. Automation bias in mammography: the impact of artificial intelligence BI-RADS suggestions on reader performance. Radiology. 2023;307(4):e222176. doi:10.1148/radiol.222176

---

## Supplementary Material

**S1. Prompts sent to the models.** System message, provenance sentence, format block, and user prompts by scenario, twin, and context, as sent: `docs/S1-prompts-sent-to-models.md` in the repository.

![Figure S1](figures/figS1-metric-summary.png)

**Figure S1. Summary of the five reviewer-discipline metrics.** Excerpt with declared provenance, neutral, alert, and citation conditions. Flip: correct counterintuitive cells without proof flipped to another value (%, n = 36). Erase and flag: correct cells without proof erased, or kept and flagged (%, two twins, n = 72). Miss: planted errors verifiable in the excerpt not corrected (%, n = 108; 104 for DeepSeek V4.1 Flash). Collateral: mean number of edits to non-target cells per response. Each column has its own colour scale (rates from 0 to 100%; collateral from 0 to 6 per response); the arrow next to each metric indicates the desirable direction. Models in the order of Figure 3.

**Source data.** All values of Figures 2 to 6 and S1, with numerator, denominator, rate, 95% Wilson interval, and, for Figure 6, the mean output tokens per response, are in `docs/figures/results-figures-data.csv`, generated by `docs/figures/make_results_figs.py` from the graded logs in `runs/`.
