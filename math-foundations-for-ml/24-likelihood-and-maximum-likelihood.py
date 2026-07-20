"""
Mathematical Foundations for Machine Learning
Chapter 24: Likelihood and Maximum Likelihood
Section: Probability Distributions

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/likelihood-and-maximum-likelihood

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

# data: 1 = heads, 0 = tails.  Observed H H T:
data = np.array([1, 1, 0])

def log_likelihood(p, data):
    # sum of log f(x_i; p) for a Bernoulli(p)
    return np.sum(data * np.log(p) + (1 - data) * np.log(1 - p))

# sweep candidate parameters and pick the best
grid = np.linspace(0.01, 0.99, 99)
scores = [log_likelihood(p, data) for p in grid]
p_hat = grid[int(np.argmax(scores))]

print(round(p_hat, 3))     # -> 0.667  (i.e. 2/3, the MLE)
