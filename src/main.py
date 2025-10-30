from fastapi import FastAPI
from src.api.v1.routers import parking

app = FastAPI(title="Parking Management API")

app.include_router(parking.router, prefix="/api/v1/parking")

@app.get("/")
def root():
    return {"message": "Parking Management API is running"}
