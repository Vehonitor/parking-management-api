from sqlalchemy import Column, Integer, String, Boolean, Text, TIMESTAMP
from sqlalchemy.sql import func
from src.db.base import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    address = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, server_default='true')
    email_verified = Column(Boolean, default=False, server_default='false')
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<User(user_id={self.user_id}, email='{self.email}')>"
