"""Build the Cureus version of the manuscript from the English preprint.

- keeps 30 of the 35 references (Cureus free-publication limit for original articles)
- renumbers citations in order of first mention, references in Cureus style
- Figure S1 becomes Figure 5 (cited before the instruction and reasoning figures); 5 -> 6, 6 -> 7
- copies figure files with Cureus-style names

Usage: python docs/cureus/build_cureus.py
"""
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE.parent
SRC = DOCS / "PREPRINT-medRxiv-2026-10-24.en.md"
OUT = HERE / "CUREUS-manuscript.en.md"

# old reference number -> key (order of the medRxiv list)
OLD = ["mathes", "buscemi", "gart24", "gart25", "huang", "zheng", "chengh", "lampinen", "mccoy", "perez",
       "sharma", "chens", "arcos", "hughes", "campbell", "rajpurkar", "wen", "xu", "kalai", "zhang",
       "goddard", "richards", "dendunnen", "ghosh", "gardner", "wilson", "brown", "hanley", "miller", "wei",
       "turpin", "zhou", "gema", "parasuraman", "dratsch"]
DROP = {"perez", "ghosh", "brown", "miller", "dratsch"}

CUREUS = {
    "mathes": "Mathes T, Klaßen P, Pieper D: Frequency of data extraction errors and methods to increase data extraction quality: a methodological review. BMC Med Res Methodol. 2017, 17:152. 10.1186/s12874-017-0431-4",
    "buscemi": "Buscemi N, Hartling L, Vandermeer B, Tjosvold L, Klassen TP: Single data extraction generated more errors than double data extraction in systematic reviews. J Clin Epidemiol. 2006, 59:697-703. 10.1016/j.jclinepi.2005.11.010",
    "gart24": "Gartlehner G, Kahwati L, Hilscher R, et al.: Data extraction for evidence synthesis using a large language model: a proof-of-concept study. Res Synth Methods. 2024, 15:576-89. 10.1002/jrsm.1710",
    "gart25": "Gartlehner G, Kugley S, Crotty K, et al.: Artificial intelligence-assisted data extraction with a large language model: a study within reviews. Ann Intern Med. 2025, 178:1763-71. 10.7326/ANNALS-25-00739",
    "huang": "Huang J, Yang DM, Rong R, et al.: A critical assessment of using ChatGPT for extracting structured data from clinical notes. NPJ Digit Med. 2024, 7:106. 10.1038/s41746-024-01079-8",
    "zheng": "Zheng L, Chiang WL, Sheng Y, et al.: Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. Advances in Neural Information Processing Systems 36 (NeurIPS 2023). 2023, 46595-623. 10.52202/075280-2020",
    "chengh": "Chen GH, Chen S, Liu Z, Jiang F, Wang B: Humans or LLMs as the judge? A study on judgement bias. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. 2024, 8301-27. 10.18653/v1/2024.emnlp-main.474",
    "lampinen": "Lampinen AK, Dasgupta I, Chan SC, et al.: Language models, like humans, show content effects on reasoning tasks. PNAS Nexus. 2024, 3:pgae233. 10.1093/pnasnexus/pgae233",
    "mccoy": "McCoy RT, Yao S, Friedman D, Hardy MD, Griffiths TL: Embers of autoregression show how large language models are shaped by the problem they are trained to solve. Proc Natl Acad Sci U S A. 2024, 121:e2322420121. 10.1073/pnas.2322420121",
    "sharma": "Sharma M, Tong M, Korbak T, et al.: Towards understanding sycophancy in language models. The Twelfth International Conference on Learning Representations (ICLR 2024). 2024. https://arxiv.org/abs/2310.13548",
    "chens": "Chen S, Gao M, Sasse K, et al.: When helpfulness backfires: LLMs and the risk of false medical information due to sycophantic behavior. NPJ Digit Med. 2025, 8:605. 10.1038/s41746-025-02008-z",
    "arcos": "Arcos-Burgos M, Muenke M: Genetics of population isolates. Clin Genet. 2002, 61:233-47. 10.1034/j.1399-0004.2002.610401.x",
    "hughes": "Hughes IA, Davies JD, Bunch TI, Pasterski V, Mastroyannopoulou K, MacDougall J: Androgen insensitivity syndrome. Lancet. 2012, 380:1419-28. 10.1016/S0140-6736(12)60071-3",
    "campbell": "Campbell IM, Yuan B, Robberecht C, et al.: Parental somatic mosaicism is underrecognized and influences recurrence risk of genomic disorders. Am J Hum Genet. 2014, 95:173-82. 10.1016/j.ajhg.2014.07.003",
    "rajpurkar": "Rajpurkar P, Jia R, Liang P: Know what you don't know: unanswerable questions for SQuAD. Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics. 2018, 784-9. 10.18653/v1/P18-2124",
    "wen": "Wen B, Yao J, Feng S, Xu C, Tsvetkov Y, Howe B, Wang LL: Know your limits: a survey of abstention in large language models. Trans Assoc Comput Linguist. 2025, 13:529-56. 10.1162/tacl_a_00754",
    "xu": "Xu R, Qi Z, Guo Z, Wang C, Wang H, Zhang Y, Xu W: Knowledge conflicts for LLMs: a survey. Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. 2024, 8541-65. 10.18653/v1/2024.emnlp-main.486",
    "kalai": "Kalai AT, Nachum O, Vempala SS, Zhang E: Evaluating large language models for accuracy incentivizes hallucinations. Nature. 2026, 653:1047-51. 10.1038/s41586-026-10549-w",
    "zhang": "Zhang Z, Peng X, Sun J, Yao R, Jiang B, Han B: Rethinking faithfulness in LLMs: a pairwise context-sensitive perspective [PREPRINT]. arXiv. 2026. https://arxiv.org/abs/2610.07894",
    "goddard": "Goddard K, Roudsari A, Wyatt JC: Automation bias: a systematic review of frequency, effect mediators, and mitigators. J Am Med Inform Assoc. 2012, 19:121-7. 10.1136/amiajnl-2011-000089",
    "richards": "Richards S, Aziz N, Bale S, et al.: Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. Genet Med. 2015, 17:405-24. 10.1038/gim.2015.30",
    "dendunnen": "den Dunnen JT, Dalgleish R, Maglott DR, et al.: HGVS recommendations for the description of sequence variants: 2016 update. Hum Mutat. 2016, 37:564-9. 10.1002/humu.22981",
    "gardner": "Gardner M, Artzi Y, Basmov V, et al.: Evaluating models' local decision boundaries via contrast sets. Findings of the Association for Computational Linguistics: EMNLP 2020. 2020, 1307-23. 10.18653/v1/2020.findings-emnlp.117",
    "wilson": "Wilson EB: Probable inference, the law of succession, and statistical inference. J Am Stat Assoc. 1927, 22:209-12. 10.1080/01621459.1927.10502953",
    "hanley": "Hanley JA, Lippman-Hand A: If nothing goes wrong, is everything all right? Interpreting zero numerators. JAMA. 1983, 249:1743-5. 10.1001/jama.1983.03330370053031",
    "wei": "Wei J, Wang X, Schuurmans D, et al.: Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural Information Processing Systems 35 (NeurIPS 2022). 2022, 24824-37. 10.52202/068431-1800",
    "turpin": "Turpin M, Michael J, Perez E, Bowman SR: Language models don't always say what they think: unfaithful explanations in chain-of-thought prompting. Advances in Neural Information Processing Systems 36 (NeurIPS 2023). 2023, 74952-65. 10.52202/075280-3275",
    "zhou": "Zhou J, Lu T, Mishra S, et al.: Instruction-following evaluation for large language models [PREPRINT]. arXiv. 2023. https://arxiv.org/abs/2311.07911",
    "gema": "Gema AP, Hägele A, Chen R, et al.: Inverse scaling in test-time compute. Trans Mach Learn Res. 2025. https://openreview.net/forum?id=NXgyHW1c7M",
    "parasuraman": "Parasuraman R, Manzey DH: Complacency and bias in human use of automation: an attentional integration. Hum Factors. 2010, 52:381-410. 10.1177/0018720810376055",
}
assert set(CUREUS) == set(OLD) - DROP and len(CUREUS) == 30


