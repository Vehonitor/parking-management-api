from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.core.security import get_current_user
from src.db.models.user import User

def get_user(db: Session = Depends(get_db), token: str = Depends(get_current_user)) -> User:
    user = db.query(User).filter(User.id == token.user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def get_current_active_user(current_user: User = Depends(get_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user")
    return current_user