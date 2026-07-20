"""
Computer Vision Bootcamp
Chapter 8: Drawing and Annotation on Images
Section: OpenCV and Classical Image Processing

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/drawing-and-annotation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
RED   = (0,   0,   255)   # BGR: max Red channel
GREEN = (0,   255, 0)     # BGR: max Green channel
BLUE  = (255, 0,   0)     # BGR: max Blue channel
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)

# --- block 2 ---
import cv2

img = cv2.imread("street.jpg")          # BGR, shape (300, 400, 3)

# 1. bounding box — the detector's main output
cv2.rectangle(img, (120, 50), (260, 220), (0, 255, 0), 2)

# 2. a filled dot at the box centre
cv2.circle(img, (190, 135), 4, (0, 0, 255), -1)   # -1 thickness = filled

# 3. a guide line, corner to corner
cv2.line(img, (0, 0), (400, 300), (255, 0, 0), 1)

# 4. the label above the box
cv2.putText(img, "person 0.94", (120, 42),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# --- block 3 ---
label = "person 0.94"
(w, h), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
# w, h is the text's pixel width and height for that font/scale/thickness

x, y = 120, 50                                   # box top-left
cv2.rectangle(img, (x, y - h - 6), (x + w, y), (0, 255, 0), -1)   # filled strip
cv2.putText(img, label, (x, y - 4),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)          # black text on it
