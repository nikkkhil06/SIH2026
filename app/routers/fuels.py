from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.fuel_types import FuelType
from app.schemas.fuel import FuelResponse


router = APIRouter(
    prefix="/fuel-types",
    tags=["Fuel Types"]
)


@router.get("/", response_model=list[FuelResponse])
def get_fuel_types(db: Session = Depends(get_db)):
    return db.query(FuelType).all()