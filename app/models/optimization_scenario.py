from sqlalchemy import Column, String, Numeric, DateTime

from app.database.connection import Base


class OptimizationScenario(Base):
    __tablename__ = "optimization_scenarios"

    scenario_id = Column(String, primary_key=True, index=True)
    cargo_demand = Column(Numeric)
    distance = Column(Numeric)
    max_time = Column(Numeric)
    objective = Column(String)
    created_at = Column(DateTime)