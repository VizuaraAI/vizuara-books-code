"""
Mathematical Foundations for Machine Learning
Chapter 2: How to Read This Book
Section: Why Math for Machine Learning

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/how-to-read-this-book

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# This opening chapter previews a neuron and calls sigmoid(), which the book
# does not define until chapter 41 (A Neuron from Scratch).
from context import sigmoid

# --- block 1 ---
def neuron(x, w, b):
    z = sum(xi * wi for xi, wi in zip(x, w)) + b   # a dot product, plus a bias
    return sigmoid(z)                               # squashed through a nonlinearity
