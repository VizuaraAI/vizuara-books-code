"""
Modern Robot Learning
Chapter 7: Multimodal Data, VLMs, and VLAs
Section: Foundations of Robot Learning

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/multimodal-data-vlms-and-vlas

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

d = 8
# 4 visual + 1 proprio + 3 language tokens, each a d-vector
X = np.random.randn(8, d)          # the fused multimodal sequence
Wq, Wk, Wv = (np.random.randn(d, d) for _ in range(3))

Q, K, V = X @ Wq, X @ Wk, X @ Wv   # each (8 × 8)
scores  = Q @ K.T / np.sqrt(d)     # (8 × 8): every token scored against every token
attn    = np.exp(scores - scores.max(1, keepdims=True))
attn   /= attn.sum(1, keepdims=True)
fused   = attn @ V                 # (8 × 8): each token now a blend of ALL modalities
