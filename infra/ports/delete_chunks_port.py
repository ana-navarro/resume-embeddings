from abc import ABC, abstractmethod


class DeleteChunksPort(ABC):
    @abstractmethod
    def execute(self, idioma: str, tipo: str) -> None:
        raise NotImplementedError
