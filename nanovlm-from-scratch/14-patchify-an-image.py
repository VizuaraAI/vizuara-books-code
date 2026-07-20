"""
Build a NanoVLM from Scratch
Chapter 14: Patchify an Image
Section: Encoding Images into Vectors

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/patchify-an-image

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
                  [120, 130, 140, 150]], dtype=float)   # 4×4 grayscale, shape (4, 4)

# --- block 2 ---
patches = np.array([
    image[0:2, 0:2].reshape(-1),   # patch 0 -> [  0,  10,  40,  50]
    image[0:2, 2:4].reshape(-1),   # patch 1 -> [ 20,  30,  60,  70]
    image[2:4, 0:2].reshape(-1),   # patch 2 -> [ 80,  90, 120, 130]
    image[2:4, 2:4].reshape(-1),   # patch 3 -> [100, 110, 140, 150]
])
# patches.shape == (4, 4)

# --- block 3 ---
naive = image.reshape(4, 4)       # "4 patches of 4 numbers each", supposedly
# naive[0] -> [ 0, 10, 20, 30]    <- this is the FIRST ROW of the image, not a patch!

# --- block 4 ---
C, H, W, P = 1, 4, 4, 2                     # toy: 1 channel, 4×4 image, 2×2 patches
img = image.reshape(C, H, W)                # (1, 4, 4)  -- make channels explicit

# 1. split the HEIGHT axis into (num_patch_rows, P) and the WIDTH axis into (num_patch_cols, P)
x = img.reshape(C, H // P, P, W // P, P)    # (1, 2, 2, 2, 2)  == (C, gh, P, gw, P)

# 2. move the two patch-grid axes to the front, keep (channel, P, P) together at the back
x = x.transpose(1, 3, 0, 2, 4)              # (2, 2, 1, 2, 2)  == (gh, gw, C, P, P)

# 3. flatten the grid (gh, gw) -> N patches, and flatten (C, P, P) -> patch_dim
patches = x.reshape((H // P) * (W // P), C * P * P)   # (4, 4)

# --- block 5 ---
# patches ==
# [[  0,  10,  40,  50],    <- patch 0  (top-left)
#  [ 20,  30,  60,  70],    <- patch 1  (top-right)
#  [ 80,  90, 120, 130],    <- patch 2  (bottom-left)
#  [100, 110, 140, 150]]    <- patch 3  (bottom-right)
