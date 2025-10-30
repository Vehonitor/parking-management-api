# src/db/models/enums.py
from enum import Enum

class VehicleTypeEnum(str, Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"
