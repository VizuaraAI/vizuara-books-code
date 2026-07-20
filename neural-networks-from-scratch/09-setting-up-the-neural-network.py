"""
Neural Networks from Scratch
Chapter 9: Setting Up the Neural Network
Section: Weights and Wiring

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/setting-up-the-neural-network

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added so this file runs standalone) ---
# Block 1 uses numpy, but the chapter's own `import numpy as np` does not
# appear until block 2, further down this file.
import numpy as np

# --- placeholders (added so this file runs standalone) ---
# The layer's shape is whatever the reader chooses. Block 2 below builds its
# first layer as 2 -> 8, so those are used here as stand-in sizes.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/setting-up-the-neural-network
n_inputs  = 2   # TODO: how many numbers arrive at this layer
n_neurons = 8   # TODO: how many neurons this layer has

# --- block 1 ---
weights = 0.01 * np.random.randn(n_inputs, n_neurons)   # small random values
biases  = np.zeros((1, n_neurons))                       # start biases at zero

# --- block 2 ---
import numpy as np
np.random.seed(0)                          # reproducible numbers

X = np.random.randn(5, 2)                  # 5 sample points, 2 features each

# Layer 1: 2 -> 8
W1 = 0.01 * np.random.randn(2, 8)          # shape (2, 8)
b1 = np.zeros((1, 8))                       # shape (1, 8)

# Layer 2: 8 -> 3
W2 = 0.01 * np.random.randn(8, 3)          # shape (8, 3)
b2 = np.zeros((1, 3))                       # shape (1, 3)

# Forward pass: push the batch straight through
h1  = X  @ W1 + b1                          # (5, 2)@(2, 8) -> (5, 8)
out = h1 @ W2 + b2                          # (5, 8)@(8, 3) -> (5, 3)

print(h1.shape, out.shape)                 # (5, 8) (5, 3)
