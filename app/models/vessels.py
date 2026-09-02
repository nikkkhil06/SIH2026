from sqlalchemy import Column, String, Numeric

from app.database.connection import Base


class Vessel(Base):
    __tablename__ = "vessels"

    vessel_id = Column(String, primary_key=True, index=True)
    vessel_name = Column(String)
    capacity = Column(Numeric)
    engine_power = Column(Numeric)
    fuel_type = Column(String)