
# ============================================================================
# FILE: src/db/models/otp.py
# ============================================================================
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from src.db.base import Base
from datetime import datetime

class OTP(Base):
    __tablename__ = 'otp_codes'

    otp_id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(15), nullable=False, index=True)
    otp_code = Column(String(10), nullable=False)
    expiry_time = Column(DateTime, nullable=False)
    is_used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<OTP(otp_id={self.otp_id})>"
