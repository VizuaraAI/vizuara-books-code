"""
Deep Learning Fundamentals
Chapter 18: Input derivatives in backpropagation
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/input-derivatives

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

W = np.array([[0.1, 0.4],
              [0.2, 0.5],
              [0.3, 0.6]])
dvalues = np.array([[1.0, -2.0]])       # (1, 2) — one gradient per neuron

dinputs = dvalues @ W.T                  # (1, 2) @ (2, 3) → (1, 3)
print(dinputs)                           # [[-0.7 -0.8 -0.9]]
