
# ============================================================================
# STEP 10: Create src/repositories/otp_repo.py
# ============================================================================
from sqlalchemy.orm import Session
from src.db.models.otp import OTP
from typing import Optional
from datetime import datetime

class OTPRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, otp: OTP) -> OTP:
        self.db.add(otp)
        self.db.commit()
        self.db.refresh(otp)
        return otp

    def get_latest_valid(self, phone: str, otp_code: str) -> Optional[OTP]:
        return self.db.query(OTP).filter(
            OTP.phone == phone,
            OTP.otp_code == otp_code,
            OTP.is_used == False,
            OTP.expiry_time > datetime.utcnow()
        ).order_by(OTP.created_at.desc()).first()

    def mark_as_used(self, otp_id: int) -> Optional[OTP]:
        print(f"Marking OTP {otp_id} as used")  # For debugging purposes
        otp = self.db.query(OTP).filter(OTP.otp_id == otp_id).first()
        print(f"Marking OTP {otp_id} as used: found OTP: {otp}")  # For debugging purposes
        if otp:
            otp.is_used = True
            otp.created_at = datetime.utcnow()
            self.db.commit()
            self.db.refresh(otp)
        return otp

    def invalidate_phone_otps(self, phone: str) -> int:
        count = self.db.query(OTP).filter(
            OTP.phone == phone,
            OTP.is_used == False
        ).update({"is_used": True})
        self.db.commit()
        return count

