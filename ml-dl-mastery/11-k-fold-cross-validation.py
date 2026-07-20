"""
Machine Learning & Deep Learning Mastery
Chapter 11: K-Fold Cross-Validation
Section: Overfitting, Features & Generalization

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/k-fold-cross-validation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The chapter uses these names without defining them. Placeholders so the file runs.
X = None  # TODO: your full feature matrix, shape (n_samples, n_features)
y = None  # TODO: your full label vector, shape (n_samples,)

# --- block 1 ---
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

# The chapter's own comment below says "X, y are the FULL dataset" - they are
# yours to supply, so they are stubbed here rather than invented.

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = []

for train_idx, val_idx in kf.split(X):          # X, y are the FULL dataset
    model = LogisticRegression()                 # a FRESH model every fold
    model.fit(X[train_idx], y[train_idx])        # train on K−1 folds
    preds = model.predict(X[val_idx])            # predict the held-out fold
    scores.append(accuracy_score(y[val_idx], preds))

print(np.mean(scores), np.std(scores))           # → 0.89 0.024
