import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Twilio
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_FROM_NUMBER: str

    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database
    DATABASE_URL: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    # App config
    DEBUG: bool = True
    STAGE: str = "dev"
    OTP_EXPIRY_MINUTES: int = 10
    OTP_LENGTH: int = 6
    APP_NAME: str = "Parking Management API"

    class Config:
        env_prefix = ""  # read variables as-is
        case_sensitive = True

    @classmethod
    def load(cls, use_ssm: bool = False, region_name: str = "us-east-1"):
        """
        Load settings:
        - Default: from environment variables
        - Optional: fetch from AWS SSM if use_ssm=True
        """
        if not use_ssm:
            return cls()

        import boto3

        client = boto3.client("ssm", region_name=region_name)

        def get_param(name: str) -> str:
            return client.get_parameter(Name=name, WithDecryption=True)["Parameter"]["Value"]

        stage = os.getenv("STAGE", "dev")

        return cls(
            TWILIO_ACCOUNT_SID=get_param(f"/parking/{stage}/TWILIO_ACCOUNT_SID"),
            TWILIO_AUTH_TOKEN=get_param(f"/parking/{stage}/TWILIO_AUTH_TOKEN"),
            TWILIO_FROM_NUMBER=get_param(f"/parking/{stage}/TWILIO_FROM_NUMBER"),
            JWT_SECRET=get_param(f"/parking/{stage}/JWT_SECRET"),
            JWT_ALGORITHM="HS256",
            ACCESS_TOKEN_EXPIRE_MINUTES=int(get_param(f"/parking/{stage}/ACCESS_TOKEN_EXPIRE_MINUTES")),
            DATABASE_URL=get_param(f"/parking/{stage}/DATABASE_URL"),
            DB_USER=get_param(f"/parking/{stage}/DB_USER"),
            DB_PASSWORD=get_param(f"/parking/{stage}/DB_PASSWORD"),
            DB_HOST=get_param(f"/parking/{stage}/DB_HOST"),
            DB_PORT=get_param(f"/parking/{stage}/DB_PORT"),
            DB_NAME=get_param(f"/parking/{stage}/DB_NAME"),
            DEBUG=get_param(f"/parking/{stage}/DEBUG").lower() == "true",
            STAGE=stage,
            OTP_EXPIRY_MINUTES=int(get_param(f"/parking/{stage}/OTP_EXPIRY_MINUTES")),
            OTP_LENGTH=int(get_param(f"/parking/{stage}/OTP_LENGTH")),
            APP_NAME=get_param(f"/parking/{stage}/APP_NAME"),
        )

# Load settings from environment or SSM
settings = Settings.load(use_ssm=False)
