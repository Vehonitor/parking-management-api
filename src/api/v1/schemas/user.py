
# ============================================================================
# STEP 8: Update src/api/v1/schemas/user.py
# ============================================================================
from pydantic import BaseModel, Field, validator
from typing import Optional
import re

class PhoneNumberRequest(BaseModel):
    phone: str = Field(..., min_length=10, max_length=15)
    
    @validator('phone')
    def validate_phone(cls, v):
        # Remove spaces, dashes, and parentheses
        phone = re.sub(r'[\s\-\(\)]', '', v)
        
        # Check if it's a valid phone number (basic validation)
        if not re.match(r'^\+?[1-9]\d{9,14}$', phone):
            raise ValueError('Invalid phone number format')
        
        return phone

class OTPVerifyRequest(BaseModel):
    phone: str = Field(..., min_length=10, max_length=15)
    otp_code: str = Field(..., min_length=4, max_length=6)

class UserResponse(BaseModel):
    user_id: int
    phone: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    is_active: bool
    phone_verified: bool

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

