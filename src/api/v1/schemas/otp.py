
# ============================================================================
# FILE: src/api/v1/schemas/otp.py
# ============================================================================
from pydantic import BaseModel
from datetime import datetime

class OTPCreate(BaseModel):
    email: str

class OTPVerify(BaseModel):
    email: str
    otp_code: str

class OTPResponse(BaseModel):
    message: str
    expires_at: datetime