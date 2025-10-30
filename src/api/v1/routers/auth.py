

# ============================================================================
# STEP 14: Update src/api/v1/routers/auth.py
# ============================================================================
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.services.auth_service import AuthService
from src.api.v1.schemas.user import (
    PhoneNumberRequest,
    OTPVerifyRequest,
    TokenResponse
)

router = APIRouter()

@router.post("/send-otp")
async def send_otp(
    request: PhoneNumberRequest,
    db: Session = Depends(get_db)
):
    """Send OTP to phone number"""
    auth_service = AuthService(db)
    return await auth_service.send_otp(request.phone)

@router.post("/verify-otp", response_model=TokenResponse)
async def verify_otp(
    request: OTPVerifyRequest,
    db: Session = Depends(get_db)
):
    """Verify OTP and login"""
    auth_service = AuthService(db)
    return await auth_service.verify_otp(request.phone, request.otp_code)

@router.post("/login")
async def login(request: PhoneNumberRequest, db: Session = Depends(get_db)):
    """Alias for send-otp (for backward compatibility)"""
    auth_service = AuthService(db)
    return await auth_service.send_otp(request.phone)
