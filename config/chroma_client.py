import os

import chromadb
from chromadb.api.models.Collection import Collection
from dotenv import load_dotenv

load_dotenv()

REQUIRED_ENV_VARS = ("CHROMA_API_KEY", "CHROMA_TENANT", "CHROMA_DATABASE")
COLLECTION_NAME = "resume_content"


def get_chroma_client() -> chromadb.CloudClient:
    missing = [name for name in REQUIRED_ENV_VARS if not os.getenv(name)]
    if missing:
        raise RuntimeError(
            "Missing required ChromaDB environment variable(s): "
            f"{', '.join(missing)}. Copy .env.example to .env and fill in the real values."
        )

    return chromadb.CloudClient(
        api_key=os.environ["CHROMA_API_KEY"],
        tenant=os.environ["CHROMA_TENANT"],
        database=os.environ["CHROMA_DATABASE"],
    )


def get_collection() -> Collection:
    return get_chroma_client().get_or_create_collection(COLLECTION_NAME)
