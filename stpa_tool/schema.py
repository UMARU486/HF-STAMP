from __future__ import annotations

from pydantic import BaseModel, Field


class ProcessModel(BaseModel):
    actors: list[str] = Field(default_factory=list)
    steps: list[str] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)
    handoffs: list[str] = Field(default_factory=list)


class Hazard(BaseModel):
    id: str
    description: str
    severity: int = Field(ge=1, le=5)
    likelihood: int = Field(ge=1, le=5)
    detectability: int = Field(ge=1, le=5)
    rpn: int
    related_steps: list[str] = Field(default_factory=list)


class UnsafeControlAction(BaseModel):
    id: str
    controller: str
    control_action: str
    context: str
    hazard_ids: list[str] = Field(default_factory=list)
    type: str = Field(pattern=r"^(not_provided|provided_wrong|too_early_too_late|too_long_too_short)$")


class ControlFlaw(BaseModel):
    id: str
    category: str = Field(
        pattern=r"^(feedback_missing|model_incorrect|interface_ambiguous|procedure_gap|training_gap|overload)$"
    )
    description: str
    linked_uca_ids: list[str] = Field(default_factory=list)


class Constraint(BaseModel):
    id: str
    description: str
    enforcement: str = Field(pattern=r"^(checklist|ui_constraint|double_check|automation|role_clarity)$")
    linked_hazard_ids: list[str] = Field(default_factory=list)


class AnalysisResult(BaseModel):
    process_model: ProcessModel
    hazards: list[Hazard] = Field(default_factory=list)
    ucas: list[UnsafeControlAction] = Field(default_factory=list)
    control_flaws: list[ControlFlaw] = Field(default_factory=list)
    constraints: list[Constraint] = Field(default_factory=list)
