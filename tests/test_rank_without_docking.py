import pandas as pd

from drugdiscovery.prioritization.ranker import rank_hits


def test_rank_hits_works_without_docking_scores():
    df = pd.DataFrame({
        "compound_id": ["A", "B"],
        "smiles": ["CCO", "CCCCCCCCCCCCCCCCCCCC"],
        "molecular_weight": [46.07, 282.55],
        "hbd": [1, 0],
        "hba": [1, 0],
        "tpsa": [20.23, 0.00],
        "rotatable_bonds": [0, 15],
    })

    ranked = rank_hits(df)

    assert "priority_score" in ranked.columns
    assert "docking_component" in ranked.columns
    assert "ligand_efficiency_component" in ranked.columns
    assert ranked["priority_score"].notna().all()
    assert (ranked["docking_component"] == 0.0).all()
