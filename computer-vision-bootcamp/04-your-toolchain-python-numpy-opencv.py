"""
Computer Vision Bootcamp
Chapter 4: Your Toolchain: Python, NumPy, OpenCV
Section: Foundations of Computer Vision

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/your-toolchain-python-numpy-opencv

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2
import numpy as np
print("OpenCV:", cv2.__version__)      # e.g. 4.x.x
print("NumPy:", np.__version__)

fake = np.zeros((3, 4, 3), dtype=np.uint8)   # a tiny 3×4 "black image"
print(fake.shape, fake.dtype)                 # (3, 4, 3) uint8

# --- block 2 ---
img = np.array([
    [[  0,   0, 255], [  0, 255,   0]],   # row 0: red pixel,  green pixel
    [[255,   0,   0], [255, 255, 255]],   # row 1: blue pixel, white pixel
], dtype=np.uint8)

print(img.shape)      # (2, 2, 3)
print(img.size)       # 12  = 2 * 2 * 3 numbers total

# --- block 3 ---
brighter = cv2.add(img, 40)   # saturating add: clips at 255, never wraps around

# --- block 4 ---
import cv2

img = cv2.imread("cat.jpg")                     # 1. READ  -> a (H, W, 3) BGR uint8 array
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 2. TRANSFORM -> now (H, W), 1 channel
edges = cv2.Canny(gray, 100, 200)               # 2. TRANSFORM -> edge map, still an array
cv2.imwrite("cat_edges.jpg", edges)             # 3. DISPLAY/SAVE
