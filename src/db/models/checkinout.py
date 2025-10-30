
# ============================================================================
# FILE: src/db/models/checkinout.py
# ============================================================================
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from src.db.base import Base

class CheckInOut(Base):
    __tablename__ = 'check_in_out'

    check_id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('bookings.booking_id'), nullable=False, unique=True)
    check_in_time = Column(DateTime, nullable=True)
    check_out_time = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<CheckInOut(check_id={self.check_id}, booking_id={self.booking_id})>"
