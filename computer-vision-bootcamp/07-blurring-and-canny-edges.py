"""
Computer Vision Bootcamp
Chapter 7: Blurring and Canny Edge Detection
Section: OpenCV and Classical Image Processing

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/blurring-and-canny-edges

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import cv2

img  = cv2.imread("street.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # edges live in intensity
blur = cv2.GaussianBlur(gray, (5, 5), 0)        # smooth to suppress noise
edges = cv2.Canny(blur, 100, 200)               # 5-stage detector, two thresholds
