

# ============================================================================
# STEP 9: Create src/db/models/__init__.py
# ============================================================================

# Import all models here so Alembic can detect them
from src.db.models.user import User
from src.db.models.vehicle import Vehicle
from src.db.models.otp import OTP
from src.db.models.parking_zone import ParkingZone
from src.db.models.parking_profile import ParkingSpaceProfile
from src.db.models.schedule import ParkingSpaceSchedule
from src.db.models.booking import Booking
from src.db.models.checkinout import CheckInOut
from src.db.models.payment import Payment
from src.db.models.chat import ChatMessage

__all__ = [
    'User',
    'Vehicle',
    'OTP',
    'ParkingZone',
    'ParkingSpaceProfile',
    'ParkingSpaceSchedule',
    'Booking',
    'CheckInOut',
    'Payment',
    'ChatMessage'
]
