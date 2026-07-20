"""
Machine Learning Fundamentals
Chapter 15: Feature Representation: Turning the World into Numbers
Section: Features and Representation

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/feature-representation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = [850, 2, 1, 0, 0, 1, 2]
#     ↑   ↑  └──┬───┘  ↑  ↑
#    sqft beds  Bandra bal days
#              (one-hot, k=3)

# --- block 2 ---
x_scaled = (x - mean) / std   # applied per column
