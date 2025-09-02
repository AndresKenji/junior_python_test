
import pytest
from fastapi.testclient import TestClient
from api import app, items

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_items():
    items.clear()
    yield
    items.clear()

class TestRootEndpoint:
    
    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Bienvenido a la Prueba Técnica de Python API"}

class TestItemsEndpoints:
    def test_get_empty_items(self):
        response = client.get("/items")
        assert response.status_code == 200
        assert response.json() == []
    
    def test_create_item(self):
        item_data = {
            "name": "Laptop",
            "description": "Computadora portátil",
            "price": 999.99,
            "tax": 99.99
        }
        response = client.post("/items", json=item_data)
        assert response.status_code == 200
        
        response_data = response.json()
        assert response_data["name"] == item_data["name"]
        assert response_data["description"] == item_data["description"]
        assert response_data["price"] == item_data["price"]
        assert response_data["tax"] == item_data["tax"]
    
    def test_create_item_without_optional_fields(self):
        item_data = {
            "name": "Mouse",
            "price": 25.50
        }
        response = client.post("/items", json=item_data)
        assert response.status_code == 200
        
        response_data = response.json()
        assert response_data["name"] == "Mouse"
        assert response_data["price"] == 25.50
        assert response_data["description"] is None
        assert response_data["tax"] is None
    
    def test_create_multiple_items_and_get_all(self):
        item1 = {
            "name": "Teclado",
            "description": "Teclado mecánico",
            "price": 75.00,
            "tax": 7.50
        }
        response1 = client.post("/items", json=item1)
        assert response1.status_code == 200
        
        item2 = {
            "name": "Monitor",
            "price": 299.99
        }
        response2 = client.post("/items", json=item2)
        assert response2.status_code == 200
        
        response = client.get("/items")
        assert response.status_code == 200
        
        items_list = response.json()
        assert len(items_list) == 2
        assert items_list[0]["name"] == "Teclado"
        assert items_list[1]["name"] == "Monitor"
    
    def test_get_item_by_index(self):
        item_data = {
            "name": "Smartphone",
            "description": "Teléfono inteligente",
            "price": 599.99,
            "tax": 59.99
        }
        client.post("/items", json=item_data)
        
        response = client.get("/items/0")
        assert response.status_code == 200
        
        response_data = response.json()
        assert response_data["name"] == "Smartphone"
        assert response_data["price"] == 599.99
    
    def test_get_item_by_invalid_index(self):
        response = client.get("/items/0")
        assert response.status_code == 200
        assert response.json() == {"error": "Item not found"}
        
        item_data = {
            "name": "Tablet",
            "price": 399.99
        }
        client.post("/items", json=item_data)
        
        response = client.get("/items/5")
        assert response.status_code == 200
        assert response.json() == {"error": "Item not found"}
        
        response = client.get("/items/-1")
        assert response.status_code == 200
        assert response.json() == {"error": "Item not found"}

class TestItemValidation:
    def test_create_item_missing_required_fields(self):
        item_data = {
            "price": 100.0
        }
        response = client.post("/items", json=item_data)
        assert response.status_code == 422  
        
        item_data = {
            "name": "Item sin precio"
        }
        response = client.post("/items", json=item_data)
        assert response.status_code == 422
    
    def test_create_item_invalid_price_type(self):
        item_data = {
            "name": "Item con precio inválido",
            "price": "no es un número"
        }
        response = client.post("/items", json=item_data)
        assert response.status_code == 422

class TestAdvancedScenarios:
    
    def test_create_100_items_performance(self):
        for i in range(100):
            item_data = {
                "name": f"Item {i}",
                "description": f"Descripción del item {i}",
                "price": 10.0 + i,
                "tax": 1.0 + (i * 0.1)
            }
            response = client.post("/items", json=item_data)
            assert response.status_code == 200
        
        response = client.get("/items")
        assert response.status_code == 200
        items_list = response.json()
        assert len(items_list) == 100
        
        assert items_list[0]["name"] == "Item 0"
        assert items_list[50]["name"] == "Item 50"
        assert items_list[99]["name"] == "Item 99"
    
    def test_business_logic_total_value(self):
        items_data = [
            {"name": "Item1", "price": 100.0, "tax": 10.0},
            {"name": "Item2", "price": 200.0, "tax": 20.0},
            {"name": "Item3", "price": 50.0, "tax": 5.0}
        ]
        
        for item_data in items_data:
            client.post("/items", json=item_data)

        response = client.get("/items")
        assert len(response.json()) == 3

def test_api_integration():

    response = client.get("/")
    assert response.status_code == 200
    
    response = client.get("/items")
    assert len(response.json()) == 0
    
    items_to_create = [
        {"name": "Producto A", "price": 100.0, "tax": 21.0},
        {"name": "Producto B", "price": 50.0, "description": "Producto de prueba"},
        {"name": "Producto C", "price": 75.0, "tax": 15.75, "description": "Producto completo"}
    ]
    
    for item in items_to_create:
        response = client.post("/items", json=item)
        assert response.status_code == 200
    
    response = client.get("/items")
    assert len(response.json()) == 3
    
    for i in range(3):
        response = client.get(f"/items/{i}")
        assert response.status_code == 200
        assert "name" in response.json()
