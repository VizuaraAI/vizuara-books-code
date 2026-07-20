"""
Convolutional Neural Networks Fundamentals
Chapter 9: How ML Is Taught, and How We Will Teach It
Section: From Machine Learning to Deep Learning

Read this chapter: https://books.vizuara.ai/read/cnn-fundamentals/transitioning-to-ml

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
signal = [1, 2, 3, 4, 5]
kernel = [1, 0, -1]     # a tiny "difference" detector

# --- block 2 ---
def conv1d(signal, kernel):
    K = len(kernel)
    O = len(signal) - K + 1          # the rule you just derived
    out = []
    for i in range(O):               # each output position = one "stop"
        window = signal[i:i + K]     # the K values the kernel sits on
        s = sum(w * x for w, x in zip(kernel, window))  # multiply-add
        out.append(s)
    return out

conv1d([1, 2, 3, 4, 5], [1, 0, -1])   # → [-2, -2, -2]
