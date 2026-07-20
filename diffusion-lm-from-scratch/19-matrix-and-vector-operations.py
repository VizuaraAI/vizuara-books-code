"""
Build a Diffusion Language Model from Scratch
Chapter 19: The Matrix and Vector Operations Under the Hood
Section: Diffusion Language Model Theory

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/matrix-and-vector-operations

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
ids = [1, 2, 0, 5]          # the, cat, [MASK], mat
X   = E[ids]                # (4, 8): four rows pulled from the (9, 8) table

# --- block 2 ---
H = block(X)     # (4, 8) in → (4, 8) out

# --- block 3 ---
# H:   (4, 8)   contextual vectors
# W_U: (8, 9)   learned unembedding
logits = H @ W_U     # (4, 9): a score for every vocab word, at every position
