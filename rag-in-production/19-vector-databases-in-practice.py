"""
RAG in Production
Chapter 19: Vector Databases in Practice
Section: Embeddings & Indexing

Read this chapter: https://books.vizuara.ai/read/rag-in-production/vector-databases-in-practice

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not in the book; the reader supplies these) ---
# https://books.vizuara.ai/read/rag-in-production/vector-databases-in-practice
emb_1 = None         # TODO: the 1536-dim embedding of the first payload's text
emb_2 = None         # TODO: the 1536-dim embedding of the second payload's text
emb_3 = None         # TODO: the 1536-dim embedding of the third payload's text
query_vector = None  # TODO: the embedded user question - see chapters 15-16

# --- block 1 ---
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(":memory:")   # in-process; swap for url=... in prod
client.create_collection(
    collection_name="docs",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
)

# --- block 2 ---
from qdrant_client.models import PointStruct

client.upsert(
    collection_name="docs",
    points=[
        PointStruct(id=1, vector=emb_1, payload={
            "text": "Model X battery lasts 400 km on a full charge.",
            "source": "handbook_v3.pdf", "year": 2024, "plan": "enterprise"}),
        PointStruct(id=2, vector=emb_2, payload={
            "text": "The 2019 policy capped range claims at 300 km.",
            "source": "policy_2019.pdf", "year": 2019, "plan": "enterprise"}),
        PointStruct(id=3, vector=emb_3, payload={
            "text": "Refund window is 30 days from delivery.",
            "source": "handbook_v3.pdf", "year": 2024, "plan": "starter"}),
    ],
)

# --- block 3 ---
from qdrant_client.models import Filter, FieldCondition, MatchValue

hits = client.query_points(
    collection_name="docs",
    query=query_vector,                    # the embedded user question
    limit=3,                               # top-k
    query_filter=Filter(must=[
        FieldCondition(key="year", match=MatchValue(value=2024)),
        FieldCondition(key="plan", match=MatchValue(value="enterprise")),
    ]),
).points

for h in hits:
    print(h.score, h.payload["source"], h.payload["text"][:40])
