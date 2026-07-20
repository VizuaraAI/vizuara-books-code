"""
Machine Learning Fundamentals
Chapter 7: Linear Classifiers, Part 1: Drawing a Decision Boundary
Section: Linear Classifiers and the Perceptron

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/linear-classifiers-part-1

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
z = w @ x + b        # w·x is the dot product: w[0]*x[0] + w[1]*x[1] + ... , then add b
