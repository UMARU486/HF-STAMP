from __future__ import annotations

import csv
from pathlib import Path

from .schema import AnalysisResult


def _to_csv(rows: list[dict], path: Path) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return

    fieldnames = sorted({k for row in rows for k in row.keys()})
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def render_markdown(result: AnalysisResult) -> str:
    pm = result.process_model
    lines = [
        "# STPA/HFMEA MVP Result",
        "",
        "## Process Model",
        f"- Actors: {len(pm.actors)}",
        f"- Steps: {len(pm.steps)}",
        f"- Artifacts: {len(pm.artifacts)}",
        f"- Handoffs: {len(pm.handoffs)}",
        "",
        "## Risk Objects",
        f"- Hazards: {len(result.hazards)}",
        f"- UCAs: {len(result.ucas)}",
        f"- Control Flaws: {len(result.control_flaws)}",
        f"- Constraints: {len(result.constraints)}",
        "",
    ]
    return "\n".join(lines)


def export_outputs(result: AnalysisResult, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "hazards.csv": [x.model_dump() for x in result.hazards],
        "stpa_uca.csv": [x.model_dump() for x in result.ucas],
        "constraints.csv": [x.model_dump() for x in result.constraints],
    }

    generated: list[Path] = []
    for file_name, rows in outputs.items():
        p = out_dir / file_name
        _to_csv(rows, p)
        generated.append(p)

    md_file = out_dir / "summary.md"
    md_file.write_text(render_markdown(result), encoding="utf-8")
    generated.append(md_file)

    return generated
