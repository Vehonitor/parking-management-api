from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from src.api.v1.schemas.user import UserCreate, UserLogin, UserResponse
from src.services.auth_service import AuthService
from src.core.security import create_access_token

router = APIRouter()

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate):
    user_created = await AuthService.create_user(user)
    if not user_created:
        raise HTTPException(status_code=400, detail="User already exists")
    return user_created

@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin):
    user_data = await AuthService.authenticate_user(user)
    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user_data.email})
    return {"access_token": access_token, "token_type": "bearer"}