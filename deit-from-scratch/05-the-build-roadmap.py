"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 5: The Build Roadmap
Section: Why DeiT?

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/the-build-roadmap

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
x = x + attn(norm1(x))   # mix across tokens, then add the input back
x = x + mlp(norm2(x))    # process each token, then add the input back
