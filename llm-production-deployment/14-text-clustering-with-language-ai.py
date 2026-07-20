"""
LLM Production & Deployment
Chapter 14: Text Clustering with Language AI
Section: Clustering & Topic Modeling

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/text-clustering-with-language-ai

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
docs = None  # TODO: the list of documents to cluster - your own corpus.
# --- end fixups ---

# --- block 1 ---
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
embeddings = model.encode(docs)   # (N, 768) — one vector per document

# --- block 2 ---
import numpy as np
# 6 docs, d = 4 toy embeddings (really 768)
X = np.array([
    [0.9, 0.1, 0.0, 0.1],   # "my card was declined"
    [0.8, 0.2, 0.1, 0.0],   # "the payment didn't go through"
    [0.1, 0.9, 0.1, 0.0],   # "I want to return my order"
    [0.0, 0.8, 0.2, 0.1],   # "how do I send this back"
    [0.1, 0.0, 0.9, 0.1],   # "my package is taking forever"
    [0.0, 0.1, 0.8, 0.2],   # "delivery is really slow"
])

# --- block 3 ---
import umap
reducer = umap.UMAP(n_components=5, n_neighbors=15, metric="cosine")
reduced = reducer.fit_transform(embeddings)   # (N, 768) -> (N, 5)

# --- block 4 ---
from hdbscan import HDBSCAN
clusterer = HDBSCAN(min_cluster_size=50, metric="euclidean")
labels = clusterer.fit_predict(reduced)   # e.g. [0,0,1,1,2,2] ; -1 = noise
