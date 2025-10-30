

# ============================================================================
# FILE: src/api/v1/schemas/schedule.py
# ============================================================================
from pydantic import BaseModel
from typing import Optional
from datetime import time
from src.db.models.schedule import DayOfWeekEnum

class ScheduleBase(BaseModel):
    day_of_week: DayOfWeekEnum
    is_available_24_7: bool = False
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    is_not_available: bool = False

class ScheduleCreate(ScheduleBase):
    parking_zone_id: int

class ScheduleUpdate(BaseModel):
    is_available_24_7: Optional[bool] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    is_not_available: Optional[bool] = None

class ScheduleResponse(ScheduleBase):
    schedule_id: int
    parking_zone_id: int

    class Config:
        from_attributes = True

