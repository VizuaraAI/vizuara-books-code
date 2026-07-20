"""
Neural Networks from Scratch
Chapter 31: Coding the Optimizer
Section: Loss, Optimizer, and Training

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/optimizers-in-code

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- context (added so this file runs standalone) ---
# The network objects and the spiral dataset are built in earlier chapters of
# this same book (21, 22-24, 26, 27). context.py holds them verbatim.
from context import dense1, activation1, dense2, X, y

# --- placeholders (added so this file runs standalone) ---
# The book calls the fused softmax + cross-entropy object `loss_activation`,
# but no code block in the book defines the class it is an instance of.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/optimizers-in-code
loss_activation = None   # TODO: the fused softmax + cross-entropy object

# --- block 1 ---
class Optimizer_SGD:
    def __init__(self, learning_rate=1.0):
        self.learning_rate = learning_rate

    def update_params(self, layer):
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases  += -self.learning_rate * layer.dbiases

# --- block 2 ---
optimizer = Optimizer_SGD(learning_rate=1.0)

# forward pass
dense1.forward(X)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
loss = loss_activation.forward(dense2.output, y)

# backward pass
loss_activation.backward(loss_activation.output, y)
dense2.backward(loss_activation.dinputs)
activation1.backward(dense2.dinputs)
dense1.backward(activation1.dinputs)

# the new part: step
optimizer.update_params(dense1)
optimizer.update_params(dense2)
