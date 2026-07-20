"""
Deep Learning Fundamentals
Chapter 9: Coding activation functions
Section: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/activation-functions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def relu(z):
    return np.maximum(0, z)          # elementwise: negatives → 0, positives unchanged

# --- block 2 ---
def sigmoid(z):
    return 1 / (1 + np.exp(-z))       # squashes any real number into (0, 1)

# --- block 3 ---
def softmax(z):
    z_shift = z - np.max(z, axis=1, keepdims=True)   # subtract each row's max: no overflow
    exp = np.exp(z_shift)
    return exp / np.sum(exp, axis=1, keepdims=True)   # normalize each row to sum to 1
