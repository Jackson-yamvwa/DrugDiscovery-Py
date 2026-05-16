from pathlib import Path

import pandas as pd


REQUIRED_DOCKING_COLUMNS = {
    "compound_id",
    "docking_score",
}


def load_docking_scores(path: str | Path) -> pd.DataFrame:
    """
    Load docking scores from a CSV file.

    Required columns:
    - compound_id
    - docking_score

    Optional columns may include:
    - docking_program
    - pose_id
    - binding_mode
    - target_id
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)

    missing = REQUIRED_DOCKING_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required docking columns: {sorted(missing)}")

    return df


def merge_docking_scores(
    library: pd.DataFrame,
    docking_scores: pd.DataFrame,
    on: str = "compound_id",
) -> pd.DataFrame:
    """
    Merge docking scores into a compound library table.

    If the library already contains a docking_score column, the external docking
    score table takes priority.
    """
    if on not in library.columns:
        raise ValueError(f"Library is missing merge column: {on}")

    if on not in docking_scores.columns:
        raise ValueError(f"Docking score table is missing merge column: {on}")

    result = library.copy()

    if "docking_score" in result.columns:
        result = result.drop(columns=["docking_score"])

    merged = result.merge(docking_scores, on=on, how="left")

    if merged["docking_score"].isna().any():
        missing_ids = merged.loc[merged["docking_score"].isna(), on].tolist()
        raise ValueError(
            "Missing docking scores for compound IDs: "
            f"{missing_ids}"
        )

    return merged
