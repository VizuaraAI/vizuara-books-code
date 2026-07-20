"""
Mathematical Foundations for Machine Learning
Chapter 37: Gradient Descent
Section: Calculus and the Engine of Learning

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/gradient-descent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# NOTE: every block in this chapter is prose in the book, not runnable code.
# They are the gradient-descent update rule in maths notation, and then the
# same rule spelled out component by component as pseudo-code. theta, eta,
# grad, grad_L and N are symbols in a formula, not variables or functions any
# block defines. Chapter 38 is the runnable version.

# --- block 1 ---
# NOTE: this block is prose in the book, not runnable code.
# theta = theta - eta * grad_L(theta)

# --- block 2 ---
# NOTE: this block is prose in the book, not runnable code.
# # theta and grad are both length-N vectors (N = number of parameters)
# for i in range(N):
#     theta[i] = theta[i] - eta * grad[i]
# # ...but in practice, one vectorized line: theta -= eta * grad
