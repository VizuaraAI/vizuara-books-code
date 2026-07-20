"""
Computer Vision Bootcamp
Chapter 13: What Object Detection Really Asks
Section: Object Detection: The R-CNN Family

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/what-object-detection-really-asks

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x_min, y_min, x_max, y_max = 20, 120, 90, 190
w = x_max - x_min          # 90 - 20  = 70
h = y_max - y_min          # 190 - 120 = 70
cx = x_min + w / 2         # 20 + 35  = 55
cy = y_min + h / 2         # 120 + 35 = 155
# center form: (cx, cy, w, h) = (55, 155, 70, 70)

# --- block 2 ---
TP, FP, FN = 4, 2, 1
precision = TP / (TP + FP)   # 4 / 6 = 0.67  → a third of my boxes were junk
recall    = TP / (TP + FN)   # 4 / 5 = 0.80  → I found four of the five objects
