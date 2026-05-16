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
    values = pd.to_numeric(series, errors="coerce")

    if values.isna().all():
        return pd.Series(0.0, index=series.index)

    min_value = values.min()
    max_value = values.max()

    if min_value == max_value:
        return pd.Series(1.0, index=series.index)

    return (max_value - values) / (max_value - min_value)


def _normalise_higher_is_better(series: pd.Series) -> pd.Series:
    values = pd.to_numeric(series, errors="coerce")

    if values.isna().all():
        return pd.Series(0.0, index=series.index)

    min_value = values.min()
    max_value = values.max()

    if min_value == max_value:
        return pd.Series(1.0, index=series.index)

    return (values - min_value) / (max_value - min_value)


def _range_desirability(
    series: pd.Series,
    lower: float,
    upper: float,
    ideal_lower: float,
    ideal_upper: float,
) -> pd.Series:
    """
    Convert a numeric descriptor into a 0-1 desirability score.

    - Values inside the ideal range score 1.0.
    - Values outside the broad acceptable range score 0.0.
    - Values between broad and ideal limits are linearly scaled.
    """
    values = pd.to_numeric(series, errors="coerce")
    score = pd.Series(0.0, index=series.index)

    ideal_mask = (values >= ideal_lower) & (values <= ideal_upper)
    score.loc[ideal_mask] = 1.0

    lower_slope = (values >= lower) & (values < ideal_lower)
    if ideal_lower != lower:
        score.loc[lower_slope] = (
            (values.loc[lower_slope] - lower) / (ideal_lower - lower)
        )

    upper_slope = (values > ideal_upper) & (values <= upper)
    if upper != ideal_upper:
        score.loc[upper_slope] = (
            (upper - values.loc[upper_slope]) / (upper - ideal_upper)
        )

    return score.clip(0.0, 1.0)


def add_descriptor_desirability_components(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add descriptor desirability components for descriptor-only prioritisation.

    These components are heuristic and intended for early-stage triage, not as
    validated medicinal chemistry decision rules.
    """
    result = df.copy()

    result["mw_desirability"] = _range_desirability(
        result["molecular_weight"],
        lower=150,
        upper=500,
        ideal_lower=250,
        ideal_upper=450,
    )

    result["tpsa_desirability"] = _range_desirability(
        result["tpsa"],
        lower=20,
        upper=140,
        ideal_lower=40,
        ideal_upper=100,
    )

    result["rotb_desirability"] = _range_desirability(
        result["rotatable_bonds"],
        lower=0,
        upper=10,
        ideal_lower=0,
        ideal_upper=6,
    )

    result["hbd_desirability"] = _range_desirability(
        result["hbd"],
        lower=0,
        upper=5,
        ideal_lower=0,
        ideal_upper=3,
    )

    result["hba_desirability"] = _range_desirability(
        result["hba"],
        lower=0,
        upper=10,
        ideal_lower=1,
        ideal_upper=8,
    )

    result["descriptor_desirability_component"] = (
        0.30 * result["mw_desirability"]
        + 0.25 * result["tpsa_desirability"]
        + 0.20 * result["rotb_desirability"]
        + 0.125 * result["hbd_desirability"]
        + 0.125 * result["hba_desirability"]
    )

    return result


def add_priority_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a weighted priority score.

    If docking scores are available, the score rewards:
    - stronger docking score
    - higher ligand efficiency
    - descriptor desirability
    - Lipinski pass
    - Veber pass

    If docking scores are absent, ranking uses:
    - descriptor desirability
    - Lipinski pass
    - Veber pass
    """
    result = df.copy()

    result = add_descriptor_desirability_components(result)

    has_docking = "docking_score" in result.columns

    if has_docking:
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

    if has_docking:
        result["priority_score"] = (
            0.35 * result["docking_component"]
            + 0.20 * result["ligand_efficiency_component"]
            + 0.20 * result["descriptor_desirability_component"]
            + 0.15 * result["lipinski_component"]
            + 0.10 * result["veber_component"]
        )
    else:
        result["priority_score"] = (
            0.50 * result["descriptor_desirability_component"]
            + 0.30 * result["lipinski_component"]
            + 0.20 * result["veber_component"]
        )

    return result
