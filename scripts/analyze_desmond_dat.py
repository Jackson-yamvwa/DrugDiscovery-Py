#!/usr/bin/env python3
"""
Parse Desmond Simulation Interactions Diagram .dat files.

This script summarizes:
- protein-ligand RMSD
- ligand properties
- ligand RMSF
- protein RMSF for selected residues
- protein-ligand contact occupancy

Expected input: a directory containing Desmond-exported .dat files, e.g.
PL_RMSD.dat, L-Properties.dat, L_RMSF.dat, P_RMSF.dat,
PL-Contacts_HBond.dat, PL-Contacts_Hydrophobic.dat, etc.

Usage:
    python scripts/analyze_desmond_dat.py --input results/md/CPD_1422/raw_dat --output results/md/CPD_1422/processed
"""

from __future__ import annotations

import argparse
from io import StringIO
from pathlib import Path

import pandas as pd


def read_rmsd(path: Path) -> pd.DataFrame:
    cols = [
        "frame",
        "Prot_CA",
        "Prot_Backbone",
        "Prot_Sidechain",
        "Prot_All_Heavy",
        "Lig_wrt_Protein",
        "Lig_wrt_Ligand",
    ]
    return pd.read_csv(path, sep=r"\s+", comment="#", names=cols)


def read_ligand_properties(path: Path) -> pd.DataFrame:
    cols = ["Frame", "RMSD", "rGyr", "intraHB", "MolSA", "SASA", "PSA"]
    return pd.read_csv(path, sep=r"\s+", skiprows=1, names=cols)


def read_ligand_rmsf(path: Path) -> pd.DataFrame:
    return pd.read_csv(
        path,
        sep=r"\s+",
        comment="#",
        names=["Atom", "wrt_Protein", "wrt_Ligand"],
    ).dropna()


def read_protein_rmsf(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, sep=r"\s+", comment="#", names=[
        "ResidueIndex", "Chain", "ResName", "LigandContact", "CA",
        "Backbone", "Sidechain", "All_Heavy", "B_factor"
    ])


def read_contact(path: Path) -> pd.DataFrame:
    name = path.name
    lines = [
        line for line in path.read_text(errors="ignore").splitlines(True)
        if line.strip() and not line.strip().startswith("#")
    ]

    if "Hydrophobic" in name:
        cols = ["Frame", "Residue", "Chain", "ResName", "LigandFragment"]
    elif "HBond" in name:
        cols = ["Frame", "Residue", "Chain", "ResName", "AtomName", "LigandFragment", "LigandAtomName"]
    elif "WaterBridge" in name:
        cols = ["Frame", "Residue", "Chain", "ResName", "AtomName", "LigandFragment", "LigandAtom"]
    elif "Ionic" in name:
        cols = ["Frame", "Residue", "Chain", "ResName", "AtomName", "LigandFragment", "LigandAtom", "Distance"]
    elif "Pi-Pi" in name:
        cols = ["Frame", "Residue", "Chain", "ResName", "LigandFragment", "Distance", "Type"]
    elif "Pi-Cation" in name:
        cols = ["Frame", "Residue", "Chain", "ResName", "LigandFragment", "Distance"]
    else:
        return pd.DataFrame()

    if not lines:
        return pd.DataFrame(columns=cols)

    return pd.read_csv(StringIO("".join(lines)), sep=r"\s+", names=cols)


def summarize_numeric(df: pd.DataFrame, frame_col: str | None = None) -> pd.DataFrame:
    cols = df.select_dtypes(include="number").columns.tolist()
    if frame_col in cols:
        cols.remove(frame_col)

    rows = []
    for col in cols:
        s = df[col]
        rows.append({
            "metric": col,
            "mean": s.mean(),
            "sd": s.std(),
            "min": s.min(),
            "max": s.max(),
            "median": s.median(),
        })
    return pd.DataFrame(rows)


def contact_occupancy(df: pd.DataFrame, interaction_type: str, nframes: int) -> pd.DataFrame:
    if df.empty or "Residue" not in df.columns:
        return pd.DataFrame(columns=[
            "Residue", "ResName", "contact_events", "frames_present",
            "occupancy_pct", "interaction_type"
        ])

    out = (
        df.groupby(["Residue", "ResName"])
        .agg(contact_events=("Frame", "size"), frames_present=("Frame", "nunique"))
        .reset_index()
    )
    out["occupancy_pct"] = 100 * out["frames_present"] / nframes
    out["interaction_type"] = interaction_type
    return out.sort_values("occupancy_pct", ascending=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--binding-residues",
        default="76,77,78,84,97,99,131,133,145,147,148,150,152,154,157,197,200,214,215,218",
    )
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)

    rmsd = read_rmsd(args.input / "PL_RMSD.dat")
    nframes = int(rmsd["frame"].nunique())

    rmsd_summary = pd.concat([
        summarize_numeric(rmsd, frame_col="frame").assign(window="overall"),
        summarize_numeric(rmsd[rmsd["frame"] >= 500], frame_col="frame").assign(window="frames_500_1000"),
    ])
    rmsd_summary.to_csv(args.output / "rmsd_summary.csv", index=False)

    props_path = args.input / "L-Properties.dat"
    if props_path.exists():
        props = read_ligand_properties(props_path)
        props_summary = pd.concat([
            summarize_numeric(props, frame_col="Frame").assign(window="overall"),
            summarize_numeric(props[props["Frame"] >= 500], frame_col="Frame").assign(window="frames_500_1000"),
        ])
        props_summary.to_csv(args.output / "ligand_property_summary.csv", index=False)

    lrmsf_path = args.input / "L_RMSF.dat"
    if lrmsf_path.exists():
        lrmsf = read_ligand_rmsf(lrmsf_path)
        lrmsf.to_csv(args.output / "ligand_rmsf.csv", index=False)

    prmsf_path = args.input / "P_RMSF.dat"
    if prmsf_path.exists():
        prmsf = read_protein_rmsf(prmsf_path)
        prmsf["ResidueName"] = prmsf["ResName"].str.split("_").str[0]
        prmsf["ResidueActual"] = prmsf["ResName"].str.extract(r"_(\d+)").astype(int)
        residues = [int(x) for x in args.binding_residues.split(",") if x.strip()]
        prmsf[prmsf["ResidueActual"].isin(residues)].to_csv(
            args.output / "binding_site_rmsf_summary.csv", index=False
        )

    all_contacts = []
    for contact_path in args.input.glob("PL-Contacts_*.dat"):
        interaction_type = contact_path.stem.replace("PL-Contacts_", "")
        df = read_contact(contact_path)
        occ = contact_occupancy(df, interaction_type, nframes)
        if not occ.empty:
            all_contacts.append(occ)

    if all_contacts:
        pd.concat(all_contacts).sort_values(
            ["interaction_type", "occupancy_pct"], ascending=[True, False]
        ).to_csv(args.output / "contact_occupancy_summary.csv", index=False)


if __name__ == "__main__":
    main()
