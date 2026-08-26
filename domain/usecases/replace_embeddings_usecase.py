from domain.ports.replace_embeddings_port import ReplaceEmbeddingsPort
from infra.ports.add_chunks_port import AddChunksPort
from infra.ports.delete_chunks_port import DeleteChunksPort


class ReplaceEmbeddingsUseCase(ReplaceEmbeddingsPort):
    def __init__(self, delete_chunks: DeleteChunksPort, add_chunks: AddChunksPort) -> None:
        self._delete_chunks = delete_chunks
        self._add_chunks = add_chunks

    def execute(self, chunks: list[str], idioma: str, tipo: str) -> None:
        # Substituição: apaga os chunks existentes deste idioma+tipo antes de inserir os
        # novos, garantindo idempotência (chamadas repetidas nunca acumulam duplicatas).
        self._delete_chunks.execute(idioma, tipo)
        self._add_chunks.execute(chunks, idioma, tipo)
