# CPD-1422 Desmond `.dat` Analysis Summary

**System:** PfCDPK4 4QOX–CPD-1422  
**Input files:** Desmond Simulation Interactions Diagram `.dat` exports  
**Frames parsed:** 1001  
**Assumed simulation time:** 100.102 ns  
**Approximate frame spacing:** 0.1 ns per frame, based on 1001 frames over ~100 ns.

## Files parsed

```text
L_RMSF(1).dat
L_Torsions(1).dat
L-Properties(1).dat
P_RMSF(1).dat
PL_RMSD(1).dat
PL-Contacts_HBond(1).dat
PL-Contacts_Hydrophobic(1).dat
PL-Contacts_Ionic(1).dat
PL-Contacts_Metal(1).dat
PL-Contacts_Pi-Cation(1).dat
PL-Contacts_Pi-Pi(1).dat
PL-Contacts_WaterBridge(1).dat
```

## RMSD summary

### Overall trajectory

| metric          |   mean |    sd |   min |   max |   median |
|:----------------|-------:|------:|------:|------:|---------:|
| Prot_CA         |  4.033 | 1.158 | 0.000 | 5.971 |    4.552 |
| Prot_Backbone   |  4.041 | 1.150 | 0.000 | 5.986 |    4.553 |
| Prot_Sidechain  |  4.723 | 1.040 | 0.000 | 6.458 |    5.209 |
| Prot_All_Heavy  |  4.337 | 1.112 | 0.000 | 6.213 |    4.844 |
| Lig_wrt_Protein |  3.043 | 0.924 | 0.000 | 5.502 |    3.190 |
| Lig_wrt_Ligand  |  0.443 | 0.173 | 0.000 | 1.461 |    0.392 |

### Equilibrated/second-half window: frames 500–1000

| metric          |   mean |    sd |   min |   max |   median |
|:----------------|-------:|------:|------:|------:|---------:|
| Prot_CA         |  4.961 | 0.295 | 3.999 | 5.971 |    4.957 |
| Prot_Backbone   |  4.964 | 0.297 | 3.993 | 5.986 |    4.965 |
| Prot_Sidechain  |  5.563 | 0.260 | 4.762 | 6.458 |    5.554 |
| Prot_All_Heavy  |  5.233 | 0.283 | 4.307 | 6.213 |    5.228 |
| Lig_wrt_Protein |  3.729 | 0.541 | 2.534 | 5.502 |    3.660 |
| Lig_wrt_Ligand  |  0.489 | 0.184 | 0.201 | 1.461 |    0.447 |

## Ligand property summary: frames 500–1000

| metric   |    mean |     sd |     min |     max |   median |
|:---------|--------:|-------:|--------:|--------:|---------:|
| RMSD     |   0.489 |  0.184 |   0.201 |   1.461 |    0.447 |
| rGyr     |   4.099 |  0.045 |   3.952 |   4.198 |    4.103 |
| intraHB  |   0.000 |  0.000 |   0.000 |   0.000 |    0.000 |
| MolSA    | 329.794 |  2.447 | 322.499 | 334.725 |  330.016 |
| SASA     |  95.734 | 14.693 |  60.313 | 153.206 |   93.533 |
| PSA      | 201.703 |  2.909 | 187.655 | 208.462 |  201.995 |

## Ligand RMSF summary

| metric      |   mean |    sd |   min |   max |   median |
|:------------|-------:|------:|------:|------:|---------:|
| wrt_Protein |  1.355 | 0.229 | 1.153 | 2.021 |    1.255 |
| wrt_Ligand  |  0.355 | 0.211 | 0.139 | 1.024 |    0.300 |

Most mobile ligand atoms relative to ligand frame:

|   Atom |   wrt_Protein |   wrt_Ligand |
|-------:|--------------:|-------------:|
|     25 |         2.021 |        1.024 |
|     16 |         1.486 |        0.754 |
|     17 |         1.503 |        0.746 |
|     24 |         1.873 |        0.483 |
|     22 |         1.739 |        0.446 |

## Protein–ligand contact occupancy

Occupancy was calculated as:

```text
number of unique frames with a residue-level contact / total trajectory frames × 100
```

Top residue-level contacts across interaction classes:

