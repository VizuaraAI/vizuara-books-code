"""
NLP & Computer Vision Mastery
Chapter 30: Mask R-CNN and Instance Segmentation
Section: Object Detection and Segmentation

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/mask-rcnn-instance-segmentation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added to make this file runnable) ---
# The backbone feature map that RoIAlign samples into. The chapter works the
# bilinear arithmetic by hand and then indexes four of its cells.
# TODO: supply your own feature map, e.g. a (C, H, W) tensor from the backbone.
# See https://books.vizuara.ai/read/nlp-cv-mastery/mask-rcnn-instance-segmentation
feat = None

# --- block 1 ---
# fractional sample point inside the feature map
x, y = 6.25, 3.75
x0, y0 = int(x), int(y)          # 6, 3
dx, dy = x - x0, y - y0          # 0.25, 0.75

# four corner weights (they sum to 1.0)
w00 = (1 - dx) * (1 - dy)        # (0.75)(0.25) = 0.1875  -> feat[3,6]
w10 = dx       * (1 - dy)        # (0.25)(0.25) = 0.0625  -> feat[3,7]
w01 = (1 - dx) * dy             # (0.75)(0.75) = 0.5625  -> feat[4,6]
w11 = dx       * dy             # (0.25)(0.75) = 0.1875  -> feat[4,7]

value = w00*feat[3,6] + w10*feat[3,7] + w01*feat[4,6] + w11*feat[4,7]
