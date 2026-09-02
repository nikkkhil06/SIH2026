from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.vessels import Vessel
from app.schemas.vessels import VesselResponse


router = APIRouter(
    prefix="/vessels",
    tags=["Vessels"]
)


@router.get("/", response_model=list[VesselResponse])
def get_vessels(db: Session = Depends(get_db)):

    return db.query(Vessel).all()     