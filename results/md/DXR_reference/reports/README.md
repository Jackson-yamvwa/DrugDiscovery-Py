# PfCDPK4 4QOX DXR Co-crystallized Ligand Desmond Interaction Report

**Update timestamp:** 2026-05-22

## Source output

- Original report file: `4QOX-Cocrystalised-44501-out_pl_1.pdf`
- Software/report type: Schrödinger Simulation Interactions Diagram Report
- System/job name: `4QOX-Cocrystalised-44501`
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
| Helix | 38.54% |
| Strand | 8.33% |
| Total SSE | 46.87% |

## Main MD interpretation

The DXR co-crystallized/reference ligand simulation shows a stable ligand-binding profile over the 100 ns trajectory. The protein RMSD increases during early equilibration and then fluctuates mostly around approximately 2.5–3.5 Å, with transient excursions near 4 Å. The ligand RMSD relative to protein remains below the protein RMSD for most of the trajectory and does not indicate ligand dissociation.

The protein RMSF profile shows expected flexible loop/terminal regions, while the ligand-binding region maintains persistent interactions. The ligand RMSF plot indicates moderate atom-level flexibility, with the central scaffold comparatively stable and higher fluctuations around selected substituent atoms.

## Protein–ligand interaction summary

The report identifies a compact reference contact network involving:

| Residue | Interaction interpretation |
|---|---|
| Asp148 | Persistent H-bond interaction with ligand amine region |
| Tyr150 | Persistent H-bond/polar interaction with the heteroaromatic core |
| Lys99 | π-cation interaction with the bromophenyl/aromatic region |
| Val84, Ala97, Leu76, Met131, Leu200, Ile214 | Hydrophobic pocket support |
| Asp215 | Intermittent water-bridge/polar support |

The ligand–protein contact diagram reports interactions above the 30% trajectory threshold for **Asp148 (~98%)**, **Tyr150 (~95%)**, and **Lys99 (~39%)**. This establishes a useful native/reference interaction fingerprint for comparing CPD-1422, CPD-2175, and CPD-2176.

## Manuscript-ready interpretation

Molecular dynamics simulation of the PfCDPK4–DXR co-crystallized reference complex was performed for 100.102 ns under NPT conditions at 300 K. The system contained 23,889 atoms and 5,500 water molecules, with the neutral DXR ligand represented by 22 heavy atoms and four rotatable bonds. The protein–ligand RMSD profile indicated stabilization after early conformational adjustment, while the ligand remained accommodated within the ATP-binding pocket throughout the trajectory. Contact analysis showed persistent interactions with Asp148 and Tyr150, with occupancies of approximately 98% and 95%, respectively, together with a Lys99 π-cation interaction of approximately 39%. Additional hydrophobic support involved Val84, Ala97, Leu76, Met131, Leu200, and Ile214. These results define the dynamic reference interaction fingerprint for the native 4QOX ligand-binding mode and provide a baseline for evaluating candidate PfCDPK4 inhibitors.

## Comparison relevance

This DXR reference trajectory should be used to evaluate candidate compounds against the experimentally observed ligand-binding mode. In particular, candidate ligands should be assessed for:

1. retention of Asp148 and Tyr150 anchoring contacts,
2. ligand RMSD relative to the protein pocket,
3. ligand self-RMSD and scaffold stability,
4. hydrophobic pocket occupancy near Val84/Ala97/Leu76/Ile214,
5. water-mediated and π-interaction profiles,
6. comparative MM-GBSA/MM-PBSA values.

## Interpretation cautions

- This report was generated at 300 K, whereas some candidate simulations were documented at 310 K. Temperature differences should be noted when making strict quantitative comparisons.
- The report supports stable reference-ligand accommodation, not direct proof of candidate potency.
- Final candidate prioritization should integrate docking enrichment, XP score, pose conservation, MD stability, contact occupancy, binding free-energy estimates, and experimental validation where available.
