import pandas as pd

from drugdiscovery.descriptors.smiles_basic import (
    add_basic_smiles_descriptors,
    calculate_basic_smiles_descriptors,
)


def test_calculate_basic_smiles_descriptors_returns_values():
    descriptors = calculate_basic_smiles_descriptors("CCO")

    assert descriptors.hbd >= 0
    assert descriptors.hba >= 1
    assert descriptors.tpsa > 0
    assert descriptors.rotatable_bonds >= 0


def test_add_basic_smiles_descriptors_fills_missing_values():
    df = pd.DataFrame({
        "compound_id": ["A"],
        "smiles": ["CCO"],
        "molecular_weight": [46.07],
        "hbd": [None],
        "hba": [None],
        "tpsa": [None],
        "rotatable_bonds": [None],
    })

    result = add_basic_smiles_descriptors(df)

    assert result["hbd"].notna().all()
    assert result["hba"].notna().all()
    assert result["tpsa"].notna().all()
    assert result["rotatable_bonds"].notna().all()


def test_add_basic_smiles_descriptors_preserves_existing_values():
    df = pd.DataFrame({
        "compound_id": ["A"],
        "smiles": ["CCO"],
        "molecular_weight": [46.07],
        "hbd": [9],
        "hba": [8],
        "tpsa": [7.0],
        "rotatable_bonds": [6],
    })

    result = add_basic_smiles_descriptors(df)

    assert result.loc[0, "hbd"] == 9
    assert result.loc[0, "hba"] == 8
    assert result.loc[0, "tpsa"] == 7.0
    assert result.loc[0, "rotatable_bonds"] == 6
