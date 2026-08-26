from fastapi import APIRouter

from applications.controllers.replace_embeddings_controller import (
    ReplaceEmbeddingsController,
)
from applications.dto.replace_embeddings_dto import ReplaceEmbeddingsDTO
from domain.usecases.replace_embeddings_usecase import ReplaceEmbeddingsUseCase
from infra.adapters.add_chunks_adapter import AddChunksAdapter
from infra.adapters.delete_chunks_adapter import DeleteChunksAdapter

router = APIRouter()

_usecase = ReplaceEmbeddingsUseCase(
    delete_chunks=DeleteChunksAdapter(), add_chunks=AddChunksAdapter()
)
_controller = ReplaceEmbeddingsController(_usecase)


@router.post("/embeddings/replace")
def replace_embeddings(payload: ReplaceEmbeddingsDTO):
    return _controller.handle(payload.chunks, payload.idioma, payload.tipo)
