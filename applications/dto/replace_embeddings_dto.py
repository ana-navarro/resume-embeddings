from pydantic import BaseModel, field_validator

VALID_IDIOMAS = ("pt", "en")
VALID_TIPOS = ("presentation", "curriculo")


class ReplaceEmbeddingsDTO(BaseModel):
    chunks: list[str]
    idioma: str
    tipo: str

    @field_validator("chunks")
    @classmethod
    def validate_chunks(cls, value: list[str]) -> list[str]:
        if not value:
            raise ValueError("A lista de chunks não pode estar vazia.")
        return value

    @field_validator("idioma")
    @classmethod
    def validate_idioma(cls, value: str) -> str:
        if value not in VALID_IDIOMAS:
            raise ValueError("O campo idioma deve ser 'pt' ou 'en'.")
        return value

    @field_validator("tipo")
    @classmethod
    def validate_tipo(cls, value: str) -> str:
        if value not in VALID_TIPOS:
            raise ValueError("O campo tipo deve ser 'presentation' ou 'curriculo'.")
        return value
