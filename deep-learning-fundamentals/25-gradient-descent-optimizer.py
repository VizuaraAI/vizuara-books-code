"""
Deep Learning Fundamentals
Chapter 25: Coding the gradient descent optimizer
Section: Optimizers

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/gradient-descent-optimizer

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- shared context (not book text) ---
# Block 2 trains the network the book builds across chapters 7-22 (and the
# batch X, y it feeds it), but this chapter never constructs it in a code block
# of its own. context.py holds those objects, copied verbatim from the book.
from context import dense1, relu, dense2, loss_activation, X, y

# --- block 1 ---
class Optimizer_SGD:
    def __init__(self, learning_rate=1.0):
        self.learning_rate = learning_rate

    def update_params(self, layer):
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases  += -self.learning_rate * layer.dbiases

# --- block 2 ---
optimizer = Optimizer_SGD(learning_rate=1.0)

for epoch in range(101):
    # 1. forward pass: data -> predictions -> loss
    dense1.forward(X)
    relu.forward(dense1.output)
    dense2.forward(relu.output)
    loss = loss_activation.forward(dense2.output, y)   # softmax + cross-entropy, fused

    # 2. backward pass: fill every dweights / dbiases
    loss_activation.backward(loss_activation.output, y)
    dense2.backward(loss_activation.dinputs)
    relu.backward(dense2.dinputs)
    dense1.backward(relu.dinputs)

    # 3. update: the optimizer walks every layer downhill
    optimizer.update_params(dense1)
    optimizer.update_params(dense2)

    if epoch % 20 == 0:
        print(f"epoch {epoch:3d}   loss {loss:.4f}")
