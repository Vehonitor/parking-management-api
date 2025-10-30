from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.services.parking_service import list_parking_spots

router = APIRouter()

@router.get("/")
def get_parking_spots(db: Session = Depends(get_db)):
    return list_parking_spots(db)
