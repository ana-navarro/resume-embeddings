from unittest.mock import Mock

from domain.usecases.replace_embeddings_usecase import ReplaceEmbeddingsUseCase


def test_execute_deletes_before_adding_the_new_chunks():
    delete_chunks = Mock()
    add_chunks = Mock()
    usecase = ReplaceEmbeddingsUseCase(delete_chunks=delete_chunks, add_chunks=add_chunks)

    manager = Mock()
    manager.attach_mock(delete_chunks, "delete_chunks")
    manager.attach_mock(add_chunks, "add_chunks")

    usecase.execute(["chunk one", "chunk two"], "pt", "curriculo")

    delete_chunks.execute.assert_called_once_with("pt", "curriculo")
    add_chunks.execute.assert_called_once_with(["chunk one", "chunk two"], "pt", "curriculo")
    assert manager.mock_calls[0][0] == "delete_chunks.execute"
    assert manager.mock_calls[1][0] == "add_chunks.execute"
