from pydantic import BaseSettings

class Settings(BaseSettings):
    google_maps_api_key: str
    razorpay_key_id: str
    razorpay_key_secret: str
    dynamodb_table_user: str
    dynamodb_table_parking: str
    dynamodb_table_booking: str
    s3_bucket: str
    jwt_secret: str

    class Config:
        env_file = ".env"

settings = Settings()