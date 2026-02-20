from stpa_tool.extract import extract_process_model


def test_extract_stub_returns_empty_process_model() -> None:
    model = extract_process_model("synthetic case")
    assert model.actors == []
    assert model.steps == []
    assert model.artifacts == []
    assert model.handoffs == []
