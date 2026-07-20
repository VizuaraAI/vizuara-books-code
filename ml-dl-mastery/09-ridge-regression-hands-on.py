"""
Machine Learning & Deep Learning Mastery
Chapter 9: Ridge Regression: A Hands-On Demo
Section: Regression

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/ridge-regression-hands-on

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The chapter uses these names without defining them. Placeholders so the file runs.
b2 = None  # TODO: authoring bug - see the note above

# --- block 1 ---
import numpy as np

X = np.array([[1.0, 1.1],
              [2.0, 1.9],
              [3.0, 3.1],
              [4.0, 3.9]])
y = np.array([2, 4, 6, 8], dtype=float)

def ridge_fit(X, y, lam):
    p = X.shape[1]
    # closed form: (XᵀX + λI)⁻¹ Xᵀy
    return np.linalg.solve(X.T @ X + lam * np.eye(p), X.T @ y)

print(ridge_fit(X, y, lam=0.0))    # OLS

# AUTHORING BUG: block 2 unpacks the two coefficients as `b0, b1` but then
# prints `b1` and `b2`. The chapter's prose calls them beta1 and beta2, so the
# unpacking line is the typo. Stubbed here so the file checks clean; the fix
# belongs in the book, not here.

# --- block 2 ---
for lam in [0.0, 0.01, 0.1, 1.0, 10.0, 100.0]:
    b0, b1 = ridge_fit(X, y, lam)
    print(f"λ={lam:6.2f}   β1={b1:7.2f}   β2={b2:7.2f}   sum={b1+b2:5.2f}")
