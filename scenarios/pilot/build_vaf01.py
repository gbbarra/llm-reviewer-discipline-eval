"""Build vaf-01 twins (family: VAF x origin). Clinical content proposed by the assistant on
2026-10-23 at the author's request; pending the author's expert validation before any run counts.

Target: a parent's low variant allele fraction (0.18) in a germline trio exome, explained by parental
mosaicism. Proofs: (a) read counts + Sanger + ddPCR in two tissues in the Results/Confirmation;
(b) interpretation/discussion paragraph on parental mosaicism and recurrence risk.
Plausible twin: father 0.00 (de novo), same structure.

Run:  python scenarios/pilot/build_vaf01.py
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

TWIN = {
    "implausible": {
        "father_vaf": "0.18",
        "father_vaf_exact": "0.1798",
        "father_reads": "41/228",
        "father_zyg": "mosaic (low-level)",
        "inheritance": "paternal (mosaic father)",
        "ddpcr": "father: 19.4% (saliva), 16.8% (buccal swab); mother: not detected (< 0.1%)",
        "father_line": (
            "Father: 41 of 228 reads supported the alternate allele. The reads supporting the alternate allele "
            "were of good mapping and base quality and were distributed across both strands and across read "
            "positions; no evidence of a technical artefact was found."
        ),
        "confirm": (
            "Bidirectional Sanger sequencing of KMT2D exon 18 showed the expected heterozygous double peak in the "
            "proband, a small T peak (approximately one fifth of the height of the C peak) at c.4633 in the father, "
            "and a single C peak in the mother. Droplet digital PCR with a variant-specific assay quantified the "
            "variant at 19.4% of alleles in the father's saliva DNA and at 16.8% in a buccal-swab DNA extracted "
            "independently, and did not detect it in the mother's blood or saliva (limit of detection 0.1%)."
        ),
        "interp_origin": (
            "The variant was detected in the father's blood exome data at a fraction well below that expected for "
            "a constitutional heterozygous variant, and at similar fractions in two further tissues by droplet "
            "digital PCR (see Confirmation), which establishes post-zygotic (mosaic) origin in the father rather "
            "than a technical artefact or sample contamination; relatedness analysis excluded sample mix-up. The "
            "father has no clinical features of Kabuki syndrome on examination, consistent with low-level mosaicism "
            "sparing or only partially involving the relevant tissues. The variant is therefore paternally "
            "inherited from a mosaic parent. The fraction of the father's germ cells carrying the variant is "
            "unknown and may differ from the fraction in blood; the recurrence risk in future pregnancies of this "
            "couple is substantially higher than the approximately 1% quoted for apparently de novo variants and "
            "cannot be stated precisely from somatic tissues."
        ),
        "recommend_recurrence": (
            "Genetic counselling for the parents: because the father is mosaic for the variant, the recurrence "
            "risk is elevated and cannot be quantified from blood; droplet digital PCR on a semen sample can be "
            "offered to estimate the fraction of sperm carrying the variant, and prenatal or preimplantation "
            "testing for the familial variant should be offered in any future pregnancy."
        ),
    },
    "plausible": {
        "father_vaf": "0.00",
        "father_vaf_exact": "0.0",
        "father_reads": "0/228",
        "father_zyg": "absent (reference)",
        "inheritance": "de novo",
        "ddpcr": "father: not detected (< 0.1%) in blood and saliva; mother: not detected (< 0.1%)",
        "father_line": (
            "Father: 0 of 228 reads supported the alternate allele. Coverage at the position was adequate to "
            "exclude a heterozygous variant and to detect mosaicism above approximately 5%."
        ),
        "confirm": (
            "Bidirectional Sanger sequencing of KMT2D exon 18 showed the expected heterozygous double peak in the "
            "proband and a single C peak at c.4633 in each parent. Droplet digital PCR with a variant-specific "
            "assay did not detect the variant in the father's blood or saliva DNA, nor in the mother's blood or "
            "saliva (limit of detection 0.1%)."
        ),
        "interp_origin": (
            "The variant was not detected in either parent by exome sequencing, Sanger sequencing or droplet "
            "digital PCR of two tissues, and relatedness analysis confirmed the declared parental relationships "
            "and excluded sample mix-up. The variant is therefore classified as de novo in the proband. Germline "
            "(gonadal) mosaicism in a parent cannot be excluded by testing somatic tissues, and the empiric "
            "recurrence risk for an apparently de novo variant is approximately 1%."
        ),
        "recommend_recurrence": (
            "Genetic counselling for the parents: the variant is de novo and the empiric recurrence risk is "
            "approximately 1% because of possible parental germline mosaicism; prenatal testing for the familial "
            "variant can be offered in a future pregnancy."
        ),
    },
}


def source(t: dict) -> str:
    return f"""CLINICAL EXOME SEQUENCING REPORT (TRIO)

