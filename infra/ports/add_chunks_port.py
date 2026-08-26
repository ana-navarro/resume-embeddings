from abc import ABC, abstractmethod


class AddChunksPort(ABC):
    @abstractmethod
    def execute(self, chunks: list[str], idioma: str, tipo: str) -> None:
        raise NotImplementedError
