"""
Deep Learning Fundamentals
Chapter 24: The entire forward-backward pass in Python
Section: The Full Training Loop

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/forward-backward-pass-in-python

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np
np.random.seed(0)

# ---- the building blocks (built in earlier chapters) ----
class Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases  = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.inputs  = inputs                          # remember for backward
        self.output  = inputs @ self.weights + self.biases
    def backward(self, dvalues):
        self.dweights = self.inputs.T @ dvalues        # (n_inputs, n_neurons)
        self.dbiases  = np.sum(dvalues, axis=0, keepdims=True)
        self.dinputs  = dvalues @ self.weights.T       # baton to the previous layer

class ReLU:
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)
    def backward(self, dvalues):
        self.dinputs = dvalues.copy()
        self.dinputs[self.inputs <= 0] = 0             # zero the dead neurons

class SoftmaxCrossEntropy:
    def forward(self, logits, y_true):
        exp = np.exp(logits - logits.max(axis=1, keepdims=True))   # stable softmax
        self.output = exp / exp.sum(axis=1, keepdims=True)         # ŷ, rows sum to 1
        clipped = np.clip(self.output, 1e-7, 1 - 1e-7)             # avoid log(0)
        correct = np.sum(clipped * y_true, axis=1)                 # ŷ of the true class
        return np.mean(-np.log(correct))                          # scalar loss
    def backward(self, y_true):
        batch = len(y_true)
        self.dinputs = (self.output - y_true) / batch             # the ŷ - y shortcut

# --- block 2 ---
# ---- the network: a 4 -> 5 -> 3 classifier ----
dense1 = Dense(4, 5)
relu   = ReLU()
dense2 = Dense(5, 3)
loss_fn = SoftmaxCrossEntropy()

layers = [dense1, relu, dense2]        # forward order

# ---- a tiny batch: 2 samples, 4 features, 3 classes ----
X = np.array([[1.0, 2.0, 3.0, 2.5],
              [2.0, 5.0, -1.0, 2.0]])
y = np.array([[1.0, 0.0, 0.0],         # sample 0 is class 0
              [0.0, 0.0, 1.0]])         # sample 1 is class 2

# ---- ONE TRAINING STEP ----
# 1. FORWARD: walk the list, feeding each output into the next
out = X
for layer in layers:
    layer.forward(out)
    out = layer.output                 # this layer's output = next layer's input

# 2. LOSS: fused softmax + cross-entropy on the final logits
loss = loss_fn.forward(out, y)

# 3. BACKWARD: kick off with the fused gradient, then walk the list in reverse
loss_fn.backward(y)
dvalues = loss_fn.dinputs
for layer in reversed(layers):
    layer.backward(dvalues)
    dvalues = layer.dinputs

print("loss:", loss)
print("dense1.dweights.shape:", dense1.dweights.shape)   # (4, 5)
print("dense2.dweights.shape:", dense2.dweights.shape)   # (5, 3)

# --- stubs (not book code) ---
# The chapter writes `range(EPOCHS)` and uses `LR` but never assigns either one.
# The values below are NOT from the book - they are placeholders so the file runs.
# Choose your own; nothing in the chapter depends on these particular numbers.
EPOCHS = 1000   # placeholder, not the book's value
LR = 1.0        # placeholder, not the book's value

# --- block 3 ---

for step in range(EPOCHS):
    # --- forward ---
    out = X
    for layer in layers:
        layer.forward(out); out = layer.output
    loss = loss_fn.forward(out, y)

    # --- backward ---
    loss_fn.backward(y)
    dvalues = loss_fn.dinputs
    for layer in reversed(layers):
        layer.backward(dvalues); dvalues = layer.dinputs

    # --- update (NEXT CHAPTER) ---
    for layer in (dense1, dense2):
        layer.weights -= LR * layer.dweights     # gradient descent, coming next
        layer.biases  -= LR * layer.dbiases

    if step % 100 == 0:
        print(f"step {step}: loss {loss:.4f}")
