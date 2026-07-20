"""
NLP & Computer Vision Mastery
Chapter 27: The Object Detection Problem
Section: Object Detection and Segmentation

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/the-object-detection-problem

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def iou(boxA, boxB):
    # boxes in corner form: (x1, y1, x2, y2)
    # 1. intersection rectangle
    ix1 = max(boxA[0], boxB[0])
    iy1 = max(boxA[1], boxB[1])
    ix2 = min(boxA[2], boxB[2])
    iy2 = min(boxA[3], boxB[3])
    inter = max(0, ix2 - ix1) * max(0, iy2 - iy1)   # 0 if they don't overlap

    # 2. each area
    areaA = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    areaB = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])

    # 3. union = A + B - overlap  (don't double-count the overlap!)
    union = areaA + areaB - inter
    return inter / union
