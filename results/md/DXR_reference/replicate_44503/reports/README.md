# PfCDPK4 4QOX DXR Reference Ligand MD Report — Replicate 44503

**Update timestamp:** 2026-05-22

## Source output

- Original report file: `4QOX-Cocrystalised-44503-out_pl_1.pdf`
- Software/report type: Schrödinger Simulation Interactions Diagram Report
- System/job name: `4QOX-Cocrystalised-44503`
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
| Helix | 38.21% |
| Strand | 9.04% |
| Total SSE | 47.25% |

## Main MD interpretation

The 44503 DXR reference replicate shows retained ligand accommodation within the PfCDPK4 ATP-binding pocket during the 100.102 ns trajectory. The protein RMSD rises rapidly during early equilibration, then shows a pronounced conformational adjustment around 38–45 ns, after which the protein fluctuates mostly around approximately 3.0–3.5 Å. The ligand RMSD relative to the protein increases compared with early frames but remains below the protein RMSD for most of the simulation, supporting retained binding-site accommodation rather than ligand dissociation.

The protein RMSF plot shows expected high-flexibility peaks in loop/terminal regions, with the main binding-site interaction profile preserved. The secondary-structure profile is broadly maintained, with total SSE of approximately 47.25%, the highest among the documented DXR reference report summaries so far.

## Protein–ligand interaction summary

The report identifies the following reference interaction pattern:

| Residue | Interaction interpretation |
|---|---|
| Asp148 | Persistent H-bond anchoring interaction with ligand amine region |
| Tyr150 | Persistent H-bond/polar interaction with the heteroaromatic core |
| Lys99 | π-cation/contact contribution near the bromophenyl/aromatic region |
| Val84 | Hydrophobic pocket support |
| Leu76, Ala97, Met131, Leu200, Ile214, Asp215 | Additional intermittent hydrophobic or water-mediated/polar support |

The ligand–protein 2D contact diagram reports interactions above the 30% trajectory threshold for **Asp148 (~98%)**, **Tyr150 (~93%)**, and **Lys99 (~39%)**. This is highly consistent with the 44501 reference interaction fingerprint and supports reproducibility of the Asp148/Tyr150 anchoring pattern across DXR reference simulations.

## Manuscript-ready interpretation

A third DXR reference simulation replicate, 4QOX-Cocrystalised-44503, was performed for 100.102 ns under NPT conditions at 300 K. The system contained 23,889 atoms and 5,500 water molecules, with the neutral DXR ligand represented by 22 heavy atoms and four rotatable bonds. The protein–ligand RMSD plot indicated early equilibration followed by a conformational adjustment around 38–45 ns, after which the system remained within a moderate RMSD range. The ligand remained accommodated in the ATP-binding pocket and retained the characteristic DXR interaction pattern. Contact analysis identified persistent Asp148 and Tyr150 interactions, with approximate occupancies of 98% and 93%, respectively, together with a Lys99 π-cation/contact contribution of approximately 39%. These findings reinforce the reproducibility of the Asp148/Tyr150 reference anchoring pattern and provide a third replicate baseline for evaluating candidate PfCDPK4 inhibitors.

## Comparison with previous DXR reference replicates

| Feature | Replicate 44501 | Replicate 44502 | Replicate 44503 | Interpretation |
|---|---|---|---|---|
| Temperature | 300 K | 300 K | 300 K | directly comparable |
| Simulation time | 100.102 ns | 100.102 ns | 100.102 ns | directly comparable |
| Total atoms | 23,889 | 23,889 | 23,889 | same system size |
| Waters | 5,500 | 5,500 | 5,500 | same solvation size |
| Total SSE | 46.87% | 46.27% | 47.25% | similar global fold retention |
| Asp148 contact | ~98% | ~93–99%, depending on source summary | ~98% | conserved primary anchor |
| Tyr150 contact | ~95% | ~89–94%, depending on source summary | ~93% | conserved primary anchor |
| Additional >30% contact | Lys99 ~39% | Val84 or Lys99 depending on summary source | Lys99 ~39% | peripheral contact variability, but Lys99 recurs |

## Interpretation cautions

- The 44503 RMSD plot shows a stronger mid-trajectory conformational adjustment than a perfectly flat trajectory; report it as stabilization after conformational adjustment, not as minimal protein deviation.
- The core Asp148/Tyr150 contacts are reproducible, but peripheral contacts vary across reference runs.
- Candidate superiority should be assessed against replicate-averaged DXR behaviour, not against one reference run only.
- Quantitative comparison should use parsed `.dat` files when available.
