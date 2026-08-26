from domain.ports.replace_embeddings_port import ReplaceEmbeddingsPort


class ReplaceEmbeddingsController:
    def __init__(self, replace_embeddings: ReplaceEmbeddingsPort) -> None:
        self._replace_embeddings = replace_embeddings

    def handle(self, chunks: list[str], idioma: str, tipo: str) -> dict:
        self._replace_embeddings.execute(chunks, idioma, tipo)
        return {"status": "replaced", "idioma": idioma, "tipo": tipo}
