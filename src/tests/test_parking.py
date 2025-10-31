from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.api.v1.routers.parking import router as parking_router

app = FastAPI()
app.include_router(parking_router)

client = TestClient(app)

def test_create_parking_spot():
    response = client.post("/api/v1/parking", json={"name": "Spot A", "location": "Location A"})
    assert response.status_code == 201
    assert response.json()["name"] == "Spot A"

def test_get_parking_spots():
    response = client.get("/api/v1/parking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_parking_spot():
    response = client.post("/api/v1/parking", json={"name": "Spot B", "location": "Location B"})
    parking_id = response.json()["id"]
    response = client.put(f"/api/v1/parking/{parking_id}", json={"name": "Updated Spot B"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Spot B"

def test_delete_parking_spot():
    response = client.post("/api/v1/parking", json={"name": "Spot C", "location": "Location C"})
    parking_id = response.json()["id"]
    response = client.delete(f"/api/v1/parking/{parking_id}")
    assert response.status_code == 204

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}