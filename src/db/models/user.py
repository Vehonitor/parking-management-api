<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, Boolean, Text, TIMESTAMP
from sqlalchemy.sql import func
from src.db.base import Base
=======
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
>>>>>>> 1c47c5c (first commit)

class User(Base):
    __tablename__ = 'users'

<<<<<<< HEAD
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(15), unique=True, nullable=False, index=True)
    full_name = Column(String(100), nullable=True)
    email = Column(String(100), unique=True, nullable=True)
    address = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True, server_default='true')
    phone_verified = Column(Boolean, default=False, server_default='false')
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<User(user_id={self.user_id}, email='{self.email}')>"
=======
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String, index=True)
    disabled = Column(Integer, default=0)  # 0 for False, 1 for True

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
>>>>>>> 1c47c5c (first commit)
