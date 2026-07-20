"""
Machine Learning Fundamentals
Chapter 6: How a Model Learns from Data
Section: Foundations of Machine Learning

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/how-a-model-learns-from-data

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

x = np.array([1.0, 2.0, 3.0, 4.0])   # inputs (house sizes)
y = np.array([2.0, 4.0, 6.0, 8.0])   # targets (prices), true rule y = 2x

w   = 0.0     # PARAMETER  — the single knob we tune, start deliberately wrong
eta = 0.02    # learning rate η — how big a step we take downhill

for step in range(50):
    y_hat = w * x                       # forward pass: the model's predictions
    loss  = np.mean((y_hat - y) ** 2)   # LOSS      — mean squared error
    grad  = 2 * np.mean((y_hat - y) * x)  # OPTIMIZER — slope: (pred − target)·input
    w     = w - eta * grad              # update rule: step downhill
