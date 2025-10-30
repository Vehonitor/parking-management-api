from sqlalchemy import Column, Integer, String
from src.db.base import Base

class ParkingSpot(Base):
    __tablename__ = "parking_spots"

    id = Column(Integer, primary_key=True, index=True)
    spot_number = Column(String, unique=True, index=True)
    is_occupied = Column(Integer, default=0)
