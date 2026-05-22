# DXR Reference Replicate 44503 MD Figures

**Update timestamp:** 2026-05-22

## Source figure files received

```text
L_2d_main.png
LP-Contacts_2d-Summary(2).png
LP-Contacts_2d-Summary(2).svg
L-Properties(3).png
L-Properties(3).svg
L-RMSF(1).png
L-RMSF.svg
L-Torsions(1).png
L-Torsions(1).svg
```

## Figure interpretation summary

These figures correspond to the **DXR reference replicate 44503** simulation and support the report summary stored under:

```text
results/md/DXR_reference/replicate_44503/reports/README.md
```

The 44503 figure set supports the same core DXR reference binding fingerprint observed in other DXR replicates: persistent **Asp148** and **Tyr150** anchoring, with additional **Lys99** π-cation/contact contribution.

## Figure-level observations

### Ligand 2D structure

The uploaded 2D ligand structure confirms the DXR scaffold used in the reference simulation: a pyrazolo-pyrimidine core with a tert-butyl substituent, an amino group, and a bromophenyl-containing hydrophobic/aromatic region.

### 2D ligand–protein contact summary

The 2D ligand-contact summary identifies interactions above the trajectory reporting threshold:

| Residue | Approximate occupancy / role |
|---|---|
| Asp148 | ~98% H-bond anchor |
| Tyr150 | ~93% H-bond/polar anchor |
| Lys99 | ~39% π-cation/contact contribution near the bromophenyl/aromatic region |

This contact pattern is highly consistent with the previously documented DXR reference fingerprint and confirms that **Asp148/Tyr150** are the primary conserved anchor residues.

### Ligand properties

The ligand property panel indicates stable ligand behaviour during the trajectory:

| Property | Visual interpretation |
|---|---|
| Ligand RMSD | Low-to-moderate fluctuation with a brief early spike; remains generally stable afterward |
| Radius of gyration | Stable around ~3.9–4.0 Å, supporting retained compactness |
| Intramolecular H-bonds | Mostly absent, with only rare brief events |
| Molecular surface area | Stable around ~328–336 Å² in this figure set |
| SASA | Moderate fluctuation, reflecting changing solvent exposure during binding-pocket accommodation |
| PSA | Stable around ~184–192 Å² in this figure set |

### Ligand RMSF

The ligand RMSF figure shows generally low atom-level fluctuation, with most atoms fluctuating around ~0.8–1.0 Å when fitted on protein. The profile indicates retained ligand conformation without large atom-specific destabilization.

### Ligand torsions

The ligand torsion plots show multiple rotatable-bond conformational states. Some torsions remain narrowly distributed, while others sample broader angular ranges. This indicates peripheral torsional flexibility while the ligand maintains its main binding orientation.

## Manuscript-ready figure interpretation

The DXR reference replicate 44503 figures support stable ligand accommodation within the PfCDPK4 ATP-binding pocket during the 100 ns simulation. The 2D contact summary identifies persistent Asp148 and Tyr150 interactions, with approximate occupancies of 98% and 93%, respectively, and an additional Lys99 π-cation/contact contribution of approximately 39%. Ligand property plots indicate stable ligand compactness, low-to-moderate RMSD, limited intramolecular hydrogen bonding, and moderate solvent-exposure fluctuation. Ligand RMSF and torsion profiles suggest that the ligand retains its core binding orientation while allowing limited peripheral conformational flexibility. Together, these findings reinforce the reproducibility of the DXR reference interaction fingerprint across replicate simulations.

## Comparison with previous DXR reference figure sets

| Feature | Replicate 44501 | Replicate 44502 | Replicate 44503 | Interpretation |
|---|---|---|---|---|
| Primary anchors | Asp148/Tyr150 | Asp148/Tyr150 | Asp148/Tyr150 | conserved |
| Additional contact emphasized | Lys99 | Val84 or Lys99 depending on summary source | Lys99 | peripheral contact variability, but Lys99 recurs |
| Ligand compactness | stable | stable | stable | reproducible |
| Ligand torsional behaviour | peripheral flexibility | peripheral flexibility | peripheral flexibility | expected for substituents |

## Repository handling decision

The uploaded PNG and SVG files are suitable for repository inclusion because they are compact, interpretable analysis artifacts. Recommended destinations are:

```text
results/md/DXR_reference/replicate_44503/figures/L_2d_main.png
results/md/DXR_reference/replicate_44503/figures/LP-Contacts_2d-Summary.png
results/md/DXR_reference/replicate_44503/figures/LP-Contacts_2d-Summary.svg
results/md/DXR_reference/replicate_44503/figures/L-Properties.png
results/md/DXR_reference/replicate_44503/figures/L-Properties.svg
results/md/DXR_reference/replicate_44503/figures/L-RMSF.png
results/md/DXR_reference/replicate_44503/figures/L-RMSF.svg
results/md/DXR_reference/replicate_44503/figures/L-Torsions.png
results/md/DXR_reference/replicate_44503/figures/L-Torsions.svg
```

At this stage, this README documents the figure set and interpretation. Binary figure files can be committed locally with `git add`.

## Recommended local commit commands

```bash
git add results/md/DXR_reference/replicate_44503/figures/
git commit -m "figures: add DXR reference replicate 44503 ligand plots"
git push origin main
```
