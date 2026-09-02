from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class FuelPredictionResponse(BaseModel):
    prediction_id: int
    vessel_id: str
    timestamp: datetime
    actual_fuel_consumption: Decimal
    predicted_fuel_consumption: Decimal
    model_version: str

    model_config = ConfigDict(from_attributes=True)