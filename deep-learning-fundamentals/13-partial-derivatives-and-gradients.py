"""
Deep Learning Fundamentals
Chapter 13: Partial derivatives and gradients
Section: Optimization and Calculus

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/partial-derivatives-and-gradients

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def loss(w):
    return w**2       # a parabola, minimum at w = 0

# --- block 2 ---
def loss(w1, w2):
    return w1**2 + 3*w2      # depends on two parameters
