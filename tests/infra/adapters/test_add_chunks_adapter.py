from unittest.mock import MagicMock, patch

from infra.adapters.add_chunks_adapter import AddChunksAdapter


def test_execute_adds_documents_with_ids_and_metadata():
    fake_collection = MagicMock()

    with patch(
        "infra.adapters.add_chunks_adapter.get_collection", return_value=fake_collection
    ):
        AddChunksAdapter().execute(["chunk one", "chunk two"], "pt", "curriculo")

    fake_collection.add.assert_called_once_with(
        documents=["chunk one", "chunk two"],
        ids=["curriculo_pt_0", "curriculo_pt_1"],
        metadatas=[
            {"idioma": "pt", "tipo": "curriculo"},
            {"idioma": "pt", "tipo": "curriculo"},
        ],
    )
