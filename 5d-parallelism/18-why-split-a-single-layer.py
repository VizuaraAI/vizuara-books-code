"""
5D Parallelism for Large Model Training
Chapter 18: Why Split a Single Layer
Section: Tensor Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/why-split-a-single-layer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

X = np.random.randn(4, 3)      # 4 tokens, hidden dim 3
W = np.random.randn(3, 6)      # up-projection to dim 6

# The whole thing, on one imaginary GPU:
Y_full = X @ W                 # shape (4, 6)

# Split W by columns into two halves — one per GPU:
W_left, W_right = W[:, :3], W[:, 3:]     # each (3, 3)

# GPU 0 only ever sees X and W_left; GPU 1 only sees X and W_right:
Y_left  = X @ W_left           # (4, 3)  <- output columns 0,1,2
Y_right = X @ W_right          # (4, 3)  <- output columns 3,4,5

# Glue the halves back:
Y_split = np.concatenate([Y_left, Y_right], axis=1)   # (4, 6)

assert np.allclose(Y_full, Y_split)    # identical, bit-for-bit up to fp noise
