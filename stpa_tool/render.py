from __future__ import annotations

import csv
from pathlib import Path

from .schema import AnalysisResult


def _to_csv(rows: list[dict], path: Path) -> None:
    try:
        import pandas as pd  # optional runtime helper

        pd.DataFrame(rows).to_csv(path, index=False, encoding="utf-8-sig")
        return
    except Exception:
        pass

    if not rows:
        path.write_text("", encoding="utf-8")
        return

    fieldnames = sorted({k for row in rows for k in row.keys()})
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def render_markdown(result: AnalysisResult) -> str:
    lines = [
        "# STPA/HFMEA MVP Result",
        "",
        f"- Source: `{result.source_file}`",
        "",
        "## Actors",
        "- (empty)" if not result.actors else "",
    ]
    if result.actors:
        lines.extend([f"- {x.actor_id}: {x.name}" for x in result.actors])
    lines.extend([
        "",
        "## Steps",
        "- (empty)" if not result.steps else "",
    ])
    if result.steps:
        lines.extend([f"- {x.step_id}: {x.text}" for x in result.steps])
    lines.extend([
        "",
        "## Hazards",
        "- (empty)" if not result.hazards else "",
    ])
    return "\n".join([x for x in lines if x != ""]) + "\n"


def export_outputs(result: AnalysisResult, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "actors.csv": [x.model_dump() for x in result.actors],
        "steps.csv": [x.model_dump() for x in result.steps],
        "artifacts.csv": [x.model_dump() for x in result.artifacts],
        "handoff_points.csv": [x.model_dump() for x in result.handoff_points],
        "hazards.csv": [x.model_dump() for x in result.hazards],
        "ucas.csv": [x.model_dump() for x in result.ucas],
        "control_defects.csv": [x.model_dump() for x in result.control_defects],
        "constraints_mitigations.csv": [x.model_dump() for x in result.constraints_mitigations],
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
