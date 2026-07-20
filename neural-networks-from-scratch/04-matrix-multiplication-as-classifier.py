"""
Neural Networks from Scratch
Chapter 4: Matrix Multiplication as a Classifier
Section: The Ten Questions

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/matrix-multiplication-as-classifier

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

x = np.array([[0.6, -0.2]])          # shape (1, 2): one sample, one row
W = np.array([[ 1.5, -1.0,  0.5],    # column 0 = red neuron's weights
              [-2.0,  1.0,  0.5]])   # column 1 = green, column 2 = blue
b = np.array([[0.3, 0.1, -0.2]])     # shape (1, 3): one bias per neuron

scores = x @ W + b                   # shape (1, 3)
print(scores)                        # [[ 1.6  -0.7   0.  ]]

# --- block 2 ---
X = np.array([[ 0.6, -0.2],
              [-0.5,  0.9],
              [ 0.1,  0.1],
              [-0.8, -0.4]])          # shape (4, 2): four samples, one per row
scores = X @ W + b                    # shape (4, 3)
