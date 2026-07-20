"""
Foundations for AI & ML
Chapter 8: Determinants Deeper: Invertibility and Collapse
Section: Linear Algebra for ML

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/determinants-deeper-invertibility-and-collapse

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# It is the algebraic closed form of the 2x2 inverse (symbolic maths written
# in Python-ish notation): a, b, c, d are symbols, and scalar * list-of-lists
# is not a valid Python operation.
# A_inv = (1 / (a*d - b*c)) * [[ d, -b],
#                              [-c,  a]]

# --- block 2 ---
A = [[1, 2],
     [2, 4]]      # det = 1·4 − 2·2 = 4 − 4 = 0
