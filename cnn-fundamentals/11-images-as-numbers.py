"""
Convolutional Neural Networks Fundamentals
Chapter 11: Images as Numbers: Pixels, Channels, and Tensors
Section: Why Convolutional Neural Networks

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/images-as-numbers

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# A 2x2 GRAYSCALE image: one brightness per pixel, 0-255.
gray = np.array([[  0, 128],
                 [255,  64]], dtype=np.uint8)
print(gray.shape)          # (2, 2)          -> (H, W)

# Normalize to floats in [0, 1] — the usual first step before a network.
gray_f = gray / 255.0
print(gray_f)              # [[0.  , 0.502], [1.  , 0.251]]

# A 2x2 COLOR image in HWC: each pixel is an (R, G, B) triple.
color = np.array([[[255,   0,   0], [  0, 255,   0]],   # red pixel, green pixel
                  [[  0,   0, 255], [255, 255,   0]]],  # blue pixel, yellow pixel
                 dtype=np.uint8)
print(color.shape)         # (2, 2, 3)       -> (H, W, C), the HWC convention

# Reorder to CHW for PyTorch: channels first.
color_chw = color.transpose(2, 0, 1)
print(color_chw.shape)     # (3, 2, 2)       -> (C, H, W)
