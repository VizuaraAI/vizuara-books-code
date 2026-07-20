"""
Computer Vision Bootcamp
Chapter 20: RoI Pooling vs RoI Align
Section: Instance Segmentation with Mask R-CNN

Read this chapter: https://books.vizuara.ai/read/computer-vision-bootcamp/roi-pooling-vs-roi-align

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# fractional offsets from the top-left integer cell (4, 5)
dx, dy = 0.3, 0.7
# bilinear weights for the four surrounding cells
w_TL = (1 - dx) * (1 - dy)   # cell (4,5): 0.7 * 0.3 = 0.21
w_TR = dx       * (1 - dy)   # cell (5,5): 0.3 * 0.3 = 0.09
w_BL = (1 - dx) * dy         # cell (4,6): 0.7 * 0.7 = 0.49
w_BR = dx       * dy         # cell (5,6): 0.3 * 0.7 = 0.21
# weights sum to 1.0 by construction
value = w_TL*F[5,4] + w_TR*F[5,5] + w_BL*F[6,4] + w_BR*F[6,5]