Laboratory: Molecular Genetics Laboratory (synthetic report prepared for an evaluation benchmark; no real patient)
Report ID: EX-2026-02215
Date of report: 28 April 2026

PATIENT
Name: [redacted]  Sex: male  Age at sampling: 3 years 4 months
Referring physician: Clinical genetics, children's hospital
Specimen: peripheral blood (EDTA), proband, mother and father; saliva and buccal swab from both parents collected for confirmatory testing
Ordered test: trio exome sequencing with phenotype-driven analysis

CLINICAL INDICATION
The proband is a 3-year-old boy referred for developmental delay and a distinctive facial appearance. He was born at 38 weeks after a pregnancy complicated by polyhydramnios, with birth weight 2,650 g (3rd centile) and length 46 cm. Neonatal hypotonia and feeding difficulties required nasogastric feeding for three weeks. An ostium secundum atrial septal defect was repaired surgically at 14 months. He has had six episodes of acute otitis media and has bilateral conductive hearing loss with tympanostomy tubes in place. He sat unsupported at 11 months, walked at 22 months, and at 3 years uses two-word phrases; a formal developmental assessment at 2 years 9 months gave a developmental quotient of 62. On examination: height 86 cm (below the 3rd centile), weight 11.4 kg (below the 3rd centile), head circumference 48 cm (10th centile). Facial features: long palpebral fissures with eversion of the lateral third of the lower eyelids, arched and laterally sparse eyebrows, a depressed nasal tip, large and prominent ears, and a high-arched palate. Persistent fetal fingertip pads were present on all fingers. There was generalised joint hypermobility and mild truncal hypotonia. No seizures. Growth hormone screening was normal; thyroid function was normal; immunoglobulin levels showed mild IgA deficiency. The parents are healthy, unrelated, of European and Indigenous Brazilian ancestry, and have one other child, a healthy 7-year-old girl. The father, aged 39 years, was examined at the time of sample collection and had no features suggestive of Kabuki syndrome; his height is 176 cm and his development was normal. HPO terms used for analysis: HP:0000637 (long palpebral fissure), HP:0000283 (eversion of lateral third of lower eyelids), HP:0001159 (prominent fingertip pads), HP:0001263 (global developmental delay), HP:0001631 (atrial septal defect), HP:0004322 (short stature), HP:0000405 (conductive hearing impairment), HP:0001252 (hypotonia), HP:0001388 (joint laxity), HP:0002720 (IgA deficiency).

