from pydantic import BaseModel


class VesselResponse(BaseModel):
    vessel_id: str
    vessel_name: str | None = None
    vessel_category: str | None = None
    capacity: float | None = None
    engine_power: float | None = None
    max_speed: float | None = None
    fuel_type: str | None = None
    status: str | None = None

    class Config:
        from_attributes = True