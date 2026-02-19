from __future__ import annotations

from pathlib import Path

from .extract import extract_actors, extract_artifacts, extract_handoff_points, extract_steps
from .schema import AnalysisResult


def analyze_text(text: str, source_file: Path) -> AnalysisResult:
    return AnalysisResult(
        source_file=source_file,
        actors=extract_actors(text),
        steps=extract_steps(text),
        artifacts=extract_artifacts(text),
        handoff_points=extract_handoff_points(text),
        hazards=[],
        ucas=[],
        control_defects=[],
        constraints_mitigations=[],
    )
