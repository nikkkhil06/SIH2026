from sqlalchemy import Column, Integer, String, DateTime, Float

from app.database.connection import Base


class FuelPrediction(Base):
    __tablename__ = "fuel_prediction"

    prediction_id = Column(Integer, primary_key=True, index=True)
    vessel_id = Column(String)
    timestamp = Column(DateTime)
    actual_fuel_consumption = Column(Float)
    predicted_fuel_consumption = Column(Float)
    model_version = Column(String)