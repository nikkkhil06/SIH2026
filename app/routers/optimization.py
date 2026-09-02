from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import uuid

from app.database.dependencies import get_db
from app.models.optimization_scenario import OptimizationScenario
from app.schemas.optimization import OptimizationRequest


router = APIRouter(
    prefix="/optimization",
    tags=["Optimization"]
)


@router.post("/")
def create_optimization(
    data: OptimizationRequest,
    db: Session = Depends(get_db)
):
    scenario_id = f"S{uuid.uuid4().hex[:8].upper()}"

    scenario = OptimizationScenario(
        scenario_id=scenario_id,
        cargo_demand=data.cargo_demand,
        distance=data.distance,
        max_time=data.max_time,
        objective=data.objective,
        created_at=datetime.utcnow()
    )

    db.add(scenario)
    db.commit()
    db.refresh(scenario)

    return {
        "scenario_id": scenario.scenario_id,
        "message": "Optimization scenario created successfully",
        "status": "pending"
    }