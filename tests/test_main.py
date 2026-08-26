from fastapi.testclient import TestClient

from main import app


def test_root_returns_hello_message():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"mensagem": "Olá, Mundo!"}
