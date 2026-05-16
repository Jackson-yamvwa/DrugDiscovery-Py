import argparse
from pathlib import Path

from drugdiscovery.descriptors.smiles_basic import add_basic_smiles_descriptors
from drugdiscovery.io.csv_loader import load_library
from drugdiscovery.io.docking_scores import load_docking_scores
from drugdiscovery.prepare.excel_library import prepare_library_from_excel
from drugdiscovery.prioritization.ranker import rank_hits
from drugdiscovery.reports.export import export_top_candidates
from drugdiscovery.reports.summary import summarize_ranked_results


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

    summarize_parser = subparsers.add_parser(
        "summarize",
        help="Summarize a ranked DrugDiscovery-Py CSV output file.",
    )
    summarize_parser.add_argument("--input", required=True)
    summarize_parser.add_argument("--top", type=int, default=10)

    export_parser = subparsers.add_parser(
        "export-top",
        help="Export the top-ranked candidates from a ranked CSV file.",
    )
    export_parser.add_argument("--input", required=True)
    export_parser.add_argument("--output", required=True)
    export_parser.add_argument("--top", type=int, default=50)
    export_parser.add_argument("--sort-column", default="priority_score")

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


def run_summarize(args: argparse.Namespace) -> None:
    summary = summarize_ranked_results(args.input, top_n=args.top)
    print(summary)


def run_export_top(args: argparse.Namespace) -> None:
    top = export_top_candidates(
        input_path=args.input,
        output_path=args.output,
        top_n=args.top,
        sort_column=args.sort_column,
    )

    print(f"Exported {len(top)} top candidates.")
    print(f"Output written to: {args.output}")


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "rank":
        run_rank(args)
    elif args.command == "prepare-library":
        run_prepare_library(args)
    elif args.command == "summarize":
        run_summarize(args)
    elif args.command == "export-top":
        run_export_top(args)
    else:
        parser.error(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
