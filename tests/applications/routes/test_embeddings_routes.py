from unittest.mock import Mock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from applications.routes import embeddings_routes


def _build_app():
    app = FastAPI()
    app.include_router(embeddings_routes.router)
    return app


def test_replace_embeddings_returns_200_on_success(monkeypatch):
    fake_controller = Mock()
    fake_controller.handle.return_value = {
        "status": "replaced",
        "idioma": "pt",
        "tipo": "curriculo",
    }
    monkeypatch.setattr(embeddings_routes, "_controller", fake_controller)

    client = TestClient(_build_app())
    response = client.post(
        "/embeddings/replace",
        json={"chunks": ["a", "b"], "idioma": "pt", "tipo": "curriculo"},
    )

    assert response.status_code == 200
    assert response.json() == {"status": "replaced", "idioma": "pt", "tipo": "curriculo"}
    fake_controller.handle.assert_called_once_with(["a", "b"], "pt", "curriculo")


def test_replace_embeddings_returns_422_on_invalid_payload():
    client = TestClient(_build_app())
    response = client.post(
        "/embeddings/replace",
        json={"chunks": [], "idioma": "pt", "tipo": "curriculo"},
    )

    assert response.status_code == 422
