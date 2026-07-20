"""
Neural Networks from Scratch
Chapter 20: Masterclass: Building the Whole Thing in Code
Section: Context and Review

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/masterclass-introduction

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The chapter uses these names without defining them. Placeholders so the file runs.
predicted_probs = None   # TODO: (n_samples, n_classes) softmax output
true_labels     = None   # TODO: (n_samples, n_classes) one-hot true labels
n_samples       = None   # TODO: number of samples in the batch

# --- block 1 ---
import numpy as np

X  = np.array([[1.0, 2.0]])                 # (1, 2): one sample, two features
W1 = np.array([[0.1, -0.2,  0.3],
               [0.4,  0.5, -0.6]])          # (2, 3): 2 inputs -> 3 neurons
b1 = np.zeros((1, 3))                       # (1, 3): one bias per neuron

z = X @ W1 + b1          # -> [[0.9, 0.8, -0.9]]
a = np.maximum(0, z)     # ReLU -> [[0.9, 0.8, 0.0]]   (neuron 3 switched off)

# --- placeholders (added so this file runs standalone) ---
# Block 2 is the seed of the backward pass. Its three inputs come from the
# forward pass over whatever batch the reader is running.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/masterclass-introduction

# --- block 2 ---
dscores = (predicted_probs - true_labels) / n_samples   # p - y, averaged
