

# ============================================================================
# STEP 11: Create src/services/auth_service.py (New)
# ============================================================================
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.api.v1.schemas.user import TokenResponse, UserResponse
from src.db.models.user import User
from src.db.models.otp import OTP
from src.repositories.user_repo import UserRepository
from src.repositories.otp_repo import OTPRepository
from src.core.security import Security
from src.utils.twilio_client import TwilioClient
from src.core.config import settings
from datetime import datetime, timedelta
import random
import string
import logging

logger = logging.getLogger(__name__)

class AuthService:
    """Service for authentication and authorization."""
    
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)
        self.otp_repo = OTPRepository(db)
        self.twilio_client = TwilioClient()

    def generate_otp(self) -> str:
        """Generate random OTP"""
        return ''.join(random.choices(string.digits, k=settings.OTP_LENGTH))

    async def send_otp(self, phone: str) -> dict:
        """Send OTP to phone number"""
        try:
            # Check if user exists, if not create
            # user = self.user_repo.get_by_phone(phone)
            # if not user:
            #     user = User(phone=phone)
            #     user = self.user_repo.create(user)
            #     logger.info(f"New user created with phone: {phone}")
            
            # Invalidate old OTPs
            # self.otp_repo.invalidate_phone_otps(phone)
            
            # Generate new OTP
            otp_code = self.generate_otp()
            print(f"Generated OTP for {phone}: {otp_code}")  # For debugging purposes
            expiry_time = datetime.utcnow() + timedelta(minutes=settings.OTP_EXPIRY_MINUTES)
            print(f"OTP expiry time: {expiry_time}")  # For debugging purposes
            
            # Save OTP to database
            otp = OTP(
                phone=phone,
                otp_code=otp_code,
                expiry_time=expiry_time
            )
            print(f"Saving OTP to DB for {phone}")  # For debugging purposes
            self.otp_repo.create(otp)
            print(f"OTP saved to DB for {phone}")  # For debugging purposes
            # Send OTP via Twilio
            result = self.twilio_client.send_otp(phone, otp_code)
            print(f"Twilio send result for {phone}: {result}")  # For debugging purposes
            if not result.get('success'):
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Failed to send OTP: {result.get('error', 'Unknown error')}"
                )
            
            return {
                "message": "OTP sent successfully",
                "phone": phone,
                "expires_in_minutes": settings.OTP_EXPIRY_MINUTES,
                # Only include OTP in development mode
                "otp": otp_code if settings.DEBUG else None
            }
        
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error sending OTP: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to send OTP: {str(e)}"
            )

    async def verify_otp(self, phone: str, otp_code: str) -> dict:
        """Verify OTP and login user"""
        try:
            # Check if OTP is valid
            otp = self.otp_repo.get_latest_valid(phone, otp_code)
            print(f"Verifying OTP for {phone}: found OTP: {otp}")  # For debugging purposes
            if not otp:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid or expired OTP"
                )
            print(f"OTP is valid for {otp.otp_id}")  # For debugging purposes
            # Mark OTP as used
            self.otp_repo.mark_as_used(otp.otp_id)
            
            # Get or create user
            user = self.user_repo.get_by_phone(phone)
            print(f"User fetched for {phone}: {user}")  # For debugging purposes
            if not user:
                user = User(phone=phone, phone_verified=True)
                user = self.user_repo.create(user)
            else:
                # Mark phone as verified
                self.user_repo.verify_phone(phone)
                user = self.user_repo.get_by_phone(phone)
            print(f"User after verification for {phone}: {user}")  # For debugging purposes
            # Generate JWT token
            access_token = Security.create_access_token(
                data={"sub": phone, "user_id": user.user_id}
            )
            print(f"Access token generated for {phone}: {access_token}")  # For debugging purposes
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
        
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error verifying OTP: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to verify OTP: {str(e)}"
            )

