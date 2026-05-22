# DXR Reference Replicate 44502 MD Figures

**Update timestamp:** 2026-05-22

## Source figure files received

```text
LP-Contacts_2d-Summary(1).png
LP-Contacts_2d-Summary(1).svg
L-Properties(2).png
L-Properties(2).svg
PL-Contacts_Histogram(1).svg
PL-Contacts_Timeline(2).svg
P-RMSF(2).png
P-SSE_Timeline.svg
```

## Figure interpretation summary

These figures correspond to the **DXR reference replicate 44502** simulation and support the report summary stored under:

```text
results/md/DXR_reference/replicate_44502/reports/README.md
```

The replicate 44502 figures confirm the conserved DXR reference binding pattern, especially persistent **Asp148** and **Tyr150** anchoring contacts, with additional peripheral hydrophobic support from **Val84**.

## Figure-level observations

### 2D ligand–protein contact summary

The 2D ligand-contact figure identifies the main contacts above the reporting threshold:

| Residue | Approximate occupancy / role |
|---|---|
| Asp148 | ~98% H-bond anchor in the uploaded figure; report page shows ~93% in the 44502 PDF |
| Tyr150 | ~93% H-bond/polar anchor in the uploaded figure; report page shows ~89% in the 44502 PDF |
| Lys99 | ~39% π-cation/contact contribution shown in one uploaded figure variant |

The interaction pattern confirms that the **Asp148/Tyr150 anchoring pair** is the dominant reference signature for DXR binding in PfCDPK4.

### Ligand properties

The ligand property panel shows stable ligand behaviour over the trajectory:

| Property | Visual interpretation |
|---|---|
| Ligand RMSD | Mostly low-amplitude fluctuation, generally below ~0.75–0.9 Å |
| Radius of gyration | Stable around ~4.1–4.2 Å, indicating compact ligand geometry |
| Intramolecular H-bonds | None detected |
| Molecular surface area | Stable near ~296–302 Å² |
| SASA | Moderate fluctuation, with some increase toward later trajectory windows |
| PSA | Stable near ~74–80 Å² |

### Protein–ligand contact histogram

The contact histogram supports a stable interaction network dominated by:

| Residue | Contact interpretation |
|---|---|
| Asp148 | high-occupancy H-bond contact |
| Tyr150 | high-occupancy H-bond/polar contact |
| Val84 | hydrophobic contribution above the 30% reporting threshold in replicate 44502 |
| Lys99 | intermittent water-mediated/contact contribution depending on summary file variant |
| Leu76, Ala97, Leu200, Ile214, Asp215 | intermittent supporting contacts |

### Protein–ligand contact timeline

The contact timeline shows near-continuous contact bands for **Asp148** and **Tyr150** across the 100 ns simulation. Other residues, including **Val84**, **Lys99**, **Leu76**, **Ala97**, **Leu200**, **Ile214**, and **Asp215**, appear intermittently. This supports a binding mode with stable core anchoring and dynamic peripheral support.

### Protein RMSF

The protein RMSF figure shows expected high-flexibility peaks in loop or terminal regions, while the ligand-contacting residues are largely located in relatively stable regions. This supports preservation of the reference binding-site scaffold during the replicate simulation.

### Protein secondary structure timeline

The SSE timeline indicates broadly maintained secondary-structure organization across the trajectory, consistent with the report-derived total SSE value of approximately **46.27%** for replicate 44502.

## Manuscript-ready figure interpretation

The DXR reference replicate 44502 figures support stable ligand accommodation within the PfCDPK4 ATP-binding pocket over the 100 ns trajectory. The ligand property plots show low internal RMSD, stable radius of gyration, absence of intramolecular hydrogen bonding, and moderate solvent-exposure fluctuation. Contact histogram and timeline plots indicate persistent Asp148 and Tyr150 interactions throughout the simulation, with Val84 and other hydrophobic residues providing intermittent peripheral support. Protein RMSF and secondary-structure plots indicate that the global fold and binding-site scaffold remain broadly stable. These findings reinforce the reproducibility of the Asp148/Tyr150 DXR reference interaction fingerprint across replicate simulations.

## Comparison with replicate 44501

| Feature | Replicate 44501 | Replicate 44502 | Interpretation |
|---|---|---|---|
| Primary H-bond anchors | Asp148/Tyr150 | Asp148/Tyr150 | conserved |
| Additional >30% contact emphasized | Lys99 | Val84 | peripheral contact variability |
| Ligand compactness | stable | stable | reproducible |
| Intramolecular H-bonds | absent | absent | consistent |
| Global fold | stable | stable | reproducible |

## Repository handling decision

The uploaded PNG and SVG files are suitable for repository inclusion because they are compact, interpretable analysis artifacts. Recommended destinations are:

```text
results/md/DXR_reference/replicate_44502/figures/LP-Contacts_2d-Summary.png
results/md/DXR_reference/replicate_44502/figures/LP-Contacts_2d-Summary.svg
results/md/DXR_reference/replicate_44502/figures/L-Properties.png
results/md/DXR_reference/replicate_44502/figures/L-Properties.svg
results/md/DXR_reference/replicate_44502/figures/PL-Contacts_Histogram.svg
results/md/DXR_reference/replicate_44502/figures/PL-Contacts_Timeline.svg
results/md/DXR_reference/replicate_44502/figures/P-RMSF.png
results/md/DXR_reference/replicate_44502/figures/P-SSE_Timeline.svg
```

At this stage, this README documents the figure set and interpretation. Binary figure files can be committed locally with `git add`.

## Recommended local commit commands

```bash
git add results/md/DXR_reference/replicate_44502/figures/
git commit -m "figures: add DXR reference replicate 44502 MD plots"
git push origin main
```
