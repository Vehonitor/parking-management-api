# File: /parking-management-api/parking-management-api/src/tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client