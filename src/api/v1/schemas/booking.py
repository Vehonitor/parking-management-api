
# ============================================================================
# FILE: src/api/v1/schemas/booking.py
# ============================================================================
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal
from src.db.models.booking import BookingStatusEnum, RefundStatusEnum
from src.db.models.parking_profile import BookingTypeEnum

class BookingBase(BaseModel):
    vehicle_id: int
    space_profile_id: int
    start_time: datetime
    end_time: datetime
    booking_type: BookingTypeEnum
    amount_expected: Decimal = Field(..., ge=0, decimal_places=2)

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    end_time: Optional[datetime] = None
    status: Optional[BookingStatusEnum] = None

class BookingCancel(BaseModel):
    reason: str

class BookingResponse(BookingBase):
    booking_id: int
    user_id: int
    status: BookingStatusEnum
    reason: Optional[str] = None
    cancelled_at: Optional[datetime] = None
    refund_status: RefundStatusEnum
    created_at: datetime

    class Config:
        from_attributes = True

