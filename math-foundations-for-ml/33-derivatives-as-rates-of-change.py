"""
Mathematical Foundations for Machine Learning
Chapter 33: Derivatives as Rates of Change
Section: Calculus and the Engine of Learning

Read this chapter: https://books.vizuara.ai/read/math-foundations-for-ml/derivatives-as-rates-of-change

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def numerical_derivative(f, x, h=1e-5):
    # the difference quotient with a small, fixed step h
    return (f(x + h) - f(x)) / h

numerical_derivative(lambda t: t**2, 3.0)   # ≈ 6.00001, our f'(3) = 6
