from sqlalchemy import Column, Integer, String, DateTime, Float

from app.database.connection import Base


class EnvironmentalData(Base):
    __tablename__ = "environmental_data_table"

    environment_id = Column(Integer, primary_key=True, index=True)
    vessel_id = Column(String)
    timestamp = Column(DateTime)

    air_temperature = Column(Float)
    sea_floor_depth = Column(Float)
    wave_height = Column(Float)
    wind_speed = Column(Float)
    wave_period = Column(Float)
    ocean_current_velocity = Column(Float)