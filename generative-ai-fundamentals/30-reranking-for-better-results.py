"""
Generative AI Fundamentals
Chapter 30: Reranking for Better Results
Section: Semantic Search & Dense Retrieval

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/reranking-for-better-results

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from sentence_transformers import CrossEncoder

# a small, fast cross-encoder fine-tuned on MS MARCO
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

query = "how do I cancel my subscription"
# `candidates` = the top-N passages your bi-encoder already retrieved
pairs = [(query, passage) for passage in candidates]   # N (query, doc) pairs

scores = reranker.predict(pairs)                        # one relevance score per pair
reranked = sorted(zip(candidates, scores),
                  key=lambda x: x[1], reverse=True)     # re-sort, high score first

top_k = [passage for passage, _ in reranked[:5]]        # keep the best 5
