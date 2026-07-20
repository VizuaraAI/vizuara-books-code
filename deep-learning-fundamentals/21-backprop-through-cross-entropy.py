"""
Deep Learning Fundamentals
Chapter 21: Backpropagation through cross-entropy loss
Section: The Backward Pass (Backpropagation)

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/backprop-through-cross-entropy

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

y_pred = np.array([[0.7, 0.1, 0.2],     # sample 0, truth = class 0
                   [0.1, 0.5, 0.4],     # sample 1, truth = class 1
                   [0.02, 0.9, 0.08]])  # sample 2, truth = class 1

y_true = np.array([[1, 0, 0],           # one-hot labels, same batch as the forward chapter
                   [0, 1, 0],
                   [0, 1, 0]])

# --- block 2 ---
class CategoricalCrossEntropy:
    def backward(self, y_pred, y_true):
        n = len(y_pred)                                 # batch size N
        y_pred = np.clip(y_pred, 1e-7, 1 - 1e-7)        # same clip as forward → bounds 1/ŷ
        self.dinputs = -y_true / y_pred                 # ∂L/∂ŷ = -y/ŷ, element-wise
        self.dinputs = self.dinputs / n                 # normalize by batch size
        return self.dinputs
