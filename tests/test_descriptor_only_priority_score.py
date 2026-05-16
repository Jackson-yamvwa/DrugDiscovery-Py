import pandas as pd

from drugdiscovery.prioritization.ranker import rank_hits


def test_descriptor_only_priority_scores_can_differ_without_docking():
    df = pd.DataFrame({
        "compound_id": ["A", "B", "C"],
        "smiles": ["CCO", "CCCCCCCCCCCCCCCCCCCC", "c1ccccc1N"],
        "molecular_weight": [320.0, 650.0, 180.0],
        "hbd": [1, 0, 1],
        "hba": [3, 0, 1],
        "tpsa": [65.0, 0.0, 26.0],
        "rotatable_bonds": [4, 15, 1],
    })

    ranked = rank_hits(df)

    assert "descriptor_desirability_component" in ranked.columns
    assert "priority_score" in ranked.columns
    assert ranked["priority_score"].nunique() > 1
    assert ranked.iloc[0]["compound_id"] == "A"


def test_descriptor_desirability_components_are_present():
    df = pd.DataFrame({
        "compound_id": ["A"],
        "smiles": ["CCO"],
        "molecular_weight": [320.0],
        "hbd": [1],
        "hba": [3],
        "tpsa": [65.0],
        "rotatable_bonds": [4],
    })

    ranked = rank_hits(df)

    expected_columns = [
        "mw_desirability",
        "tpsa_desirability",
        "rotb_desirability",
        "hbd_desirability",
        "hba_desirability",
        "descriptor_desirability_component",
    ]

    for column in expected_columns:
        assert column in ranked.columns
