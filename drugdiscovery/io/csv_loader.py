from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "compound_id",
    "smiles",
    "molecular_weight",
    "hbd",
    "hba",
    "tpsa",
    "rotatable_bonds",
}


def load_library(path: str | Path) -> pd.DataFrame:
    """
    Load a compound library from a CSV file.

    Version 0.1 expects supplied descriptors. Later versions will calculate
    descriptors directly from molecular structures.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)

    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    return df
