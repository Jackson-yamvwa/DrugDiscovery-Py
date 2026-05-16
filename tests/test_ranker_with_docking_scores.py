import pandas as pd

from drugdiscovery.prioritization.ranker import rank_hits


def test_rank_hits_accepts_external_docking_scores():
    library = pd.DataFrame({
        "compound_id": ["A", "B"],
        "smiles": ["CCO", "c1ccccc1"],
        "molecular_weight": [46.07, 78.11],
        "hbd": [1, 0],
        "hba": [1, 0],
        "tpsa": [20.23, 0.00],
        "rotatable_bonds": [0, 0],
    })

    docking_scores = pd.DataFrame({
        "compound_id": ["A", "B"],
        "docking_score": [-4.2, -5.0],
    })

    ranked = rank_hits(library, docking_scores=docking_scores)

    assert "docking_score" in ranked.columns
    assert "priority_score" in ranked.columns
    assert len(ranked) == 2
    assert ranked["priority_score"].notna().all()
