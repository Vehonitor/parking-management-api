

# ============================================================================
# STEP 14: Update src/api/v1/routers/auth.py
# ============================================================================
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.repositories import user_repo
from src.db.models.user import User
from src.db.session import get_db
from src.core.security import Security
from src.services.auth_service import AuthService
from src.api.v1.schemas.user import (
    PhoneNumberRequest,
    OTPVerifyRequest,
    TokenResponse,
    UserAdded,
    UserResponse
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
async def login(users: UserAdded, db: Session = Depends(get_db)):
    """Alias for send-otp (for backward compatibility)"""
    print(f"Logging in user with name: {users.full_name}")  # For debugging purposes
    repo = user_repo.UserRepository(db)
    print(f"Logging in user with ID: {users.user_id}")  # For debugging purposes
    user = repo.user_login(users)
    print(f"User found: {user}")  # For debugging purposes
    # Generate JWT token
    access_token = Security.create_access_token(
                data={"sub": user.phone, "user_id": user.user_id}
            )
    print(f"Access token generated for {user.phone}: {access_token}")  # For debugging purposes
    print(f"User logged in: {user}")  # For debugging purposes
            
            # logger.info(f"User logged in: {phone}")
            
    return TokenResponse(
                access_token=access_token,
                token_type="bearer",
                user=UserResponse(
                    user_id=user.user_id,
                    phone=user.phone,
                    full_name=user.full_name,
                    email=user.email,
                    is_active=user.is_active,
                    phone_verified=user.phone_verified
                )
            )
    # return {"message": "Login successful",
    #          "user_id": user.user_id}

    # auth_service = AuthService(db)
    # return await auth_service.send_otp(request.phone)
