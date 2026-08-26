from abc import ABC, abstractmethod


class ReplaceEmbeddingsPort(ABC):
    @abstractmethod
    def execute(self, chunks: list[str], idioma: str, tipo: str) -> None:
        raise NotImplementedError
