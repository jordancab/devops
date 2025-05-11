from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={
        "id": 1,
        "name": "Laptop",
        "price": 1200.99,
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Laptop"

def test_get_item():
    client.post("/items", json={
        "id": 2,
        "name": "Mouse",
        "price": 25.5,
        "in_stock": True
    })
    response = client.get("/items/2")
    assert response.status_code == 200
    assert response.json()["name"] == "Mouse"

def test_update_item():
    client.post("/items", json={
        "id": 3,
        "name": "Keyboard",
        "price": 45.0,
        "in_stock": True
    })
    response = client.put("/items/3", json={
        "id": 3,
        "name": "Mechanical Keyboard",
        "price": 75.0,
        "in_stock": False
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Mechanical Keyboard"

def test_delete_item():
    client.post("/items", json={
        "id": 4,
        "name": "Monitor",
        "price": 300.0,
        "in_stock": True
    })
    response = client.delete("/items/4")
    assert response.status_code == 200
    assert response.json()["message"] == "Item deleted"
