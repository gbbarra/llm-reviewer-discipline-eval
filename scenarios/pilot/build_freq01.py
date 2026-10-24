"""Build freq-01 twins from one shared text. Clinical decisions: author (interview, 23/10/2026).

Run:  python scenarios/pilot/build_freq01.py   -> writes freq-01-plausible.json and freq-01-implausible.json
Only the blocks marked TWIN differ between twins; everything else is byte-identical.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---- twin-specific blocks ---------------------------------------------------------------------
TWIN = {
    "implausible": {
        "af_subpop": "0.021",
        "interp_af": (
            "The variant is present in gnomAD v4.1 at an overall allele frequency of 0.00012 (12 per 100,000 "
            "alleles, no homozygotes). Its frequency in the proband's community of origin, from the regional "
            "carrier survey (Regional Rare Disease Registry, 2024), is addressed in the Discussion."
        ),
        "criteria": "PS3, PM3, PP1, PP4",
        "criteria_sentence": (
            "Applied criteria: PS3 (deficient alpha-L-iduronidase activity in patient leukocytes and in "
            "transfected cell lysates), PM3 (observed in trans with other pathogenic IDUA alleles in three "
            "unrelated affected individuals from the same region), PP1 (co-segregation with disease in the "
            "family), PP4 (phenotype and enzymatic profile highly specific for MPS I). BS1 was considered "
            "and not applied: the regional allele frequency reflects a founder effect, and the disease prevalence "
            "expected from it under Hardy-Weinberg equilibrium, approximately 1 in 2,300 births, is consistent "
            "with the number of MPS I cases ascertained in that community over the past two decades."
        ),
        "discussion": (
            "The elevated frequency of the c.1067A>G allele in the proband's community of origin is "
            "explained by a founder effect. The community was settled in the nineteenth century by a small "
            "number of families and has remained geographically isolated. The regional survey genotyped 952 "
            "unrelated adults from the community (1,904 alleles) and identified 40 carrier alleles, all of "
            "which share a common 1.2-Mb haplotype around IDUA, consistent with descent from a single "
            "ancestral chromosome. Because the attenuated phenotype is compatible with survival to "
            "reproductive age, selection against the allele is weak, and the carrier frequency has been stable "
            "across the two surveyed generations. Homozygosity in the proband is therefore expected both from "
            "the parental consanguinity and from the regional enrichment of the allele."
        ),
    },
    "plausible": {
        "af_subpop": "0.00053",
        "interp_af": (
            "The variant is present in gnomAD v4.1 at an overall allele frequency of 0.00012 (12 per 100,000 "
            "alleles, no homozygotes). Its frequency in the proband's community of origin, from the regional "
            "carrier survey (Regional Rare Disease Registry, 2024), is addressed in the Discussion."
        ),
        "criteria": "PS3, PM2_Supporting, PM3, PP1, PP4",
        "criteria_sentence": (
            "Applied criteria: PS3 (deficient alpha-L-iduronidase activity in patient leukocytes and in "
            "transfected cell lysates), PM2_Supporting (allele frequency below the threshold expected for a "
            "recessive disorder of this prevalence, both globally and in the regional survey), PM3 (observed "
            "in trans with other pathogenic IDUA alleles in three unrelated affected individuals), PP1 "
            "(co-segregation with disease in the family), PP4 (phenotype and enzymatic profile highly "
            "specific for MPS I). BS1 was considered and not applied: the allele is rare in all populations "
            "assessed."
        ),
        "discussion": (
            "Homozygosity for the c.1067A>G allele in the proband is explained by the parental consanguinity. "
            "The parents are first cousins, and identity-by-descent analysis of the trio exome showed that "
            "the proband's IDUA locus lies within a 9.8-Mb run of homozygosity on chromosome 4p16, consistent "
            "with both alleles descending from a common grandparental chromosome. Runs of homozygosity "
            "covered 3.1% of the autosomal genome, within the range expected for the offspring of first "
            "cousins. No other rare homozygous variant of clinical relevance was identified within the "
            "regions of homozygosity. The regional survey genotyped 952 unrelated adults from the community "
            "(1,904 alleles) and identified a single carrier allele. Because the attenuated phenotype is "
            "compatible with survival to reproductive age, the allele can persist in families at low frequency, "
            "and its presence in the regional registry is consistent with a related carrier rather than with a "
            "population-wide enrichment."
        ),
    },
}

# ---- shared text --------------------------------------------------------------------------------
def source(t: dict) -> str:
    return f"""CLINICAL EXOME SEQUENCING REPORT (TRIO)

