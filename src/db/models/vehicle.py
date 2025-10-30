

# ============================================================================
# FILE: src/api/v1/schemas/vehicle.py
# ============================================================================
from pydantic import BaseModel, Field
from typing import Optional
from src.db.models.vehicle import VehicleTypeEnum

class VehicleBase(BaseModel):
    nick_name: Optional[str] = Field(None, max_length=100)
    vehicle_type: VehicleTypeEnum
    model: Optional[str] = Field(None, max_length=50)
    registration_no: str = Field(..., max_length=20)

class VehicleCreate(VehicleBase):
    pass

class VehicleUpdate(BaseModel):
    nick_name: Optional[str] = None
    vehicle_type: Optional[VehicleTypeEnum] = None
    model: Optional[str] = None

class VehicleResponse(VehicleBase):
    vehicle_id: int
    user_id: int

    class Config:
        from_attributes = True
