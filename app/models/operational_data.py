from sqlalchemy import Column, Integer, String, DateTime, Float

from app.database.connection import Base


class OperationalData(Base):
    __tablename__ = "operational_data"

    operation_id = Column(Integer, primary_key=True, index=True)
    vessel_id = Column(String)
    timestamp = Column(DateTime)
    ship_speed_through_water = Column(Float)