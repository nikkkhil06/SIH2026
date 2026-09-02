from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class OperationalDataResponse(BaseModel):
    operation_id: int
    vessel_id: str
    timestamp: datetime
    ship_speed_through_water: Decimal

    model_config = ConfigDict(from_attributes=True)