from config.chroma_client import get_collection
from infra.ports.add_chunks_port import AddChunksPort


class AddChunksAdapter(AddChunksPort):
    def execute(self, chunks: list[str], idioma: str, tipo: str) -> None:
        collection = get_collection()
        ids = [f"{tipo}_{idioma}_{index}" for index in range(len(chunks))]
        metadatas = [{"idioma": idioma, "tipo": tipo} for _ in chunks]
        collection.add(documents=chunks, ids=ids, metadatas=metadatas)
