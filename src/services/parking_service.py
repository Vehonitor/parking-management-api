from sqlalchemy.orm import Session
from src.db.models.parking_spot import ParkingSpot
from src.db.models.user import User
from src.repositories.parking_repo import ParkingRepo
from src.core.security import get_current_user
from fastapi import Depends, HTTPException, status

class ParkingService:
    def __init__(self, db: Session):
        self.db = db
        self.parking_repo = ParkingRepo(db)

    def create_parking_spot(self, parking_spot_data, user: User):
        parking_spot = ParkingSpot(**parking_spot_data.dict(), owner_id=user.id)
        return self.parking_repo.create(parking_spot)

    def get_parking_spots(self, skip: int = 0, limit: int = 10):
        return self.parking_repo.get_all(skip=skip, limit=limit)

    def get_parking_spot(self, parking_spot_id: int):
        parking_spot = self.parking_repo.get(parking_spot_id)
        if not parking_spot:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Parking spot not found")
        return parking_spot

    def update_parking_spot(self, parking_spot_id: int, parking_spot_data, user: User):
        parking_spot = self.parking_repo.get(parking_spot_id)
        if not parking_spot or parking_spot.owner_id != user.id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Parking spot not found or not owned by user")
        for key, value in parking_spot_data.dict().items():
            setattr(parking_spot, key, value)
        return self.parking_repo.update(parking_spot)

    def delete_parking_spot(self, parking_spot_id: int, user: User):
        parking_spot = self.parking_repo.get(parking_spot_id)
        if not parking_spot or parking_spot.owner_id != user.id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Parking spot not found or not owned by user")
        self.parking_repo.delete(parking_spot)