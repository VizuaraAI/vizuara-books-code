"""
Machine Learning Fundamentals
Chapter 16: One-Hot Encoding for Categorical Data
Section: Features and Representation

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/one-hot-encoding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
red   = [1, 0, 0]
green = [0, 1, 0]
blue  = [0, 0, 1]

# --- block 2 ---
# columns: [ weight_g , is_red , is_green , is_yellow ]
X = [[150, 1, 0, 0],   # red
     [120, 0, 1, 0],   # green
     [180, 0, 0, 1],   # yellow
     [130, 1, 0, 0]]   # red
