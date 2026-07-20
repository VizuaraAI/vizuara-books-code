"""
Machine Learning Fundamentals
Chapter 29: Stochastic Gradient Descent
Section: Linear Regression

Read this chapter: https://books.vizuara.ai/read/machine-learning-fundamentals/stochastic-gradient-descent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# batch gradient descent: ONE step
grad_w = (2/n) * sum((y_hat[i] - y[i]) * x[i] for i in range(n))
w = w - eta * grad_w

# --- block 2 ---
# stochastic gradient descent: ONE step
i = random_index()                      # pick a single example
grad_w = 2 * (y_hat[i] - y[i]) * x[i]   # gradient from just that one point
w = w - eta * grad_w

# --- block 3 ---
# mini-batch gradient descent: ONE step over B examples
batch = sample(B)                        # e.g. B = 64 random examples
grad_w = (2/B) * sum((y_hat[i] - y[i]) * x[i] for i in batch)
w = w - eta * grad_w
