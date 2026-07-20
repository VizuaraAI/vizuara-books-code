"""
RAG in Production
Chapter 20: Building the Index
Section: Embeddings & Indexing

Read this chapter: https://books.vizuara.ai/read/rag-in-production/building-the-index

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")   # 384-dim vectors

chunks = [
    "The Model X battery lasts 400 kilometres on a full charge.",
    "Charging from 10% to 80% takes about 30 minutes on a fast charger.",
    "The car seats five adults and has 2000 litres of cargo space.",
    "Our return policy allows refunds within 30 days of delivery.",
]

vectors = model.encode(
    chunks,
    batch_size=64,             # embed up to 64 chunks per forward pass
    normalize_embeddings=True, # L2-normalize → cosine == dot product
    show_progress_bar=True,
)
print(vectors.shape)           # (4, 384)

# --- block 2 ---
records = []
for i, (chunk, vec) in enumerate(zip(chunks, vectors)):
    records.append({
        "id": f"c{i}",                       # stable, unique
        "vector": vec.tolist(),              # the 384-dim address
        "text": chunk,                       # what we actually return
        "metadata": {"source": "manual.pdf", "chunk_index": i},
    })

# --- block 3 ---
import chromadb

client = chromadb.Client()
index = client.create_collection(
    name="car_manual",
    metadata={"hnsw:space": "cosine"},   # match the metric to our normalized vectors
)

index.upsert(
    ids=[r["id"] for r in records],
    embeddings=[r["vector"] for r in records],
    documents=[r["text"] for r in records],
    metadatas=[r["metadata"] for r in records],
)
print(index.count())   # 4

# --- block 4 ---
query = "how far can it drive?"
q_vec = model.encode([query], normalize_embeddings=True)   # (1, 384), unit length

results = index.query(
    query_embeddings=q_vec.tolist(),
    n_results=2,                        # top-k = 2
    include=["documents", "distances"],
)
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(round(dist, 3), doc)
