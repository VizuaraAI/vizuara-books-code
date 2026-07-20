"""
Computer Vision Bootcamp
Chapter 6: Resizing, Cropping, and Color Spaces
Section: OpenCV and Classical Image Processing

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/resizing-cropping-color-spaces

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

img = cv2.imread("cat.jpg")          # shape (H, W, 3), e.g. (720, 1280, 3)

# Absolute size — note (width, height), NOT (height, width)!
resized = cv2.resize(img, (640, 360))          # -> (360, 640, 3)

# Or scale by a factor along each axis:
half = cv2.resize(img, None, fx=0.5, fy=0.5)   # -> (360, 640, 3)

# Downscaling? Prefer INTER_AREA:
small = cv2.resize(img, (640, 360), interpolation=cv2.INTER_AREA)

# --- block 2 ---
# img has shape (H, W, 3). Crop rows 100..300, columns 200..500:
crop = img[100:300, 200:500]     # -> shape (200, 300, 3)

# --- block 3 ---
import cv2
import matplotlib.pyplot as plt

bgr = cv2.imread("cat.jpg")                     # OpenCV gives BGR
rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)      # swap to RGB for matplotlib
plt.imshow(rgb)                                  # now colours are correct

# --- block 4 ---
frame = cv2.imread("street.jpg")                    # (H, W, 3) BGR
rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      # fix ordering for the model
small = cv2.resize(rgb, (224, 224))                 # model wants 224×224
roi   = small[50:174, 30:154]                        # crop a 124×124 patch
