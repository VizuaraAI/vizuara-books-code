"""
Transformers: Theory, intuition, and Building from Scratch
Chapter 15: The Encoder Block
Section: Piecing It All Together

Read this chapter: https://books.vizuara.ai/read/transformers-from-scratch/the-encoder-block

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def ffn(x, W1, b1, W2, b2):
    # x: (seq_len, 512)
    hidden = relu(x @ W1 + b1)   # (seq_len, 2048): expand and squash negatives
    return hidden @ W2 + b2       # (seq_len, 512): project back down

# --- block 2 ---
def encoder_block(x):
    # x: (seq_len, 512)
    x = layer_norm(x + multi_head_attention(x))   # sublayer 1: communicate
    x = layer_norm(x + feed_forward(x))            # sublayer 2: compute
    return x                                        # (seq_len, 512)
