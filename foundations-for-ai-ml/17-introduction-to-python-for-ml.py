"""
Foundations for AI & ML
Chapter 17: Introduction to Python for ML
Section: Python & the ML Toolkit

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/introduction-to-python-for-ml

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file is runnable standalone) ---
# Block 4 is an if/elif/else excerpt about early stopping. These names come
# from a training loop the chapter does not show.
# See https://books.vizuara.ai/read/foundations-for-ai-ml/introduction-to-python-for-ml
loss = None       # TODO: this epoch's loss
best_loss = None  # TODO: the best loss seen so far
patience = None   # TODO: how many checks since the last improvement

# --- block 1 ---
learning_rate = 0.01      # a float
epochs = 100              # an int
model_name = "logreg"     # a string
is_trained = False        # a boolean

# --- block 2 ---
weights = [0.5, 0.5, 0.5]
backup = weights          # NOT a copy — same list, two names
weights.append(0.5)       # mutate through one name...
print(backup)             # [0.5, 0.5, 0.5, 0.5]  — the "backup" changed too

# --- block 3 ---
config = {"lr": 0.01, "epochs": 100, "batch_size": 32}
print(config["lr"])                 # 0.01
print(config.get("dropout", 0.0))   # 0.0  — key absent, fallback used
config["epochs"] = 200              # dicts are mutable: change one knob

# --- block 4 ---
if loss < best_loss:
    best_loss = loss
    patience = 0            # improved — reset our patience counter
elif patience >= 5:
    print("early stopping") # no improvement for 5 checks — quit
else:
    patience += 1           # be patient a little longer

# --- block 5 ---
losses = [0.9, 0.6, 0.42, 0.31]
total = 0.0
for value in losses:       # hands you each element, in order
    total += value
mean_loss = total / len(losses)   # 2.23 / 4 = 0.5575

# --- block 6 ---
def mse(predictions, targets):
    """Mean squared error: average of squared prediction errors."""
    total = 0.0
    for p, t in zip(predictions, targets):   # march in lockstep
        error = p - t
        total += error ** 2                  # ** is exponentiation
    return total / len(predictions)

# --- block 7 ---
preds   = [2.0, 3.0, 4.0]
truth   = [2.5, 2.0, 5.0]
print(mse(preds, truth))   # 0.75
