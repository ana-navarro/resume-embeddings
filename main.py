from fastapi import FastAPI

from applications.routes.embeddings_routes import router as embeddings_router

app = FastAPI()


@app.get("/")
def ler_raiz():
  return {"mensagem": "Olá, Mundo!"}


app.include_router(embeddings_router)