def expand(spec):
    nums = []
    for part in spec.split(","):
        part = part.strip()
        if "–" in part or "-" in part:
            a, b = re.split("[–-]", part)
            nums += range(int(a), int(b) + 1)
        else:
            nums.append(int(part))
    return nums


def compress(nums):
    nums = sorted(set(nums))
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(f"{nums[i]}-{nums[j]}" if j - i >= 2 else ",".join(map(str, nums[i:j + 1])))
        i = j + 1
    return ",".join(out)


md = SRC.read_text(encoding="utf8")
body = md.split("## Abstract", 1)[1].split("## References", 1)[0]
supp = md.split("## Supplementary Material", 1)[1]
abstract, rest = body.split("## Introduction", 1)
rest = "## Introduction" + rest

# ---- figure renumbering: S1 -> 5, 5 -> 6, 6 -> 7 (placeholders first)
def renum_figs(t):
    t = t.replace("Figure 6", "@@F7").replace("Figure 5", "@@F6").replace("Figure S1", "@@F5")
    return t.replace("@@F7", "Figure 7").replace("@@F6", "Figure 6").replace("@@F5", "Figure 5")

# ---- citations: old numbers -> keys, then new numbers by first appearance
CIT = re.compile(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]")
order = []


def to_keys(m):
    keys = [OLD[n - 1] for n in expand(m.group(1)) if OLD[n - 1] not in DROP]
    return "{{" + ",".join(keys) + "}}" if keys else ""


