"""
NLP & Computer Vision Mastery
Chapter 5: TensorFlow vs NumPy: Why Speed Matters
Section: Foundations of Vision

Read this chapter: https://books.vizuara.ai/read/nlp-cv-mastery/tensorflow-vs-numpy-speed

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def conv2d_naive(image, kernel):          # image (H, W), kernel (k, k)
    H, W = image.shape
    k = kernel.shape[0]
    out = np.zeros((H - k + 1, W - k + 1))
    for i in range(H - k + 1):            # every output row
        for j in range(W - k + 1):        # every output col
            acc = 0.0
            for di in range(k):           # every kernel row
                for dj in range(k):       # every kernel col
                    acc += image[i + di, j + dj] * kernel[di, dj]
            out[i, j] = acc
    return out

# --- block 2 ---
def conv2d_vectorized(image, kernel):     # same result, no Python inner loops
    H, W = image.shape
    k = kernel.shape[0]
    oh, ow = H - k + 1, W - k + 1
    # build (oh*ow, k*k): one row per output position, one col per kernel cell
    cols = np.stack([image[i:i+oh, j:j+ow].ravel()
                     for i in range(k) for j in range(k)], axis=1)
    return (cols @ kernel.ravel()).reshape(oh, ow)
