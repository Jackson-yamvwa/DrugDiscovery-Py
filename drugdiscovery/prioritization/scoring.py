import pandas as pd


def add_ligand_efficiency(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate ligand efficiency when docking scores are available.

    Ligand efficiency is approximated as:

        LE = -docking_score / heavy_atom_count

    If heavy_atom_count is absent, molecular_weight / 14 is used as a rough
    fallback for Version 0.1.

    If docking_score is absent, ligand_efficiency is set to NA.
    """
    result = df.copy()

    if "heavy_atom_count" not in result.columns:
        result["heavy_atom_count"] = (result["molecular_weight"] / 14).round()

    if "docking_score" in result.columns:
        result["ligand_efficiency"] = (
            -result["docking_score"] / result["heavy_atom_count"]
        )
    else:
        result["ligand_efficiency"] = pd.NA

    return result


def _normalise_lower_is_better(series: pd.Series) -> pd.Series:
    """
    Normalise a numeric series where lower values are better.
    """
    values = pd.to_numeric(series, errors="coerce")

    if values.isna().all():
        return pd.Series(0.0, index=series.index)

    min_value = values.min()
    max_value = values.max()

    if min_value == max_value:
        return pd.Series(1.0, index=series.index)

    return (max_value - values) / (max_value - min_value)


def _normalise_higher_is_better(series: pd.Series) -> pd.Series:
    """
    Normalise a numeric series where higher values are better.
    """
    values = pd.to_numeric(series, errors="coerce")

    if values.isna().all():
        return pd.Series(0.0, index=series.index)

    min_value = values.min()
    max_value = values.max()

    if min_value == max_value:
        return pd.Series(1.0, index=series.index)

    return (values - min_value) / (max_value - min_value)


def add_priority_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a weighted priority score.

    If docking scores are available, the score rewards:
    - stronger docking score
    - higher ligand efficiency
    - Lipinski pass
    - Veber pass

    If docking scores are absent, docking and ligand-efficiency components are
    set to zero, allowing descriptor-only ranking based on Lipinski and Veber
    filters.
    """
    result = df.copy()

    if "docking_score" in result.columns:
        result["docking_component"] = _normalise_lower_is_better(
            result["docking_score"]
        )
    else:
        result["docking_component"] = 0.0

    if "ligand_efficiency" not in result.columns:
        result = add_ligand_efficiency(result)

    result["ligand_efficiency_component"] = _normalise_higher_is_better(
        result["ligand_efficiency"]
    )

    result["lipinski_component"] = result.get("lipinski_pass", False).astype(float)
    result["veber_component"] = result.get("veber_pass", False).astype(float)

    result["priority_score"] = (
        0.40 * result["docking_component"]
        + 0.25 * result["ligand_efficiency_component"]
        + 0.20 * result["lipinski_component"]
        + 0.15 * result["veber_component"]
    )

    return result
