from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.fuel_prediction import FuelPrediction
from app.schemas.fuel_prediction import FuelPredictionResponse


router = APIRouter(
    prefix="/fuel-predictions",
    tags=["Fuel Predictions"]
)


@router.get("/", response_model=list[FuelPredictionResponse])
def get_fuel_predictions(db: Session = Depends(get_db)):
    predictions = db.query(FuelPrediction).all()
    return predictions