|   Residue | ResName   |   contact_events |   frames_present |   occupancy_pct | interaction_type   |
|----------:|:----------|-----------------:|-----------------:|----------------:|:-------------------|
|       148 | ASP       |              993 |              993 |           99.20 | HBond              |
|       150 | TYR       |              981 |              957 |           95.60 | HBond              |
|       154 | GLU       |             1349 |              811 |           81.02 | HBond              |
|       152 | GLY       |              753 |              648 |           64.74 | WaterBridge        |
|       150 | TYR       |              565 |              556 |           55.54 | Pi-Pi              |
|        78 | LYS       |              777 |              523 |           52.25 | WaterBridge        |
|        84 | VAL       |              324 |              282 |           28.17 | Hydrophobic        |
|        99 | LYS       |              218 |              218 |           21.78 | WaterBridge        |
|        99 | LYS       |              190 |              190 |           18.98 | Pi-Cation          |
|        97 | ALA       |              172 |              170 |           16.98 | Hydrophobic        |
|       133 | LEU       |              170 |              170 |           16.98 | Hydrophobic        |
|       150 | TYR       |              155 |              143 |           14.29 | WaterBridge        |
|       145 | LEU       |              138 |              138 |           13.79 | Hydrophobic        |
|       154 | GLU       |              144 |              124 |           12.39 | WaterBridge        |
|       131 | MET       |              120 |              120 |           11.99 | Hydrophobic        |
|        76 | LEU       |              107 |              105 |           10.49 | Hydrophobic        |
|        76 | LEU       |              110 |              100 |            9.99 | WaterBridge        |
|       214 | ILE       |               57 |               57 |            5.69 | Hydrophobic        |
|       200 | LEU       |               58 |               57 |            5.69 | Hydrophobic        |
|       154 | GLU       |               49 |               49 |            4.90 | Ionic              |

## Interpretation

The `.dat` files support a stable CPD-1422-bound PfCDPK4 complex, but with a more conservative RMSD interpretation than the static interaction diagram alone. The second-half protein Cα RMSD averages approximately **4.96 Å**, indicating that the protein adopts a displaced but relatively stable conformational state after equilibration. The ligand remains internally stable, with ligand RMSD relative to itself averaging approximately **0.49 Å** in the second half.

The strongest dynamic contacts are the direct hydrogen bonds involving **Asp148**, **Tyr150**, and **Glu154**, with occupancy values of approximately **99.2%**, **95.6%**, and **81.0%**, respectively. This supports the docking-derived interpretation that CPD-1422 is stabilized by a persistent polar anchoring network. Additional contacts include **Tyr150 π–π interaction** (~55.5%), **Gly152 water bridge** (~64.7%), **Lys78 water bridge** (~52.2%), and hydrophobic support from **Val84**, **Ala97**, **Leu133**, **Leu145**, **Met131**, and **Leu76**.

## Manuscript-ready interpretation

Analysis of the Desmond trajectory output files showed that CPD-1422 remained accommodated within the PfCDPK4 ATP-binding pocket during the 100 ns simulation. Although the protein Cα RMSD shifted to an average of approximately 4.96 Å in the second half of the trajectory, the relatively low second-half standard deviation suggests stabilization around a new conformational state rather than continuous drift. The ligand maintained a stable internal conformation, with ligand RMSD relative to itself averaging approximately 0.49 Å during the equilibrated phase. Contact analysis revealed persistent hydrogen bonding with Asp148, Tyr150, and Glu154, together with water-mediated contacts involving Gly152 and Lys78 and hydrophobic support from Val84, Ala97, Leu133, Leu145, Met131, and Leu76. These findings support the predicted dynamic stability of CPD-1422 in the PfCDPK4 binding site, while further replicate simulations and binding free-energy analysis are required before making strong potency claims.

## Cautions

- The protein RMSD is higher than a simple 1–3 Å small-globular-protein heuristic; this should be reported as stabilization after conformational adjustment, not as minimal protein deviation.
- The ligand does not appear to dissociate, but the ligand RMSD relative to protein is higher than the ligand self-RMSD, indicating positional adjustment inside the binding pocket.
- These are single-trajectory results. Replicate MD and MM-GBSA/MM-PBSA are needed before final prioritization.
