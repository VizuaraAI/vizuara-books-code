"""
Deep Learning Fundamentals
Chapter 10: One full forward pass (no loss yet)
Section: The Forward Pass

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/one-forward-pass-no-loss

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

np.random.seed(0)

# A batch of 2 samples, 4 features each
X = np.array([[1.0, 2.0, 3.0, 2.5],
              [2.0, 5.0, -1.0, 2.0]])          # (2, 4)

# Dense layer 1: 4 inputs -> 5 neurons
W1 = 0.01 * np.random.randn(4, 5)              # (4, 5)
b1 = np.zeros((1, 5))                           # (1, 5)

# Dense layer 2: 5 inputs -> 3 neurons
W2 = 0.01 * np.random.randn(5, 3)              # (5, 3)
b2 = np.zeros((1, 3))                           # (1, 3)

# --- block 2 ---
z1 = X @ W1 + b1          # (2, 5)  pre-activations, tiny numbers
a1 = np.maximum(0, z1)    # (2, 5)  ReLU: negatives -> 0

# --- block 3 ---
z2 = a1 @ W2 + b2                                   # (2, 3)  logits

# Softmax, row by row, with the max-subtraction stability trick
exp_scores = np.exp(z2 - np.max(z2, axis=1, keepdims=True))
probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)   # (2, 3)

# --- block 4 ---
import numpy as np
np.random.seed(0)

X  = np.array([[1.0, 2.0, 3.0, 2.5],
               [2.0, 5.0, -1.0, 2.0]])   # (2, 4)

W1 = 0.01 * np.random.randn(4, 5); b1 = np.zeros((1, 5))
W2 = 0.01 * np.random.randn(5, 3); b2 = np.zeros((1, 3))

z1    = X @ W1 + b1                        # (2, 5)  dense 1
a1    = np.maximum(0, z1)                  # (2, 5)  ReLU
z2    = a1 @ W2 + b2                       # (2, 3)  dense 2  (logits)
exp_s = np.exp(z2 - np.max(z2, axis=1, keepdims=True))
probs = exp_s / np.sum(exp_s, axis=1, keepdims=True)   # (2, 3)  softmax

print(probs)          # ~ [[0.334, 0.333, 0.333],
                      #    [0.334, 0.333, 0.333]]
print(probs.sum(1))   # [1. 1.]  each row is a valid distribution
