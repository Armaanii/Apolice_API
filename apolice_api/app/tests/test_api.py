import pytest
from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_produto_invalido():
    payload = {
        "produto": 999,  # Produto que não existe
        "item": {},
        "valores": {
            "precoTotal": 1000.0,
            "parcelas": 5
        }
    }

    response = client.post("/emitir", json=payload)
    assert response.status_code == 400
    assert response.json() == {"detail": "Produto não suportado"}
