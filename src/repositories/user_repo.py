from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from src.db.models.user import User, UserRole
from src.api.v1.schemas.user import UserCreate, UserUpdate
from src.core.security import get_password_hash


class UserRepository:
    """Repository for user database operations."""
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, user_id: str) -> Optional[User]:
        """Get user by ID."""
        return self.db.query(User).filter(User.id == user_id).first()
    
    def get_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        return self.db.query(User).filter(User.email == email).first()
    
    def get_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        return self.db.query(User).filter(User.username == username).first()
    
    def create(self, user_data: UserCreate, role: UserRole = UserRole.USER) -> User:
        """Create a new user."""
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=get_password_hash(user_data.password),
            full_name=user_data.full_name,
            phone_number=user_data.phone_number,
            role=role
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def update(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        """Update user information."""
        user = self.get_by_id(user_id)
        if not user:
            return None
        
        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        
        user.updated_at = datetime.utcnow()
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update_last_login(self, user_id: str) -> Optional[User]:
        """Update user's last login timestamp."""
        user = self.get_by_id(user_id)
        if user:
            user.last_login = datetime.utcnow()
            self.db.commit()
            self.db.refresh(user)
        return user
    
    def delete(self, user_id: str) -> bool:
        """Delete a user."""
        user = self.get_by_id(user_id)
        if not user:
            return False
        
        self.db.delete(user)
        self.db.commit()
        return True
    
    def get_all(self, skip: int = 0, limit: int = 100):
        """Get all users with pagination."""
        return self.db.query(User).offset(skip).limit(limit).all()