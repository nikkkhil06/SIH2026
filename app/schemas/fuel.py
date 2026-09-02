from pydantic import BaseModel


class FuelResponse(BaseModel):
    fuel_id: str
    fuel_name: str | None = None
    emission_factor: float | None = None
    cost_per_unit: float | None = None

    class Config:
        from_attributes = True