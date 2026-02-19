from stpa_tool.extract import (
    extract_actors,
    extract_artifacts,
    extract_handoff_points,
    extract_steps,
)


def test_extract_stub_returns_empty_lists() -> None:
    text = "synthetic case"
    assert extract_actors(text) == []
    assert extract_steps(text) == []
    assert extract_artifacts(text) == []
    assert extract_handoff_points(text) == []
