"""
Build a NanoVLM from Scratch
Chapter 16: The CNN Route to an Image Vector
Section: Encoding Images into Vectors

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/the-cnn-route-to-an-image-vector

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

image = np.array([[ 0,  1,  2,  3],
                  [ 4,  5,  6,  7],
                  [ 8,  9, 10, 11],
                  [12, 13, 14, 15]], dtype=float)     # 4x4, one channel

kernel = np.ones((3, 3))                               # sums whatever is under it

# slide the 3x3 window to each of the 4 valid positions
out = np.array([
    [(image[0:3, 0:3] * kernel).sum(), (image[0:3, 1:4] * kernel).sum()],
    [(image[1:4, 0:3] * kernel).sum(), (image[1:4, 1:4] * kernel).sum()],
])
# out == [[ 45,  54],
#         [ 81,  90]]    <- a 2x2 feature map

# --- block 2 ---
feature_map = np.random.randn(512, 7, 7)          # C x H x W from the backbone
image_vector = feature_map.mean(axis=(1, 2))      # average over the 7x7 grid
# image_vector.shape == (512,)   <- ONE fixed-length vector for the whole image

# --- block 3 ---
W_proj = np.random.randn(512, 256)                # learned head: C=512 -> d=256
image_embed = image_vector @ W_proj               # shape (256,) <- matches the text vector
