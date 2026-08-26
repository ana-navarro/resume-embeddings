from unittest.mock import Mock

from applications.controllers.replace_embeddings_controller import (
    ReplaceEmbeddingsController,
)


def test_handle_calls_usecase_and_returns_status():
    replace_embeddings = Mock()
    controller = ReplaceEmbeddingsController(replace_embeddings)

    result = controller.handle(["a", "b"], "pt", "curriculo")

    replace_embeddings.execute.assert_called_once_with(["a", "b"], "pt", "curriculo")
    assert result == {"status": "replaced", "idioma": "pt", "tipo": "curriculo"}
