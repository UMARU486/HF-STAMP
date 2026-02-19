from __future__ import annotations

import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stpa_tool",
        description="STPA/HFMEA semi-automated analyzer (MVP)",
    )
    sub = parser.add_subparsers(dest="command")

    analyze_cmd = sub.add_parser("analyze", help="Analyze a markdown/text case")
    analyze_cmd.add_argument("input_file", type=Path, help="Input markdown/text file")
    analyze_cmd.add_argument("--out", "-o", type=Path, default=Path("outputs"), help="Output directory")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    if args.command == "analyze":
        from .analyze import analyze_text
        from .render import export_outputs
        from .utils import read_text

        text = read_text(args.input_file)
        result = analyze_text(text, args.input_file)
        files = export_outputs(result, args.out)
        print(f"Generated {len(files)} files")
        for f in files:
            print(f"- {f}")
        return 0

    parser.print_help()
    return 1
