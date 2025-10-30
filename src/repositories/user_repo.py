
# ============================================================================
# STEP 9: Update src/repositories/user_repo.py
# ============================================================================
from sqlalchemy.orm import Session
from src.db.models.user import User
from typing import Optional

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

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

