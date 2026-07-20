"""
LLM Production & Deployment
Chapter 26: Embedding & Retrieval
Section: RAG in Production

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/embedding-and-retrieval

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
chunks = [
    "The Eiffel Tower is located in Paris, France.",   # C0
    "Photosynthesis converts sunlight into glucose.",  # C1
    "Paris is the capital city of France.",            # C2
]
query = "Where is the Eiffel Tower?"

# --- block 2 ---
import numpy as np
E = np.array([
    [0.90, 0.10, 0.30, 0.00],   # C0  Eiffel / Paris
    [0.05, 0.95, 0.00, 0.10],   # C1  photosynthesis
    [0.70, 0.10, 0.60, 0.05],   # C2  Paris / capital
])
q = np.array([0.85, 0.05, 0.25, 0.00])  # the query, embedded the SAME way

# --- block 3 ---
def retrieve(q, E, k=2):
    scores = E @ q                     # dot product with every chunk = cosine (if normalised)
    return np.argsort(scores)[::-1][:k]  # indices of the top-k highest scores
# retrieve(q, E) -> array([0, 2])  ->  C0, then C2
