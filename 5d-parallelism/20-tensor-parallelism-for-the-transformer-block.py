"""
5D Parallelism for Large Model Training
Chapter 20: Tensor Parallelism for the Transformer Block
Section: Tensor Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/tensor-parallelism-for-the-transformer-block

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# x: (seq_len, d_model)
h = gelu(x @ A)   # A: (d_model, d_ff)   → h: (seq_len, d_ff)
y = h @ B         # B: (d_ff, d_model)   → y: (seq_len, d_model)
