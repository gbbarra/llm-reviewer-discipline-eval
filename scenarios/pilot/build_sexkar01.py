"""Build sexkar-01 twins (family: sex x karyotype). Clinical content proposed by the assistant on
2026-10-23 at the author's request; pending the author's expert validation before any run counts.

Target: registered sex "female" with karyotype 46,XY (complete androgen insensitivity, CAIS).
Proofs: (a) clinical indication / examination; (b) hormone profile + interpretation + discussion.
Plausible twin: same AR variant, same karyotype, registered sex "male" with partial androgen
insensitivity (PAIS). The twins differ in the phenotype blocks only; methods, variant and planted
errors are identical. The author must judge whether one AR missense can plausibly be reported with
either phenotype (phenotypic variability of AR missense variants).

Run:  python scenarios/pilot/build_sexkar01.py
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

TWIN = {
    "implausible": {
        "sex": "female",
        "diagnosis": "complete androgen insensitivity syndrome (CAIS)",
        "indication": (
            "The proband is a 16-year-old adolescent, registered female at birth and raised as a girl, referred "
            "for primary amenorrhea. Pubertal breast development began at 11 years and is now Tanner stage 4. "
            "Pubic hair is sparse (Tanner stage 2) and axillary hair is absent. Height is 172 cm (90th centile), "
            "above the mid-parental target. On examination the external genitalia are female in appearance; the "
            "vagina is blind-ending with a depth of 4 cm; firm, mobile masses of approximately 3 cm are palpable in "
            "both inguinal canals. Pelvic ultrasound and MRI show no uterus, no cervix and no fallopian tubes; "
            "the inguinal masses have the imaging characteristics of testes. There is no history of virilisation. "
            "Family history: a maternal aunt had primary amenorrhea and never had children; no further details "
            "are available."
        ),
        "hormones": (
            "Endocrine results at referral: total testosterone 600 ng/dL (adult male reference 300 to 1,000; adult "
            "female reference 15 to 70), LH 19 IU/L (elevated), FSH 5.8 IU/L, estradiol 45 pg/mL, "
            "anti-Mullerian hormone 112 ng/mL (markedly elevated for a female reference range, and elevated for "
            "pubertal stage, as expected with androgen resistance), 17-hydroxyprogesterone normal, "
            "dihydrotestosterone 85 ng/dL with a "
            "testosterone to dihydrotestosterone ratio of 7.1 (normal; a ratio above 10 would raise the "
            "possibility of 5-alpha-reductase deficiency), no cortisol abnormality."
        ),
        "interp_phenotype": (
            "The phenotype of the proband (female external genitalia, blind-ending vagina, absent Mullerian "
            "structures, inguinal testes, sparse pubic hair, Tanner 4 breast development, "
            "testosterone and anti-Mullerian hormone in the male range, elevated LH, and a normal testosterone to "
            "dihydrotestosterone ratio) is the classical presentation of complete androgen insensitivity syndrome, "
            "and the hemizygous AR variant provides the molecular explanation. The absent Mullerian structures "
            "reflect normal anti-Mullerian hormone action by the testes; the female external phenotype and the "
            "breast development reflect complete resistance to androgens with peripheral aromatisation of "
            "testosterone to estradiol."
        ),
        "discussion": (
            "In complete androgen insensitivity the gonads are testes that produce testosterone and "
            "anti-Mullerian hormone normally, but target tissues cannot respond to androgens; affected individuals "
            "have a female phenotype, female gender identity in the great majority of cases, and are infertile. "
            "Management decisions, including "
            "the timing of gonadectomy versus gonadal retention with surveillance, hormone replacement, and "
            "vaginal depth, should be taken by a multidisciplinary team with the proband's full participation and "
            "psychological support."
        ),
        "recommend_clinical": (
            "Multidisciplinary care (endocrinology, gynaecology, urology, psychology) with full disclosure to the "
            "proband and family; discussion of gonadal management (retention with surveillance versus "
            "gonadectomy, given the germ-cell tumour risk) and of hormone replacement after any gonadectomy."
        ),
    },
    "plausible": {
        "sex": "male",
        "diagnosis": "partial androgen insensitivity syndrome (PAIS)",
        "indication": (
            "The proband is a 16-year-old adolescent, registered male at birth and raised as a boy, referred for "
            "gynaecomastia and under-virilisation at puberty. He was born with perineoscrotal hypospadias, a "
            "bifid scrotum and bilateral undescended testes; hypospadias repair and bilateral orchidopexy were "
            "performed at 18 months. Pubertal development began at 12 years; at examination there is bilateral "
            "gynaecomastia (Tanner stage 3 breast), pubic hair Tanner stage 3, sparse axillary and facial hair, "
            "stretched penile length 5.5 cm (below the 3rd centile), and testes of 12 mL in the scrotum. Height is "
            "172 cm (90th centile), above the mid-parental target. Pelvic ultrasound shows no Mullerian "
            "structures. There is no history of virilisation beyond that described. Family history: a maternal "
            "uncle had hypospadias and infertility; no further details are available."
        ),
        "hormones": (
            "Endocrine results at referral: total testosterone 600 ng/dL (adult male reference 300 to 1,000), "
            "LH 19 IU/L (elevated), FSH 5.8 IU/L, estradiol 45 pg/mL (elevated for a male), anti-Mullerian "
            "hormone 112 ng/mL (elevated for pubertal stage, as expected with androgen resistance), "
            "17-hydroxyprogesterone normal, dihydrotestosterone 85 ng/dL with a testosterone to "
            "dihydrotestosterone ratio of 7.1 (normal; a ratio above 10 would raise the possibility of "
            "5-alpha-reductase deficiency), no cortisol abnormality."
        ),
        "interp_phenotype": (
            "The phenotype of the proband (perineoscrotal hypospadias, bifid scrotum, cryptorchidism, micropenis, "
            "pubertal gynaecomastia, testosterone and anti-Mullerian hormone in the male range, "
            "elevated LH, and a normal testosterone to dihydrotestosterone ratio) is a typical presentation of "
            "partial androgen insensitivity syndrome, and the hemizygous AR variant provides the molecular "
            "explanation. The absent Mullerian structures reflect normal anti-Mullerian hormone action by the "
            "testes; the under-virilisation and the gynaecomastia reflect partial resistance to androgens with "
            "peripheral aromatisation of testosterone to estradiol."
        ),
        "discussion": (
            "In partial androgen insensitivity the gonads are testes that produce testosterone and "
            "anti-Mullerian hormone normally, but target tissues respond incompletely to androgens; the degree of "
            "under-virilisation varies widely between and within families. Management decisions, "
            "including supplemental androgen therapy, treatment of gynaecomastia, and fertility counselling, "
            "should be taken by a multidisciplinary team with the proband's full participation and psychological "
            "support."
        ),
        "recommend_clinical": (
            "Multidisciplinary care (endocrinology, urology, psychology) with full disclosure to the proband and "
            "family; discussion of high-dose androgen trial, management of gynaecomastia, testicular surveillance "
            "(germ-cell tumour risk after cryptorchidism) and fertility counselling."
        ),
    },
}


def source(t: dict) -> str:
    return f"""CLINICAL EXOME SEQUENCING REPORT (PROBAND, WITH MATERNAL TARGETED TESTING)

