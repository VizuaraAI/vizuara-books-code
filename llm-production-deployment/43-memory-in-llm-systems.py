"""
LLM Production & Deployment
Chapter 43: Memory in LLM Systems
Section: Agents & Memory

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/memory-in-llm-systems

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def cosine(a, b):
    a, b = np.array(a), np.array(b)
    return a @ b / (np.linalg.norm(a) * np.linalg.norm(b))

q = [0.8, 0.2]
cosine(q, [0.9, 0.1])   # calculus memory -> 0.991
cosine(q, [0.1, 0.8])   # pasta memory    -> 0.361
