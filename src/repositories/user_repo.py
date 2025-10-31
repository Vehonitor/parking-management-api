
# ============================================================================
# STEP 9: Update src/repositories/user_repo.py
# ============================================================================
from sqlalchemy.orm import Session
from src.api.v1.schemas.user import UserAdded
from src.db.models.user import User
from typing import Optional

class UserRepository:
    """Repository for user database operations."""
    
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.user_id == user_id).first()

    def get_by_phone(self, phone: str) -> Optional[User]:
        return self.db.query(User).filter(User.phone == phone).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def update(self, user_id: int, update_data: dict) -> Optional[User]:
        user = self.get_by_id(user_id)
        if user:
            for key, value in update_data.items():
                if value is not None:
                    setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
        return user

    def verify_phone(self, phone: str) -> Optional[User]:
        user = self.get_by_phone(phone)
        if user:
            user.phone_verified = True
            self.db.commit()
            self.db.refresh(user)
        return user

    def user_login(self, users: UserAdded) -> Optional[User]:
        user = self.get_by_id(users.user_id)
        print(f"User retrieved for login: {users}")  # Debugging statement
        print(f"User email for login: {users.email }")  # Debugging statement
        print(f"User name for login: {users.full_name }")  # Debugging statement
        if user:
            user.is_active = True
            user.email = users.email  # Example of updating last login timestamp or similar
            user.full_name = users.full_name

            self.db.commit()
            self.db.refresh(user)
        return user
