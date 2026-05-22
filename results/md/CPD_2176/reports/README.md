# PfCDPK4 4QOX–CPD-2176 Desmond MD Interaction Report

**Update timestamp:** 2026-05-22

## Source output

- Original report file: `4QOX-CPD-2176-out_pl_1.pdf`
- Software/report type: Schrödinger Simulation Interactions Diagram Report
- System/job name: `4QOX-CPD-2176`
- Entry title: Full System

## Simulation details

| Parameter | Value |
|---|---:|
| Job type | `mdsim` |
| Ensemble | NPT |
| Temperature | 310.0 K |
| Simulation time | 100.102 ns |
| Total atoms | 23,914 |
| Waters | 5,506 |
| Net system charge | 0 |
| Protein residues | 462 |
| Protein atoms | 7,307 |
| Protein heavy atoms | 3,629 |
| Protein charge | -12 |

## Ligand details

| Parameter | Value |
|---|---|
| Ligand name in report | `UNK` |
| SMILES | `Nc1ncnc(c12)n(C(C)(C)CNC(N)=[NH2+])nc2-c(cc3)ccc3C` |
| Formula | C17H23N8 |
| Atomic mass | 339.426 au |
| Charge | +1 |
| Total atoms | 48 |
| Heavy atoms | 25 |
| Rotatable bonds | 7 |
| Number of fragments | 7 |

## Counter ions and salt

| Ion | Number | Concentration | Total charge |
|---|---:|---:|---:|
| Na+ | 26 | 85.857 mM | +26 |
| Cl- | 15 | 49.533 mM | -15 |

## Secondary structure summary

| SSE class | Percentage |
|---|---:|
| Helix | 36.49% |
| Strand | 8.87% |
| Total SSE | 45.36% |

## Main MD interpretation

The 100 ns Desmond Simulation Interactions Diagram report indicates that CPD-2176 remains associated with the PfCDPK4 ATP-binding pocket, but the RMSD behaviour is more conservative than an ideal minimal-deviation trajectory. The protein RMSD increases progressively during the simulation and approaches approximately 5–6 Å toward the late trajectory window. This should be described as conformational adjustment followed by partial stabilization, rather than as a low-RMSD trajectory.

The ligand RMSD relative to the protein remains lower than the protein RMSD but shows moderate fluctuation. The ligand does not appear to completely dissociate from the binding site in the report, but it undergoes positional adaptation inside the pocket.

## Protein–ligand interaction summary

The report identifies a persistent contact network involving the following residues:

| Residue | Interaction interpretation |
|---|---|
| Asp148 | Major charged/polar anchoring residue near the ligand core |
| Tyr150 | Persistent ligand-core interaction; also indicated as pi-related contact in the ligand diagram |
| Glu154 | Distal polar/charged interaction near the ligand terminal group |
| Lys78 | Water-mediated/polar support near the charged terminal region |
| Gly152 | Water-mediated contact close to the ligand polar extension |
| Val84, Ala97, Leu133, Leu145, Leu200, Ile214 | Hydrophobic pocket support |

The ligand–protein contact diagram shows interactions above the 30% trajectory threshold, including strong contacts with Asp148 and Tyr150 and a distal polar network involving Glu154 and Lys78/water-mediated contacts.

## Manuscript-ready interpretation

Molecular dynamics simulation of the PfCDPK4–CPD-2176 complex was performed for 100.102 ns under NPT conditions at 310 K. The system contained 23,914 atoms and 5,506 water molecules, with CPD-2176 represented as a positively charged ligand with 25 heavy atoms and seven rotatable bonds. The trajectory showed that CPD-2176 remained accommodated within the PfCDPK4 ATP-binding pocket, although the protein RMSD increased during the simulation, indicating conformational adjustment of the protein–ligand complex. Protein–ligand interaction analysis showed recurring contacts with Asp148, Tyr150, Glu154, Lys78, and Gly152, supported by hydrophobic interactions involving residues such as Val84, Ala97, Leu133, Leu145, Leu200, and Ile214. These findings support the structural plausibility of CPD-2176 as a PfCDPK4-binding candidate, but the higher protein RMSD profile suggests that its dynamic stability should be interpreted cautiously and compared against CPD-1422, CPD-2175, and DXR-602 using parsed `.dat` metrics and replicate MD simulations.

## Interpretation cautions

- CPD-2176 should not be described as unequivocally more stable than CPD-1422 based only on this PDF report.
- The protein RMSD profile appears higher and more progressive than the CPD-1422 summary; quantitative `.dat` parsing is required for a fair comparison.
- The report supports predicted binding-site retention, not experimental potency.
- Stronger prioritization requires parsed RMSD/RMSF/contact `.dat` files, replicate MD, MM-GBSA/MM-PBSA, and biochemical validation.

## Recommended next analysis steps

1. Add the CPD-2176 `.dat` files under `results/md/CPD_2176/raw_dat/`.
2. Run `scripts/analyze_desmond_dat.py` using the same workflow used for CPD-1422.
3. Generate comparative tables for CPD-1422, CPD-2175, CPD-2176, DXR-602, and primaquine.
4. Rank compounds using combined evidence: docking score, pose conservation, RMSD stability, contact persistence, ligand compactness, and MM-GBSA/MM-PBSA.