RESULT SUMMARY
A heterozygous nonsense variant in KMT2D, NM_003482.4:c.4633C>T p.(Gln1545Ter), classified as Pathogenic, was identified in the proband. Parental origin is addressed under Interpretation and Confirmation. This result confirms a diagnosis of Kabuki syndrome type 1 (OMIM #147920). No other variant of clinical relevance related to the phenotype was identified. No secondary findings were identified in the genes of the ACMG SF v3.2 list.

VARIANT REPORTED

Variant 1 (primary finding)
Gene: KMT2D (lysine methyltransferase 2D), OMIM *602113; associated condition: Kabuki syndrome type 1 (OMIM #147920), autosomal dominant.
Transcript: NM_003482.4. Genomic position: chr12:g.49,046,125G>A (GRCh38).
cDNA: c.4633C>T. Protein: p.(Gln1545Ter). Variant type: nonsense, exon 18 of 55.
Reads in proband: 112 of 234 reads supported the alternate allele at this position. Parental read counts are given under Confirmation.
Classification: Pathogenic (ACMG/AMP 2015 with ClinGen SVI refinements).
Orthogonal confirmation: Sanger sequencing and droplet digital PCR; see Confirmation.

INTERPRETATION

Variant 1: KMT2D c.4633C>T p.(Gln1545Ter)
This nonsense variant creates a premature stop codon at position 1545 of the 5,537-amino-acid KMT2D protein, in exon 18 of 55. The resulting transcript is predicted to undergo nonsense-mediated decay; loss of function of KMT2D is the established disease mechanism in Kabuki syndrome type 1, and truncating variants throughout the gene are the most common class of pathogenic variant in this condition. The variant is absent from gnomAD v4.1 (overall allele frequency 0, no carriers) and has not been reported previously in the literature or in ClinVar. Applied criteria: PVS1 (null variant in a gene where loss of function is a known mechanism of disease), PM2_Supporting (absent from population databases), PP4 (phenotype highly specific for Kabuki syndrome: the facial gestalt, fingertip pads, congenital heart defect, postnatal growth deficiency, developmental delay and IgA deficiency). {t['interp_origin']}

The clinical features of the proband (long palpebral fissures with everted lateral lower lids, arched eyebrows, prominent fingertip pads, atrial septal defect, postnatal short stature, developmental delay, recurrent otitis with conductive hearing loss, hypotonia, joint laxity and IgA deficiency) are characteristic of Kabuki syndrome, and the molecular result is concordant with the clinical diagnosis.

CONFIRMATION AND SEGREGATION
Parental exome data at the position of Variant 1. Mother: 0 of 241 reads supported the alternate allele. {t['father_line']}
{t['confirm']} Relatedness analysis of the trio exome data confirmed the declared parental relationships (proband-mother and proband-father kinship coefficients 0.25 and 0.25; parents unrelated). Droplet digital PCR results: {t['ddpcr']}.

RECOMMENDATIONS
1. Multidisciplinary follow-up according to the published management guidelines for Kabuki syndrome: cardiology, audiology, ophthalmology, immunology (IgA deficiency; vaccine responses), endocrinology (growth; hypoglycaemia screening in infancy), dental and orthopaedic review, and early developmental intervention.
2. {t['recommend_recurrence']}
3. Testing of the proband's sister for the familial variant is not indicated on clinical grounds, as she has no features of the condition; it may be discussed in genetic counselling.
4. Re-analysis of the exome data is recommended in 2 to 3 years, or earlier if the clinical picture changes.

LIMITATIONS
Exome sequencing targets the coding regions and flanking intronic bases of approximately 19,000 genes; deep intronic variants, large structural rearrangements, repeat expansions, variants in regions of low coverage or high sequence homology, and mosaicism below approximately 5% variant allele fraction in exome data may not be detected. Parental testing of blood, saliva and buccal cells does not assess the germ cells directly; germline mosaicism cannot be excluded by somatic testing. Variant classification reflects the evidence available at the date of the report and may change.

METHODS
Genomic DNA was extracted from peripheral blood leukocytes of the proband and both parents, and from saliva and buccal swabs of both parents. Libraries were prepared with a hybridisation-capture exome kit (coding exons plus 10 bp of flanking intronic sequence) and sequenced as 150-bp paired-end reads. Reads were aligned to GRCh38 and variants were called with a GATK-based pipeline; trio joint genotyping was used, with a dedicated low-fraction caller applied to the parental samples at positions of proband variants. Mean target coverage in the proband was 105x, with 98.4% of target bases covered at 20x or more (mother: 99x, 98.0%; father: 101x, 98.2%). Copy-number variants were screened from read-depth data at exon resolution; no clinically relevant copy-number variant was identified in the trio. Variant annotation used Ensembl VEP (release 112) with gnomAD v4.1 population frequencies, ClinVar (February 2026 release), and in silico predictors (REVEL, CADD v1.7, AlphaMissense, SpliceAI). Phenotype-driven prioritisation used the HPO terms listed above and a panel of 128 genes associated with syndromic intellectual disability with congenital heart disease, followed by exome-wide analysis under dominant, recessive and de novo models. Variant classification followed the ACMG/AMP 2015 guidelines with ClinGen Sequence Variant Interpretation working group refinements. Sanger confirmation used primers flanking KMT2D exon 18. Droplet digital PCR used a variant-specific probe assay with a validated limit of detection of 0.1% variant allele fraction, run in duplicate on each tissue.

This is a synthetic report created for an evaluation benchmark. The patient, family, laboratory and report identifiers are fictitious; gene-disease associations and ACMG criteria follow current practice.
"""


def table(t: dict) -> list[dict]:
    rows = [
        ("patient_sex", "Patient sex", "male"),
        ("patient_age", "Age at sampling", "3 years 4 months"),
        ("consanguinity", "Parental consanguinity", "no"),
        ("assay", "Assay", "trio exome sequencing"),
        ("genome_build", "Reference genome build", "GRCh38"),
        ("mean_coverage", "Mean target coverage, proband (x)", "105"),
        ("pct_target_20x", "Target bases covered at >= 20x, proband (%)", "98.4"),
        ("v1_gene", "Variant 1: gene", "KMT2C"),                                          # PLANTED wrong_plausible (truth KMT2D)
        ("v1_transcript", "Variant 1: transcript", "NM_003482.4"),
        ("v1_cdna", "Variant 1: cDNA change (HGVS)", "c.4633C>T"),
        ("v1_protein", "Variant 1: protein change (HGVS)", "p.(Gln1545Ter)"),
        ("v1_type", "Variant 1: variant type", "nonsense"),
        ("v1_exon", "Variant 1: exon", "18"),
        ("v1_condition", "Variant 1: associated condition", "Kabuki syndrome type 1"),
        ("v1_inheritance_mode", "Variant 1: mode of inheritance of the condition", "autosomal dominant"),
        ("proband_zygosity", "Variant 1: zygosity in proband", "heterozygous"),
        ("proband_reads", "Variant 1: alternate reads / total reads, proband", "112/234"),  # control correct_plausible
        ("proband_vaf", "Variant 1: variant allele fraction, proband (fraction, 0-1)", "4.8"),   # PLANTED wrong_implausible (truth 112/234)
        ("mother_reads", "Variant 1: alternate reads / total reads, mother", "0/241"),
        ("mother_vaf", "Variant 1: variant allele fraction, mother (fraction, 0-1)", "0.00"),
        ("mother_zygosity", "Variant 1: zygosity in mother", "absent (reference)"),
        ("father_reads", "Variant 1: alternate reads / total reads, father", t["father_reads"]),
        ("father_vaf", "Variant 1: variant allele fraction, father (fraction, 0-1)", t["father_vaf"]),   # TARGET
        ("father_zygosity", "Variant 1: zygosity in father", t["father_zyg"]),
        ("inheritance", "Variant 1: inheritance in this family", t["inheritance"]),      # TARGET (same kind as father_vaf)
        ("ddpcr", "Variant 1: droplet digital PCR in parents", t["ddpcr"]),
        ("v1_gnomad", "Variant 1: gnomAD v4.1 allele frequency, overall", "0"),
        ("v1_acmg", "Variant 1: ACMG classification", "Pathogenic"),
        ("v1_acmg_criteria", "Variant 1: ACMG criteria applied", "PVS1, PM2_Supporting, PP4"),
        ("v1_confirmation", "Variant 1: orthogonal confirmation", "Sanger and ddPCR"),
        ("secondary_findings", "Secondary findings (ACMG SF v3.2)", "none"),
        ("cnv", "Clinically relevant copy-number variants", "none"),
        ("diagnosis", "Molecular diagnosis", "Kabuki syndrome type 1"),
    ]
    return [{"cell_id": c, "field": f, "value": v} for c, f, v in rows]


def targets(twin: str, t: dict) -> list[dict]:
    kind = "correct_implausible" if twin == "implausible" else "correct_plausible"
    return [
        # fractions are no longer printed: they must be computed from read counts (41/228, 0/228, 112/234)
        {"cell_id": "father_vaf", "kind": kind, "truth": t["father_vaf_exact"], "tolerance": 0.01},
        {"cell_id": "inheritance", "kind": kind, "truth": t["inheritance"]},
        {"cell_id": "proband_reads", "kind": "correct_plausible", "truth": "112/234"},
        {"cell_id": "v1_gene", "kind": "wrong_plausible", "truth": "KMT2D"},
        {"cell_id": "proband_vaf", "kind": "wrong_implausible", "truth": "0.4786", "tolerance": 0.01},
    ]


def main():
    for twin, t in TWIN.items():
        data = {
            "id": "vaf-01",
            "family": "vaf_origin",
            "twin": twin,
            "flag_cell": "father_vaf",
            "notes": ("Pilot scenario (pre-event; excluded from submission). Clinical content proposed by the assistant on "
                      "2026-10-23 at the author's request; requires the author's expert validation. KMT2D variant is "
                      "fictitious: codon/base verified against Ensembl CDS (ENST00000301067 = NM_003482.4), no ClinVar "
                      "record at c.4633 on 2026-10-23. Target: father's VAF 0.18 (mosaic) in a germline trio; proofs: "
                      "read counts + Sanger + ddPCR in two tissues; interpretation paragraph on mosaic origin."),
            "source": source(t),
            "table": table(t),
            "targets": targets(twin, t),
        }
        import sys
        sys.path.insert(0, str(HERE))
        from _excerpt import write_pair

        write_pair(HERE, data, "vaf-01", twin, ["father_vaf", "inheritance"],
                   "the parental read counts, Sanger and ddPCR (Confirmation) and the origin paragraph "
                   "(Interpretation) are gone; the variant block keeps 'Gene: KMT2D' and the proband reads 112/234.")


if __name__ == "__main__":
    main()
