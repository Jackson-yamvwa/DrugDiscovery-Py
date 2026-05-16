import pandas as pd


def apply_veber(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply a simple Veber-style oral bioavailability filter.

    Criteria:
    - TPSA <= 140 Å²
    - Rotatable bonds <= 10
    """
    result = df.copy()

    result["veber_tpsa_pass"] = result["tpsa"] <= 140
    result["veber_rotb_pass"] = result["rotatable_bonds"] <= 10
    result["veber_pass"] = result["veber_tpsa_pass"] & result["veber_rotb_pass"]

    return result
