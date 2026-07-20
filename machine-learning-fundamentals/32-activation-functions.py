"""
Machine Learning Fundamentals
Chapter 32: Activation Functions: Where Nonlinearity Comes From
Section: Neural Networks

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/activation-functions

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
def relu(z):
    return np.maximum(0.0, z)
