"""
Mathematical Foundations for Machine Learning
Chapter 35: Partial Derivatives and the Gradient
Section: Calculus and the Engine of Learning

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/partial-derivatives-and-gradients

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def f(v):                       # v = [x, y]
    x, y = v
    return x**2 + 3*x*y + y**2

def gradient(f, v, h=1e-5):
    v = np.asarray(v, dtype=float)
    grad = np.zeros_like(v)
    for i in range(len(v)):     # nudge ONE coordinate, freeze the rest
        step = np.zeros_like(v); step[i] = h
        grad[i] = (f(v + step) - f(v - step)) / (2 * h)
    return grad

gradient(f, [1.0, 2.0])         # ≈ [8.0, 7.0], matching our hand calculation
