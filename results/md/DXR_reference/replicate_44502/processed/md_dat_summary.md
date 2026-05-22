# DXR Reference Replicate 44502 Desmond `.dat` Analysis Summary

**System:** PfCDPK4 4QOX–DXR reference ligand, replicate 44502  
**Input files:** Desmond Simulation Interactions Diagram `.dat` exports  
**Frames parsed:** 1001 usable trajectory frames  
**Assumed simulation time:** 100 ns  
**Approximate frame spacing:** 0.1 ns per frame

## Files parsed

```text
L_RMSF(3).dat
L_Torsions(5).dat
L-Properties(5).dat
P_RMSF(5).dat
PL-Contacts_HBond(5).dat
PL-Contacts_Hydrophobic(5).dat
PL-Contacts_WaterBridge(4).dat
```

No RMSD `.dat` file was included in this upload batch, so this summary focuses on ligand properties, ligand RMSF, protein RMSF, and contact occupancy. Direct RMSD interpretation for replicate 44502 should use the associated report PDF and any RMSD `.dat` file if provided later.

## Ligand property summary

### Overall trajectory

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| Ligand RMSD | 0.314 Å | 0.109 | 0.000 | 1.110 | 0.299 |
| Radius of gyration | 4.151 Å | 0.039 | 3.994 | 4.253 | 4.152 |
| Intramolecular H-bonds | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Molecular surface area | 297.742 Å² | 1.765 | 290.983 | 303.805 | 297.710 |
| SASA | 56.041 Å² | 15.146 | 15.985 | 114.310 | 55.364 |
| PSA | 76.246 Å² | 2.641 | 67.457 | 83.238 | 76.395 |

### Equilibrated/second-half window: frames 500–1000

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| Ligand RMSD | 0.307 Å | 0.100 | 0.100 | 0.673 | 0.295 |
| Radius of gyration | 4.151 Å | 0.037 | 4.048 | 4.253 | 4.152 |
| Intramolecular H-bonds | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Molecular surface area | 297.518 Å² | 1.686 | 292.264 | 302.630 | 297.496 |
| SASA | 62.581 Å² | 13.858 | 34.334 | 114.310 | 61.372 |
| PSA | 75.869 Å² | 2.703 | 67.457 | 82.870 | 76.060 |

## Ligand RMSF summary

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| wrt protein | 1.173 Å | 0.320 | 0.870 | 1.900 | 1.094 |
| wrt ligand | 0.418 Å | 0.438 | 0.110 | 1.493 | 0.260 |

Most mobile ligand atoms relative to the ligand frame:

| Atom | wrt protein Å | wrt ligand Å |
|---:|---:|---:|
| 13 | 1.880 | 1.493 |
| 12 | 1.867 | 1.478 |
| 14 | 1.900 | 1.413 |
| 22 | 1.251 | 0.620 |
| 7 | 1.109 | 0.345 |

The highest ligand mobility is localized around atoms 12–14, consistent with the tert-butyl/peripheral substituent region observed in the figure outputs.

## Binding-site RMSF summary

Representative binding-site Cα RMSF values:

| Residue | Cα RMSF Å | Interpretation |
|---|---:|---|
| Leu76 | 1.333 | stable-to-moderately flexible hydrophobic contact region |
| Ser80 | 1.195 | stable local polar residue |
| Val84 | 1.073 | stable hydrophobic pocket residue |
| Ala97 | 1.004 | stable hydrophobic pocket residue |
| Lys99 | 0.973 | stable basic/aromatic-contact region |
| Met131 | 0.763 | stable hydrophobic pocket residue |
| Asp148 | 1.082 | stable acidic anchoring residue |
| Val149 | 1.259 | moderately flexible adjacent hydrophobic residue |
| Tyr150 | 1.366 | stable-to-moderately flexible aromatic/polar anchoring residue; side chain more mobile |
| Gly152 | 1.438 | moderately flexible local loop/water-bridge region |
| Asn198 | 0.676 | stable polar residue |
| Leu200 | 0.719 | stable hydrophobic residue |
| Ile214 | 0.566 | highly stable hydrophobic pocket residue |
| Asp215 | 0.709 | stable acidic region |

## Protein–ligand contact occupancy

Occupancy was calculated as:

```text
number of unique frames with a residue-level contact / total trajectory frames × 100
```

Top contacts from the uploaded `.dat` files:

| Residue | ResName | Occupancy % | Interaction type |
|---:|---|---:|---|
| 148 | ASP | 98.70 | H-bond |
| 150 | TYR | 93.81 | H-bond |
| 84 | VAL | 28.17 | hydrophobic |
| 97 | ALA | 17.08 | hydrophobic |
| 214 | ILE | 15.18 | hydrophobic |
| 76 | LEU | 11.09 | hydrophobic |
| 99 | LYS | 9.39 | water bridge |
| 215 | ASP | 9.09 | water bridge |
| 200 | LEU | 7.69 | hydrophobic |
| 131 | MET | 6.99 | hydrophobic |
| 150 | TYR | 4.00 | water bridge |

## Interpretation

The replicate 44502 `.dat` outputs reinforce the core DXR reference interaction fingerprint. Direct hydrogen bonds with **Asp148** and **Tyr150** persist across most of the 100 ns trajectory, with occupancies of approximately **98.7%** and **93.8%**, respectively. Hydrophobic contacts are more intermittent, led by **Val84**, **Ala97**, **Ile214**, **Leu76**, **Leu200**, and **Met131**. Water-mediated interactions involving **Lys99**, **Asp215**, and **Tyr150** are present but less persistent than the direct H-bond anchors.

The ligand remains compact and internally stable, with second-half ligand RMSD of approximately **0.31 Å**, radius of gyration around **4.15 Å**, and no intramolecular hydrogen bonds. SASA increases moderately in the second half, indicating some fluctuation in solvent exposure while the ligand remains anchored by Asp148/Tyr150.

## Manuscript-ready interpretation

Analysis of the DXR reference replicate 44502 `.dat` files confirmed stable ligand behaviour and reproducible binding-site interactions during the 100 ns simulation. The ligand maintained a compact conformation, with second-half ligand RMSD averaging approximately 0.31 Å and radius of gyration averaging approximately 4.15 Å. Direct contact analysis showed highly persistent hydrogen bonding with Asp148 and Tyr150, with occupancies of approximately 98.7% and 93.8%, respectively. Hydrophobic stabilization was provided intermittently by Val84, Ala97, Ile214, Leu76, Leu200, and Met131, while Lys99 and Asp215 contributed lower-occupancy water-mediated interactions. These findings strengthen the use of Asp148/Tyr150 persistence as the core dynamic reference criterion for candidate PfCDPK4 inhibitor evaluation.

## Comparison note

The `.dat` contact occupancies are broadly consistent with the 44502 report interpretation but are not identical to the visual percentages in every figure/report panel because some report panels may aggregate or threshold interaction classes differently. For reproducible quantitative comparison, use the `.dat`-derived values in this folder.

## Cautions

- No PL_RMSD `.dat` file was included in this upload batch; add it later if available for complete replicate-level RMSD quantification.
- This is still one replicate; final conclusions should use replicate-averaged metrics across DXR reference runs.
- Candidate prioritization should integrate RMSD, RMSF, contact occupancy, docking enrichment, MM-GBSA/MM-PBSA, and experimental data where available.
