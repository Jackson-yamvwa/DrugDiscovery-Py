# PfCDPK4 4QOX Co-crystallized Ligand Desmond MD Run

**Update timestamp:** 2026-05-22

## Source files received

```text
4QOX-Cocrystalised.cfg
4QOX-Cocrystalised.cms
4QOX-Cocrystalised.cpt
4QOX-Cocrystalised.ene
4QOX-Cocrystalised.log
4QOX-Cocrystalised.msj
```

## Repository handling decision

The uploaded files represent a full Desmond run package for the 4QOX co-crystallized/reference ligand system. The binary/runtime files should not be committed directly unless Git LFS or external archival storage is configured.

| File | Role | Repository decision |
|---|---|---|
| `4QOX-Cocrystalised.cfg` | Desmond run configuration | Document key settings; optionally commit later if needed |
| `4QOX-Cocrystalised.cms` | Full Desmond system structure | Do not commit without Git LFS |
| `4QOX-Cocrystalised.cpt` | Checkpoint file | Do not commit without Git LFS |
| `4QOX-Cocrystalised.ene` | Energy output | Do not commit without compression/LFS; parse summary first |
| `4QOX-Cocrystalised.log` | Full execution log | Summarize key metadata; raw log optional if size acceptable |
| `4QOX-Cocrystalised.msj` | Desmond job/control file | Document key settings; optional commit later |

## Key run metadata

| Parameter | Value |
|---|---:|
| System/job name | `4QOX-Cocrystalised` |
| Engine | Desmond / Schrödinger 2019-4 |
| Backend | `mdsim` |
| Execution mode | GPU Desmond |
| GPU | NVIDIA GeForce RTX 3080 |
| Ensemble | NPT |
| Temperature | 310.0 K |
| Pressure | 1.01325 bar, isotropic |
| Simulation length | 100,000 ps = 100 ns |
| Main timestep | 0.002 ps |
| RESPA timesteps | 0.002, 0.002, 0.006 ps |
| Trajectory interval | 100 ps |
| Energy interval | 1.2 ps |
| Cutoff radius | 9.0 Å |
| Coulomb method | `useries` |
| Velocity seed | 2007 |
| Restraints | none |
| Checkpoint interval | 240.06 ps |

## Execution status

The log indicates that the simulation reached the intended endpoint at approximately **100,000 ps** and ended normally. The final log section reports writing the last checkpoint at **100000.008 ps**, followed by `finished`, license check-in, and `Child returned 0`.

## Performance note

The run used GPU Desmond on an NVIDIA GeForce RTX 3080. The log reports a final total rate of approximately **749.160 ns/day**.

## Scientific role in the project

This co-crystallized 4QOX simulation should be treated as the **reference MD system** for evaluating candidate compounds such as CPD-1422, CPD-2175, and CPD-2176. Its primary value is comparative:

1. Establish baseline RMSD/RMSF behaviour for the native/reference ligand-bound PfCDPK4 structure.
2. Provide a reference contact network for the ATP-binding pocket.
3. Support comparison of candidate ligands against a known binding pose.
4. Help distinguish candidate-specific instability from protein-intrinsic flexibility.

## Recommended next processing steps

1. Extract Desmond Simulation Interactions Diagram `.dat` files from this co-crystallized run.
2. Process the `.dat` outputs using:

```bash
python scripts/analyze_desmond_dat.py \
  --input results/md/4QOX_Cocrystalised/raw_dat \
  --output results/md/4QOX_Cocrystalised/processed
```

3. Compare the reference system against candidate systems using:
   - protein Cα RMSD,
   - ligand RMSD relative to protein,
   - ligand self-RMSD,
   - protein RMSF at binding-site residues,
   - contact occupancy,
   - ligand compactness and SASA/PSA trends.

## Interpretation caution

This file set confirms successful execution of the co-crystallized/reference-ligand MD simulation. It does not, by itself, provide contact occupancy or RMSD statistics comparable to the processed CPD-1422 `.dat` outputs. Those metrics require extracting and parsing the corresponding Simulation Interactions Diagram `.dat` files.
