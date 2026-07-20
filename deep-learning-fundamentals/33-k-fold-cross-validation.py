"""
Deep Learning Fundamentals
Chapter 33: K-fold cross validation
Section: Regularization and Testing

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/k-fold-cross-validation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The chapter uses these names without defining them. Placeholders so the file runs.
X = None              # TODO: your feature matrix, shape (n_samples, n_features)
y = None              # TODO: your labels, shape (n_samples,)
build_network = None  # TODO: a callable returning a fresh, untrained network

# --- block 1 ---
import numpy as np

def k_fold_indices(n_samples, k=5, seed=0):
    idx = np.arange(n_samples)
    np.random.default_rng(seed).shuffle(idx)   # shuffle ONCE, up front
    folds = np.array_split(idx, k)             # k roughly-equal chunks

    for i in range(k):
        val_idx = folds[i]                                  # this fold = validation
        train_idx = np.concatenate(folds[:i] + folds[i+1:]) # every OTHER fold = train
        yield train_idx, val_idx

# --- placeholders the reader supplies ---
# Block 2 is the usage sketch. The chapter never loads a dataset and never
# defines build_network(); they are yours to bring.
# See https://books.vizuara.ai/read/deep-learning-fundamentals/k-fold-cross-validation

# --- block 2 ---
scores = []
for train_idx, val_idx in k_fold_indices(len(X), k=5):
    model = build_network()                 # a NEW network each fold
    model.train(X[train_idx], y[train_idx])
    scores.append(model.evaluate(X[val_idx], y[val_idx]))

scores = np.array(scores)
print(f"{scores.mean():.3f} ± {scores.std():.3f}")   # e.g. 0.810 ± 0.058
