"""
LLM Production & Deployment
Chapter 3: Representation vs Generative Models
Section: Foundations of Language AI

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/representation-vs-generative-models

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# toy decoder step: 4 tokens processed, d_model = 8, vocab = 6
import numpy as np

h_last = np.array([0.2, -0.5, 1.1, 0.3, -0.9, 0.7, 0.0, 0.4])   # (8,) last token's vector
W_head = np.random.randn(8, 6)                                    # (d_model × vocab)
logits = h_last @ W_head                                          # (6,) one score per word
probs  = np.exp(logits) / np.exp(logits).sum()                    # softmax → sums to 1
# e.g. probs = [0.05, 0.02, 0.61, 0.10, 0.19, 0.03]  → token 2 ("Paris") wins
