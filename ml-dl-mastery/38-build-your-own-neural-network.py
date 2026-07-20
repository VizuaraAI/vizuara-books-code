"""
Machine Learning & Deep Learning Mastery
Chapter 38: Project: Build Your Own Neural Network
Section: Optimizers & Training

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/build-your-own-neural-network

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# This project chapter assembles components built earlier in the book.
# Dense and ReLU exist in the extracted code (chapters 32 and 33):
from context import Dense, ReLU

# Dropout, SoftmaxCrossEntropy and Adam are described in chapters 37, 27 and
# 35/36 but never printed as classes anywhere in the book, so they are stubbed
# rather than invented, along with the dataset the project trains on.
# TODO: see https://books.vizuara.ai/read/ml-dl-mastery/build-your-own-neural-network
Dropout = None              # TODO: the chapter asks you to build this (ch 37 explains it)
SoftmaxCrossEntropy = None  # TODO: the chapter asks you to build this (ch 27 explains it)
Adam = None                 # TODO: the chapter asks you to build this (ch 35/36 explain it)
X = None                    # TODO: your two-feature, two-class training data
y = None                    # TODO: the matching integer class labels

# --- block 1 ---
# --- the model: 2 -> 16 (ReLU) -> 2 (softmax) ---
layer1 = Dense(n_in=2, n_out=16)     # W1: (2,16), b1: (16,)
relu   = ReLU()
drop   = Dropout(p=0.2)              # train only
layer2 = Dense(n_in=16, n_out=2)     # W2: (16,2), b2: (2,)
loss_fn = SoftmaxCrossEntropy()      # softmax + CE fused
optimizer = Adam(lr=0.02)

def forward(X, training=True):
    z1 = layer1.forward(X)           # (N,2) @ (2,16) -> (N,16)
    a1 = relu.forward(z1)
    a1 = drop.forward(a1, training)  # off when training=False
    z2 = layer2.forward(a1)          # (N,16) @ (16,2) -> (N,2)
    return z2                        # logits; softmax lives in the loss

# --- block 2 ---
for epoch in range(2000):
    logits = forward(X, training=True)          # 1. FORWARD
    loss, dlogits = loss_fn(logits, y)          # 2. LOSS  (returns value AND gradient seed)

    # 3. BACKWARD — chain rule, top to bottom
    da1 = layer2.backward(dlogits)              # ∂L/∂a1, and stashes ∂L/∂W2, ∂L/∂b2
    da1 = drop.backward(da1)
    dz1 = relu.backward(da1)
    layer1.backward(dz1)                        # stashes ∂L/∂W1, ∂L/∂b1

    # 4. STEP — optimizer applies every stashed gradient
    optimizer.step([layer1, layer2])
