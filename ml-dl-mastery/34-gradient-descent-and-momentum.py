"""
Machine Learning & Deep Learning Mastery
Chapter 34: Gradient Descent and Momentum
Section: Optimizers & Training

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/gradient-descent-and-momentum

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# NOTE: every block in this chapter is prose in the book, not runnable code.
# They are the update rules in maths notation; theta, eta, grad, beta and v
# are symbols in those formulas. Chapter 36 is the runnable version.

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# theta = theta - eta * grad   # gradient descent: step downhill

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# v = beta * v + grad          # accumulate a velocity (beta ~ 0.9)
# theta = theta - eta * v      # step along the accumulated velocity
