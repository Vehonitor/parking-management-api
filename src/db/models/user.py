# ============================================================================
# FILE: src/db/models/user.py
# ============================================================================
from sqlalchemy import Column, Integer, String, Boolean, Text
from src.db.base import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    address = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    email_verified = Column(Boolean, default=False)
    hashed_password = Column(String(255), nullable=False)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, email='{self.email}')>"
