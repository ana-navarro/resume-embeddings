from unittest.mock import MagicMock, patch

from infra.adapters.delete_chunks_adapter import DeleteChunksAdapter


def test_execute_deletes_chunks_matching_idioma_and_tipo():
    fake_collection = MagicMock()

    with patch(
        "infra.adapters.delete_chunks_adapter.get_collection", return_value=fake_collection
    ):
        DeleteChunksAdapter().execute("pt", "curriculo")

    fake_collection.delete.assert_called_once_with(
        where={"$and": [{"idioma": "pt"}, {"tipo": "curriculo"}]}
    )
