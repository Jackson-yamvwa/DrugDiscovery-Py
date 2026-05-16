# Changelog

## v0.1.0 - Ligand Triage MVP

### Added

- CSV ligand library loading.
- Excel-to-ligand-library preparation workflow.
- Docking-score import and merging.
- Basic approximate SMILES descriptor estimation.
- Descriptor validation before ranking.
- Descriptor-only priority scoring.
- Ranking with or without docking scores.
- CLI commands:
  - `prepare-library`
  - `rank`
  - `summarize`
  - `export-top`
- Ranking summary report generation.
- Export of top-ranked candidate compounds.
- Malaria Libre descriptor-only triage workflow.
- Unit test suite with 17 passing tests.

### Notes

- Descriptor estimates are approximate and intended for early-stage triage.
- Descriptor-only ranking does not assess target binding, potency, selectivity, ADMET risk, or mechanism of action.
- Docking-based prioritisation requires external docking-score input.
