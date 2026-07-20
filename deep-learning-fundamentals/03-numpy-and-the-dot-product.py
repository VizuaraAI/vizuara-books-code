"""
Deep Learning Fundamentals
Chapter 3: NumPy and the dot product primer
Section: Foundations

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/numpy-and-the-dot-product

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
inputs  = [1.0, 2.0, 3.0]
weights = [0.2, 0.8, -0.5]

# --- block 2 ---
total = 0.0
for i in range(len(inputs)):
    total += inputs[i] * weights[i]
# total is 0.3

# --- block 3 ---
import numpy as np

inputs  = np.array([1.0, 2.0, 3.0])
weights = np.array([0.2, 0.8, -0.5])
z = np.dot(inputs, weights) + 2.0   # weighted sum, then add the bias
# z == 2.3   (0.3 from the dot product, plus a bias of 2.0)

# --- block 4 ---
inputs  = [1.0, 2.0, 3.0]

weights = [[ 0.2,  0.8, -0.5],    # neuron 1's weights
           [ 0.5, -0.9,  0.3],    # neuron 2's weights
           [-0.3,  0.7,  0.1]]    # neuron 3's weights

biases  = [2.0, 3.0, 0.5]

# --- block 5 ---
import numpy as np

inputs  = np.array([1.0, 2.0, 3.0])                 # shape (3,)
weights = np.array([[ 0.2,  0.8, -0.5],
                    [ 0.5, -0.9,  0.3],
                    [-0.3,  0.7,  0.1]])            # shape (3, 3): 3 neurons × 3 weights
biases  = np.array([2.0, 3.0, 0.5])                 # shape (3,)

layer_outputs = np.dot(weights, inputs) + biases    # -> array([2.3, 2.6, 1.9])
