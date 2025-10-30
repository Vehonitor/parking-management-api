
# ============================================================================
# FILE: src/db/models/vehicle.py
# ============================================================================
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.db.base import Base
import enum

class VehicleTypeEnum(str, enum.Enum):
    BIKE = "Bike"
    CAR = "Car"
    SEDAN = "Sedan"
    SUV = "SUV"

class Vehicle(Base):
    __tablename__ = 'vehicles'

    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    nick_name = Column(String(100), nullable=True)
    vehicle_type = Column(Enum(VehicleTypeEnum), nullable=False)
    model = Column(String(50), nullable=True)
    registration_no = Column(String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"<Vehicle(vehicle_id={self.vehicle_id}, registration_no='{self.registration_no}')>"

