"""
Convolutional Neural Networks Fundamentals
Chapter 16: Filters in 2-D
Section: Filtering and Convolution

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/filters-in-2d

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
out = b + sum(w[i][j] * x[i][j] for i in range(3) for j in range(3))
