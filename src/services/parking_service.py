from sqlalchemy.orm import Session
from src.repositories.parking_repo import get_parking_spots

def list_parking_spots(db: Session):
    return get_parking_spots(db)
