from unittest.mock import MagicMock, patch

import pytest

from config.chroma_client import COLLECTION_NAME, get_chroma_client, get_collection


def test_get_chroma_client_builds_client_from_env_vars(monkeypatch):
    monkeypatch.setenv("CHROMA_API_KEY", "test-key")
    monkeypatch.setenv("CHROMA_TENANT", "test-tenant")
    monkeypatch.setenv("CHROMA_DATABASE", "test-database")

    fake_client = MagicMock()
    with patch(
        "config.chroma_client.chromadb.CloudClient", return_value=fake_client
    ) as mock_cloud_client:
        client = get_chroma_client()

    mock_cloud_client.assert_called_once_with(
        api_key="test-key", tenant="test-tenant", database="test-database"
    )
    assert client is fake_client


@pytest.mark.parametrize("missing_var", ["CHROMA_API_KEY", "CHROMA_TENANT", "CHROMA_DATABASE"])
def test_get_chroma_client_raises_when_a_required_var_is_missing(monkeypatch, missing_var):
    monkeypatch.setenv("CHROMA_API_KEY", "test-key")
    monkeypatch.setenv("CHROMA_TENANT", "test-tenant")
    monkeypatch.setenv("CHROMA_DATABASE", "test-database")
    monkeypatch.delenv(missing_var)

    with pytest.raises(RuntimeError, match=missing_var):
        get_chroma_client()


def test_get_collection_creates_or_gets_the_expected_collection(monkeypatch):
    monkeypatch.setenv("CHROMA_API_KEY", "test-key")
    monkeypatch.setenv("CHROMA_TENANT", "test-tenant")
    monkeypatch.setenv("CHROMA_DATABASE", "test-database")

    fake_collection = MagicMock()
    fake_client = MagicMock()
    fake_client.get_or_create_collection.return_value = fake_collection

    with patch("config.chroma_client.chromadb.CloudClient", return_value=fake_client):
        collection = get_collection()

    fake_client.get_or_create_collection.assert_called_once_with(COLLECTION_NAME)
    assert collection is fake_collection
