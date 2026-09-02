from fastapi import APIRouter

from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.prediction_service import predict_fuel

router = APIRouter(
    prefix="/fuel",
    tags=["Fuel Prediction"]
)

@router.post("/predict", response_model=PredictionResponse)
def predict_fuel_endpoint(data: PredictionRequest):
    result = predict_fuel(data)
    return result