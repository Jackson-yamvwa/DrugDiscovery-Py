# DXR Reference Ligand MD Figures

**Update timestamp:** 2026-05-22

## Source figure files received

### Ligand and contact-summary figures

```text
LP-Contacts_2d-Summary.svg
L-Properties(1).png
L-Properties(1).svg
L-RMSF.png
L-Torsions.png
L-Torsions.svg
L-Torsions-2d.png
PL-Contacts_Histogram.png
PL-Contacts_Histogram.svg
```

### Protein/contact-timeline figures

```text
PL-Contacts_Timeline.png
PL-Contacts_Timeline.svg
P-RMSF.png
P-RMSF.svg
P-SSE_Histogram.png
P-SSE_Histogram.svg
```

## Figure interpretation summary

These figures correspond to the DXR co-crystallized/reference ligand MD simulation and support the processed `.dat` summaries already stored under:

```text
results/md/DXR_reference/processed/
```

## Figure-level observations

### Ligand properties

The ligand property panel shows that the DXR ligand remains internally stable over the 100 ns trajectory:

| Property | Visual interpretation |
|---|---|
| Ligand RMSD | Mostly low-amplitude fluctuation, generally below ~0.75 Å |
| Radius of gyration | Stable around ~4.1–4.2 Å, indicating preserved compactness |
| Intramolecular H-bonds | None detected |
| Molecular surface area | Stable around ~296–302 Å² |
| SASA | Fluctuates over time, indicating changing solvent exposure while ligand remains bound |
| PSA | Stable around ~74–80 Å² |

### Ligand RMSF

The ligand RMSF plot shows that most DXR atoms fluctuate below ~1.0 Å when fitted on protein. The highest mobility is concentrated around atoms 12–14, corresponding to the tert-butyl substituent region. This is consistent with peripheral substituent flexibility while the core remains more stable.

### Ligand torsions

The torsion plots indicate that some rotatable bonds sample multiple conformational states, particularly around the benzyl/aryl linker and tert-butyl-associated torsional region. This suggests torsional flexibility in peripheral substituents rather than instability of the central heteroaromatic scaffold.

### Protein–ligand contact histogram

The contact histogram confirms that the dominant DXR reference interactions involve:

| Residue | Contact interpretation |
|---|---|
| Asp148 | High-occupancy H-bond contact |
| Tyr150 | High-occupancy H-bond/polar contact |
| Lys99 | Significant π-cation or water-mediated contribution in the report-derived interaction profile |
| Val84, Ala97, Leu76, Leu200, Ile214 | Hydrophobic pocket support |

### Protein–ligand contact timeline

The contact timeline shows that **Asp148** and **Tyr150** maintain near-continuous interaction bands across the 100 ns trajectory. **Val84**, **Ala97**, **Lys99**, **Leu76**, **Leu200**, **Ile214**, and **Asp215** appear intermittently. This pattern supports a reference binding mode dominated by persistent Asp148/Tyr150 anchoring, with additional hydrophobic and water-mediated/polar contacts contributing episodically.

### Protein RMSF

The protein RMSF figure shows that most binding-site residues remain relatively stable, while larger RMSF peaks occur in loop/terminal or flexible regions outside the central binding-pocket scaffold. Green vertical markers indicate ligand-contacting residues. The contact residues cluster largely in lower-RMSF regions, supporting a stable binding-site environment for the reference ligand.

### Protein secondary structure elements

The SSE histogram shows persistent alpha-helical and beta-strand segments throughout the protein. Secondary-structure content remains broadly stable over the 100 ns trajectory, supporting the conclusion that the global fold is maintained during the DXR reference simulation.

### 2D ligand–protein contact diagram

The 2D summary diagram highlights the reference interaction fingerprint involving:

- **Asp148**: persistent polar/H-bond anchoring interaction
- **Tyr150**: persistent polar interaction with the heteroaromatic core
- **Lys99**: π-cation interaction near the aromatic bromophenyl region
- hydrophobic contacts around the ATP-pocket scaffold

## Manuscript-ready figure interpretation

The DXR reference ligand figures indicate stable accommodation of the co-crystallized ligand within the PfCDPK4 ATP-binding pocket during the 100 ns simulation. The ligand property plots show low internal RMSD, stable radius of gyration, absence of intramolecular hydrogen bonding, and moderate solvent-exposure fluctuations. Ligand RMSF analysis indicates that the central scaffold remains relatively stable, with higher mobility localized to peripheral substituent atoms. Protein RMSF and SSE plots support preservation of the global fold and relative stability of ligand-contacting residues. The protein–ligand contact histogram, timeline, and 2D contact summary identify Asp148 and Tyr150 as the dominant reference anchoring residues, with additional contribution from Lys99 and hydrophobic residues including Val84, Ala97, Leu76, Leu200, and Ile214. Together, these figures support use of the DXR trajectory as a dynamic reference profile for evaluating candidate PfCDPK4 inhibitors.

## Repository handling decision

The uploaded PNG and SVG figures are suitable for repository inclusion because they are compact, interpretable analysis artifacts. If committed directly, recommended destinations are:

```text
results/md/DXR_reference/figures/LP-Contacts_2d-Summary.svg
results/md/DXR_reference/figures/L-Properties.png
results/md/DXR_reference/figures/L-Properties.svg
results/md/DXR_reference/figures/L-RMSF.png
results/md/DXR_reference/figures/L-Torsions.png
results/md/DXR_reference/figures/L-Torsions.svg
results/md/DXR_reference/figures/L-Torsions-2d.png
results/md/DXR_reference/figures/PL-Contacts_Histogram.png
results/md/DXR_reference/figures/PL-Contacts_Histogram.svg
results/md/DXR_reference/figures/PL-Contacts_Timeline.png
results/md/DXR_reference/figures/PL-Contacts_Timeline.svg
results/md/DXR_reference/figures/P-RMSF.png
results/md/DXR_reference/figures/P-RMSF.svg
results/md/DXR_reference/figures/P-SSE_Histogram.png
results/md/DXR_reference/figures/P-SSE_Histogram.svg
```

At this stage, this README documents the figure set and its scientific interpretation. Binary figure upload can be performed locally with `git add`, or through a future GitHub file upload workflow if binary support is configured.

## Recommended local commit commands

```bash
git add results/md/DXR_reference/figures/
git commit -m "figures: add DXR reference MD interaction plots"
git push origin main
```
