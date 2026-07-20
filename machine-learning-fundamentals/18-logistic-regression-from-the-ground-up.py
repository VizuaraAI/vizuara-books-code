"""
Machine Learning Fundamentals
Chapter 18: Logistic Regression from the Ground Up
Section: Logistic Regression and Optimization

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/logistic-regression-from-the-ground-up

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
z = w @ x + b        # one scalar per example

# --- block 2 ---
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def predict_proba(w, b, x):
    z = w @ x + b            # 1. linear score  (a scalar)
    p = sigmoid(z)           # 2. squash to (0, 1)
    return p                 # 3. P(y=1 | x)

w = np.array([1.5, -2.0])
b = 0.5
x = np.array([2.0, 1.0])

p = predict_proba(w, b, x)   # -> 0.8175...
pred = 1 if p >= 0.5 else 0  # threshold -> class 1
