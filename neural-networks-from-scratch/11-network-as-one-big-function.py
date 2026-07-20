"""
Neural Networks from Scratch
Chapter 11: The Network as One Big Function
Section: Weights and Wiring

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/network-as-one-big-function

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def forward(x, W1, b1, W2, b2):
    z1 = x @ W1 + b1                 # dense layer 1  → (n, 3)
    a1 = np.maximum(0, z1)           # ReLU (switch)  → (n, 3)
    z2 = a1 @ W2 + b2                # dense layer 2  → (n, 2)  logits
    e  = np.exp(z2 - z2.max(axis=1, keepdims=True))
    return e / e.sum(axis=1, keepdims=True)   # softmax → (n, 2)  probabilities
