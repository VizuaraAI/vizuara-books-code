"""
Mathematical Foundations for Machine Learning
Chapter 39: The Adam Optimizer
Section: Calculus and the Engine of Learning

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/the-adam-optimizer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# state, created once
m = 0            # first moment  (like momentum's velocity)
v = 0            # second moment (like RMSProp's s)
t = 0

def adam_step(theta, grad, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    global m, v, t
    t += 1
    m = b1 * m + (1 - b1) * grad          # smooth the direction
    v = b2 * v + (1 - b2) * grad**2       # smooth the squared magnitude
    m_hat = m / (1 - b1**t)               # bias-correct the direction
    v_hat = v / (1 - b2**t)               # bias-correct the magnitude
    return theta - lr * m_hat / (v_hat**0.5 + eps)
