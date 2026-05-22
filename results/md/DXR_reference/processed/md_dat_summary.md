# DXR Reference Ligand Desmond `.dat` Analysis Summary

**System:** PfCDPK4 4QOX–DXR co-crystallized/reference ligand  
**Input files:** Desmond Simulation Interactions Diagram `.dat` exports  
**Frames parsed:** 1001 usable trajectory frames  
**Assumed simulation time:** 100 ns  
**Approximate frame spacing:** 0.1 ns per frame

## Files parsed

```text
L_Torsions(4).dat
L-Properties(4).dat
P_RMSF(4).dat
PL_RMSD(4).dat
PL-Contacts_HBond(4).dat
PL-Contacts_Hydrophobic(4).dat
```

Only direct hydrogen-bond and hydrophobic contact files were included in this upload. Pi-cation, pi-pi, ionic, metal, and water-bridge `.dat` files were not included in this batch; therefore, this processed table is more conservative than the PDF interaction diagram.

## RMSD summary

### Overall trajectory

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| Protein Cα RMSD | 2.720 Å | 0.393 | 0.000 | 3.989 | 2.708 |
| Protein backbone RMSD | 2.746 Å | 0.392 | 0.000 | 4.024 | 2.733 |
| Protein side-chain RMSD | 3.467 Å | 0.397 | 0.000 | 4.598 | 3.451 |
| Protein all-heavy RMSD | 3.013 Å | 0.392 | 0.000 | 4.239 | 2.992 |
| Ligand RMSD relative to protein | 1.142 Å | 0.327 | 0.000 | 2.411 | 1.107 |
| Ligand RMSD relative to ligand | 0.338 Å | 0.101 | 0.000 | 0.844 | 0.327 |

### Equilibrated/second-half window: frames 500–1000

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| Protein Cα RMSD | 2.976 Å | 0.294 | 2.356 | 3.989 | 2.944 |
| Protein backbone RMSD | 2.999 Å | 0.294 | 2.356 | 4.024 | 2.970 |
| Protein side-chain RMSD | 3.748 Å | 0.265 | 3.197 | 4.598 | 3.717 |
| Protein all-heavy RMSD | 3.282 Å | 0.282 | 2.726 | 4.239 | 3.250 |
| Ligand RMSD relative to protein | 1.127 Å | 0.283 | 0.459 | 2.319 | 1.098 |
| Ligand RMSD relative to ligand | 0.345 Å | 0.098 | 0.123 | 0.676 | 0.334 |

## Ligand property summary: frames 500–1000

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| Ligand RMSD | 0.345 Å | 0.098 | 0.123 | 0.676 | 0.334 |
| Radius of gyration | 4.142 Å | 0.039 | 3.982 | 4.260 | 4.142 |
| Intramolecular H-bonds | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Molecular surface area | 298.164 Å² | 1.719 | 293.131 | 304.691 | 298.150 |
| SASA | 54.486 Å² | 10.986 | 28.501 | 95.194 | 53.685 |
| PSA | 77.284 Å² | 2.306 | 70.672 | 83.253 | 77.169 |

## Binding-site RMSF summary

Representative binding-site Cα RMSF values:

| Residue | Cα RMSF Å | Interpretation |
|---|---:|---|
| Leu76 | 0.992 | stable hydrophobic contact region |
| Lys78 | 1.048 | stable backbone; flexible side chain expected |
| Ser80 | 1.003 | stable local polar residue |
| Val84 | 0.770 | stable hydrophobic pocket residue |
| Ala97 | 0.718 | stable hydrophobic pocket residue |
| Lys99 | 0.735 | stable basic/aromatic-contact region |
| Met131 | 0.695 | stable hydrophobic pocket residue |
| Asp148 | 0.967 | stable acidic anchoring residue |
| Tyr150 | 0.913 | stable aromatic/polar anchoring residue |
| Gly152 | 0.912 | stable local loop region |
| Glu154 | 0.785 | stable acidic pocket residue |
| Glu197 | 0.785 | stable acidic pocket residue |
| Leu200 | 0.666 | stable hydrophobic residue |
| Ile214 | 0.583 | highly stable hydrophobic pocket residue |
| Asp215 | 0.817 | stable acidic region |

## Direct contact occupancy

Occupancy was calculated as:

```text
number of unique frames with a residue-level contact / total trajectory frames × 100
```

Top direct contacts from the uploaded `.dat` files:

| Residue | ResName | Occupancy % | Interaction type |
|---:|---|---:|---|
| 148 | ASP | 93.51 | H-bond |
| 150 | TYR | 89.41 | H-bond |
| 84 | VAL | 38.86 | hydrophobic |
| 214 | ILE | 20.38 | hydrophobic |
| 97 | ALA | 19.48 | hydrophobic |
| 200 | LEU | 17.88 | hydrophobic |
| 76 | LEU | 15.18 | hydrophobic |
| 131 | MET | 4.70 | hydrophobic |

## Interpretation

The DXR reference simulation shows a stable binding profile. During the second half of the trajectory, protein Cα RMSD averaged approximately **2.98 Å**, while ligand RMSD relative to protein averaged approximately **1.13 Å**. The ligand self-RMSD averaged approximately **0.35 Å**, indicating a very stable ligand conformation.

The strongest direct contacts are the conserved H-bonds with **Asp148** and **Tyr150**, with occupancies of approximately **93.5%** and **89.4%**, respectively. Hydrophobic stabilization is provided mainly by **Val84**, **Ile214**, **Ala97**, **Leu200**, **Leu76**, and **Met131**.

## Manuscript-ready interpretation

Analysis of the DXR reference ligand `.dat` files showed stable accommodation of the native ligand within the PfCDPK4 ATP-binding site over the 100 ns simulation. In the equilibrated phase, the protein Cα RMSD averaged approximately 2.98 Å, while ligand RMSD relative to the protein averaged approximately 1.13 Å. The ligand retained a stable internal conformation, with self-RMSD of approximately 0.35 Å. Direct contact analysis confirmed persistent hydrogen bonding with Asp148 and Tyr150, together with hydrophobic support from Val84, Ile214, Ala97, Leu200, Leu76, and Met131. This profile provides a conservative dynamic reference for comparing candidate compounds such as CPD-1422, CPD-2175, and CPD-2176.

## Cautions

- This processed summary is based only on the `.dat` contact files uploaded in this batch: H-bond and hydrophobic contacts.
- The associated PDF report indicates additional interaction classes, including Lys99 π-cation contact, but the corresponding `.dat` files were not included here.
- Candidate superiority should not be inferred from one metric alone; use RMSD, ligand stability, contact occupancy, XP enrichment, MM-GBSA/MM-PBSA, and replicate MD evidence.
