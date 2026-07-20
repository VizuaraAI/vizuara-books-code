"""
Build a Mini ClawdBot from Scratch
Chapter 3: The Three Pillars: RAG, Memory, and MCP
Section: The ClawdBot Story

Read this chapter: https://books.vizuara.ai/read/mini-clawdbot-from-scratch/the-three-pillars-rag-memory-mcp

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

q = np.array([0.8, 0.2, 0.7, 0.1])   # the question
d = np.array([0.9, 0.1, 0.8, 0.2])   # "cap retries at 3"
e = np.array([0.1, 0.9, 0.0, 0.7])   # "lunch order for Friday?"

cosine(q, d)   # ≈ 0.99  → very close
cosine(q, e)   # ≈ 0.28  → far away
