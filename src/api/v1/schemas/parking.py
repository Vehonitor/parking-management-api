from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from src.db.models.parking_spot import ParkingSpotStatus, VehicleType


# Base schemas
class ParkingSpotBase(BaseModel):
    """Base parking spot schema."""
    spot_number: str = Field(..., description="Unique spot number/identifier")
    floor: Optional[int] = None
    section: Optional[str] = None
    location_description: Optional[str] = None
    vehicle_type: VehicleType = VehicleType.CAR
    hourly_rate: float = Field(default=5.0, ge=0)
    daily_rate: float = Field(default=30.0, ge=0)
    is_covered: bool = False
    is_disabled_accessible: bool = False
    is_ev_charging: bool = False
    has_camera: bool = False


class ParkingSpotCreate(ParkingSpotBase):
    """Schema for creating a parking spot."""
    pass


class ParkingSpotUpdate(BaseModel):
    """Schema for updating a parking spot."""
    spot_number: Optional[str] = None
    floor: Optional[int] = None
    section: Optional[str] = None
    location_description: Optional[str] = None
    vehicle_type: Optional[VehicleType] = None
    hourly_rate: Optional[float] = Field(None, ge=0)
    daily_rate: Optional[float] = Field(None, ge=0)
    is_covered: Optional[bool] = None
    is_disabled_accessible: Optional[bool] = None
    is_ev_charging: Optional[bool] = None
    has_camera: Optional[bool] = None
    status: Optional[ParkingSpotStatus] = None


class ParkingSpotInDB(ParkingSpotBase):
    """Parking spot schema with database fields."""
    id: str
    status: ParkingSpotStatus
    owner_id: Optional[str] = None
    current_vehicle_number: Optional[str] = None
    occupied_at: Optional[datetime] = None
    occupied_by: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ParkingSpotResponse(ParkingSpotInDB):
    """Parking spot response schema."""
    pass


class OccupySpotRequest(BaseModel):
    """Schema for occupying a parking spot."""
    vehicle_number: str = Field(..., description="Vehicle registration number")
    user_id: Optional[str] = None


class VacateSpotRequest(BaseModel):
    """Schema for vacating a parking spot."""
    vehicle_number: str = Field(..., description="Vehicle registration number")


class ParkingSpotFilter(BaseModel):
    """Schema for filtering parking spots."""
    status: Optional[ParkingSpotStatus] = None
    vehicle_type: Optional[VehicleType] = None
    floor: Optional[int] = None
    section: Optional[str] = None
    is_covered: Optional[bool] = None
    is_disabled_accessible: Optional[bool] = None
    is_ev_charging: Optional[bool] = None
