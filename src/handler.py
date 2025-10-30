from fastapi import FastAPI
from mangum import Mangum
from api.v1.routers import auth, parking, health

app = FastAPI()

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(parking.router, prefix="/api/v1/parking", tags=["parking"])
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])

handler = Mangum(app)