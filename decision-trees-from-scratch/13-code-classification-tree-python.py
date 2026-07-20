"""
Build Decision Trees from Scratch
Chapter 13: Code an Entire Classification Tree in Python
Section: Classification Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/code-classification-tree-python

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
class Node:
    def __init__(self, feature=None, threshold=None,
                 left=None, right=None, *, value=None):
        self.feature = feature      # index of the column we test
        self.threshold = threshold  # the split point, e.g. 25.5
        self.left = left            # Node for rows with feature <= threshold
        self.right = right          # Node for rows with feature >  threshold
        self.value = value          # set ONLY on a leaf: the predicted class

    def is_leaf(self):
        return self.value is not None

# --- block 2 ---
from collections import Counter
import numpy as np

def _majority(y):
    return Counter(y).most_common(1)[0][0]   # the mode: the majority class

def gini(y):
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    return 1.0 - np.sum(p ** 2)              # 1 − Σ pₖ²

# --- block 3 ---
def _best_split(X, y):
    n, n_features = X.shape
    parent = gini(y)
    best = {"gain": 0.0, "feature": None, "threshold": None}
    for f in range(n_features):                     # every feature
        values = np.unique(X[:, f])                 # sorted, distinct
        for a, b in zip(values[:-1], values[1:]):
            t = (a + b) / 2                          # midpoint threshold
            left  = y[X[:, f] <= t]
            right = y[X[:, f] >  t]
            if len(left) == 0 or len(right) == 0:
                continue
            score = (len(left)/n)*gini(left) + (len(right)/n)*gini(right)
            gain = parent - score                    # Gini gain
            if gain > best["gain"]:                  # keep the biggest drop
                best = {"gain": gain, "feature": f, "threshold": t}
    return best

# --- block 4 ---
class DecisionTree:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X, y):
        self.root = self._grow(np.asarray(X), np.asarray(y), depth=0)
        return self

    def _grow(self, X, y, depth):
        # --- base cases (pre-pruning) → make a leaf ---
        if (gini(y) == 0                                     # pure node
            or (self.max_depth is not None and depth >= self.max_depth)
            or len(y) < self.min_samples_split):
            return Node(value=_majority(y))

        split = _best_split(X, y)
        if split["feature"] is None:                        # no positive gain
            return Node(value=_majority(y))

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
y = np.array(["yes","yes","no","yes","no","yes"])

tree = DecisionTree(max_depth=3).fit(X, y)
print(tree.predict([[19, 60]]))     # a mild new morning
