
# ============================================================================
# FILE: src/db/models/schedule.py
# ============================================================================
from sqlalchemy import Column, Integer, ForeignKey, Enum, Boolean, Time
from src.db.base import Base
import enum

class DayOfWeekEnum(str, enum.Enum):
    SUN = "Sun"
    MON = "Mon"
    TUE = "Tue"
    WED = "Wed"
    THU = "Thu"
    FRI = "Fri"
    SAT = "Sat"

class ParkingSpaceSchedule(Base):
    __tablename__ = 'parking_space_schedules'

    schedule_id = Column(Integer, primary_key=True, autoincrement=True)
    parking_zone_id = Column(Integer, ForeignKey('parking_zones.parking_zone_id'), nullable=False)
    day_of_week = Column(Enum(DayOfWeekEnum), nullable=False)
    is_available_24_7 = Column(Boolean, default=False)
    start_time = Column(Time, nullable=True)
    end_time = Column(Time, nullable=True)
    is_not_available = Column(Boolean, default=False)

    def __repr__(self):
        return f"<ParkingSpaceSchedule(schedule_id={self.schedule_id}, day={self.day_of_week})>"

