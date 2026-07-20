"""
Deep Learning Fundamentals
Chapter 36: Regression project: California Housing
Section: Hands-On Projects

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/regression-california-housing

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- shared context (not book text) ---
# This chapter reuses Dense (chapters 7 and 16) and ReLU (chapter 20) without
# redefining them. context.py holds both, copied verbatim from the book.
from context import Dense, ReLU

# --- block 1 ---
import numpy as np

# X_train: (N, 8) already standardized;  y_train: (N, 1) house values in $100k units
dense1 = Dense(8, 64)          # 8 features  -> 64 hidden neurons
activation1 = ReLU()
dense2 = Dense(64, 1)          # 64 hidden   -> 1 output neuron (the price)
# no activation on the output: it stays linear

def forward(X):
    dense1.forward(X)
    activation1.forward(dense1.output)
    dense2.forward(activation1.output)
    return dense2.output       # (N, 1): raw predicted values, no squashing

def mse(y_pred, y_true):
    return np.mean((y_pred - y_true) ** 2)
