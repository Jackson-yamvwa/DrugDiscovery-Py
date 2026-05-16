import pandas as pd
import pytest

from drugdiscovery.validation.descriptors import (
    descriptor_missing_summary,
    validate_descriptors_for_ranking,
)
from drugdiscovery.prioritization.ranker import rank_hits


def test_descriptor_missing_summary_counts_missing_values():
    df = pd.DataFrame({
        "molecular_weight": [46.07, 78.11],
        "hbd": [1, None],
        "hba": [1, None],
        "tpsa": [20.23, None],
        "rotatable_bonds": [0, None],
    })

    summary = descriptor_missing_summary(df)

    assert summary["hbd"] == 1
    assert summary["hba"] == 1
    assert summary["tpsa"] == 1
    assert summary["rotatable_bonds"] == 1


def test_validate_descriptors_raises_for_missing_values():
    df = pd.DataFrame({
        "compound_id": ["A"],
        "smiles": ["CCO"],
        "molecular_weight": [46.07],
        "hbd": [None],
        "hba": [None],
        "tpsa": [None],
        "rotatable_bonds": [None],
        "docking_score": [-4.2],
    })

    with pytest.raises(ValueError, match="Missing descriptor values detected"):
        validate_descriptors_for_ranking(df)


def test_rank_hits_stops_when_descriptors_are_missing():
    df = pd.DataFrame({
        "compound_id": ["A"],
        "smiles": ["CCO"],
        "molecular_weight": [46.07],
        "hbd": [None],
        "hba": [None],
        "tpsa": [None],
        "rotatable_bonds": [None],
        "docking_score": [-4.2],
    })

    with pytest.raises(ValueError, match="Ranking cannot proceed"):
        rank_hits(df)
