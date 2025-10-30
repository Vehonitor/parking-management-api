from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.v1.routers import auth, parking, health

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(parking.router, prefix="/api/v1/parking", tags=["parking"])
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])