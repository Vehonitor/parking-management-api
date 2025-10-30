
# ============================================================================
# FILE: src/db/models/booking.py
# ============================================================================
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, DECIMAL, Text
from src.db.base import Base
from datetime import datetime
import enum

class BookingStatusEnum(str, enum.Enum):
    BOOKED = "Booked"
    STARTED = "Started"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class RefundStatusEnum(str, enum.Enum):
    INITIATED = "Initiated"
    COMPLETED = "Completed"
    NOT_APPLICABLE = "NotApplicable"

class Booking(Base):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id'), nullable=False)
    space_profile_id = Column(Integer, ForeignKey('parking_space_profiles.space_profile_id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(Enum(BookingStatusEnum), default=BookingStatusEnum.BOOKED)
    booking_type = Column(Enum(BookingTypeEnum), nullable=False)
    amount_expected = Column(DECIMAL(10, 2), nullable=False)
    reason = Column(Text, nullable=True)
    cancelled_at = Column(DateTime, nullable=True)
    refund_status = Column(Enum(RefundStatusEnum), default=RefundStatusEnum.NOT_APPLICABLE)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Booking(booking_id={self.booking_id}, status='{self.status}')>"
