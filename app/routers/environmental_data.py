from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.environmental_data import EnvironmentalData
from app.schemas.environmental_data import EnvironmentalDataResponse


router = APIRouter(
    prefix="/environmental-data",
    tags=["Environmental Data"]
)


@router.get("/", response_model=list[EnvironmentalDataResponse])
def get_environmental_data(db: Session = Depends(get_db)):
    data = db.query(EnvironmentalData).all()
    return data