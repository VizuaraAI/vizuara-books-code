"""
Machine Learning & Deep Learning Mastery
Chapter 30: The Backward Pass Through a Layer
Section: Neural Networks: Backpropagation

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/backward-pass-layer-of-neurons

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# NOTE: every block in this chapter is prose in the book, not runnable code.
# The chapter derives the layer gradients one line at a time; X, W, b and dZ
# are symbols in those formulas, not variables any block defines. The runnable
# version of all of this is chapter 32's Dense.backward and chapter 33's
# Layer_Dense.backward.

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# Z = X @ W + b        # (batch, n_in) @ (n_in, n_out) -> (batch, n_out)

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# dW = X.T @ dZ        # (n_in, batch) @ (batch, n_out) -> (n_in, n_out)

# --- block 3 ---
# NOTE: this block is prose in the book, not runnable code.
# db = dZ.sum(axis=0, keepdims=True)   # (batch, n_out) summed over rows -> (1, n_out)

# --- block 4 ---
# NOTE: this block is prose in the book, not runnable code.
# dX = dZ @ W.T        # (batch, n_out) @ (n_out, n_in) -> (batch, n_in)

# --- block 5 ---
# NOTE: this block is prose in the book, not runnable code.
# dW = X.T @ dZ                        # gradient for the weights
# db = dZ.sum(axis=0, keepdims=True)   # gradient for the bias
# dX = dZ @ W.T                        # gradient to pass upstream
