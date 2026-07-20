"""
Modern Robot Learning
Chapter 19: The Encoder-Decoder Framework
Section: Transformer Architecture from Scratch

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/the-transformer-encoder-decoder

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# x   : decoder state so far, shape (out_len, d)
# mem : encoder memory (frozen for all decode steps), shape (in_len, d)
def decoder_block(x, mem, causal_mask):
    # 1. look at my own past only
    x = layernorm(x + masked_self_attention(x, x, x, mask=causal_mask))
    # 2. reach into the encoder: Q from x, K and V from mem  <-- the hinge
    x = layernorm(x + cross_attention(q=x, k=mem, v=mem))
    # 3. think, per token
    x = layernorm(x + feed_forward(x))
    return x                                   # same shape (out_len, d)
