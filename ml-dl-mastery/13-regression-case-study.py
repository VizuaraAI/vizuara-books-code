"""
Machine Learning & Deep Learning Mastery
Chapter 13: A Regression Case Study
Section: Overfitting, Features & Generalization

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/regression-case-study

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# The case study standardizes a split the reader brings; these are yours to
# supply, so they are stubbed here rather than invented.
# TODO: see https://books.vizuara.ai/read/ml-dl-mastery/regression-case-study
X_train = None  # TODO: your training features, shape (n_train, n_features)
X_test = None   # TODO: your test features, shape (n_test, n_features)

# --- block 1 ---
mu    = X_train.mean(axis=0)
sigma = X_train.std(axis=0)

X_train_std = (X_train - mu) / sigma
X_test_std  = (X_test  - mu) / sigma   # reuse TRAIN's mu, sigma — never recompute on test
