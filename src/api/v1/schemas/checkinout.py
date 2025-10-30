
# ============================================================================
# FILE: src/api/v1/schemas/checkinout.py
# ============================================================================
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CheckInOutBase(BaseModel):
    booking_id: int

class CheckInCreate(CheckInOutBase):
    check_in_time: datetime

class CheckOutCreate(BaseModel):
    check_out_time: datetime

class CheckInOutResponse(BaseModel):
    check_id: int
    booking_id: int
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None

    class Config:
        from_attributes = True

