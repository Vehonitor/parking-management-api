from fastapi import APIRouter
from src.api.v1.routers import  auth, parking

# Create main API router
api_router = APIRouter(prefix="/api/v1")

# Include all routers
# api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(parking.router)