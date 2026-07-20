"""
Generative AI Fundamentals
Chapter 13: Text Clustering with LLMs
Section: Text Clustering & Topic Modeling

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/text-clustering-with-llms

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

docs = ["my payment failed twice", "the invoice is wrong",
        "card declined at checkout", "how do I reset my password",
        "I'm locked out of my account", "login page won't load"]

model = SentenceTransformer("all-MiniLM-L6-v2")
X = model.encode(docs)          # shape (6, 384)
labels = KMeans(n_clusters=2, n_init="auto").fit_predict(X)
# labels -> array([0, 0, 0, 1, 1, 1])

# --- block 2 ---
import umap, hdbscan
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs)                      # (N, 384)

reduced = umap.UMAP(n_components=5,                  # 384 -> 5 dims
                    n_neighbors=15,
                    metric="cosine").fit_transform(embeddings)

clusterer = hdbscan.HDBSCAN(min_cluster_size=15,
                            metric="euclidean")
labels = clusterer.fit_predict(reduced)              # e.g. [0,0,1,2,-1,1,...]
