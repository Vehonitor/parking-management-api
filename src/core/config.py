
# ============================================================================
# STEP 3: Update src/core/config.py
# ============================================================================
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database - PostgreSQL
    DATABASE_URL: str
    
    # Alternative: Build URL from components
    DB_USER: Optional[str] = None
    DB_PASSWORD: Optional[str] = None
    DB_HOST: Optional[str] = None
    DB_PORT: Optional[int] = 5432
    DB_NAME: Optional[str] = None
    
    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # # API Keys
    # GOOGLE_MAPS_API_KEY: Optional[str] = None
    # RAZORPAY_KEY_ID: Optional[str] = None
    # RAZORPAY_KEY_SECRET: Optional[str] = None
    
    # # AWS
    # AWS_ACCESS_KEY_ID: Optional[str] = None
    # AWS_SECRET_ACCESS_KEY: Optional[str] = None
    # AWS_REGION: Optional[str] = "us-east-1"
    # S3_BUCKET: Optional[str] = None
    
    # # Email/SMS
    # SMTP_HOST: Optional[str] = None
    # SMTP_PORT: Optional[int] = 587
    # SMTP_USER: Optional[str] = None
    # SMTP_PASSWORD: Optional[str] = None
    # SMS_API_KEY: Optional[str] = None
    
    # App
    APP_NAME: str = "Parking Management API"
    DEBUG: bool = True
    
    # Pool settings for PostgreSQL
    DB_POOL_SIZE: int = 5
    DB_MAX_OVERFLOW: int = 10
    DB_POOL_TIMEOUT: int = 30
    DB_POOL_RECYCLE: int = 3600
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    def get_database_url(self) -> str:
        """Get database URL, build from components if needed"""
        if self.DATABASE_URL:
            return self.DATABASE_URL
        
        if all([self.DB_USER, self.DB_PASSWORD, self.DB_HOST, self.DB_NAME]):
            return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        
        raise ValueError("Database configuration incomplete")

settings = Settings()
