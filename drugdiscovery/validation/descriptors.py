import pandas as pd


REQUIRED_DESCRIPTOR_COLUMNS = [
    "molecular_weight",
    "hbd",
    "hba",
    "tpsa",
    "rotatable_bonds",
]


def descriptor_missing_summary(df: pd.DataFrame) -> pd.Series:
    """
    Return missing-value counts for descriptor columns required by ranking.
    """
    missing_columns = [
        column for column in REQUIRED_DESCRIPTOR_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            "Missing required descriptor columns: "
            f"{missing_columns}"
        )

    return df[REQUIRED_DESCRIPTOR_COLUMNS].isna().sum()


def validate_descriptors_for_ranking(df: pd.DataFrame) -> None:
    """
    Validate that required descriptor columns exist and contain no missing values.
    """
    summary = descriptor_missing_summary(df)
    missing = summary[summary > 0]

    if not missing.empty:
        message_lines = [
            "Missing descriptor values detected.",
            "Ranking cannot proceed until descriptor values are supplied or calculated.",
            "",
            "Missing values by descriptor:",
        ]

        for column, count in missing.items():
            message_lines.append(f"- {column}: {count} missing")

        raise ValueError("\n".join(message_lines))
