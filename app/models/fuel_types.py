from sqlalchemy import Column, String, Numeric

from app.database.connection import Base


class FuelType(Base):
    __tablename__ = "fuel_types"

    fuel_id = Column(String, primary_key=True, index=True)
    fuel_name = Column(String)
    emission_factor = Column(Numeric)
    cost_per_unit = Column(Numeric)