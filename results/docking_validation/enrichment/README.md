# PfCDPK4 Docking Protocol Enrichment Validation

**Update timestamp:** 2026-05-22

## Source files received

```text
Enrichment_Report_HTVS_enrichment_from_project_selection.maegz
Enrichment_Report_HTVS_report.txt
ROC_PLOT_HTVS.png
Enrichment_Report_SP_enrichment_from_project_selection.maegz
Enrichment_Report_SP_report.txt
ROC_PLOT_SP.png
Enrichment_Report_XP_enrichment_from_project_selection.maegz
Enrichment_Report_XP_report.txt
ROC_PLOT_XP.png
```

## Purpose

This folder documents enrichment-validation outputs for the PfCDPK4 docking workflow across the Glide screening hierarchy:

1. HTVS
2. SP
3. XP

The validation set contained **20 known actives** and **1020 total ligands** including actives and decoys.

## Summary metrics

| Docking mode | Ranked actives | ROC AUC | RIE | BEDROC alpha=160.9 | BEDROC alpha=20 | BEDROC alpha=8 | Interpretation |
|---|---:|---:|---:|---:|---:|---:|---|
| HTVS | 19/20 | 0.55 | 0.55 | 0.000 | 0.034 | 0.110 | Weak enrichment; near-random early recognition |
| SP | 20/20 | 0.52 | 2.88 | 0.333 | 0.174 | 0.194 | Moderate early enrichment despite weak global ROC |
| XP | 20/20 | 0.77 | 6.76 | 0.475 | 0.409 | 0.500 | Best enrichment; strong early recognition and improved global discrimination |

## Early enrichment by percentage of total results

| Docking mode | Actives in top 1% | Actives in top 2% | Actives in top 5% | Actives in top 10% | Actives in top 20% |
|---|---:|---:|---:|---:|---:|
| HTVS | 0/20 (0%) | 0/20 (0%) | 1/20 (5%) | 1/20 (5%) | 4/20 (20%) |
| SP | 3/20 (15%) | 3/20 (15%) | 3/20 (15%) | 3/20 (15%) | 3/20 (15%) |
| XP | 4/20 (20%) | 6/20 (30%) | 7/20 (35%) | 11/20 (55%) | 12/20 (60%) |

## Enrichment factors by sample size

| Docking mode | EF1% | EF2% | EF5% | EF10% | EF20% |
|---|---:|---:|---:|---:|---:|
| HTVS | 0 | 0 | 1 | 0.5 | 1 |
| SP | 15 | 7.6 | 3 | 1.5 | 0.75 |
| XP | 20 | 15 | 7 | 5.5 | 3 |

## Interpretation

The enrichment results show a clear improvement across the Glide hierarchy. HTVS produced weak discrimination, with ROC AUC approximately 0.55 and no active compounds recovered within the top 1–2% of results. SP showed improved early recognition, recovering three actives within the top 1% and producing EF1% of 15, although its global ROC AUC remained close to random at approximately 0.52. XP produced the strongest validation profile, with ROC AUC of 0.77, RIE of 6.76, BEDROC(alpha=160.9) of 0.475, and recovery of 4 actives in the top 1%, 6 in the top 2%, 7 in the top 5%, and 11 in the top 10% of ranked results.

## Scientific conclusion

The XP docking stage provided the most reliable enrichment of known PfCDPK4 actives over decoys. The enrichment profile supports use of XP as the main pose-ranking and final prioritization stage in the virtual screening workflow. HTVS and SP remain useful as sequential filtering stages, but the validation results indicate that final candidate prioritization should rely more heavily on XP score, XP interaction quality, pose conservation, and subsequent MD/MM-GBSA evidence.

## Manuscript-ready interpretation

Docking-protocol validation using a benchmark set of 20 known PfCDPK4 actives and decoys demonstrated progressive enrichment across the Glide screening hierarchy. HTVS showed weak early enrichment, with ROC AUC of 0.55 and no active compounds recovered within the top 1–2% of ranked results. SP improved early active recovery, identifying three actives within the top 1% of results and yielding EF1% of 15, although its overall ROC AUC remained close to random. XP produced the strongest validation performance, with ROC AUC of 0.77, RIE of 6.76, BEDROC(alpha=160.9) of 0.475, and EF values of 20, 15, 7, 5.5, and 3 at the 1%, 2%, 5%, 10%, and 20% sample thresholds, respectively. These findings support the use of XP docking as the final prioritization stage for PfCDPK4 ligand ranking, while HTVS and SP serve primarily as computationally efficient filtering stages.

## Repository handling decision

- The `.txt` enrichment reports are compact and suitable for repository storage if needed.
- The ROC plots are compact figures and may be committed later under `results/docking_validation/enrichment/figures/`.
- The `.maegz` files should be treated as proprietary/large molecular project artifacts and should not be committed unless intentionally archived with Git LFS.

## Recommended next steps

1. Add numeric enrichment summary tables to downstream manuscript/thesis results.
2. Generate a unified publication-quality ROC figure comparing HTVS, SP, and XP in a single panel.
3. Report EF1%, EF5%, BEDROC(alpha=160.9), RIE, and ROC AUC as core validation metrics.
4. Use XP enrichment results to justify final hit selection for MD simulation and MM-GBSA/MM-PBSA.
