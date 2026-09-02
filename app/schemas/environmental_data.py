from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class EnvironmentalDataResponse(BaseModel):
    environment_id: int
    vessel_id: str
    timestamp: datetime
    air_temperature: Decimal
    sea_floor_depth: Decimal
    wave_height: Decimal
    wind_speed: Decimal
    wave_period: Decimal
    ocean_current_velocity: Decimal

    model_config = ConfigDict(from_attributes=True)