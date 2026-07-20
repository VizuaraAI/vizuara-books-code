"""
Machine Learning Fundamentals
Chapter 10: The Perceptron Explained
Section: Linear Classifiers and the Perceptron

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/the-perceptron-explained

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# labels y are in {-1, +1}; eta is the learning rate
z = w @ x + b
prediction = 1 if z >= 0 else -1
if prediction != y:          # only mistakes trigger an update
    w = w + eta * y * x
    b = b + eta * y
