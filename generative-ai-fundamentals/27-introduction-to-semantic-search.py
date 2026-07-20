"""
Generative AI Fundamentals
Chapter 27: Introduction to Semantic Search
Section: Semantic Search & Dense Retrieval

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/introduction-to-semantic-search

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
query = [0.90, 0.10]   # "reset my password"
docA  = [0.85, 0.15]   # "recover account access"   ← the right answer
docB  = [0.20, 0.95]   # "configure database TTL"
docC  = [0.05, 0.90]   # "sharding your Postgres cluster"
