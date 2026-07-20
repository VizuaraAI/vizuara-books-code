"""
Computer Vision Bootcamp
Chapter 2: An Image Is a Tensor
Section: Foundations of Computer Vision

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/an-image-is-a-tensor

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

img = np.array([
    [  0, 128, 255],   # row 0 (top)
    [128, 128, 128],   # row 1 (middle)
    [255, 128,   0],   # row 2 (bottom)
], dtype=np.uint8)

img.shape        # (3, 3)
img[0, 2]        # 255  -> top-right pixel, bright white
img[2, 0]        # 255  -> bottom-left pixel, bright white
img[2, 2]        # 0    -> bottom-right pixel, black

# --- block 2 ---
import cv2

img_bgr = cv2.imread("apple.jpg")               # shape (H, W, 3), channels in B, G, R
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)   # now R, G, B
