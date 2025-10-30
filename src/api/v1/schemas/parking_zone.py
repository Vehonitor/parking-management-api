
# ============================================================================
# FILE: src/api/v1/schemas/parking_zone.py
# ============================================================================
from pydantic import BaseModel, Field
from typing import Optional
from src.db.models.parking_zone import ZoneTypeEnum

class ParkingZoneBase(BaseModel):
    name: str = Field(..., max_length=100)
    door_no: Optional[str] = Field(None, max_length=20)
    address1: Optional[str] = Field(None, max_length=200)
    address2: Optional[str] = Field(None, max_length=200)
    city: str = Field(..., max_length=100)
    state: str = Field(..., max_length=100)
    country: str = Field(..., max_length=100)
    pin_code: int
    type: ZoneTypeEnum

class ParkingZoneCreate(ParkingZoneBase):
    pass

class ParkingZoneUpdate(BaseModel):
    name: Optional[str] = None
    door_no: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    pin_code: Optional[int] = None
    type: Optional[ZoneTypeEnum] = None

class ParkingZoneResponse(ParkingZoneBase):
    parking_zone_id: int
    user_id: int

    class Config:
        from_attributes = True

