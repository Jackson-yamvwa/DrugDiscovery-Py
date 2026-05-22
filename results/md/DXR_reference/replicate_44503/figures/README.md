# DXR Reference Replicate 44503 MD Figures

**Update timestamp:** 2026-05-22

## Source figure files received

### Ligand and contact-summary figures

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
L-Torsions-2d(1).png
```

### Protein/contact/RMSD figures

```text
PL-Contacts_Histogram(1).png
PL-Contacts_Histogram(2).svg
PL-Contacts_Timeline(2).png
PL-Contacts_Timeline(3).svg
PL-RMSD.png
PL-RMSD.svg
P-RMSF(3).png
P-RMSF(2).svg
```

### Protein secondary-structure figures

```text
P-SSE_Histogram(2).png
P-SSE_Histogram(2).svg
P-SSE_Timeline.png
P-SSE_Timeline(1).svg
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

### Protein–ligand contact histogram

The contact histogram shows a stronger and more distributed interaction network than earlier DXR reference summaries, with major contributions from:

| Residue | Contact interpretation |
|---|---|
| Asp148 | high-occupancy H-bond anchor |
| Tyr150 | high-occupancy H-bond/polar plus water-mediated contribution |
| Glu154 | strong polar/water-mediated contact contribution |
| Glu197 | strong polar/water-mediated contact contribution |
| Lys99 | mixed contact contribution, including water-mediated support |
| Val84, Ala97, Leu76, Leu200, Ile214 | hydrophobic pocket support |

### Protein–ligand contact timeline

The contact timeline shows persistent contact bands for **Asp148**, **Tyr150**, **Glu154**, and **Glu197**, with additional intermittent contacts involving **Val84**, **Ala97**, **Lys99**, **Met131**, **Leu133**, **Leu145**, **Leu200**, and **Ile214**. The total contact count remains generally high across the trajectory, typically between approximately 5 and 9 contacts, indicating continuous ligand engagement with the binding pocket.

### Protein–ligand RMSD

The PL-RMSD plot shows that protein Cα RMSD rises during early equilibration and then fluctuates mostly around approximately **2.5–3.0 Å** after the first 20–30 ns. Ligand RMSD relative to protein remains mostly around approximately **1.6–2.0 Å**, supporting retained binding-pocket accommodation. There is no visual evidence of ligand dissociation.

### Protein RMSF

The protein RMSF figure shows expected high-flexibility peaks in loop or terminal regions, while the ligand-contacting residues are largely located in relatively stable regions. This supports preservation of the reference binding-site scaffold during the replicate simulation.

### Protein secondary structure

The SSE histogram and timeline show broadly stable secondary-structure organization throughout the 100 ns trajectory. The total secondary-structure percentage remains close to the report-derived value of approximately **47.25%**, with persistent alpha-helical and beta-strand segments across the protein. The SSE timeline does not show global unfolding or large-scale secondary-structure loss, supporting preservation of the PfCDPK4 fold during the replicate simulation.

## Manuscript-ready figure interpretation

The DXR reference replicate 44503 figures support stable ligand accommodation within the PfCDPK4 ATP-binding pocket during the 100 ns simulation. The 2D contact summary identifies persistent Asp148 and Tyr150 interactions, with approximate occupancies of 98% and 93%, respectively, and an additional Lys99 π-cation/contact contribution of approximately 39%. Ligand property plots indicate stable ligand compactness, low-to-moderate RMSD, limited intramolecular hydrogen bonding, and moderate solvent-exposure fluctuation. Contact histogram and timeline plots further indicate sustained interactions with Asp148, Tyr150, Glu154, and Glu197, while PL-RMSD shows protein stabilization around a moderate RMSD range and retention of ligand accommodation within the binding pocket. Protein RMSF and secondary-structure plots support preservation of the global fold and binding-site scaffold. Ligand RMSF and torsion profiles suggest that the ligand retains its core binding orientation while allowing limited peripheral conformational flexibility. Together, these findings reinforce the reproducibility of the DXR reference interaction fingerprint across replicate simulations.

## Comparison with previous DXR reference figure sets

| Feature | Replicate 44501 | Replicate 44502 | Replicate 44503 | Interpretation |
|---|---|---|---|---|
| Primary anchors | Asp148/Tyr150 | Asp148/Tyr150 | Asp148/Tyr150 | conserved |
| Additional contact emphasized | Lys99 | Val84 or Lys99 depending on summary source | Lys99, Glu154, Glu197 | peripheral/polar network varies by run and summary source |
| Ligand compactness | stable | stable | stable | reproducible |
| Ligand torsional behaviour | peripheral flexibility | peripheral flexibility | peripheral flexibility | expected for substituents |
| Ligand accommodation | retained | retained | retained | no dissociation signal |
| Secondary structure | stable | stable | stable | global fold preserved |

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
results/md/DXR_reference/replicate_44503/figures/L-Torsions-2d.png
results/md/DXR_reference/replicate_44503/figures/PL-Contacts_Histogram.png
results/md/DXR_reference/replicate_44503/figures/PL-Contacts_Histogram.svg
results/md/DXR_reference/replicate_44503/figures/PL-Contacts_Timeline.png
results/md/DXR_reference/replicate_44503/figures/PL-Contacts_Timeline.svg
results/md/DXR_reference/replicate_44503/figures/PL-RMSD.png
results/md/DXR_reference/replicate_44503/figures/PL-RMSD.svg
results/md/DXR_reference/replicate_44503/figures/P-RMSF.png
results/md/DXR_reference/replicate_44503/figures/P-RMSF.svg
results/md/DXR_reference/replicate_44503/figures/P-SSE_Histogram.png
results/md/DXR_reference/replicate_44503/figures/P-SSE_Histogram.svg
results/md/DXR_reference/replicate_44503/figures/P-SSE_Timeline.png
results/md/DXR_reference/replicate_44503/figures/P-SSE_Timeline.svg
```

At this stage, this README documents the figure set and interpretation. Binary figure files can be committed locally with `git add`.

## Recommended local commit commands

```bash
git add results/md/DXR_reference/replicate_44503/figures/
git commit -m "figures: add DXR reference replicate 44503 MD plots"
git push origin main
```
