"""
Build a Vision Transformer (ViT) from Scratch
Chapter 13: Queries, Keys, and Values
Section: Attention Inside the ViT

Read this chapter: https://books.vizuara.ai/read/vit-from-scratch/queries-keys-values

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
Q = X @ W_q     # (4, 8) @ (8, 8) -> (4, 8)
K = X @ W_k     # (4, 8)
V = X @ W_v     # (4, 8)

# --- block 2 ---
weights = softmax(Q @ K.T / d_k**0.5, dim=-1)   # (4, 4), each row sums to 1
out     = weights @ V                            # (4, 8), the new token representations
