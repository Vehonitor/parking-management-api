from fastapi import HTTPException
from fastapi.testclient import TestClient
from src.main import app
from src.services.auth_service import AuthService

client = TestClient(app)

def test_signup_success():
    response = client.post("/api/v1/auth/signup", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 201
    assert "access_token" in response.json()

def test_signup_user_already_exists():
    client.post("/api/v1/auth/signup", json={
        "username": "testuser",
        "password": "testpassword"
    })
    response = client.post("/api/v1/auth/signup", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}

def test_login_success():
    client.post("/api/v1/auth/signup", json={
        "username": "testuser",
        "password": "testpassword"
    })
    response = client.post("/api/v1/auth/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_credentials():
    response = client.post("/api/v1/auth/login", json={
        "username": "testuser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}