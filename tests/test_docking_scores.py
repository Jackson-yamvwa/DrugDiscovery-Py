import pandas as pd

from drugdiscovery.io.docking_scores import (
    load_docking_scores,
    merge_docking_scores,
)


def test_load_docking_scores_reads_required_columns(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text(
        "compound_id,docking_score\n"
        "A,-7.1\n"
        "B,-6.4\n"
    )

    df = load_docking_scores(path)

    assert list(df.columns) == ["compound_id", "docking_score"]
    assert len(df) == 2


def test_merge_docking_scores_replaces_existing_score():
    library = pd.DataFrame({
        "compound_id": ["A", "B"],
        "smiles": ["CCO", "c1ccccc1"],
        "molecular_weight": [46.07, 78.11],
        "hbd": [1, 0],
        "hba": [1, 0],
        "tpsa": [20.23, 0.00],
        "rotatable_bonds": [0, 0],
        "docking_score": [-1.0, -1.0],
    })

    scores = pd.DataFrame({
        "compound_id": ["A", "B"],
        "docking_score": [-7.1, -6.4],
    })

    merged = merge_docking_scores(library, scores)

    assert merged.loc[merged["compound_id"] == "A", "docking_score"].iloc[0] == -7.1
    assert merged.loc[merged["compound_id"] == "B", "docking_score"].iloc[0] == -6.4
