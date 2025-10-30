
# ============================================================================
# FILE: src/api/v1/schemas/parking_profile.py
# ============================================================================
from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from src.db.models.parking_profile import SlotTypeEnum, VehicleCategoryEnum, BookingTypeEnum

class ParkingProfileBase(BaseModel):
    slot_type: SlotTypeEnum
    height: Optional[str] = Field(None, max_length=50)
    width: Optional[str] = Field(None, max_length=50)
    vehicle_category: VehicleCategoryEnum
    covered: bool = False
    is_active: bool = True
    price_per_hour: Decimal = Field(..., ge=0, decimal_places=2)
    price_24_hour: Optional[Decimal] = Field(None, ge=0, decimal_places=2)
    booking_type: BookingTypeEnum
    available_24_7: bool = False

class ParkingProfileCreate(ParkingProfileBase):
    parking_zone_id: int

class ParkingProfileUpdate(BaseModel):
    slot_type: Optional[SlotTypeEnum] = None
    height: Optional[str] = None
    width: Optional[str] = None
    vehicle_category: Optional[VehicleCategoryEnum] = None
    covered: Optional[bool] = None
    is_active: Optional[bool] = None
    price_per_hour: Optional[Decimal] = None
    price_24_hour: Optional[Decimal] = None
    booking_type: Optional[BookingTypeEnum] = None
    available_24_7: Optional[bool] = None

class ParkingProfileResponse(ParkingProfileBase):
    space_profile_id: int
    parking_zone_id: int

    class Config:
        from_attributes = True

