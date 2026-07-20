"""
Build a NanoVLM from Scratch
Chapter 9: Image Embeddings from Scratch
Section: Embeddings & Similarity

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/image-embeddings-from-scratch

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

image = np.array([[  0,  10,  20,  30],
                  [ 40,  50,  60,  70],
                  [ 80,  90, 100, 110],
                  [120, 130, 140, 150]], dtype=float)   # a 4×4 grayscale image

# cut into four 2×2 patches, top-left, top-right, bottom-left, bottom-right
patches = np.array([
    image[0:2, 0:2].reshape(-1),   # [  0, 10, 40, 50]
    image[0:2, 2:4].reshape(-1),   # [ 20, 30, 60, 70]
    image[2:4, 0:2].reshape(-1),   # [ 80, 90,120,130]
    image[2:4, 2:4].reshape(-1),   # [100,110,140,150]
])
# patches.shape == (4, 4):  four patch-tokens, each length 4

# --- block 2 ---
# a learned linear layer: length-4 patch  ->  length-3 embedding
W = np.array([[ 0.10, -0.20,  0.05],
              [ 0.30,  0.10, -0.10],
              [-0.05,  0.20,  0.15],
              [ 0.10, -0.10,  0.25]])          # shape (4, 3)

patch_embeds = patches @ W                      # (4, 4) @ (4, 3) -> (4, 3)
# four patch-tokens, each now a length-3 learned embedding

# --- block 3 ---
image_vector = patch_embeds.mean(axis=0)        # average the 4 patch-tokens
# shape (3,): ONE vector for the whole image

# --- block 4 ---
# project the pooled image vector to the SHARED dimension d = 5
W_proj = np.random.randn(3, 5)                  # learned head: d_model=3 -> d=5
image_embed = image_vector @ W_proj             # shape (5,)  <- SAME length as the text vector
