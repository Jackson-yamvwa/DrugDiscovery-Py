from pathlib import Path

import pandas as pd


def prepare_library_from_excel(
    input_path: str | Path,
    output_path: str | Path,
    id_column: str = "compoundID",
    smiles_column: str = "Smiles",
    mw_column: str = "MW",
    sheet_name: str | int = 0,
) -> pd.DataFrame:
    """
    Prepare a DrugDiscovery-Py-compatible ligand library from an Excel file.

    Output columns:
    - compound_id
    - smiles
    - molecular_weight
    - hbd
    - hba
    - tpsa
    - rotatable_bonds
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")

    df = pd.read_excel(input_path, sheet_name=sheet_name)

    required = {id_column, smiles_column, mw_column}
    missing = required.difference(df.columns)

    if missing:
        raise ValueError(f"Missing required Excel columns: {sorted(missing)}")

    prepared = df[[id_column, smiles_column, mw_column]].copy()

    prepared = prepared.rename(
        columns={
            id_column: "compound_id",
            smiles_column: "smiles",
            mw_column: "molecular_weight",
        }
    )

    prepared["hbd"] = pd.NA
    prepared["hba"] = pd.NA
    prepared["tpsa"] = pd.NA
    prepared["rotatable_bonds"] = pd.NA

    prepared = prepared.dropna(subset=["compound_id", "smiles"])
    prepared = prepared.drop_duplicates(subset=["compound_id"])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    prepared.to_csv(output_path, index=False)

    return prepared
