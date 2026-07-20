"""
Machine Learning & Deep Learning Mastery
Chapter 31: Backpropagation: The Complete Theory
Section: Neural Networks: Backpropagation

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/backpropagation-complete-theory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def backward(X, Y, A1, Z1, Yhat, W2):
    N = X.shape[0]                       # batch size = 3
    # --- output layer ---
    delta2 = (Yhat - Y) / N              # (3,2): softmax+CE shortcut, averaged
    dW2 = A1.T @ delta2                  # (5,3)·(3,2) → (5,2)
    db2 = delta2.sum(axis=0)             # (2,)
    # --- hand blame back to the hidden layer ---
    dA1    = delta2 @ W2.T               # (3,2)·(2,5) → (3,5): through the weights
    delta1 = dA1 * (Z1 > 0)              # (3,5): through the ReLU gate
    dW1 = X.T @ delta1                   # (4,3)·(3,5) → (4,5)
    db1 = delta1.sum(axis=0)            # (5,)
    return dW1, db1, dW2, db2
