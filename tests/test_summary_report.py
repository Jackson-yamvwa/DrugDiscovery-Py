import pandas as pd

from drugdiscovery.reports.summary import summarize_ranked_results


def test_summarize_ranked_results_outputs_expected_sections(tmp_path):
    path = tmp_path / "ranked.csv"

    df = pd.DataFrame({
        "compound_id": ["A", "B"],
        "priority_score": [0.9, 0.5],
        "molecular_weight": [320.0, 450.0],
        "hbd": [1, 2],
        "hba": [3, 5],
        "tpsa": [65.0, 90.0],
        "rotatable_bonds": [4, 7],
        "lipinski_pass": [True, True],
        "veber_pass": [True, False],
    })

    df.to_csv(path, index=False)

    summary = summarize_ranked_results(path, top_n=1)

    assert "DrugDiscovery-Py Ranking Summary" in summary
    assert "Compounds ranked: 2" in summary
    assert "Unique priority scores: 2" in summary
    assert "Lipinski pass: 2/2" in summary
    assert "Veber pass:    1/2" in summary
    assert "Top 1 compounds" in summary
    assert "A" in summary
