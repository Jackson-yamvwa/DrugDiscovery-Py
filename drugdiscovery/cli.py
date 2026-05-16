import argparse
from pathlib import Path

from drugdiscovery.io.csv_loader import load_library
from drugdiscovery.io.docking_scores import load_docking_scores
from drugdiscovery.prioritization.ranker import rank_hits


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="drugdiscovery",
        description="DrugDiscovery-Py command-line interface.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    rank_parser = subparsers.add_parser(
        "rank",
        help="Rank compounds using descriptors, docking scores, and drug-likeness filters.",
    )
    rank_parser.add_argument(
        "--ligands",
        required=True,
        help="Path to ligand library CSV file.",
    )
    rank_parser.add_argument(
        "--docking",
        required=False,
        help="Optional path to docking-score CSV file.",
    )
    rank_parser.add_argument(
        "--output",
        required=True,
        help="Path to output ranked CSV file.",
    )

    return parser


def run_rank(args: argparse.Namespace) -> None:
    library = load_library(args.ligands)

    docking_scores = None
    if args.docking:
        docking_scores = load_docking_scores(args.docking)

    ranked = rank_hits(library, docking_scores=docking_scores)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ranked.to_csv(output_path, index=False)

    print(f"Ranked {len(ranked)} compounds.")
    print(f"Output written to: {output_path}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "rank":
        run_rank(args)
    else:
        parser.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
