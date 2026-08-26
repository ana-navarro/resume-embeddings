# resume-embeddings

## Papel no ecossistema (PT)

Serviço Vetorial do Currículo Interativo. Gera embeddings locais a partir dos chunks de texto recebidos
e gerencia o banco de dados vetorial (ChromaDB) usado nas buscas semânticas que alimentam as respostas do
assistente de IA (ver Constitution Principle I, `.specify/memory/constitution.md`).

Fluxo de chamadas estrito (Constitution Principle II): `Frontend → bff → orchestrator → (guard-rails,
embeddings, llm-engine)`. Este serviço só deve ser chamado pelo `resume-orchestrator` (para buscas
semânticas) e pelo `resume-injections` (para substituição de embeddings ao trocar o currículo).

## Status atual

Stub inicial (FastAPI "Hello World", `main.py`) — nenhuma lógica de geração/gestão de embeddings foi
implementada ainda, incluindo o endpoint `POST /embeddings/replace` do qual `resume-injections` já
depende (ver `tasks/upload-replace-presentation/task.md`). A estrutura hexagonal completa
(`applications/`, `domain/`, `infra/`, `config/`) descrita na Constitution Principle II ainda não foi
criada neste serviço.

## Stack

- Python + FastAPI
- ChromaDB (banco vetorial, ainda não integrado)

## Como rodar localmente

```sh
python -m venv .venv
.venv/Scripts/activate       # Windows
# source .venv/bin/activate  # Linux/Mac
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload
```

## Role in the ecosystem (EN)

The vector service. Generates local embeddings from text chunks and manages the vector database
(ChromaDB) used for the semantic searches that power the AI assistant's answers. Currently a stub — only
the FastAPI "Hello World" endpoint exists; `resume-injections` already depends on a
`POST /embeddings/replace` endpoint here that has not been built yet.
