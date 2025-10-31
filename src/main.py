from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.routers import auth
# from src.api.v1.routers import (
#     auth, users, vehicles, parking_zones, parking_profiles,
#     schedules, bookings, checkinout, payments, chat, health
# )

app = FastAPI(
    title="Parking Management API",
    description="API for managing parking zones, bookings, and payments",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
# Include routers
# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])

# app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
# app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
# app.include_router(vehicles.router, prefix="/api/v1/vehicles", tags=["Vehicles"])
# app.include_router(parking_zones.router, prefix="/api/v1/parking-zones", tags=["Parking Zones"])
# app.include_router(parking_profiles.router, prefix="/api/v1/parking-profiles", tags=["Parking Profiles"])
# app.include_router(schedules.router, prefix="/api/v1/schedules", tags=["Schedules"])
# app.include_router(bookings.router, prefix="/api/v1/bookings", tags=["Bookings"])
# app.include_router(checkinout.router, prefix="/api/v1/checkinout", tags=["Check-In/Out"])
# app.include_router(payments.router, prefix="/api/v1/payments", tags=["Payments"])
# app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
# app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])

@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    print("🚀 Application starting...")
    print("📦 Database: PostgreSQL")
    print("🔗 Connected to RDS")

@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    print("👋 Application shutting down...")

@app.get("/")
async def root():
    return {
        "message": "Welcome to Parking Management API",
        "version": "1.0.0",
        "database": "PostgreSQL",
        "docs": "/docs"
    }
=======
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(parking.router, prefix="/api/v1/parking", tags=["parking"])
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])
>>>>>>> 1c47c5c (first commit)
