"""
LLM Production & Deployment
Chapter 28: Building a RAG Web App
Section: RAG in Production

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/building-a-rag-web-app

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
from sentence_transformers import SentenceTransformer
from fastapi.responses import StreamingResponse

app = None                # TODO: the FastAPI application object.
ChatRequest = None        # TODO: the pydantic request body with a `.message`.
GROUNDED_TEMPLATE = None  # TODO: the grounded prompt template from Chapter 27.
LLMClient = None          # TODO: the vLLM / API client wrapper.
load_index = None         # TODO: loads the FAISS index + chunks built offline.
# --- end fixups ---

# --- block 1 ---
# Loaded ONCE when the server process boots — never inside the handler.
embedder = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
index, chunks = load_index("index.faiss", "chunks.json")   # the build artifact
llm = LLMClient()                                          # vLLM / API client

@app.post("/chat")
def chat(req: ChatRequest):
    q_vec = embedder.encode([req.message])          # one short string -> (1, 768)
    top = index.search(q_vec, k=4)                  # milliseconds
    context = "\n\n".join(chunks[i] for i in top)   # the k retrieved passages
    prompt = GROUNDED_TEMPLATE.format(context=context, question=req.message)
    return StreamingResponse(llm.stream(prompt))    # tokens flow as they generate
