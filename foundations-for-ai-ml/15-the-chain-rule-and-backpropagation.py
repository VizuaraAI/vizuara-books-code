"""
Foundations for AI & ML
Chapter 15: The Chain Rule and Backpropagation
Section: Calculus for Optimization

Read this chapter: https://books.vizuara.ai/read/foundations-for-ai-ml/the-chain-rule-and-backpropagation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholders (added so this file is runnable standalone) ---
# Block 1 is an excerpt of one layer's backward pass. It assumes a cached
# forward pass that the chapter describes in prose but never codes.
# See https://books.vizuara.ai/read/foundations-for-ai-ml/the-chain-rule-and-backpropagation
grad_from_above = None  # TODO: dL/da handed down from the next layer
z = None                # TODO: cached pre-activation of this layer
x = None                # TODO: cached input to this layer
W = None                # TODO: this layer's weight matrix


def phi_prime(z):
    """TODO: derivative of this layer's activation phi. The chapter names it
    but does not define it."""
    raise NotImplementedError("placeholder - see the chapter")


# --- block 1 ---
# forward pass cached: x (input), z = W @ x + b, a = phi(z)
delta = grad_from_above * phi_prime(z)   # elementwise: dL/dz for this layer
grad_W = delta @ x.T                      # gradient for the weights
grad_b = delta                            # gradient for the bias
grad_to_below = W.T @ delta               # the delta handed to the previous layer
