"""
Build a NanoVLM from Scratch
Chapter 15: Patch Embeddings and Positions
Section: Encoding Images into Vectors

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/patch-embeddings-and-positions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# four flattened patches from the previous chapter: shape (4, 4)
patches = np.array([[  0,  10,  40,  50],   # top-left patch
                    [ 20,  30,  60,  70],   # top-right
                    [ 80,  90, 120, 130],   # bottom-left
                    [100, 110, 140, 150]], dtype=float)

W = np.array([[ 0.10, -0.20,  0.05],
              [ 0.30,  0.10, -0.10],
              [-0.05,  0.20,  0.15],
              [ 0.10, -0.10,  0.25]])       # learned patch-embedding, shape (4, 3)

patch_embeds = patches @ W                   # (4, 4) @ (4, 3) -> (4, 3)

# --- block 2 ---
# learned positional table: one vector per position, shape (4, 3)
pos_emb = np.array([[ 0.5,  0.0, -0.5],   # "I am position 0 (top-left)"
                    [-0.5,  0.5,  0.0],   # position 1 (top-right)
                    [ 0.0, -0.5,  0.5],   # position 2 (bottom-left)
                    [ 0.5,  0.5,  0.5]])  # position 3 (bottom-right)

tokens = patch_embeds + pos_emb            # element-wise add, still (4, 3)
