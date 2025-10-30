
# ============================================================================
# FILE: src/db/models/parking_profile.py
# ============================================================================
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Boolean, DECIMAL
from src.db.base import Base
import enum

class SlotTypeEnum(str, enum.Enum):
    TWO_WHEELER = "2Wheeler"
    FOUR_WHEELER = "4Wheeler"

class VehicleCategoryEnum(str, enum.Enum):
    MINI = "Mini"
    MEDIUM = "Medium"
    XL = "XL"
    VAN = "Van"
    ANY = "Any"

class BookingTypeEnum(str, enum.Enum):
    PREPAY = "Prepay"
    PAY_LATER = "PayLater"

class ParkingSpaceProfile(Base):
    __tablename__ = 'parking_space_profiles'

    space_profile_id = Column(Integer, primary_key=True, autoincrement=True)
    parking_zone_id = Column(Integer, ForeignKey('parking_zones.parking_zone_id'), nullable=False)
    slot_type = Column(Enum(SlotTypeEnum), nullable=False)
    height = Column(String(50), nullable=True)
    width = Column(String(50), nullable=True)
    vehicle_category = Column(Enum(VehicleCategoryEnum), nullable=False)
    covered = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    price_per_hour = Column(DECIMAL(10, 2), nullable=False)
    price_24_hour = Column(DECIMAL(10, 2), nullable=True)
    booking_type = Column(Enum(BookingTypeEnum), nullable=False)
    available_24_7 = Column(Boolean, default=False)

    def __repr__(self):
        return f"<ParkingSpaceProfile(space_profile_id={self.space_profile_id})>"

