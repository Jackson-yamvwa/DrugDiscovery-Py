from pathlib import Path

import pandas as pd


def export_top_candidates(
    input_path: str | Path,
    output_path: str | Path,
    top_n: int = 50,
    sort_column: str = "priority_score",
) -> pd.DataFrame:
    """
    Export the top-ranked candidates from a DrugDiscovery-Py ranked CSV file.
    """
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")

    df = pd.read_csv(input_path)

    required_columns = {"compound_id", sort_column}
    missing = required_columns.difference(df.columns)

    if missing:
        raise ValueError(f"Missing required export columns: {sorted(missing)}")

    top = df.sort_values(sort_column, ascending=False).head(top_n).copy()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    top.to_csv(output_path, index=False)

    return top
