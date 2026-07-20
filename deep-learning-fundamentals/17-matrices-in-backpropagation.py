"""
Deep Learning Fundamentals
Chapter 17: The role of matrices in backpropagation
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/matrices-in-backpropagation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (commented out) ---
# NOTE: this block is prose in the book, not runnable code. It restates the
# forward equation as shape annotation; X, W and b are symbols here, and the
# chapter never assigns W or b in any code block.
# Z = X @ W + b        # X:(batch, n_inputs)  W:(n_inputs, n_neurons)  b:(1, n_neurons)

# --- forward reference (hoisted so this file runs top to bottom) ---
# Block 2 below uses `np`, `X` and `dvalues`, but the chapter only imports
# NumPy and defines those arrays in block 3. All three are the book's own,
# copied verbatim from block 3 and hoisted here so the file is self-contained.
import numpy as np

X = np.array([[1.0, 2.0, 3.0],      # sample 1, 3 features
              [4.0, 5.0, 6.0]])     # sample 2        shape (2, 3)

dvalues = np.array([[0.1, 0.2],     # gradient at sample 1's 2 neurons
                    [0.3, 0.4]])    #                        shape (2, 2)

# --- block 2 ---
dW = X.T @ dvalues          # (n_inputs, batch) @ (batch, n_neurons) → (n_inputs, n_neurons)

# --- block 3 ---
import numpy as np

X = np.array([[1.0, 2.0, 3.0],      # sample 1, 3 features
              [4.0, 5.0, 6.0]])     # sample 2        shape (2, 3)

dvalues = np.array([[0.1, 0.2],     # gradient at sample 1's 2 neurons
                    [0.3, 0.4]])    #                        shape (2, 2)

# --- block 4 ---
dW = X.T @ dvalues
# X.T is (3, 2):  [[1, 4],
#                  [2, 5],
#                  [3, 6]]
# dW  = [[1.3, 1.8],      # (3, 2)  ✓ matches W's shape
#        [1.7, 2.4],
#        [2.1, 3.0]]

# --- block 5 ---
db = np.sum(dvalues, axis=0, keepdims=True)   # (batch, n_neurons) → (1, n_neurons)