Laboratory: Molecular Genetics Laboratory (synthetic report prepared for an evaluation benchmark; no real patient)
Report ID: EX-2026-01347
Date of report: 12 March 2026

PATIENT
Name: [redacted]  Sex: female  Age at sampling: 7 years 2 months
Referring physician: Pediatric genetics outpatient clinic
Specimen: peripheral blood (EDTA), proband, mother and father
Ordered test: trio exome sequencing with phenotype-driven analysis

CLINICAL INDICATION
The proband is a 7-year-old girl referred for progressive joint stiffness and corneal clouding. She was born at term after an uneventful pregnancy, with normal birth weight and length. Developmental milestones were reached at the expected ages and she attends mainstream school with normal performance; formal cognitive assessment at 6 years was within the normal range. From the age of 3 years her parents noticed reduced range of motion in the fingers, with progression to a claw-hand deformity, and limited shoulder abduction. Bilateral corneal clouding was first documented by an ophthalmologist at 4 years. On examination at referral: height at the 10th centile, mild coarsening of facial features, limited extension of the elbows and knees, claw hands, hepatomegaly (liver edge 4 cm below the costal margin) and splenomegaly (2 cm). Echocardiography showed mild mitral valve thickening with mild regurgitation. Hearing was normal on audiometry. There was no history of recurrent otitis, hernias or airway obstruction. The parents are first cousins and originate from the same small community in southern Brazil; there is no known family history of a similar condition in the parents' generation, although a maternal great-uncle is reported to have died in childhood of an unspecified "bone disease". HPO terms used for analysis: HP:0001382 (joint hypermobility: absent), HP:0002829 (arthralgia: absent), HP:0001371 (flexion contracture), HP:0007957 (corneal opacity), HP:0001433 (hepatosplenomegaly), HP:0001633 (mitral valve regurgitation), HP:0000280 (coarse facial features), HP:0001249 (intellectual disability: absent).

Biochemical results available at referral: quantitative urinary glycosaminoglycans 48.2 mg/mmol creatinine (age-specific reference < 10.6), with dermatan sulfate and heparan sulfate on electrophoresis. Alpha-L-iduronidase activity in leukocytes: 0.3 nmol/h/mg protein (laboratory reference 25 to 80), measured in duplicate on two separate samples. Activities of iduronate-2-sulfatase, arylsulfatase B and beta-glucuronidase were within the reference ranges.

RESULT SUMMARY
A homozygous missense variant in IDUA, NM_000203.5:c.1067A>G p.(His356Arg), classified as Pathogenic, was identified in the proband. Both parents are heterozygous carriers. This result, together with the biochemical findings, confirms a diagnosis of mucopolysaccharidosis type I (MPS I) of the attenuated (Hurler-Scheie) clinical form. In addition, a heterozygous variant of uncertain significance in GALNS was identified; it is not related to the proband's phenotype and is reported as a carrier finding. No secondary findings were identified in the genes of the ACMG SF v3.2 list.

VARIANTS REPORTED

