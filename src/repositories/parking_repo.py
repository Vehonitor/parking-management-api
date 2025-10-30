from sqlalchemy.orm import Session
from src.db.models.parking_spot import ParkingSpot

def get_parking_spots(db: Session):
    return db.query(ParkingSpot).all()
