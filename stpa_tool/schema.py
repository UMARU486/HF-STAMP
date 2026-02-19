from __future__ import annotations

from pathlib import Path

try:
    from pydantic import BaseModel, Field
except Exception:  # fallback for restricted environments

    class BaseModel:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

        def model_dump(self) -> dict:
            return self.__dict__.copy()

    def Field(default_factory=list):  # type: ignore
        return default_factory()


class Actor(BaseModel):
    actor_id: str
    name: str


class Step(BaseModel):
    step_id: str
    text: str


class Artifact(BaseModel):
    artifact_id: str
    name: str


class HandoffPoint(BaseModel):
    handoff_id: str
    description: str


class Hazard(BaseModel):
    hazard_id: str
    description: str


class UnsafeControlAction(BaseModel):
    uca_id: str
    description: str


class ControlDefect(BaseModel):
    defect_id: str
    description: str


class ConstraintMitigation(BaseModel):
    cm_id: str
    constraint: str
    mitigation: str


class AnalysisResult(BaseModel):
    source_file: Path
    actors: list[Actor] = Field(default_factory=list)
    steps: list[Step] = Field(default_factory=list)
    artifacts: list[Artifact] = Field(default_factory=list)
    handoff_points: list[HandoffPoint] = Field(default_factory=list)
    hazards: list[Hazard] = Field(default_factory=list)
    ucas: list[UnsafeControlAction] = Field(default_factory=list)
    control_defects: list[ControlDefect] = Field(default_factory=list)
    constraints_mitigations: list[ConstraintMitigation] = Field(default_factory=list)
