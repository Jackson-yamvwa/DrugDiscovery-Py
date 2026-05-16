import pandas as pd


def add_ligand_efficiency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate ligand efficiency.

    Ligand efficiency is approximated as:

        LE = -docking_score / heavy_atom_count

    If heavy_atom_count is absent, molecular_weight / 14 is used as a rough
    fallback for Version 0.1.
    """
    result = df.copy()

    if "heavy_atom_count" not in result.columns:
        result["heavy_atom_count"] = (result["molecular_weight"] / 14).round()

    if "docking_score" in result.columns:
        result["ligand_efficiency"] = (
            -result["docking_score"] / result["heavy_atom_count"]
        )
    else:
        result["ligand_efficiency"] = None

    return result


def add_priority_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a simple weighted priority score.

    This early version rewards:
    - stronger docking score
    - higher ligand efficiency
    - Lipinski pass
    - Veber pass
    """
    result = df.copy()

    if "docking_score" not in result.columns:
        result["docking_component"] = 0.0
    else:
        min_score = result["docking_score"].min()
        max_score = result["docking_score"].max()

        if min_score == max_score:
            result["docking_component"] = 1.0
        else:
            result["docking_component"] = (
                max_score - result["docking_score"]
            ) / (max_score - min_score)

    if "ligand_efficiency" not in result.columns:
        result = add_ligand_efficiency(result)

    le_min = result["ligand_efficiency"].min()
    le_max = result["ligand_efficiency"].max()

    if le_min == le_max:
        result["ligand_efficiency_component"] = 1.0
    else:
        result["ligand_efficiency_component"] = (
            result["ligand_efficiency"] - le_min
        ) / (le_max - le_min)

    result["lipinski_component"] = result.get("lipinski_pass", False).astype(float)
    result["veber_component"] = result.get("veber_pass", False).astype(float)

    result["priority_score"] = (
        0.40 * result["docking_component"]
        + 0.25 * result["ligand_efficiency_component"]
        + 0.20 * result["lipinski_component"]
        + 0.15 * result["veber_component"]
    )

    return result
