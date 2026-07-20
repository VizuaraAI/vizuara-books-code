"""
Convolutional Neural Networks Fundamentals
Chapter 14: Filters in 1-D and the Convolution Operation
Section: Filtering and Convolution

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/filters-in-1d-and-the-convolution-operation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
signal = [3, 1, 2, 4, 1, 0, 2]   # length W = 7

# --- block 2 ---
kernel = [1, 0, -1]              # length K = 3

# --- block 3 ---
def convolve_1d(signal, kernel):
    K = len(kernel)
    O = len(signal) - K + 1                 # output length: W - K + 1
    out = []
    for i in range(O):                       # slide the window
        window = signal[i : i + K]           # the K values under the kernel
        out.append(sum(w * x for w, x in zip(kernel, window)))  # dot product
    return out

convolve_1d([3, 1, 2, 4, 1, 0, 2], [1, 0, -1])
# -> [1, -3, 1, 4, -1]
