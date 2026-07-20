"""
Machine Learning Fundamentals
Chapter 17: From Scores to Probabilities: The Sigmoid
Section: Logistic Regression and Optimization

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/from-scores-to-probabilities-sigmoid

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# --- block 2 ---
def sigmoid_prime(z):
    p = sigmoid(z)
    return p * (1.0 - p)     # note: p·(1 − p), NOT p²