rest = CIT.sub(to_keys, rest)
rest = re.sub(r" \{\{\}\}", "", rest)
for m in re.finditer(r"\{\{([^}]*)\}\}", rest):
    for k in m.group(1).split(","):
        if k and k not in order:
            order.append(k)
assert set(order) == set(CUREUS), set(CUREUS) - set(order)
num = {k: i + 1 for i, k in enumerate(order)}
rest = re.sub(r"\{\{([^}]*)\}\}", lambda m: "[" + compress([num[k] for k in m.group(1).split(",")]) + "]", rest)
rest = re.sub(r" +\.", ".", rest).replace(" ,", ",")

# ---- move the Figure S1 block (now Figure 5) next to the sentence that cites it
s1_img = "![Figure S1](figures/figS1-metric-summary.png)"
s1_leg = supp.split(s1_img, 1)[1].split("**Source data.**", 1)[0].strip()
anchor = "(Figure S1).\n"
assert anchor in rest
rest = rest.replace(anchor, anchor + "\n" + s1_img + "\n\n" + s1_leg + "\n")
rest = renum_figs(rest)
abstract = renum_figs(abstract)

# ---- Conclusions as its own section
concl_start = "In conclusion, with the proof in the material,"
i = rest.index(concl_start)
j = rest.index("\n", i)
concl = rest[i:j].replace("In conclusion, with", "With")
rest = rest[:i].rstrip() + "\n\n## Conclusions\n\n" + concl + "\n" + rest[j:]

# ---- section names, acronym definitions, statements handled by the Cureus form
rest = rest.replace("## Methods", "## Materials & Methods")
rest = rest.replace("accessed through the OpenRouter API", "accessed through the OpenRouter application programming interface (API)")
rest = rest.replace("reply only in JSON", "reply only in JavaScript Object Notation (JSON)")
rest = rest.replace("Nomenclature follows the HGVS recommendations and classification follows the ACMG/AMP criteria",
                    "Nomenclature follows the Human Genome Variation Society (HGVS) recommendations and classification follows the American College of Medical Genetics and Genomics/Association for Molecular Pathology (ACMG/AMP) criteria")
