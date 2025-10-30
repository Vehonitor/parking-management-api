from pydantic import BaseModel
from typing import Optional, List

class ParkingSpotBase(BaseModel):
    name: str
    location: str
    price_per_hour: float
    is_available: bool

class ParkingSpotCreate(ParkingSpotBase):
    pass

class ParkingSpotUpdate(ParkingSpotBase):
    pass

class ParkingSpot(ParkingSpotBase):
    id: int

    class Config:
        orm_mode = True

class ParkingSpotList(BaseModel):
    spots: List[ParkingSpot]