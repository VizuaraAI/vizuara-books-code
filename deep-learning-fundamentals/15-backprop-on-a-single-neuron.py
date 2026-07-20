"""
Deep Learning Fundamentals
Chapter 15: Backpropagation on a single neuron
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/backprop-on-a-single-neuron

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# forward
x = np.array([ 1.0, -2.0,  3.0])
w = np.array([-3.0, -1.0,  2.0])
b = 1.0

z = np.dot(w, x) + b        # 6.0
a = max(0.0, z)             # ReLU -> 6.0

# backward, given upstream gradient dL/da
dL_da = 1.0
da_dz = 1.0 if z > 0 else 0.0     # ReLU local derivative
dL_dz = dL_da * da_dz             # 1.0

dw = dL_dz * x              # array([ 1., -2.,  3.])  -> the inputs, scaled
db = dL_dz * 1.0           # 1.0                     -> just the upstream
dx = dL_dz * w             # array([-3., -1.,  2.])  -> the weights, scaled
