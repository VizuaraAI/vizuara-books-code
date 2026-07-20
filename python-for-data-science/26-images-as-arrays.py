"""
Python for Data Science
Chapter 26: Images as Arrays
Section: Project: Computer Vision with OpenCV & MediaPipe

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/images-as-arrays

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

gray = np.array([
    [  0,  60, 120, 255],   # row 0: black → mid-grays → white
    [ 30,  90, 150, 200],   # row 1
    [255, 255,   0,   0],   # row 2: two white, two black
], dtype=np.uint8)

print(gray.shape)   # (3, 4)  → (height, width)
print(gray[2, 0])   # 255  → the pixel in row 2, column 0 is pure white

# --- block 2 ---
import cv2

img_bgr = cv2.imread("photo.jpg")               # shape (H, W, 3), channels in BGR order
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)  # now in RGB order for display / MediaPipe

print(img_bgr.shape)         # (H, W, 3)
print(img_bgr[0, 0])         # e.g. [232 180  95]  → that's [Blue, Green, Red], NOT [R,G,B]

# --- block 3 ---
# crop the top-left 100×100 corner — it's just NumPy slicing
patch = img_rgb[0:100, 0:100]

# brighten every pixel by 40 (clip so we don't overflow past 255)
brighter = np.clip(img_rgb.astype(int) + 40, 0, 255).astype(np.uint8)

# split out just the red channel of an RGB image
red_channel = img_rgb[:, :, 0]
