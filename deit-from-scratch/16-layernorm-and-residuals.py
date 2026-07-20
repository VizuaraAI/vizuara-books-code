"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 16: LayerNorm and Residual Connections
Section: Attention from Scratch

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/layernorm-and-residuals

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# x has shape (batch, num_tokens, d), e.g. (B, 198, 384) for DeiT-Small
x = x + attn( norm1(x) )   # mix information across tokens
x = x + mlp(  norm2(x) )   # process each token on its own
