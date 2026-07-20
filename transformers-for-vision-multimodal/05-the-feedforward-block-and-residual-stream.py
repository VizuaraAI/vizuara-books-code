"""
Transformers for Vision & Multimodal LLMs
Chapter 5: The Feedforward Block and the Residual Stream
Section: Foundations — From CNNs to Transformers

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/the-feedforward-block-and-residual-stream

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def ffn(x, W1, b1, W2, b2):
    # x: (n_tokens, d_model)
    h = gelu(x @ W1 + b1)   # (n_tokens, d_ff)  — expand, then squash
    return h @ W2 + b2      # (n_tokens, d_model) — project back down

# --- block 2 ---
x = x + attention(x)     # attention writes its result BACK onto x
x = x + ffn(x)           # ffn writes its result BACK onto x
