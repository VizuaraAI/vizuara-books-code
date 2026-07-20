"""
Neural Networks from Scratch
Chapter 15: The Backward Pass: Gradients by Hand
Section: How a Network Learns

Read this chapter: https://books.vizuara.ai/read/neural-networks-from-scratch/the-backward-pass-mechanics

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file runs standalone) ---
# The chapter walks the backward pass by hand, so the forward-pass values it
# reaches back for (the softmax output p, the one-hot labels, the layer-1
# pre-activations z1 and activations a1) are never assigned in its code blocks.
# The batch here is one sample, as block 1's X shows.
# See https://books.vizuara.ai/read/neural-networks-from-scratch/the-backward-pass-mechanics
p         = None   # TODO: (1, 2) softmax probabilities from the forward pass
y_onehot  = None   # TODO: (1, 2) one-hot encoding of the true class
n_samples = 1      # the chapter's worked example has a single sample
z1        = None   # TODO: (1, 3) Dense1 pre-activations from the forward pass
a1        = None   # TODO: (1, 3) ReLU(z1) from the forward pass

# --- block 1 ---
X  = [[1.0, 2.0]]                 # (1, 2) — one sample, two features
y  = 0                            # the true class is class 0

W1 = [[ 0.10, -0.20,  0.30],      # (2, 3) — Dense1: 2 -> 3
      [ 0.40,  0.50, -0.10]]
b1 = [[ 0.10,  0.00, -0.20]]      # (1, 3)

W2 = [[ 0.20, -0.30],             # (3, 2) — Dense2: 3 -> 2
      [ 0.10,  0.40],
      [-0.50,  0.60]]
b2 = [[ 0.00,  0.10]]             # (1, 2)

# --- block 2 ---
dz2 = (p - y_onehot) / n_samples        # the fused softmax+CE gradient

# --- block 3 ---
dW2 = a1.T @ dz2                        # (3,2): input.T @ incoming grad
db2 = dz2.sum(axis=0, keepdims=True)    # (1,2): sum over the batch
da1 = dz2 @ W2.T                        # (1,3): grad handed to the layer below

# --- block 4 ---
dW2 = [[-0.460,  0.460],    # from hidden unit 0 (a1=1.0)
       [-0.368,  0.368],    # from hidden unit 1 (a1=0.8)
       [ 0.000,  0.000]]    # from hidden unit 2 (a1=0.0) -> DEAD

# --- block 5 ---
dz1 = da1.copy()
dz1[z1 <= 0] = 0        # kill the gradient where the neuron was off

# --- block 6 ---
dW1 = X.T @ dz1                         # (2,3)
db1 = dz1.sum(axis=0, keepdims=True)    # (1,3)
# dinputs = dz1 @ W1.T would go to the previous layer — but X is the input, so we stop.

# --- block 7 ---
dW1 = [[-0.230,  0.138,  0.000],    # from input feature 1 (X=1.0)
       [-0.460,  0.276,  0.000]]    # from input feature 2 (X=2.0)
