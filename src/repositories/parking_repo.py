from sqlalchemy.orm import Session
from src.db.models.parking_spot import ParkingSpot
from src.db.models.user import User
from typing import List, Optional

class ParkingRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_parking_spot(self, parking_spot: ParkingSpot) -> ParkingSpot:
        self.db.add(parking_spot)
        self.db.commit()
        self.db.refresh(parking_spot)
        return parking_spot

    def get_parking_spot(self, parking_spot_id: int) -> Optional[ParkingSpot]:
        return self.db.query(ParkingSpot).filter(ParkingSpot.id == parking_spot_id).first()

    def get_parking_spots(self, skip: int = 0, limit: int = 10) -> List[ParkingSpot]:
        return self.db.query(ParkingSpot).offset(skip).limit(limit).all()

    def update_parking_spot(self, parking_spot_id: int, updated_data: dict) -> Optional[ParkingSpot]:
        parking_spot = self.get_parking_spot(parking_spot_id)
        if parking_spot:
            for key, value in updated_data.items():
                setattr(parking_spot, key, value)
            self.db.commit()
            self.db.refresh(parking_spot)
            return parking_spot
        return None

    def delete_parking_spot(self, parking_spot_id: int) -> bool:
        parking_spot = self.get_parking_spot(parking_spot_id)
        if parking_spot:
            self.db.delete(parking_spot)
            self.db.commit()
            return True
        return False