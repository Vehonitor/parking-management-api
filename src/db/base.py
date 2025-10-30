# src/db/base.py
from sqlalchemy.ext.declarative import declarative_base

# This is the Base class your models will inherit from
Base = declarative_base()

# Import all your models here so Alembic can see them
from .models.booking import Booking
# from .models.user import User
from src.db.base import Base
from .models.parking_profile import ParkingSpaceProfile
from .models.parking_spot import ParkingSpot
from .models.parking_zone import ParkingZone
from .models.vehicle import Vehicle
from .models.checkinout import CheckInOut
from .models.payment import Payment
from .models.otp import OTP
from .models.schedule import ParkingSpaceSchedule
from .models.chat import ChatMessage

# Optional: you can also use __all__ to define public objects
__all__ = [
    "Base",
    "Booking",
    "User",
    "ParkingSpaceProfile",
    "ParkingSpot",
    "ParkingZone",
    "Vehicle",
    "CheckInOut",
    "Payment",
    "OTP",
    "ParkingSpaceSchedule",
    "ChatMessage",
]
