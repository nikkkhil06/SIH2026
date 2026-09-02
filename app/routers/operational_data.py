from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.operational_data import OperationalData
from app.schemas.operational_data import OperationalDataResponse


router = APIRouter(
    prefix="/operational-data",
    tags=["Operational Data"]
)


@router.get(
    "/",
    response_model=list[OperationalDataResponse]
)
def get_operational_data(db: Session = Depends(get_db)):
    operational_data = db.query(OperationalData).all()

    return operational_data