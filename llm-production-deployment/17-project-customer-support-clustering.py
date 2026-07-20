"""
LLM Production & Deployment
Chapter 17: Project: Customer Support Clustering
Section: Clustering & Topic Modeling

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/project-customer-support-clustering

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo fixups: names the book uses but this chapter does not define ---
tickets = None          # TODO: the 156,900 support-ticket strings for the quarter.
central_tickets = None  # TODO: the tickets closest to one cluster's centre,
#                         picked from the `labels` computed in block 2.
# --- end fixups ---

# --- block 1 ---
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
emb = model.encode(tickets, batch_size=256, show_progress_bar=True)  # (156900, 768)
np.save("emb_2026Q1.npy", emb)   # this file is now gold — never recompute

# --- block 2 ---
import umap
from hdbscan import HDBSCAN

reduced = umap.UMAP(n_components=5, n_neighbors=50, metric="cosine").fit_transform(emb)
labels  = HDBSCAN(min_cluster_size=60, metric="euclidean").fit_predict(reduced)

noise_frac = (labels == -1).mean()   # 0.23
n_clusters = labels.max() + 1        # 34

# --- block 3 ---
prompt = f"""These customer-support tickets were grouped together.
Give a 3-5 word theme title and a one-sentence summary.

{chr(10).join(central_tickets)}
"""
# model returns: "Duplicate / double charges" — "Customers billed twice for a single order."
