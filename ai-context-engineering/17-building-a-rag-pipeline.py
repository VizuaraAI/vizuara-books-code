"""
AI Context Engineering
Chapter 17: Building a RAG Pipeline End-to-End
Section: Write and Select: RAG

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/building-a-rag-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
docs = [
    "The Engineer plan refund window is 14 days from purchase.",   # d0
    "Enterprise customers get a dedicated Slack channel.",         # d1
    "Free-tier users can access the first two course modules.",    # d2
]

# --- block 2 ---
index = []                                   # our "vector database"
for i, text in enumerate(docs):
    vec = embed(text)                        # SAME model used at query time
    index.append({"id": i, "text": text, "vec": vec})

# --- block 3 ---
def retrieve(question, index, top_k=2):
    q_vec = embed(question)                                  # 1 embed call
    scored = [(cosine(q_vec, r["vec"]), r) for r in index]   # score every chunk
    scored.sort(key=lambda pair: pair[0], reverse=True)      # best first
    return [r for _score, r in scored[:top_k]]               # keep top-k

# --- block 4 ---
def build_prompt(question, chunks):
    context = "\n\n".join(
        f"[source {c['id']}] {c['text']}" for c in chunks   # 1. tag each source
    )
    return (
        "Answer the question using ONLY the context below. "   # 2. ground it
        "If the answer is not in the context, say "
        "\"I don't have that information.\" "
        "Cite the [source N] you used.\n\n"                    # 3. force a citation
        f"Context:\n{context}\n\n"
        f"Question: {question}"
    )

# --- block 5 ---
def answer(question, index):
    chunks = retrieve(question, index, top_k=2)   # 1. select the evidence
    prompt = build_prompt(question, chunks)       # 2. assemble the context
    return model(prompt)                          # 3. generate the answer
