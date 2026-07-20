"""
Foundations for AI & ML
Chapter 21: Data Visualization for Machine Learning
Section: Python & the ML Toolkit

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/data-visualization-for-machine-learning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file is runnable standalone) ---
# Blocks 3 and 4 plot a fitted classifier over the iris petal features. The
# chapter shows the plotting calls only; the data and the model come from
# your own session (the model is built in the scikit-learn chapter).
# See https://books.vizuara.ai/read/foundations-for-ai-ml/data-visualization-for-machine-learning
length = None         # TODO: petal length array
width = None          # TODO: petal width array
species_label = None  # TODO: integer class label per sample
x_min = None          # TODO: grid bounds for the decision-region plot
x_max = None          # TODO
y_min = None          # TODO
y_max = None          # TODO
model = None          # TODO: a fitted classifier with .predict() - see
#                       https://books.vizuara.ai/read/foundations-for-ai-ml/scikit-learn-the-ml-workhorse

# --- block 1 ---
import matplotlib.pyplot as plt
import numpy as np

# --- block 2 ---
petal_length = np.array([1.4, 1.5, 1.3, 4.7, 4.5, 4.9,
                         1.4, 4.6, 5.9, 6.0, 5.8, 6.1])
plt.hist(petal_length, bins=3, edgecolor="black")
plt.xlabel("petal length (cm)")
plt.ylabel("count")
plt.title("Distribution of petal length")
plt.show()

# --- block 3 ---
plt.scatter(length, width, c=species_label, cmap="viridis")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")
plt.title("Petal features, coloured by species")
plt.show()

# --- block 4 ---
# 1. build a grid of points covering the feature space
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))
grid = np.c_[xx.ravel(), yy.ravel()]      # every grid point as (n, 2)

# 2. classify every point on the grid
Z = model.predict(grid).reshape(xx.shape)

# 3. paint the regions, then scatter the real data on top
plt.contourf(xx, yy, Z, alpha=0.3)         # coloured background = regions
plt.scatter(length, width, c=species_label, edgecolor="black")
plt.show()
