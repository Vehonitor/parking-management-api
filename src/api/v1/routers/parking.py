from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.api.v1.schemas.parking import ParkingSpotCreate, ParkingSpot, ParkingSpotUpdate
from src.services.parking_service import ParkingService
from src.api.v1.dependencies import get_current_user

router = APIRouter()
parking_service = ParkingService()

@router.post("/", response_model=ParkingSpot)
async def create_parking_spot(parking_spot: ParkingSpotCreate, current_user: str = Depends(get_current_user)):
    return await parking_service.create_parking_spot(parking_spot, current_user)

@router.get("/", response_model=List[ParkingSpot])
async def list_parking_spots():
    return await parking_service.get_parking_spots()

@router.put("/{parking_spot_id}", response_model=ParkingSpot)
async def update_parking_spot(parking_spot_id: int, parking_spot: ParkingSpotUpdate, current_user: str = Depends(get_current_user)):
    updated_spot = await parking_service.update_parking_spot(parking_spot_id, parking_spot, current_user)
    if not updated_spot:
        raise HTTPException(status_code=404, detail="Parking spot not found")
    return updated_spot

@router.delete("/{parking_spot_id}", response_model=dict)
async def delete_parking_spot(parking_spot_id: int, current_user: str = Depends(get_current_user)):
    success = await parking_service.delete_parking_spot(parking_spot_id, current_user)
    if not success:
        raise HTTPException(status_code=404, detail="Parking spot not found")
    return {"message": "Parking spot deleted successfully"}