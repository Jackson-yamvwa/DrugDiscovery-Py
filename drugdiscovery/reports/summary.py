from pathlib import Path

import pandas as pd


def summarize_ranked_results(path: str | Path, top_n: int = 10) -> str:
    """
    Summarize a ranked DrugDiscovery-Py CSV output file.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)

    required_columns = {"compound_id", "priority_score"}
    missing = required_columns.difference(df.columns)

    if missing:
        raise ValueError(f"Missing required summary columns: {sorted(missing)}")

    lines = []
    lines.append("DrugDiscovery-Py Ranking Summary")
    lines.append("=" * 36)
    lines.append(f"Input file: {path}")
    lines.append(f"Compounds ranked: {len(df)}")
    lines.append(f"Unique priority scores: {df['priority_score'].nunique()}")

    lines.append("")
    lines.append("Priority score statistics")
    lines.append("-" * 36)
    lines.append(f"Minimum: {df['priority_score'].min():.4f}")
    lines.append(f"Mean:    {df['priority_score'].mean():.4f}")
    lines.append(f"Median:  {df['priority_score'].median():.4f}")
    lines.append(f"Maximum: {df['priority_score'].max():.4f}")

    if "lipinski_pass" in df.columns:
        lipinski_count = int(df["lipinski_pass"].sum())
        lines.append("")
        lines.append("Drug-likeness filters")
        lines.append("-" * 36)
        lines.append(
            f"Lipinski pass: {lipinski_count}/{len(df)} "
            f"({lipinski_count / len(df) * 100:.1f}%)"
        )

    if "veber_pass" in df.columns:
        veber_count = int(df["veber_pass"].sum())
        if "Drug-likeness filters" not in "\n".join(lines[-3:]):
            lines.append("")
            lines.append("Drug-likeness filters")
            lines.append("-" * 36)
        lines.append(
            f"Veber pass:    {veber_count}/{len(df)} "
            f"({veber_count / len(df) * 100:.1f}%)"
        )

    top = df.sort_values("priority_score", ascending=False).head(top_n)

    lines.append("")
    lines.append(f"Top {min(top_n, len(top))} compounds")
    lines.append("-" * 36)

    display_columns = [
        column for column in [
            "compound_id",
            "priority_score",
            "molecular_weight",
            "hbd",
            "hba",
            "tpsa",
            "rotatable_bonds",
        ]
        if column in top.columns
    ]

    lines.append(top[display_columns].to_string(index=False))

    return "\n".join(lines)
