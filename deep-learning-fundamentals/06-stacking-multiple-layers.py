"""
Deep Learning Fundamentals
Chapter 6: Stacking multiple layers together
Section: Neural Network Architecture

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/stacking-multiple-layers

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

np.random.seed(0)

# A batch of 2 samples, each with 4 features
X = np.array([[1.0, 2.0, 3.0, 2.5],
              [2.0, 5.0, -1.0, 2.0]])          # shape (2, 4)

# Layer 1: 4 inputs -> 5 neurons
W1 = 0.01 * np.random.randn(4, 5)              # shape (4, 5)
b1 = np.zeros((1, 5))                           # shape (1, 5)

# Layer 2: 5 inputs -> 3 neurons  (5 MUST match layer 1's 5 neurons)
W2 = 0.01 * np.random.randn(5, 3)              # shape (5, 3)
b2 = np.zeros((1, 3))                           # shape (1, 3)

# Forward pass: output of layer 1 becomes input to layer 2
layer1_out = X @ W1 + b1                         # (2, 4) @ (4, 5) -> (2, 5)
layer2_out = layer1_out @ W2 + b2                # (2, 5) @ (5, 3) -> (2, 3)

print(layer1_out.shape)   # (2, 5)
print(layer2_out.shape)   # (2, 3)
