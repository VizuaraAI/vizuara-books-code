"""
Foundations for AI & ML
Chapter 1: Why Foundations Matter
Section: Getting Started

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/why-foundations-matter

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file is runnable standalone) ---
# Block 2 below is an excerpt: it shows the shape of a gradient-descent step.
# These two names are never defined in the chapter, so they are stubbed here.
# See https://books.vizuara.ai/read/foundations-for-ai-ml/why-foundations-matter
loss = None  # TODO: the loss value for the current prediction


def compute_gradient(loss, w):
    """TODO: supplied by you (or by autograd). The chapter states the update
    rule; it does not give an implementation of this function."""
    raise NotImplementedError("placeholder - see the chapter")


# --- block 1 ---
import numpy as np

x = np.array([2.0, 1.0, 3.0])     # size, age, bedrooms
w = np.array([3.0, -1.0, 0.5])    # learned weights

prediction = np.dot(w, x)          # 3.0*2.0 + (-1.0)*1.0 + 0.5*3.0

# --- block 2 ---
learning_rate = 0.1
gradient = compute_gradient(loss, w)   # ∂loss/∂w for every weight
w = w - learning_rate * gradient        # step downhill
