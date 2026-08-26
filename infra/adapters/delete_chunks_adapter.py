from config.chroma_client import get_collection
from infra.ports.delete_chunks_port import DeleteChunksPort


class DeleteChunksAdapter(DeleteChunksPort):
    def execute(self, idioma: str, tipo: str) -> None:
        collection = get_collection()
        collection.delete(where={"$and": [{"idioma": idioma}, {"tipo": tipo}]})
