"""
This is a test file for the main module.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Duke"}

def test_add():
    """Test the add endpoint"""
    response = client.get("/add/2/3")
    assert response.status_code == 200
    assert response.json() == {"total": 5}

