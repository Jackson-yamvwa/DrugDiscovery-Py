# PfCDPK4 4QOX DXR Reference Ligand MD Report — Replicate 44502

**Update timestamp:** 2026-05-22

## Source output

- Original report file: `4QOX-Cocrystalised-44502-out_pl_1.pdf`
- Software/report type: Schrödinger Simulation Interactions Diagram Report
- System/job name: `4QOX-Cocrystalised-44502`
- Entry title: Full System

## Simulation details

| Parameter | Value |
|---|---:|
| Job type | `mdsim` |
| Ensemble | NPT |
| Temperature | 300.0 K |
| Simulation time | 100.102 ns |
| Total atoms | 23,889 |
| Waters | 5,500 |
| Net system charge | 0 |
| Protein residues | 462 |
| Protein atoms | 7,307 |
| Protein heavy atoms | 3,629 |
| Protein charge | -12 |

## Ligand details

| Parameter | Value |
|---|---|
| Ligand PDB name | `DXR` |
| SMILES | `Nc1ncnc(c12)n(C(C)(C)C)nc2Cc3cc(Br)ccc3` |
| Molecular formula | C16H18BrN5 |
| Atomic mass | 360.264 au |
| Charge | 0 |
| Total atoms | 40 |
| Heavy atoms | 22 |
| Rotatable bonds | 4 |
| Number of fragments | 2 |

## Counter ions and salt

| Ion | Number | Concentration | Total charge |
|---|---:|---:|---:|
| Na+ | 27 | 89.256 mM | +27 |
| Cl- | 15 | 49.587 mM | -15 |

## Secondary structure summary

| SSE class | Percentage |
|---|---:|
| Helix | 37.37% |
| Strand | 8.89% |
| Total SSE | 46.27% |

## Main MD interpretation

The 44502 DXR reference replicate shows stable ligand accommodation within the PfCDPK4 ATP-binding pocket over the 100.102 ns trajectory. The protein RMSD rises during early equilibration and then fluctuates mostly between approximately 2.5 and 3.5 Å, with late-trajectory excursions approaching approximately 4 Å. The ligand RMSD relative to the protein remains below the protein RMSD for most of the trajectory, supporting retained binding-site accommodation rather than ligand dissociation.

The protein RMSF profile shows expected peaks in flexible loop/terminal regions, while ligand-contacting residues are marked around the binding-site region and remain comparatively stable. The secondary structure profile remains broadly preserved, with total SSE around 46.27%.

## Protein–ligand interaction summary

The report identifies the following reference interaction pattern:

| Residue | Interaction interpretation |
|---|---|
| Asp148 | Persistent H-bond anchoring interaction with ligand amine region |
| Tyr150 | Persistent H-bond/polar interaction with the heteroaromatic core |
| Val84 | Hydrophobic contact above the 30% reporting threshold in the 2D ligand-contact diagram |
| Lys99 | Intermittent water-mediated/hydrophobic contribution in the protein–ligand contact histogram |
| Leu76, Ala97, Met131, Leu200, Ile214, Asp215 | Additional intermittent hydrophobic or water-mediated/polar support |

The ligand–protein 2D contact diagram reports interactions above the 30% trajectory threshold for **Asp148 (~93%)**, **Tyr150 (~89%)**, and **Val84**. Compared with replicate 44501, the same core Asp148/Tyr150 reference anchors are preserved, although the 44502 contact diagram emphasizes Val84 rather than Lys99 as the additional >30% contact.

## Manuscript-ready interpretation

A second DXR reference simulation replicate, 4QOX-Cocrystalised-44502, was performed for 100.102 ns under NPT conditions at 300 K. The system contained 23,889 atoms and 5,500 water molecules, with the neutral DXR ligand represented by 22 heavy atoms and four rotatable bonds. The protein–ligand RMSD profile indicated stabilization after early conformational adjustment, while the ligand remained accommodated within the ATP-binding pocket throughout the trajectory. The interaction profile retained the dominant reference anchoring contacts with Asp148 and Tyr150, with occupancies of approximately 93% and 89%, respectively, and additional hydrophobic contribution from Val84. These findings support the reproducibility of the Asp148/Tyr150 interaction fingerprint across DXR reference simulations and provide further baseline evidence for comparison with candidate PfCDPK4 inhibitors.

## Comparison with DXR replicate 44501

| Feature | Replicate 44501 | Replicate 44502 | Interpretation |
|---|---|---|---|
| Temperature | 300 K | 300 K | Directly comparable |
| Simulation time | 100.102 ns | 100.102 ns | Directly comparable |
| Total atoms | 23,889 | 23,889 | Same system size |
| Waters | 5,500 | 5,500 | Same solvation size |
| Total SSE | 46.87% | 46.27% | Similar global secondary structure retention |
| Asp148 contact | ~98% in report | ~93% in report | Conserved primary anchor |
| Tyr150 contact | ~95% in report | ~89% in report | Conserved primary anchor |
| Additional >30% contact | Lys99 ~39% | Val84 >30% | Peripheral contact differs between runs |

## Interpretation cautions

- This report supports replicate-level reproducibility of the main Asp148/Tyr150 reference interaction pattern.
- Peripheral contact differences between 44501 and 44502 should be treated as expected dynamic variability rather than contradiction.
- Candidate superiority requires comparison against replicate-averaged reference behaviour, not a single DXR run.
- Quantitative comparison should use parsed `.dat` files when available.
