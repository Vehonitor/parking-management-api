# src/core/config.py
import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Database
    DATABASE_URL: Optional[str] = None
    DB_USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[int] = None
    DB_NAME: Optional[str] = None

    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Twilio
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_FROM_NUMBER: str

    # OTP
    OTP_EXPIRY_MINUTES: int = 10
    OTP_LENGTH: int = 6

    # App
    APP_NAME: str = "Parking Management API"
    DEBUG: bool = True
    STAGE: Optional[str] = "dev"

    # Pool settings
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_TIMEOUT: int = 30
    DB_POOL_RECYCLE: int = 3600

    def get_database_url(self) -> str:
        """Return full PostgreSQL connection URL."""
        if self.DATABASE_URL:
            return self.DATABASE_URL
        if all([self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME]):
            return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        raise ValueError("Database configuration incomplete")


# ✅ Instantiate settings once
settings = Settings()
