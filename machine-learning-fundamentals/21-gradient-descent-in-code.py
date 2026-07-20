"""
Machine Learning Fundamentals
Chapter 21: Gradient Descent in Code: 1D and 2D
Section: Logistic Regression and Optimization

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/gradient-descent-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def loss(w):
    return (w - 3.0) ** 2

def grad(w):
    return 2.0 * (w - 3.0)     # dJ/dw

def gradient_descent(w, eta=0.1, n_steps=50):
    history = [w]                      # snapshot for plotting
    for _ in range(n_steps):
        w = w - eta * grad(w)          # THE step: downhill
        history.append(w)
    return w, history

# --- block 2 ---
def loss2d(w):
    return (w[0] - 3.0)**2 + (w[1] + 2.0)**2

def grad2d(w):
    return np.array([2.0 * (w[0] - 3.0),      # ∂J/∂w1
                     2.0 * (w[1] + 2.0)])     # ∂J/∂w2

def gradient_descent(w, eta=0.1, n_steps=50):
    history = [w.copy()]
    for _ in range(n_steps):
        w = w - eta * grad2d(w)        # SAME line, now vector arithmetic
        history.append(w.copy())
    return w, history
