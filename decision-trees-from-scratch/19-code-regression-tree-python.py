"""
Build Decision Trees from Scratch
Chapter 19: Code an Entire Regression Tree in Python
Section: Regression Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/code-regression-tree-python

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def ssr(y):
    if len(y) == 0:
        return 0.0
    return np.sum((y - y.mean()) ** 2)   # Σ (yᵢ − ȳ)²

def _leaf_value(y):
    return y.mean()                       # a regression leaf predicts the mean

# --- block 2 ---
def _best_split(X, y):
    n, n_features = X.shape
    best = {"score": np.inf, "feature": None, "threshold": None}
    for f in range(n_features):                       # every feature
        values = np.unique(X[:, f])                   # sorted, distinct
        for a, b in zip(values[:-1], values[1:]):
            t = (a + b) / 2                            # midpoint threshold
            left  = y[X[:, f] <= t]
            right = y[X[:, f] >  t]
            if len(left) == 0 or len(right) == 0:
                continue
            score = ssr(left) + ssr(right)            # total squared error
            if score < best["score"]:                 # keep the smallest
                best = {"score": score, "feature": f, "threshold": t}
    return best

# --- block 3 ---
class Node:
    def __init__(self, feature=None, threshold=None,
                 left=None, right=None, *, value=None):
        self.feature = feature      # column index we test
        self.threshold = threshold  # split point, e.g. 25.5
        self.left = left            # rows with feature <= threshold
        self.right = right          # rows with feature >  threshold
        self.value = value          # set ONLY on a leaf: the predicted MEAN

    def is_leaf(self):
        return self.value is not None

# --- block 4 ---
class RegressionTree:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X, y):
        self.root = self._grow(np.asarray(X), np.asarray(y, dtype=float), depth=0)
        return self

    def _grow(self, X, y, depth):
        # --- base cases → make a leaf that predicts the mean ---
        if (ssr(y) == 0                                        # all targets equal
            or (self.max_depth is not None and depth >= self.max_depth)
            or len(y) < self.min_samples_split):
            return Node(value=_leaf_value(y))

        split = _best_split(X, y)
        if split["feature"] is None:                          # no valid split
            return Node(value=_leaf_value(y))

        f, t = split["feature"], split["threshold"]
        mask = X[:, f] <= t
        left  = self._grow(X[mask],  y[mask],  depth + 1)
        right = self._grow(X[~mask], y[~mask], depth + 1)
        return Node(feature=f, threshold=t, left=left, right=right)

# --- block 5 ---
    def _predict_one(self, node, row):
        if node.is_leaf():
            return node.value
        if row[node.feature] <= node.threshold:
            return self._predict_one(node.left, row)
        return self._predict_one(node.right, row)

    def predict(self, X):
        X = np.asarray(X)
        return np.array([self._predict_one(self.root, row) for row in X])

# --- block 6 ---
X = np.array([[14,55],[22,40],[30,70],[18,65],[27,80],[24,45]])
y = np.array([40, 35, 0, 30, 0, 45])          # minutes run

tree = RegressionTree(max_depth=1).fit(X, y)
print(tree.predict([[19, 60]]))               # a mild new day
