import pytest
from pydantic import ValidationError

from applications.dto.replace_embeddings_dto import ReplaceEmbeddingsDTO


def test_valid_payload_passes_validation():
    dto = ReplaceEmbeddingsDTO(chunks=["a", "b"], idioma="pt", tipo="curriculo")
    assert dto.chunks == ["a", "b"]


def test_rejects_empty_chunks_list():
    with pytest.raises(ValidationError):
        ReplaceEmbeddingsDTO(chunks=[], idioma="pt", tipo="curriculo")


def test_rejects_invalid_idioma():
    with pytest.raises(ValidationError):
        ReplaceEmbeddingsDTO(chunks=["a"], idioma="fr", tipo="curriculo")


def test_rejects_invalid_tipo():
    with pytest.raises(ValidationError):
        ReplaceEmbeddingsDTO(chunks=["a"], idioma="pt", tipo="unknown")
