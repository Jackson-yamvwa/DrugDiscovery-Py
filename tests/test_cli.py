import subprocess
import sys


def test_cli_rank_command_creates_output(tmp_path):
    output = tmp_path / "ranked.csv"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "drugdiscovery.cli",
            "rank",
            "--ligands",
            "examples/example_ligands.csv",
            "--docking",
            "examples/example_docking_scores.csv",
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert output.exists()
    assert "Ranked" in result.stdout
    assert "Output written to" in result.stdout
