"""
Foundations for AI & ML
Chapter 27: Momentum-Based Gradient Descent
Section: Optimization & Neural Networks

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/momentum-based-gradient-descent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file is runnable standalone) ---
# Blocks 2 and 3 are excerpts: the gradient of the toy loss from block 1, and
# the momentum update rule. Block 4 is the self-contained version.
# See https://books.vizuara.ai/read/foundations-for-ai-ml/momentum-based-gradient-descent
x = None      # TODO: current x coordinate on the loss surface
y = None      # TODO: current y coordinate on the loss surface
v = None      # TODO: the velocity accumulator
theta = None  # TODO: the parameter vector being optimised
beta = None   # TODO: momentum coefficient
eta = None    # TODO: learning rate

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# L(x, y) = 0.5 * x**2 + 5.0 * y**2

# --- block 2 ---
grad = [x, 10*y]   # ∂L/∂x = x,  ∂L/∂y = 10y

# --- block 3 ---
v = beta * v + grad          # accumulate: keep β of old velocity, add the new gradient
theta = theta - eta * v      # step along the accumulated velocity

# --- block 4 ---
import numpy as np

def momentum_gd(grad_fn, theta, eta=0.15, beta=0.9, steps=50):
    v = np.zeros_like(theta)          # velocity starts at rest
    for _ in range(steps):
        g = grad_fn(theta)            # gradient at current point (a mini-batch estimate in practice)
        v = beta * v + g              # accumulate velocity
        theta = theta - eta * v       # step along the velocity, not the raw gradient
    return theta
