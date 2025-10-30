
# ============================================================================
# FILE: src/db/models/otp.py
# ============================================================================
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from src.db.base import Base
from datetime import datetime

class OTP(Base):
    __tablename__ = 'otp_codes'

    otp_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    otp_code = Column(String(10), nullable=False)
    expiry_time = Column(DateTime, nullable=False)
    is_used = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    verified_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<OTP(otp_id={self.otp_id}, user_id={self.user_id})>"
