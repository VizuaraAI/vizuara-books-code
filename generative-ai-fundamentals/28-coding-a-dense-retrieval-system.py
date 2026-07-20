"""
Generative AI Fundamentals
Chapter 28: Coding a Dense Retrieval System
Section: Semantic Search & Dense Retrieval

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/coding-a-dense-retrieval-system

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sentence_transformers import SentenceTransformer
import numpy as np

docs = [
    "How to reset your password",
    "Our refund and return policy",
    "Recovering a locked account",
    "Store opening hours and locations",
    "Setting up two-factor authentication",
]

model = SentenceTransformer("all-MiniLM-L6-v2")
doc_vecs = model.encode(docs, normalize_embeddings=True)   # shape (5, 384)

# --- block 2 ---
query = "I forgot my login credentials"
q = model.encode([query], normalize_embeddings=True)   # shape (1, 384)

scores = doc_vecs @ q.T          # (5, 384) · (384, 1) = (5, 1): one dot product per doc
scores = scores.ravel()          # -> 5 numbers, each a cosine similarity in [-1, 1]
top_k = scores.argsort()[::-1][:3]   # indices of the 3 highest scores

for i in top_k:
    print(f"{scores[i]:.3f}  {docs[i]}")

# --- block 3 ---
import faiss

d = doc_vecs.shape[1]                 # 384
index = faiss.IndexFlatIP(d)          # IP = inner product = cosine, since we normalized
index.add(doc_vecs)                   # store the corpus vectors

scores, ids = index.search(q, k=3)    # returns top-3 (scores, doc indices)
