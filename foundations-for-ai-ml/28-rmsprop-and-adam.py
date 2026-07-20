"""
Foundations for AI & ML
Chapter 28: RMSprop and Adam
Section: Optimization & Neural Networks

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/rmsprop-and-adam

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added so this file is runnable standalone) ---
# Blocks 3 and 5 use np before the chapter's own import in block 6.
import numpy as np

# --- placeholders (added so this file is runnable standalone) ---
# Blocks 2-5 are excerpts of the RMSprop and Adam update rules. Block 6 is the
# self-contained version.
# See https://books.vizuara.ai/read/foundations-for-ai-ml/rmsprop-and-adam
g = None      # TODO: the current gradient
theta = None  # TODO: the parameter vector being optimised
s = None      # TODO: RMSprop's running mean of squared gradients
m = None      # TODO: Adam's 1st moment
v = None      # TODO: Adam's 2nd moment
t = None      # TODO: the step counter, starting at 1
rho = None    # TODO: RMSprop decay rate
beta1 = None  # TODO: Adam 1st-moment decay rate
beta2 = None  # TODO: Adam 2nd-moment decay rate
eta = None    # TODO: learning rate
eps = None    # TODO: numerical-stability constant

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# L(x, y) = 0.5 * x**2 + 5.0 * y**2
# grad    = [x, 10*y]        # ∂L/∂x = x,  ∂L/∂y = 10y

# --- block 2 ---
s = rho * s + (1 - rho) * g**2      # running mean of squared gradients (elementwise)

# --- block 3 ---
theta = theta - eta * g / (np.sqrt(s) + eps)

# --- block 4 ---
m = beta1 * m + (1 - beta1) * g        # 1st moment: smoothed gradient  (momentum)
v = beta2 * v + (1 - beta2) * g**2     # 2nd moment: smoothed squared grad (RMSprop)

# --- block 5 ---
m_hat = m / (1 - beta1**t)             # bias-corrected 1st moment  (t = step count, from 1)
v_hat = v / (1 - beta2**t)             # bias-corrected 2nd moment
theta = theta - eta * m_hat / (np.sqrt(v_hat) + eps)

# --- block 6 ---
import numpy as np

def adam(grad_fn, theta, eta=1e-3, b1=0.9, b2=0.999, eps=1e-8, steps=1000):
    m = np.zeros_like(theta)
    v = np.zeros_like(theta)
    for t in range(1, steps + 1):          # t starts at 1 for bias correction
        g = grad_fn(theta)                 # a mini-batch gradient in practice
        m = b1 * m + (1 - b1) * g          # momentum
        v = b2 * v + (1 - b2) * g**2       # RMSprop
        m_hat = m / (1 - b1**t)            # bias-correct both moments
        v_hat = v / (1 - b2**t)
        theta = theta - eta * m_hat / (np.sqrt(v_hat) + eps)
    return theta
