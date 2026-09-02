from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    ship_speed_through_water: float = Field(gt=0)
    sea_floor_depth: float = Field(ge=0)
    air_temperature: float
    wind_speed: float = Field(ge=0)
    wave_height: float = Field(ge=0)
    wave_period: float = Field(gt=0)
    ocean_current_velocity: float

class PredictionResponse(BaseModel):
    predicted_fuel: float
    fuel_unit: str