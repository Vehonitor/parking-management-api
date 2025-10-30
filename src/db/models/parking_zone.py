
# ============================================================================
# FILE: src/db/models/parking_zone.py
# ============================================================================
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Text
from src.db.base import Base
import enum

class ZoneTypeEnum(str, enum.Enum):
    PRIVATE = "Private"
    PUBLIC = "Public"
    PARKING_LOT = "ParkingLot"

class ParkingZone(Base):
    __tablename__ = 'parking_zones'

    parking_zone_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    name = Column(String(100), nullable=False)
    door_no = Column(String(20), nullable=True)
    address1 = Column(String(200), nullable=True)
    address2 = Column(String(200), nullable=True)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    pin_code = Column(Integer, nullable=False)
    type = Column(Enum(ZoneTypeEnum), nullable=False)

    def __repr__(self):
        return f"<ParkingZone(parking_zone_id={self.parking_zone_id}, name='{self.name}')>"

