import argparse
from pathlib import Path

from drugdiscovery.descriptors.smiles_basic import add_basic_smiles_descriptors
from drugdiscovery.io.csv_loader import load_library
from drugdiscovery.io.docking_scores import load_docking_scores
from drugdiscovery.prepare.excel_library import prepare_library_from_excel
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
    rank_parser.add_argument("--ligands", required=True)
    rank_parser.add_argument("--docking", required=False)
    rank_parser.add_argument("--output", required=True)
    rank_parser.add_argument(
        "--estimate-basic-descriptors",
        action="store_true",
        help="Fill missing HBD, HBA, TPSA, and rotatable-bond values using approximate SMILES estimators.",
    )

    prepare_parser = subparsers.add_parser(
        "prepare-library",
        help="Prepare a DrugDiscovery-Py ligand CSV from an Excel workbook.",
    )
    prepare_parser.add_argument("--input", required=True)
    prepare_parser.add_argument("--output", required=True)
    prepare_parser.add_argument("--sheet", default=0)
    prepare_parser.add_argument("--id-column", default="compoundID")
    prepare_parser.add_argument("--smiles-column", default="Smiles")
    prepare_parser.add_argument("--mw-column", default="MW")

    return parser


def run_rank(args: argparse.Namespace) -> None:
    library = load_library(args.ligands)

    if args.estimate_basic_descriptors:
        library = add_basic_smiles_descriptors(library)

    docking_scores = None
    if args.docking:
        docking_scores = load_docking_scores(args.docking)

    ranked = rank_hits(library, docking_scores=docking_scores)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ranked.to_csv(output_path, index=False)

    print(f"Ranked {len(ranked)} compounds.")
    print(f"Output written to: {output_path}")


def run_prepare_library(args: argparse.Namespace) -> None:
    prepared = prepare_library_from_excel(
        input_path=args.input,
        output_path=args.output,
        id_column=args.id_column,
        smiles_column=args.smiles_column,
        mw_column=args.mw_column,
        sheet_name=args.sheet,
    )

    print(f"Prepared {len(prepared)} compounds.")
    print(f"Output written to: {args.output}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "rank":
        run_rank(args)
    elif args.command == "prepare-library":
        run_prepare_library(args)
    else:
        parser.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
