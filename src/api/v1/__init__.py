# File: /parking-management-api/parking-management-api/src/api/v1/__init__.py

from fastapi import APIRouter

router = APIRouter()

from .routers import auth, parking, health

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(parking.router, prefix="/parking", tags=["parking"])
router.include_router(health.router, prefix="/health", tags=["health"])