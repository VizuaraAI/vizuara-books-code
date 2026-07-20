"""
Computer Vision Bootcamp
Chapter 18: Detection vs Segmentation
Section: Instance Segmentation with Mask R-CNN

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/detection-vs-segmentation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# 4x4 binary mask for one object.  1 = object, 0 = background
mask = [
    [0, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 0],
]
# object area = number of 1s
area = sum(sum(row) for row in mask)   # -> 10 pixels out of 16
