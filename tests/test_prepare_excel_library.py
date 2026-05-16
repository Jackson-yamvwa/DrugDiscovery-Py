import pandas as pd

from drugdiscovery.prepare.excel_library import prepare_library_from_excel


def test_prepare_library_from_excel_creates_expected_columns(tmp_path):
    input_path = tmp_path / "library.xlsx"
    output_path = tmp_path / "prepared.csv"

    df = pd.DataFrame({
        "compoundID": ["CMPD1", "CMPD2"],
        "Smiles": ["CCO", "c1ccccc1"],
        "MW": [46.07, 78.11],
    })

    df.to_excel(input_path, index=False)

    prepared = prepare_library_from_excel(input_path, output_path)

    expected_columns = [
        "compound_id",
        "smiles",
        "molecular_weight",
        "hbd",
        "hba",
        "tpsa",
        "rotatable_bonds",
    ]

    assert output_path.exists()
    assert list(prepared.columns) == expected_columns
    assert len(prepared) == 2
