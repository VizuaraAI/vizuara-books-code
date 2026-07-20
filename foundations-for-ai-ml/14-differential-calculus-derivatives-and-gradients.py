"""
Foundations for AI & ML
Chapter 14: Differential Calculus: Derivatives and Gradients
Section: Calculus for Optimization

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/differential-calculus-derivatives-and-gradients

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def loss(p):          # p = [x, y]
    return p[0]**2 + 3*p[1]**2

def grad(p):          # ∇f = [∂f/∂x, ∂f/∂y]
    return np.array([2*p[0], 6*p[1]])

p = np.array([2.0, 1.0])   # starting parameters
eta = 0.1                  # learning rate
for step in range(4):
    print(step, p, loss(p))
    p = p - eta * grad(p)  # θ ← θ − η ∇L(θ)
