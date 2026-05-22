# 4QOX Co-crystallized/Reference Ligand Desmond `.dat` Analysis Summary

**System:** PfCDPK4 4QOX co-crystallized/reference ligand  
**Input files:** Desmond Simulation Interactions Diagram `.dat` exports  
**Frames parsed:** 1001 usable trajectory frames  
**Assumed simulation time:** 100 ns  
**Approximate frame spacing:** 0.1 ns per frame

## Files parsed

```text
L_Torsions(3).dat
L-Properties(3).dat
P_RMSF(3).dat
PL_RMSD(3).dat
PL-Contacts_HBond(3).dat
PL-Contacts_Hydrophobic(3).dat
PL-Contacts_Pi-Cation(3).dat
PL-Contacts_Pi-Pi(3).dat
PL-Contacts_WaterBridge(3).dat
```

No ionic or metal-contact `.dat` files were included in this upload.

## RMSD summary

### Overall trajectory

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| Protein Cα RMSD | 2.852 Å | 0.442 | 0.000 | 3.900 | 2.894 |
| Protein backbone RMSD | 2.862 Å | 0.441 | 0.000 | 3.916 | 2.904 |
| Protein side-chain RMSD | 3.635 Å | 0.377 | 0.000 | 4.439 | 3.692 |
| Protein all-heavy RMSD | 3.153 Å | 0.400 | 0.000 | 4.081 | 3.199 |
| Ligand RMSD relative to protein | 1.592 Å | 0.350 | 0.000 | 2.983 | 1.593 |
| Ligand RMSD relative to ligand | 0.464 Å | 0.110 | 0.000 | 1.052 | 0.459 |

### Equilibrated/second-half window: frames 500–1000

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| Protein Cα RMSD | 3.160 Å | 0.267 | 2.599 | 3.900 | 3.114 |
| Protein backbone RMSD | 3.170 Å | 0.270 | 2.614 | 3.916 | 3.120 |
| Protein side-chain RMSD | 3.896 Å | 0.188 | 3.446 | 4.439 | 3.862 |
| Protein all-heavy RMSD | 3.431 Å | 0.230 | 2.929 | 4.081 | 3.387 |
| Ligand RMSD relative to protein | 1.740 Å | 0.305 | 0.965 | 2.983 | 1.722 |
| Ligand RMSD relative to ligand | 0.450 Å | 0.094 | 0.209 | 0.741 | 0.453 |

## Ligand property summary: frames 500–1000

| metric | mean | sd | min | max | median |
|---|---:|---:|---:|---:|---:|
| Ligand RMSD | 0.450 Å | 0.094 | 0.209 | 0.741 | 0.453 |
| Radius of gyration | 4.148 Å | 0.039 | 4.012 | 4.249 | 4.147 |
| Intramolecular H-bonds | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Molecular surface area | 297.646 Å² | 1.727 | 293.219 | 303.337 | 297.587 |
| SASA | 84.027 Å² | 17.941 | 38.160 | 128.973 | 86.621 |
| PSA | 76.082 Å² | 2.539 | 65.528 | 83.583 | 76.233 |

## Binding-site RMSF summary

The reference-ligand binding pocket shows generally stable Cα fluctuations. Representative Cα RMSF values include:

| Residue | Cα RMSF Å | Interpretation |
|---|---:|---|
| Leu76 | 1.015 | stable pocket residue |
| Lys78 | 1.238 | moderately flexible basic side-chain region |
| Val84 | 0.858 | stable hydrophobic pocket residue |
| Ala97 | 0.816 | stable hydrophobic pocket residue |
| Lys99 | 0.807 | stable backbone with possible cation/π contribution |
| Met131 | 1.024 | moderate local flexibility |
| Leu133 | 0.889 | stable hydrophobic contact region |
| Asp148 | 1.071 | stable acidic anchoring residue |
| Tyr150 | 1.172 | stable aromatic/polar anchoring residue |
| Gly152 | 1.344 | moderately flexible local loop/water-bridge region |
| Glu154 | 1.017 | stable acidic pocket residue |
| Glu197 | 1.004 | stable acidic/polar pocket residue |
| Ile214 | 0.739 | highly stable hydrophobic pocket residue |
| Asp215 | 0.869 | stable acidic residue |

## Protein–ligand contact occupancy

Occupancy was calculated as:

```text
number of unique frames with a residue-level contact / total trajectory frames × 100
```

Top contacts:

| Residue | ResName | Occupancy % | Interaction type |
|---:|---|---:|---|
| 148 | ASP | 98.00 | H-bond |
| 150 | TYR | 95.60 | H-bond |
| 99 | LYS | 39.46 | π-cation |
| 84 | VAL | 30.77 | hydrophobic |
| 97 | ALA | 20.88 | hydrophobic |
| 76 | LEU | 15.78 | hydrophobic |
| 99 | LYS | 15.28 | water bridge |
| 150 | TYR | 10.99 | π–π |
| 215 | ASP | 10.59 | water bridge |
| 131 | MET | 9.79 | hydrophobic |
| 214 | ILE | 8.59 | hydrophobic |

## Interpretation

The co-crystallized/reference ligand simulation shows a stable reference binding mode. The second-half protein Cα RMSD averages approximately **3.16 Å** with a standard deviation of **0.27 Å**, indicating stabilization after early equilibration. The ligand remains internally stable, with ligand RMSD relative to itself averaging approximately **0.45 Å** in the second half. The ligand RMSD relative to protein averages approximately **1.74 Å**, consistent with retained binding-pocket accommodation rather than dissociation.

The dominant reference contacts are direct H-bonds with **Asp148** and **Tyr150**, with occupancies of approximately **98.0%** and **95.6%**, respectively. Additional stabilization is provided by **Lys99 π-cation contact**, **Val84/Ala97/Leu76 hydrophobic support**, and intermittent **Tyr150 π–π** and **Lys99/Asp215 water-mediated** interactions.

## Manuscript-ready interpretation

The co-crystallized/reference ligand simulation demonstrated stable accommodation of the ligand within the PfCDPK4 ATP-binding pocket over the 100 ns trajectory. During the equilibrated phase, the protein Cα RMSD averaged approximately 3.16 Å, while the ligand maintained a stable internal conformation with a self-RMSD of approximately 0.45 Å. Contact analysis showed highly persistent hydrogen bonding with Asp148 and Tyr150, with occupancies of approximately 98.0% and 95.6%, respectively. Additional stabilization was contributed by hydrophobic contacts involving Val84, Ala97, Leu76, Met131, and Ile214, together with a Lys99 π-cation interaction and intermittent water-mediated contacts. These findings establish a dynamic reference profile for comparing CPD-1422, CPD-2175, and CPD-2176 against the native 4QOX binding mode.

## Comparative use

This reference trajectory should be used as the baseline for candidate assessment. Candidate compounds should be judged against this profile using:

1. protein Cα RMSD stability,
2. ligand RMSD relative to protein,
3. ligand self-RMSD,
4. persistence of Asp148/Tyr150 interactions,
5. hydrophobic pocket occupancy,
6. water-bridge and π-interaction profiles,
7. MM-GBSA/MM-PBSA binding-energy estimates.

## Cautions

- These metrics represent one trajectory only.
- The co-crystallized system should be treated as a reference benchmark, not as proof that any candidate is more potent.
- Candidate superiority requires replicate MD, binding free-energy estimates, and experimental inhibition data.
