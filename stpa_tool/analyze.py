from __future__ import annotations

from .extract import extract_process_model
from .schema import AnalysisResult


def analyze_text(text: str) -> AnalysisResult:
    return AnalysisResult(
        process_model=extract_process_model(text),
        hazards=[],
        ucas=[],
        control_flaws=[],
        constraints=[],
    )
