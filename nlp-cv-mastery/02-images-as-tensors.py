"""
NLP & Computer Vision Mastery
Chapter 2: Images as Tensors
Section: Foundations of Vision

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/images-as-tensors

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

img = np.array([
    [  0,  50, 100, 150],
    [ 60, 120, 180, 240],
    [ 30,  90, 160, 220],
    [ 10,  70, 140, 200],
])
print(img.shape)   # (4, 4)

# --- block 2 ---
img = np.zeros((224, 224, 3), dtype=np.uint8)  # a black image
img[0, 0]        # -> array([0, 0, 0])  : top-left pixel, all channels
img[0, 0, 2]     # -> 0                 : the BLUE value of that pixel
img[:, :, 0]     # -> the entire RED channel, a (224, 224) grid
img[0, 0] = [255, 0, 0]   # paint the top-left pixel pure red

# --- block 3 ---
img = img.astype(np.float32) / 255.0
# pixel (200, 30, 30)  ->  (0.784, 0.118, 0.118)
