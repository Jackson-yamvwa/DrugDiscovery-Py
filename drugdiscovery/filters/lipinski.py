import pandas as pd


def apply_lipinski(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply Lipinski rule-of-five checks.

    Criteria:
    - Molecular weight <= 500
    - HBD <= 5
    - HBA <= 10
    """
    result = df.copy()

    result["lipinski_mw_pass"] = result["molecular_weight"] <= 500
    result["lipinski_hbd_pass"] = result["hbd"] <= 5
    result["lipinski_hba_pass"] = result["hba"] <= 10

    pass_columns = [
        "lipinski_mw_pass",
        "lipinski_hbd_pass",
        "lipinski_hba_pass",
    ]

    result["lipinski_violations"] = (~result[pass_columns]).sum(axis=1)
    result["lipinski_pass"] = result["lipinski_violations"] <= 1

    return result
