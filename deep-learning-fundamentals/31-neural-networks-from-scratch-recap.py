"""
Deep Learning Fundamentals
Chapter 31: Neural networks from scratch, end to end
Section: Recap: A Network from Scratch

Read this chapter: https://books.vizuara.ai/read/deep-learning-fundamentals/neural-networks-from-scratch-recap

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- stubs (not book code) ---
# The chapter uses these names without defining them. Placeholders so the file runs.
epochs = 101   # TODO: pick your own - the chapter does not set this

# --- block 1 (commented out) ---
# NOTE: this block is prose in the book, not runnable code. It is the recap of
# the fused softmax + cross-entropy gradient written as maths notation;
# y_pred, y_true and batch_size are symbols the chapter never assigns.
# dz2 = (y_pred - y_true) / batch_size   # "predicted minus true"

# --- shared context (not book text) ---
# Block 2 trains the network the book builds across chapters 7-25 (and the
# batch X, y and the optimizer it uses), but this recap chapter never
# constructs any of it in a code block of its own. context.py holds those
# objects, copied verbatim from the book.
from context import dense1, relu, dense2, loss_activation, optimizer, X, y

# The length of the training run is left to the reader.

# --- block 2 ---
for epoch in range(epochs):
    # 1. FORWARD
    dense1.forward(X)
    relu.forward(dense1.output)
    dense2.forward(relu.output)
    loss = loss_activation.forward(dense2.output, y)   # softmax + cross-entropy

    # 2. BACKWARD (gradients flow right to left)
    loss_activation.backward(loss_activation.output, y)  # dz2 = (ŷ - y)/N
    dense2.backward(loss_activation.dinputs)
    relu.backward(dense2.dinputs)
    dense1.backward(relu.dinputs)

    # 3. UPDATE (optimizer nudges every weight)
    optimizer.update_params(dense1)
    optimizer.update_params(dense2)
