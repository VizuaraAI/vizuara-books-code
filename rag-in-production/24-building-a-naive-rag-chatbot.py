"""
RAG in Production
Chapter 24: Building a Naive RAG Chatbot
Section: Retrieval & Generation

Read this chapter: https://books.vizuara.ai/read/rag-in-production/building-a-naive-rag-chatbot

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/building-a-naive-rag-chatbot
VectorStore = None                  # TODO: a local vector index class - see chapters 19-20
chunk_document = None               # TODO: the chunker from chapters 11-14
embed = None                        # TODO: your embedding function - see chapters 15-16
assemble_context = None             # TODO: the context packer from chapter 22
SYSTEM_GROUNDING_INSTRUCTION = None  # TODO: the grounding system prompt from chapter 23
generate = None                     # TODO: your LLM call, returning the answer text

# --- block 1 ---
# BUILD TIME — run once, save the result
def build_index(documents):
    index = VectorStore(dim=384)               # local vector index
    for doc in documents:
        for chunk in chunk_document(doc):       # ingestion + chunking
            vec = embed(chunk.text)             # SAME model as at query time
            index.add(vec, payload=chunk)       # store vector + text + metadata
    index.save("corpus.index")

# --- block 2 ---
# QUERY TIME — run per user message
def answer(question, index):
    q_vec   = embed(question)                          # 1. retrieval: embed query
    hits    = index.search(q_vec, k=4)                 # 2. top-k nearest chunks
    context = assemble_context(hits)                   # 3. augmentation: pack the prompt
    prompt  = f"{SYSTEM_GROUNDING_INSTRUCTION}\n\n{context}\n\nQuestion: {question}"
    return generate(prompt)                             # 4. grounded generation

# --- block 3 ---
def contextualize(history, question):
    prompt = (
        "Given the chat history and a follow-up question, rewrite the "
        "follow-up as a standalone question. Do NOT answer it.\n\n"
        f"History:\n{history}\n\nFollow-up: {question}\n\nStandalone question:"
    )
    return generate(prompt).strip()

# --- block 4 ---
class NaiveRAGChatbot:
    def __init__(self, index):
        self.index = index
        self.history = []                      # the state layer

    def chat(self, question):
        standalone = contextualize(self.history, question)   # seam 1: rewrite
        q_vec   = embed(standalone)                          # retrieval
        hits    = self.index.search(q_vec, k=4)              # top-k
        context = assemble_context(hits)                     # augmentation
        prompt  = f"{SYSTEM_GROUNDING_INSTRUCTION}\n\n{context}\n\nQuestion: {standalone}"
        answer  = generate(prompt)                           # grounded generation
        self.history.append((question, answer))              # seam 2: remember
        return answer
