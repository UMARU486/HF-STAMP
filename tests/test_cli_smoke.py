from pathlib import Path

from stpa_tool.cli import main


def test_cli_analyze_smoke(tmp_path: Path) -> None:
    input_file = tmp_path / "input.md"
    input_file.write_text("synthetic text", encoding="utf-8")

    out_dir = tmp_path / "outputs"
    rc = main(["analyze", str(input_file), "--out", str(out_dir)])

    assert rc == 0
    assert (out_dir / "summary.md").exists()
    assert (out_dir / "actors.csv").exists()