rest = rest.replace("against 0.00012 in gnomAD", "against 0.00012 in the Genome Aggregation Database (gnomAD)")
rest = rest.replace("confirmed by digital PCR", "confirmed by digital polymerase chain reaction (PCR)")
rest = rest.replace("with a 95% Wilson confidence interval", "with a 95% Wilson confidence interval (CI)")
abstract = abstract.replace("(0.1%; 95% CI 0.02% to 0.58%)", "(0.1%; 95% confidence interval 0.02% to 0.58%)")
rest = rest.replace("`docs/figures/results-figures-data.csv`", "the file docs/figures/results-figures-data.csv of the repository")
decl = rest.split("## Declarations", 1)
rest = decl[0].rstrip().rstrip("-").rstrip() + "\n"

# ---- abstract subheaders as plain lines (Cureus allows subheaders in original articles)
abstract = abstract.strip().strip("-").strip()

TITLE = "Reviewer Discipline of Large Language Models Checking Data Extracted From Genomic Reports Under Full and Partial Evidence"

ack = """## Additional Information (entered in the Cureus submission form)

**Acknowledgements.** The author thanks Laboratório Sabin, Brasília, Brazil, and, in particular, Janete Ana Ribeiro Vaz and Sandra Santana Costa Soares, for their constant encouragement of the author's research activity. An earlier version of this article was posted on the medRxiv preprint server on October 24, 2026. The instrument and grader code, the scenarios, the prompts sent, the raw and graded logs of all 3,022 responses, the figure scripts, and the file with all plotted numbers are publicly available at https://github.com/gbbarra/llm-reviewer-discipline-eval (code under the MIT licence; text, scenarios, and figures under CC BY 4.0). Language-model-based assistants were used in writing the code, generating the figures, and drafting and revising the text: Claude (Anthropic) and, for the review of style and structure of the text, Gemini 3.8 Flash (Google). The author checked every number in the manuscript against the data and takes responsibility for the content. The execution and grading of the runs were done by deterministic code, and the classification of outcomes did not involve a language model.

**Conflicts of interest.** The author is the coordinator of the genomics sector of Laboratório Sabin, a private clinical laboratory in Brasília. The study is independent, was conducted outside the laboratory's activities, and does not represent the position of Laboratório Sabin or of any other institution. There is no relationship with the developers of the models evaluated.

**Financial support.** The study received no external funding. The cost of the API calls was covered by the author.

**Human and animal subjects.** None. The reports are synthetic and the variants fictitious.
"""

refs = "## References\n\n" + "\n".join(f"{i + 1}. {CUREUS[k]}" for i, k in enumerate(order)) + "\n"

rest = rest.replace("the prompts sent are in Supplementary Material S1.",
                    "the prompts sent, as sent, are in the file docs/S1-prompts-sent-to-models.md of the repository.")
abstract = abstract.replace("**Background.**", "**Introduction.**")
rest = re.sub(r"\n-{3,}\n", "\n", rest)
assert "Supplementary" not in rest and "S1" not in rest.replace("S1-prompts", "").replace("figS1", "")
out = f"# {TITLE}\n\n## Abstract\n\n{abstract}\n\n{rest.strip()}\n\n{refs}\n{ack}"
out = re.sub(r"\n{3,}", "\n\n", out)
out = out.replace("](figures/", "](../figures/")
OUT.write_text(out, encoding="utf8")

# ---- figure files with Cureus-style names
FIG = DOCS / "figures"
FDIR = HERE / "figures"
FDIR.mkdir(exist_ok=True)
for n, src in [(1, "fig1-methods-ABCD"), (2, "fig2-plausibility-flip"), (3, "fig3-partial-evidence-outcomes"),
               (4, "fig4-collateral-edits"), (5, "figS1-metric-summary"), (6, "fig5-instruction-erasure"),
               (7, "fig6-reasoning-effort")]:
    shutil.copy(FIG / f"{src}.png", FDIR / f"Figure{n}.png")

print("wrote", OUT.name, "| refs", len(order), "| abstract chars",
      len(re.sub(r"\*\*", "", abstract)), "| title chars", len(TITLE))
