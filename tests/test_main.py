from fastapi.testclient import TestClient
import sys
import os

# Adds src directory to the path so we can import main
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "DevOps API is running"} [cite: 258, 260, 263]

def test_add():
    response = client.get("/add?a=10&b=5")
    assert response.status_code == 200
    assert response.json()["result"] == 15 [cite: 268, 269]
