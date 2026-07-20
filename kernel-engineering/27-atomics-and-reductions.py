"""
Kernel Engineering
Chapter 27: Atomics & reductions
Section: The CUDA Programming Model

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/atomics-and-reductions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
acc = 0.0
for x in array:
    acc += x     # one number, folded in, a million times
