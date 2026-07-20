"""
Foundations for AI & ML
Chapter 3: How a Model Learns: The Big Picture
Section: Getting Started

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/how-a-model-learns-the-big-picture

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file is runnable standalone) ---
# Blocks 2 and 3 are excerpts of the training loop. These names are used but
# never defined in the chapter text, so they are stubbed here.
# See https://books.vizuara.ai/read/foundations-for-ai-ml/how-a-model-learns-the-big-picture
x = None      # TODO: your input data (hours studied)
y = None      # TODO: your targets (exam scores)
w = None      # TODO: weight, re-initialised by block 3 below
b = None      # TODO: bias, re-initialised by block 3 below
eta = None    # TODO: the learning rate
dL_dw = None  # TODO: gradient of the loss w.r.t. w
dL_db = None  # TODO: gradient of the loss w.r.t. b

# --- block 1 ---
def predict(hours, w, b):
    return w * hours + b   # ŷ = w·x + b

# --- block 2 ---
# one gradient-descent step, learning rate eta
w = w - eta * dL_dw     # nudge w downhill
b = b - eta * dL_db     # nudge b downhill

# --- block 3 ---
w, b = 5, 20              # 1. start with arbitrary parameters
for step in range(10000):
    y_hat = w * x + b         # 2. MODEL: predict from data
    loss  = (y_hat - y)**2    # 3. LOSS: measure the error
    dL_dw = 2*(y_hat - y)*x   # gradient of loss w.r.t. w
    dL_db = 2*(y_hat - y)     # gradient of loss w.r.t. b
    w -= eta * dL_dw          # 4. UPDATE: nudge downhill
    b -= eta * dL_db          #    ... then REPEAT
