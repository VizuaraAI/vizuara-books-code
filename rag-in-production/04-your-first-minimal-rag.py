"""
RAG in Production
Chapter 4: Your First Minimal RAG
Section: RAG Foundations

Read this chapter: https://books.vizuara.ai/read/rag-in-production/your-first-minimal-rag

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
docs = [
    "Nimbus is a note-taking app. The free plan allows up to 3 notebooks.",
    "Nimbus Pro costs 8 dollars per month and unlocks unlimited notebooks.",
    "Nimbus stores all notes locally and syncs over end-to-end encryption.",
]

# --- block 2 ---
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_vecs = model.encode(docs, normalize_embeddings=True)   # shape (3, 384)

# --- block 3 ---
q = "How much does the paid plan cost?"
q_vec = model.encode([q], normalize_embeddings=True)   # shape (1, 384)

scores = doc_vecs @ q_vec.T          # cosine similarity, since vectors are unit-length
top = int(scores.argmax())           # index of the single best chunk

# --- block 4 ---
context = docs[top]
prompt = f"""Answer the question using ONLY the context below.
If the context does not contain the answer, say "I don't know."

Context:
{context}

Question: {q}
Answer:"""

# --- block 5 ---
from openai import OpenAI
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
)
print(resp.choices[0].message.content)
# → "The paid plan, Nimbus Pro, costs 8 dollars per month."

# --- block 6 ---
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import numpy as np

docs = [                                                        # 1. ingest (already clean)
    "Nimbus is a note-taking app. The free plan allows up to 3 notebooks.",
    "Nimbus Pro costs 8 dollars per month and unlocks unlimited notebooks.",
    "Nimbus stores all notes locally and syncs over end-to-end encryption.",
]                                                               # 2. chunk (1 doc = 1 chunk)

embedder = SentenceTransformer("all-MiniLM-L6-v2")
doc_vecs = embedder.encode(docs, normalize_embeddings=True)     # 3+4. embed + index

q = "How much does the paid plan cost?"
q_vec = embedder.encode([q], normalize_embeddings=True)
top = int((doc_vecs @ q_vec.T).argmax())                        # 5. retrieve (top-k=1)

prompt = (                                                      # 6. augment
    'Answer using ONLY the context. If it is missing, say "I don\'t know".\n\n'
    f"Context: {docs[top]}\n\nQuestion: {q}\nAnswer:"
)

client = OpenAI()
answer = client.chat.completions.create(                        # 7. generate
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
).choices[0].message.content
print(answer)
