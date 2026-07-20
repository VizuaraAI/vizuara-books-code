"""
Machine Learning & Deep Learning Mastery
Chapter 23: Logistic Regression in Code
Section: Logistic Regression

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/logistic-regression-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

rng = np.random.default_rng(0)
n = 200
X_pos = rng.normal(loc=[ 1.2,  1.2], scale=1.3, size=(n, 2))   # class 1
X_neg = rng.normal(loc=[-1.2, -1.2], scale=1.3, size=(n, 2))   # class 0

X = np.vstack([X_pos, X_neg])                 # shape (400, 2)
y = np.hstack([np.ones(n), np.zeros(n)])      # shape (400,), labels in {0, 1}

# --- block 2 ---
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict_proba(X, w, b):
    return sigmoid(X @ w + b)          # (400,) probabilities in (0,1)

def train(X, y, lr=0.1, epochs=300):
    n_samples, n_features = X.shape
    w = np.zeros(n_features)           # start at [0., 0.]
    b = 0.0
    for epoch in range(epochs):
        p = predict_proba(X, w, b)     # forward: probabilities
        grad_w = X.T @ (p - y) / n_samples   # ∂L/∂w = mean of (p−y)·x
        grad_b = (p - y).mean()              # ∂L/∂b = mean of (p−y)
        w -= lr * grad_w                     # gradient-descent step
        b -= lr * grad_b
    return w, b

# --- block 3 ---
def bce(p, y):
    eps = 1e-9                                    # guard log(0)
    return -np.mean(y*np.log(p+eps) + (1-y)*np.log(1-p+eps))

# --- block 4 ---
w, b = train(X, y)
p = predict_proba(X, w, b)

for i in [3, 61, 199, 200, 305, 388]:
    print(f"x={np.round(X[i],2)}  true={int(y[i])}  p={p[i]:.3f}")

# --- block 5 ---
for t in [0.3, 0.5, 0.7]:
    preds = (p >= t).astype(int)
    acc = (preds == y).mean()
    tp = ((preds == 1) & (y == 1)).sum()
    fn = ((preds == 0) & (y == 1)).sum()
    print(f"threshold {t}:  acc={acc:.3f}  true-positives={tp}  false-negatives={fn}")

# --- block 6 ---
bins = np.linspace(0, 1, 6)                    # 5 bins: [0,.2),[.2,.4),…
idx  = np.digitize(p, bins) - 1
for b_i in range(5):
    mask = idx == b_i
    if mask.sum():
        print(f"p in bin {b_i}:  predicted≈{p[mask].mean():.2f}"
              f"  actual class-1 rate={y[mask].mean():.2f}  (n={mask.sum()})")
