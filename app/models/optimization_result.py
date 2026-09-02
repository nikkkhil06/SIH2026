from sqlalchemy import Column, String, Numeric, Boolean, ForeignKey

from app.database.connection import Base


class OptimizationResult(Base):
    __tablename__ = "optimization_results"

    result_id = Column(String, primary_key=True, index=True)
    scenario_id = Column(
        String,
        ForeignKey("optimization_scenarios.scenario_id"),
        nullable=False
    )
    vessel_id = Column(
        String,
        ForeignKey("vessels.vessel_id"),
        nullable=False
    )
    fuel_type = Column(
        String,
        ForeignKey("fuel_types.fuel_id"),
        nullable=False
    )
    recommended_speed = Column(Numeric, nullable=False)
    predicted_fuel = Column(Numeric, nullable=False)
    estimated_cost = Column(Numeric, nullable=False)
    estimated_emissions = Column(Numeric, nullable=False)
    cargo_satisfied = Column(Boolean, nullable=False)
    schedule_satisfied = Column(Boolean, nullable=False)