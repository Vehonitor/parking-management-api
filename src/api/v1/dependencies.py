

# ============================================================================
# STEP 13: Update src/api/v1/dependencies.py
# ============================================================================
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.core.security import get_current_user_phone
from src.db.models.user import User
from src.repositories.user_repo import UserRepository

def get_current_user(
    phone: str = Depends(get_current_user_phone),
    db: Session = Depends(get_db)
) -> User:
    """Get current user from database"""
    user_repo = UserRepository(db)
    user = user_repo.get_by_phone(phone)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user

def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """Get current active user"""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    
    return current_user
