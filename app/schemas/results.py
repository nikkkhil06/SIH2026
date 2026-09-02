from pydantic import BaseModel


class OptimizationResultResponse(BaseModel):
    result_id: str
    scenario_id: str
    vessel_id: str
    fuel_type: str
    recommended_speed: float
    predicted_fuel: float
    estimated_cost: float
    estimated_emissions: float
    cargo_satisfied: bool
    schedule_satisfied: bool