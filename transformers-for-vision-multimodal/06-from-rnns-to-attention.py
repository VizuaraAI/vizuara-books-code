"""
Transformers for Vision & Multimodal LLMs
Chapter 6: From RNNs to Attention
Section: Attention From Scratch

Read this chapter: https://books.vizuara.ai/read/transformers-for-vision-multimodal/from-rnns-to-attention

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
h = 0                                  # a vector, say length 4
for x in ["the", "cat", "sat"]:        # one token at a time, in order
    h = tanh(W_h @ h + W_x @ embed(x)) # new summary = blend(old summary, new token)
