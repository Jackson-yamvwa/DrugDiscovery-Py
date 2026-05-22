# PfCDPK4 4QOX Co-crystallized Ligand Desmond MD Run

**Update timestamp:** 2026-05-22

## Source files received

### Initial Desmond run files

```text
4QOX-Cocrystalised.cfg
4QOX-Cocrystalised.cms
4QOX-Cocrystalised.cpt
4QOX-Cocrystalised.ene
4QOX-Cocrystalised.log
4QOX-Cocrystalised.msj
```

### Multisim/output package files

```text
4QOX-Cocrystalised_1-out.tgz
4QOX-Cocrystalised_2-out.tgz
4QOX-Cocrystalised_3-out.tgz
4QOX-Cocrystalised_4-out.tgz
4QOX-Cocrystalised_6-out.tgz
4QOX-Cocrystalised_7-out.tgz
4QOX-Cocrystalised_multisim.log
4QOX-Cocrystalised-in.cms
4QOX-Cocrystalised-multisim_checkpoint
```

### Final production output/checkpoint files

```text
4QOX-Cocrystalised-multisim_checkpoint(1)
4QOX-Cocrystalised-multisim_checkpoint_8
4QOX-Cocrystalised-out.cfg
4QOX-Cocrystalised-out.cms
```

## Repository handling decision

The uploaded files represent a full Desmond/Multisim run package for the 4QOX co-crystallized/reference ligand system. Binary/runtime files should not be committed directly unless Git LFS or external archival storage is configured.

| File | Role | Repository decision |
|---|---|---|
| `4QOX-Cocrystalised.cfg` / `4QOX-Cocrystalised-out.cfg` | Input/final Desmond run configuration | Document key settings; optionally commit later because text and compact |
| `4QOX-Cocrystalised.cms` / `4QOX-Cocrystalised-in.cms` / `4QOX-Cocrystalised-out.cms` | Full Desmond system structure | Do not commit without Git LFS; `out.cms` is a large final system file |
| `4QOX-Cocrystalised.cpt` / `4QOX-Cocrystalised-multisim_checkpoint` / `4QOX-Cocrystalised-multisim_checkpoint_8` | Checkpoint files | Do not commit without Git LFS |
| `4QOX-Cocrystalised.ene` | Energy output | Do not commit without compression/LFS; parse summary first |
| `4QOX-Cocrystalised.log` | Main Desmond execution log | Summarize key metadata; raw log optional if size acceptable |
| `4QOX-Cocrystalised_multisim.log` | Multisim workflow log | Document stage progression and completion |
| `4QOX-Cocrystalised.msj` | Desmond job/control file | Document key settings; optional commit later |
| `4QOX-Cocrystalised_*out.tgz` | Stage output archives | Do not commit without Git LFS; extract only compact analysis outputs |

## Key run metadata

| Parameter | Value |
|---|---:|
| System/job name | `4QOX-Cocrystalised` |
| Engine | Desmond / Schrödinger 2019-4 |
| Multisim version | 3.8.5.19 |
| mmshare version | 4.8 |
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
| Restraints | none for final production stage |
| Checkpoint interval | 240.06 ps |

## Final output file notes

The final production configuration file `4QOX-Cocrystalised-out.cfg` is a compact text configuration that records the production-stage Desmond settings, including NPT ensemble, 310 K temperature, 1.01325 bar pressure, 100,000 ps simulation time, 0.002 ps main timestep, 100 ps trajectory interval, and 1.2 ps energy interval.

The final production structure file `4QOX-Cocrystalised-out.cms` is a large Desmond CMS structure file and should be treated as a binary/large runtime artifact for repository purposes. It should be stored via Git LFS or external archival storage rather than committed directly to the standard Git history.

The files `4QOX-Cocrystalised-multisim_checkpoint(1)` and `4QOX-Cocrystalised-multisim_checkpoint_8` are Multisim checkpoint artifacts. They are useful for workflow recovery/provenance but should not be committed directly without Git LFS.

## Multisim workflow summary

The Multisim workflow was launched with the Schrödinger `multisim` utility in umbrella mode. The workflow contained eight stages:

| Stage | Description | Status |
|---:|---|---|
| 1 | Task/system detection | Completed |
| 2 | Brownian Dynamics NVT, 10 K, small timesteps, solute heavy-atom restraints, 100 ps | Completed |
| 3 | NVT, 10 K, small timesteps, solute heavy-atom restraints, 12 ps | Completed |
| 4 | NPT, 10 K, solute heavy-atom restraints, 12 ps | Completed |
| 5 | `solvate_pocket` | Skipped |
| 6 | NPT with solute heavy-atom restraints, 12 ps | Completed |
| 7 | NPT without restraints, 24 ps | Completed |
| 8 | Final production simulation | Completed |

## Execution status

The main Desmond log indicates that the simulation reached the intended endpoint at approximately **100,000 ps** and ended normally. The final log section reports writing the last checkpoint at **100000.008 ps**, followed by `finished`, license check-in, and `Child returned 0`.

The Multisim workflow also completed successfully. Stage 8, the production simulation, ran from **10:22:08 to 13:34:37 on 22 Feb 2026**, with a duration of **3 h 12 min 29 s**. The full Multisim workflow completed in **3 h 14 min 53 s**, with total GPU time of **3 h 14 min 14 s** across six GPU subjobs.

## Performance note

The run used GPU Desmond on an NVIDIA GeForce RTX 3080. The main Desmond log reports a final total rate of approximately **749.160 ns/day**.

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
