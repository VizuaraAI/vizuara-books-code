"""
Machine Learning & Deep Learning Mastery
Chapter 29: The Backward Pass Through a Single Neuron
Section: Neural Networks: Backpropagation

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/backward-pass-single-neuron

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

x = np.array([1.0, 2.0])          # input
w = np.array([0.5, -0.3]); b = 0.1
y = 1.0                            # target

# --- forward pass (cache z and a) ---
z = w @ x + b                     # 0.0
a = 1 / (1 + np.exp(-z))          # sigmoid -> 0.5
L = 0.5 * (a - y) ** 2            # 0.125

# --- backward pass ---
dL_da = a - y                     # -0.5
da_dz = a * (1 - a)               # 0.25   (sigmoid derivative)
delta = dL_da * da_dz             # -0.125 = the error signal δ

grad_w = delta * x                # [-0.125, -0.25]
grad_b = delta * 1.0              # -0.125

# --- one gradient-descent step ---
eta = 0.1
w -= eta * grad_w
b -= eta * grad_b