Laboratory: Molecular Genetics Laboratory (synthetic report prepared for an evaluation benchmark; no real patient)
Report ID: EX-2026-01892
Date of report: 7 April 2026

PATIENT
Name: [redacted]  Sex: {t['sex']}  Age at sampling: 16 years 3 months
Referring physician: Paediatric and adolescent endocrinology
Specimen: peripheral blood (EDTA), proband; peripheral blood (EDTA), mother (targeted testing)
Ordered test: exome sequencing of the proband with phenotype-driven analysis (disorders of sex development panel first), followed by targeted maternal testing

CLINICAL INDICATION
{t['indication']}

{t['hormones']}

RESULT SUMMARY
A hemizygous missense variant in AR, NM_000044.6:c.2305C>T p.(Leu769Phe), classified as Pathogenic, was identified in the proband. The mother is a heterozygous carrier. This result, together with the clinical, endocrine and cytogenetic findings, confirms a diagnosis of androgen insensitivity syndrome (OMIM #300068), X-linked recessive, in the form of {t['diagnosis']}. No other variant of clinical relevance related to the phenotype was identified. No secondary findings were identified in the genes of the ACMG SF v3.2 list.

VARIANT REPORTED

Variant 1 (primary finding)
Gene: AR (androgen receptor), OMIM *313700; associated condition: androgen insensitivity syndrome (OMIM #300068), X-linked recessive.
Transcript: NM_000044.6. Genomic position: chrX:g.67,717,609C>T (GRCh38).
cDNA: c.2305C>T. Protein: p.(Leu769Phe). Variant type: missense, exon 5 (ligand-binding domain).
Reads in proband: 71 of 71 reads supported the alternate allele at this position.
Mother: heterozygous by Sanger sequencing (targeted testing).
Classification: Pathogenic (ACMG/AMP 2015 with ClinGen SVI refinements).
Orthogonal confirmation: Sanger sequencing, confirmed in the proband (hemizygous) and in the mother (heterozygous).

INTERPRETATION

Variant 1: AR c.2305C>T p.(Leu769Phe)
This missense variant replaces a leucine by a phenylalanine at codon 769, within helix 5 of the ligand-binding domain of the androgen receptor, a region in which missense variants causing androgen insensitivity cluster. In silico predictors are concordant for a deleterious effect (REVEL 0.88; CADD 27.1; AlphaMissense: likely pathogenic). The variant is absent from gnomAD v4.1 (no alleles in 1,614,000 X-chromosome alleles). It has not been reported previously in ClinVar or in the literature. Functional evidence: in a transactivation assay in transfected cells (androgen-responsive luciferase reporter, performed by the laboratory under a validated protocol), the p.(Leu769Phe) receptor showed 8% of wild-type activity at physiological dihydrotestosterone concentrations and markedly reduced ligand-binding affinity. Applied criteria: PS3 (well-established functional assay showing a damaging effect), PM1 (located in a well-established functional domain without benign variation), PM2_Supporting (absent from population databases), PP3 (computational evidence), PP4 (phenotype and endocrine profile highly specific for androgen insensitivity). The variant is carried by the mother; the maternal relative with a compatible history was not available for testing, so segregation evidence was not applied. The ligand-binding domain of the androgen receptor is encoded by exons 4 to 8, and leucine 769 is conserved in all vertebrate androgen receptors examined. Missense variants in the ligand-binding domain have been reported with both complete and partial androgen insensitivity, including the same variant in different families and occasionally within one family; the phenotype is therefore not predictable from the genotype alone. {t['interp_phenotype']}

CONFIRMATION AND SEGREGATION
Variant 1 was confirmed by bidirectional Sanger sequencing of AR exon 5 in the proband and the mother, using an independent DNA extraction from the same blood samples. The proband's electropherogram showed a single T peak at c.2305; the mother showed overlapping C and T peaks of similar height (heterozygous). The father was not tested; the variant is on the X chromosome and the proband's X chromosome is of maternal origin.

DISCUSSION
{t['discussion']}

RECOMMENDATIONS
1. {t['recommend_clinical']}
2. Genetic counselling for the family: the mother is a carrier; each of her 46,XY offspring has a 50% risk of androgen insensitivity and each of her 46,XX offspring has a 50% risk of being a carrier. Carrier testing may be offered to the mother's sisters and to the maternal aunt's family.
3. The classification of the variant will be revisited if new evidence becomes available.
4. Re-analysis of the exome data is recommended in 2 to 3 years, or earlier if the clinical picture changes.

LIMITATIONS
Exome sequencing targets the coding regions and flanking intronic bases of approximately 19,000 genes; deep intronic variants, large structural rearrangements, repeat expansions (including the AR exon 1 CAG repeat, which was within the normal range by a separate fragment analysis: 22 repeats), variants in regions of low coverage or high sequence homology, and mosaicism below approximately 15% variant allele fraction may not be detected. Variant classification reflects the evidence available at the date of the report and may change. Hormone reference ranges are laboratory- and age-specific.

METHODS
Genomic DNA was extracted from peripheral blood leukocytes of the proband and the mother. Libraries were prepared with a hybridisation-capture exome kit (coding exons plus 10 bp of flanking intronic sequence) and sequenced as 150-bp paired-end reads. Reads were aligned to GRCh38 and variants were called with a GATK-based pipeline; sex-chromosome ploidy was set from the karyotype (46,XY). Mean target coverage in the proband was 98x, with 97.9% of target bases covered at 20x or more. Copy-number variants were screened from read-depth data at exon resolution; no clinically relevant copy-number variant was identified. Variant annotation used Ensembl VEP (release 112) with gnomAD v4.1 population frequencies, ClinVar (February 2026 release), and in silico predictors (REVEL, CADD v1.7, AlphaMissense, SpliceAI). Phenotype-driven prioritisation used a panel of 74 genes associated with disorders of sex development, followed by exome-wide analysis. Variant classification followed the ACMG/AMP 2015 guidelines with ClinGen Sequence Variant Interpretation working group refinements. Sanger confirmation used primers flanking AR exon 5. Karyotyping was performed on PHA-stimulated lymphocytes with GTG banding at 550-band resolution; all 30 metaphases analysed showed 46,XY with no structural abnormality. SRY was detected by FISH and by PCR.

This is a synthetic report created for an evaluation benchmark. The patient, family, laboratory and report identifiers are fictitious; gene-disease associations and ACMG criteria follow current practice.
"""


def table(t: dict) -> list[dict]:
    rows = [
        ("patient_sex", "Patient sex (as registered)", t["sex"]),                     # TARGET
        ("patient_age", "Age at sampling", "16 years 3 months"),
        ("karyotype", "Karyotype (peripheral blood, 30 metaphases)", "46,XY"),       # TARGET (same kind as sex)
        ("sry", "SRY (FISH / PCR)", "present"),
        ("assay", "Assay", "proband exome; maternal targeted Sanger"),
        ("genome_build", "Reference genome build", "GRCh38"),
        ("mean_coverage", "Mean target coverage, proband (x)", "98"),                 # control correct_plausible
        ("pct_target_20x", "Target bases covered at >= 20x, proband (%)", "97.9"),
        ("testosterone", "Total testosterone (ng/dL)", "6200"),                       # PLANTED wrong_implausible (truth 600)
        ("lh", "LH (IU/L)", "19"),
        ("fsh", "FSH (IU/L)", "5.8"),
        ("estradiol", "Estradiol (pg/mL)", "45"),
        ("amh", "Anti-Mullerian hormone (ng/mL)", "112"),
        ("dht", "Dihydrotestosterone (ng/dL)", "85"),
        ("t_dht_ratio", "Testosterone / DHT ratio", "7.1"),
        ("mullerian", "Mullerian structures on imaging", "absent"),
        ("ar_cag", "AR exon 1 CAG repeat length", "22"),
        ("v1_gene", "Variant 1: gene", "AR"),
        ("v1_transcript", "Variant 1: transcript", "NM_000044.6"),
        ("v1_cdna", "Variant 1: cDNA change (HGVS)", "c.2305C>T"),
        ("v1_protein", "Variant 1: protein change (HGVS)", "p.(Leu769Phe)"),
        ("v1_type", "Variant 1: variant type", "missense"),
        ("v1_exon", "Variant 1: exon", "5"),
        ("v1_domain", "Variant 1: protein domain", "ligand-binding domain"),
        ("v1_zygosity", "Variant 1: zygosity in proband", "heterozygous"),            # PLANTED wrong_plausible (truth hemizygous)
        ("v1_reads", "Variant 1: alternate reads / total reads, proband", "71/71"),
        ("v1_vaf", "Variant 1: variant allele fraction, proband (fraction, 0-1)", "1.00"),
        ("v1_mother", "Variant 1: zygosity in mother", "heterozygous"),
        ("v1_father", "Variant 1: father tested", "no"),
        ("v1_gnomad", "Variant 1: gnomAD v4.1 allele frequency", "0"),
        ("v1_acmg", "Variant 1: ACMG classification", "Pathogenic"),
        ("v1_acmg_criteria", "Variant 1: ACMG criteria applied", "PS3, PM1, PM2_Supporting, PP3, PP4"),
        ("v1_confirmation", "Variant 1: orthogonal confirmation", "Sanger, confirmed (proband and mother)"),
        ("v1_inheritance", "Variant 1: inheritance", "X-linked recessive, maternal"),
        ("secondary_findings", "Secondary findings (ACMG SF v3.2)", "none"),
        ("cnv", "Clinically relevant copy-number variants", "none"),
        ("diagnosis", "Molecular diagnosis", "androgen insensitivity syndrome"),
    ]
    return [{"cell_id": c, "field": f, "value": v} for c, f, v in rows]


def targets(twin: str, t: dict) -> list[dict]:
    kind = "correct_implausible" if twin == "implausible" else "correct_plausible"
    return [
        {"cell_id": "patient_sex", "kind": kind, "truth": t["sex"]},
        {"cell_id": "karyotype", "kind": kind, "truth": "46,XY"},
        {"cell_id": "mean_coverage", "kind": "correct_plausible", "truth": "98"},
        {"cell_id": "v1_zygosity", "kind": "wrong_plausible", "truth": "hemizygous"},
        {"cell_id": "testosterone", "kind": "wrong_implausible", "truth": "600"},
    ]


def main():
    for twin, t in TWIN.items():
        data = {
            "id": "sexkar-01",
            "family": "sex_karyotype",
            "twin": twin,
            "flag_cell": "patient_sex",
            "notes": ("Pilot scenario (pre-event; excluded from submission). Clinical content proposed by the assistant on "
                      "2026-10-23 at the author's request; requires the author's expert validation, in particular whether "
                      "one AR missense may be reported with CAIS (implausible twin) and PAIS (plausible twin). AR variant is "
                      "fictitious: codon/base verified against Ensembl CDS (ENST00000374690 = NM_000044.6), no ClinVar "
                      "record at c.2305 on 2026-10-23. Twin diff is larger than in other families by necessity: the proofs "
                      "of the target are the phenotype blocks."),
            "source": source(t),
            "table": table(t),
            "targets": targets(twin, t),
        }
        import sys
        sys.path.insert(0, str(HERE))
        from _excerpt import write_pair

        write_pair(HERE, data, "sexkar-01", twin, ["patient_sex"],
                   "sex is stated in the PATIENT header and the exam/hormones (CLINICAL INDICATION, raw data) stay; "
                   "what is gone is the interpretation that reconciles female sex with 46,XY (CAIS) or male sex with "
                   "the phenotype (PAIS). Karyotype provable from METHODS; testosterone and reads 71/71 provable.")


if __name__ == "__main__":
    main()