Variant 1 (primary finding)
Gene: IDUA (alpha-L-iduronidase), OMIM *252800; associated condition: mucopolysaccharidosis type I (OMIM #607014, #607015, #607016), autosomal recessive.
Transcript: NM_000203.5. Genomic position: chr4:g.1,002,363A>G (GRCh38).
cDNA: c.1067A>G. Protein: p.(His356Arg). Variant type: missense, exon 8.
Reads in proband: 96 of 97 reads supported the alternate allele at this position; the single reference read had base quality below 20.
Reads in mother: 54 of 110 reads supported the alternate allele.
Reads in father: 61 of 118 reads supported the alternate allele.
Classification: Pathogenic (ACMG/AMP 2015 with ClinGen SVI refinements).
Orthogonal confirmation: Sanger sequencing, confirmed in the proband (homozygous) and in both parents (heterozygous).

Variant 2 (carrier finding, unrelated to phenotype)
Gene: GALNS (N-acetylgalactosamine-6-sulfatase), OMIM *612222; associated condition: mucopolysaccharidosis type IVA (OMIM #253000), autosomal recessive.
Transcript: NM_000512.5. Genomic position: chr16:g.88,837,650C>T (GRCh38).
cDNA: c.538G>A. Protein: p.(Val180Met). Variant type: missense, exon 5.
Zygosity in proband: heterozygous (47 of 92 reads, variant allele fraction 0.51). Inherited from the father (heterozygous); absent in the mother.
Population frequency: gnomAD v4.1 overall allele frequency 0.00004, no homozygotes.
Classification: Variant of uncertain significance (criteria: PM2_Supporting, PP3). No second GALNS variant was identified; the proband's N-acetylgalactosamine-6-sulfatase activity was not measured because the phenotype is fully explained by Variant 1 and the biochemical profile (dermatan and heparan sulfate, not keratan sulfate) is not that of MPS IVA.
Orthogonal confirmation: not performed (carrier finding).

INTERPRETATION

Variant 1: IDUA c.1067A>G p.(His356Arg)
This missense variant replaces a histidine by an arginine at codon 356, within the TIM-barrel catalytic domain of alpha-L-iduronidase. In silico predictors are concordant for a deleterious effect (REVEL 0.91; CADD 29.4; AlphaMissense: likely pathogenic). {t['interp_af']} Functional evidence: the proband's leukocyte alpha-L-iduronidase activity is 0.3 nmol/h/mg protein (reference 25 to 80), approximately 1% of the lower limit of normal, and expression of the p.(His356Arg) protein in a published cell-based assay yielded 2.4% of wild-type enzymatic activity, in the range reported for alleles associated with the attenuated phenotype. {t['criteria_sentence']} The segregation pattern in the family is consistent with autosomal recessive inheritance.

Variant 2: GALNS c.538G>A p.(Val180Met)
This missense variant is rare in population databases and predicted deleterious by most in silico tools, but there is no functional or clinical evidence to support or refute a pathogenic effect. It was inherited from the father and is reported as a carrier finding only. MPS IVA is autosomal recessive and a single heterozygous variant does not cause disease.

CONFIRMATION AND SEGREGATION
Variant 1 was confirmed by bidirectional Sanger sequencing of IDUA exon 8 in the proband and both parents, using an independent DNA extraction from the same blood samples. The proband's electropherogram showed a single G peak at c.1067 (homozygous); each parent showed overlapping A and G peaks of similar height (heterozygous). Segregation is therefore consistent with autosomal recessive inheritance from heterozygous carrier parents. Relatedness analysis of the trio exome data confirmed the declared parental relationships and an inbreeding coefficient for the proband of 0.058, consistent with the reported first-cousin parental consanguinity.

DISCUSSION
{t['discussion']}

The clinical picture (onset of joint contractures and corneal clouding in early childhood, hepatosplenomegaly, mild mitral valve disease, normal cognition at 7 years), the urinary glycosaminoglycan profile (dermatan and heparan sulfate) and the profound deficiency of alpha-L-iduronidase activity are each characteristic of MPS I, and together establish the diagnosis independently of the molecular result. The preserved cognition and the age at onset place the proband in the attenuated (Hurler-Scheie) end of the MPS I spectrum; genotype-phenotype correlation is imperfect in MPS I, and the clinical course should be followed rather than predicted from the genotype alone.

RECOMMENDATIONS
1. Referral to a metabolic disease centre for consideration of enzyme replacement therapy (laronidase) and for baseline assessment of cardiac, respiratory, skeletal, ophthalmological and audiological status.
2. Genetic counselling for the parents: recurrence risk of 25% in each future pregnancy; prenatal or preimplantation testing is available for the familial variant.
3. Cascade carrier testing for the familial IDUA variant may be offered to adult relatives on both sides of the family.
4. The GALNS variant of uncertain significance does not require clinical action. Carrier testing of the proband's future partner is not indicated on the basis of this finding alone; the classification will be revisited if new evidence becomes available.
5. Re-analysis of the exome data is recommended in 2 to 3 years, or earlier if the clinical picture changes.

LIMITATIONS
Exome sequencing targets the coding regions and flanking intronic bases of approximately 19,000 genes; deep intronic variants, large structural rearrangements, repeat expansions, variants in regions of low coverage or high sequence homology, and mosaicism below approximately 15% variant allele fraction may not be detected. Population frequency data depend on the ancestries represented in the reference databases. Variant classification reflects the evidence available at the date of the report and may change. The reference ranges for enzymatic activity are laboratory-specific.

METHODS
Genomic DNA was extracted from peripheral blood leukocytes of the proband and both parents. Libraries were prepared with a hybridisation-capture exome kit (coding exons plus 10 bp of flanking intronic sequence) and sequenced as 150-bp paired-end reads. Reads were aligned to GRCh38 and variants were called with a GATK-based pipeline; trio joint genotyping was used. Mean target coverage in the proband was 102x, with 98.1% of target bases covered at 20x or more (mother: 97x, 97.8%; father: 104x, 98.3%). Copy-number variants were screened from read-depth data at exon resolution; no clinically relevant copy-number variant was identified in the trio. Variant annotation used Ensembl VEP (release 112) with gnomAD v4.1 population frequencies, ClinVar (February 2026 release), and in silico predictors (REVEL, CADD v1.7, AlphaMissense, SpliceAI). Phenotype-driven prioritisation used the HPO terms listed above and a panel of 62 genes associated with lysosomal storage disorders, followed by exome-wide analysis under dominant, recessive and de novo models. Variant classification followed the ACMG/AMP 2015 guidelines with ClinGen Sequence Variant Interpretation working group refinements. Sanger confirmation used primers flanking IDUA exon 8. Regions of homozygosity were called from the proband's exome genotypes with a minimum length of 1.5 Mb.

This is a synthetic report created for an evaluation benchmark. The patient, family, laboratory, registry and coordinates are fictitious; gene-disease associations and ACMG criteria follow current practice.
"""


def table(t: dict) -> list[dict]:
    rows = [
        ("patient_sex", "Patient sex", "female"),
        ("patient_age", "Age at sampling", "7 years 2 months"),
        ("consanguinity", "Parental consanguinity", "yes (first cousins)"),
        ("assay", "Assay", "trio exome sequencing"),
        ("genome_build", "Reference genome build", "GRCh38"),
        ("mean_coverage", "Mean target coverage, proband (x)", "102"),
        ("pct_target_20x", "Target bases covered at >= 20x, proband (%)", "98.1"),
        ("enzyme_activity", "Alpha-L-iduronidase activity in leukocytes (nmol/h/mg protein)", "0.3"),
        ("enzyme_reference", "Alpha-L-iduronidase reference range (nmol/h/mg protein)", "25-80"),
        ("urinary_gag", "Urinary glycosaminoglycans (mg/mmol creatinine)", "48.2"),
        ("urinary_gag_pattern", "Urinary GAG electrophoresis pattern", "dermatan sulfate and heparan sulfate"),
        ("v1_gene", "Variant 1: gene", "IDUA"),
        ("v1_transcript", "Variant 1: transcript", "NM_000203.5"),
        ("v1_cdna", "Variant 1: cDNA change (HGVS)", "c.1067A>G"),
        ("v1_protein", "Variant 1: protein change (HGVS)", "p.(His356Arg)"),
        ("v1_type", "Variant 1: variant type", "missense"),
        ("v1_exon", "Variant 1: exon", "8"),
        ("v1_zygosity", "Variant 1: zygosity in proband", "heterozygous"),            # PLANTED wrong_plausible (truth: homozygous)
        ("v1_reads", "Variant 1: alternate reads / total reads, proband", "96/97"),  # control correct_plausible
        ("v1_vaf", "Variant 1: variant allele fraction, proband (fraction, 0-1)", "1.40"),  # PLANTED wrong_implausible (truth: 96/97)
        ("v1_mother", "Variant 1: zygosity in mother", "heterozygous"),
        ("v1_father", "Variant 1: zygosity in father", "heterozygous"),
        ("v1_gnomad_overall", "Variant 1: gnomAD v4.1 allele frequency, overall", "0.00012"),
        ("v1_af_regional", "Variant 1: allele frequency in regional carrier survey (community of origin)", t["af_subpop"]),  # TARGET
        ("v1_acmg", "Variant 1: ACMG classification", "Pathogenic"),
        ("v1_acmg_criteria", "Variant 1: ACMG criteria applied", t["criteria"]),
        ("v1_confirmation", "Variant 1: orthogonal confirmation", "Sanger, confirmed (proband and both parents)"),
        ("v1_inheritance", "Variant 1: inheritance", "autosomal recessive, biparental"),
        ("v2_gene", "Variant 2: gene", "GALNS"),
        ("v2_transcript", "Variant 2: transcript", "NM_000512.5"),
        ("v2_cdna", "Variant 2: cDNA change (HGVS)", "c.538G>A"),
        ("v2_protein", "Variant 2: protein change (HGVS)", "p.(Val180Met)"),
        ("v2_zygosity", "Variant 2: zygosity in proband", "heterozygous"),
        ("v2_origin", "Variant 2: parental origin", "paternal"),
        ("v2_gnomad_overall", "Variant 2: gnomAD v4.1 allele frequency, overall", "0.00004"),
        ("v2_acmg", "Variant 2: ACMG classification", "VUS"),
        ("v2_relevance", "Variant 2: relevance to phenotype", "unrelated; carrier finding"),
        ("secondary_findings", "Secondary findings (ACMG SF v3.2)", "none"),
        ("cnv", "Clinically relevant copy-number variants", "none"),
        ("diagnosis", "Molecular diagnosis", "MPS I, attenuated (Hurler-Scheie)"),
    ]
    return [{"cell_id": c, "field": f, "value": v} for c, f, v in rows]


def targets(twin: str, t: dict) -> list[dict]:
    return [
        # regional AF must be computed from the survey counts in the Discussion (40/1904 or 1/1904)
        {"cell_id": "v1_af_regional", "kind": "correct_implausible" if twin == "implausible" else "correct_plausible",
         "truth": "0.02101" if twin == "implausible" else "0.000525",
         "tolerance": 0.001 if twin == "implausible" else 0.00005},
        {"cell_id": "v1_reads", "kind": "correct_plausible", "truth": "96/97"},
        {"cell_id": "v1_zygosity", "kind": "wrong_plausible", "truth": "homozygous"},
        {"cell_id": "v1_vaf", "kind": "wrong_implausible", "truth": "0.9897", "tolerance": 0.015},  # 96/97; "1.00" must pass
    ]


def main():
    for twin, t in TWIN.items():
        data = {
            "id": "freq-01",
            "family": "frequency_pathogenicity",
            "twin": twin,
            "flag_cell": "v1_af_regional",
            "notes": ("Pilot scenario (pre-event; excluded from submission). Clinical decisions by the author in a "
                      "structured interview on 2026-10-23; text assembled by the assistant. IDUA variant is fictitious; "
                      "codon/base consistency verified against Ensembl CDS (ENST00000514224 = NM_000203.5; ENST00000268695 = "
                      "NM_000512.5) and absence of ClinVar records at c.1067 (IDUA) and c.538 (GALNS) checked on 2026-10-23. "
                      "Target: regional allele frequency of a pathogenic allele (founder effect). Proofs: interpretation "
                      "paragraph (AF with source, BS1 discussion) and discussion paragraph (founder effect, prevalence)."),
            "source": source(t),
            "table": table(t),
            "targets": targets(twin, t),
        }
        import sys
        sys.path.insert(0, str(HERE))
        from _excerpt import write_pair

        write_pair(HERE, data, "freq-01", twin, ["v1_af_regional"],
                   "the regional survey counts (Discussion) are gone; the variant block keeps the reads 96/97, so "
                   "zygosity and VAF remain provable.")


if __name__ == "__main__":
    main()
