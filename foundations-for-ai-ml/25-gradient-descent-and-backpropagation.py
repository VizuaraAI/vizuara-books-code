"""
Foundations for AI & ML
Chapter 25: Gradient Descent and Backpropagation
Section: Optimization & Neural Networks

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/gradient-descent-and-backpropagation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# one input example, squared-error loss, no bias/activation for clarity
x, y = 2.0, 10.0
w1, w2 = 1.0, 1.0
eta = 0.01

for step in range(50):
    # forward pass
    h = w1 * x
    y_hat = w2 * h
    loss = (y_hat - y) ** 2

    # backward pass (chain rule, walked backwards)
    dL_dyhat = 2 * (y_hat - y)   # error signal at the output
    dL_dw2   = dL_dyhat * h      # ŷ = w2 · h
    dL_dw1   = dL_dyhat * w2 * x # ŷ = w2 · (w1 · x)

    # gradient-descent step
    w1 -= eta * dL_dw1
    w2 -= eta * dL_dw2
