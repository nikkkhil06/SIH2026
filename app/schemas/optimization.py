from pydantic import BaseModel, Field


class OptimizationRequest(BaseModel):
    cargo_demand: float = Field(gt=0)
    distance: float = Field(gt=0)
    max_time: float = Field(gt=0)
    objective: str