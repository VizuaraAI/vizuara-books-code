"""
Neural Networks from Scratch
Chapter 33: Visualizing the Results
Section: Loss, Optimizer, and Training

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/visualizing-the-results

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added so this file runs standalone) ---
# The four network objects and the spiral dataset are built in earlier
# chapters of this same book (21, 22-24, 26, 27). context.py holds them
# verbatim. NOTE: as imported they are freshly initialised - chapter 32 is
# what trains them, so re-run that training before the plot means anything.
from context import dense1, activation1, dense2, activation2, X, y

# --- block 1 ---
import numpy as np
import matplotlib.pyplot as plt

# 1. build a fine grid over the region the spiral occupies
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))
grid = np.c_[xx.ravel(), yy.ravel()]          # (90000, 2)

# 2. run the SAME forward pass we trained with — no training, just inference
dense1.forward(grid)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)            # softmax probabilities, shape (90000, 3)

# 3. collapse each row of 3 probabilities to its winning class
predictions = np.argmax(activation2.output, axis=1)   # (90000,)
zz = predictions.reshape(xx.shape)                    # back to (300, 300)

# 4. paint the regions, then scatter the real training data on top
plt.contourf(xx, yy, zz, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, s=10)
plt.show()

# --- block 2 ---
predictions = np.argmax(activation2.output, axis=1)   # class per sample, (300,)
accuracy = np.mean(predictions == y)                  # fraction that match the true label
