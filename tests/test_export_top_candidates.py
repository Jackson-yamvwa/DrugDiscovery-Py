import pandas as pd

from drugdiscovery.reports.export import export_top_candidates


def test_export_top_candidates_creates_top_n_file(tmp_path):
    input_path = tmp_path / "ranked.csv"
    output_path = tmp_path / "top.csv"

    df = pd.DataFrame({
        "compound_id": ["A", "B", "C"],
        "priority_score": [0.4, 0.9, 0.7],
        "molecular_weight": [300.0, 350.0, 400.0],
    })

    df.to_csv(input_path, index=False)

    top = export_top_candidates(input_path, output_path, top_n=2)

    assert output_path.exists()
    assert len(top) == 2
    assert list(top["compound_id"]) == ["B", "C"]
