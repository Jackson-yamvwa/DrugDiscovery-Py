# PfCDPK4 4QOX–CPD-1422 Desmond MD Interaction Report

**Update timestamp:** 2026-05-22

## Source output

- Original report file: `4QOX-CPD-1422-out_pl_1(1).pdf`
- Software/report type: Schrödinger Simulation Interactions Diagram Report
- System/job name: `4QOX-CPD-1422`
- Entry title: Full System

## Simulation details

| Parameter | Value |
|---|---:|
| Job type | `mdsim` |
| Ensemble | NPT |
| Temperature | 310.0 K |
| Simulation time | 100.102 ns |
| Total atoms | 23,912 |
| Waters | 5,505 |
| Net system charge | 0 |
| Protein residues | 462 |
| Protein atoms | 7,307 |
| Protein heavy atoms | 3,629 |
| Protein charge | -12 |

## Ligand details

| Parameter | Value |
|---|---|
| Ligand name in report | `UNK` |
| SMILES | `Nc1ncnc(c12)n(C(C)(C)CCC(N)=[NH2+])nc2-c(cc3)ccc3C` |
| Formula | C18H24N7 |
| Atomic mass | 338.439 au |
| Charge | +1 |
| Total atoms | 49 |
| Heavy atoms | 25 |
| Rotatable bonds | 7 |
| Number of fragments | 5 |

## Counter ions and salt

| Ion | Number | Concentration | Total charge |
|---|---:|---:|---:|
| Na+ | 26 | 85.872 mM | +26 |
| Cl- | 15 | 49.542 mM | -15 |

## Main MD interpretation

The 100 ns Desmond simulation supports a dynamically stable PfCDPK4–CPD-1422 complex. The protein–ligand RMSD profile indicates early equilibration followed by moderate fluctuation, with no evidence from the report that the ligand diffused away from the ATP-binding pocket.

The protein RMSF profile shows expected local flexibility in loop/terminal regions, while the binding site is supported by persistent ligand contacts. The secondary structure analysis reports approximately 37.50% helix, 9.35% strand, and 46.86% total secondary structure elements.

## Protein–ligand interaction summary

The contact analysis identifies a persistent interaction network involving the following key residues:

| Residue | Interaction interpretation |
|---|---|
| Asp148 | Major polar/H-bond anchoring contact |
| Tyr150 | Persistent polar/H-bond interaction near the ligand core |
| Glu154 | Distal polar interaction with the ligand terminal group |
| Glu197 | Additional polar/electrostatic or water-mediated contact |
| Val84, Ala97, Leu145, Ile214 | Hydrophobic pocket support |

The ligand–protein contact diagram reports interactions occurring for more than 30% of the trajectory, supporting that the Asp148/Tyr150/Glu154/Glu197 contact pattern is not merely a static docking artifact.

## Manuscript-ready interpretation

Molecular dynamics simulation of the PfCDPK4–CPD-1422 complex demonstrated stable ligand accommodation within the ATP-binding pocket over a 100 ns trajectory. The simulation was conducted under NPT conditions at 310 K and included 23,912 atoms and 5,505 water molecules. Protein–ligand interaction analysis showed persistent contacts with key binding-site residues, particularly Asp148, Tyr150, Glu154, and Glu197, while additional hydrophobic interactions with residues such as Val84, Ala97, Leu145, and Ile214 contributed to pocket stabilization. These findings support the structural plausibility of CPD-1422 as a PfCDPK4-binding candidate and justify further post-MD binding-energy analysis.

## Interpretation cautions

- This result supports predicted dynamic stability, not experimental potency.
- A single 100 ns MD trajectory should not be overinterpreted as definitive evidence of binding superiority.
- Stronger claims require replicate MD simulations, contact occupancy comparison across replicas, MM-GBSA/MM-PBSA, and preferably biochemical PfCDPK4 inhibition data.
- Large trajectory files should not be committed unless Git LFS or external archival storage is configured.

## Recommended next analysis steps

1. Parse RMSD, RMSF, ligand properties, torsions, and contact `.dat` files into reproducible summary tables.
2. Generate publication-quality plots for protein RMSD, ligand RMSD, protein RMSF, ligand RMSF, and contact occupancy.
3. Run the same MD-summary workflow for CPD-2175, CPD-2176, DXR-602, and primaquine.
4. Compare compounds using a combined matrix of docking score, pose conservation, MD stability, contact persistence, and MM-GBSA/MM-PBSA.
