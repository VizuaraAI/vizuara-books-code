"""
5D Parallelism for Large Model Training
Chapter 7: Activation Recomputation
Section: Data Parallelism

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/activation-recomputation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# naive: every internal activation of `block` is saved for backward
x = block(x)

# --- block 2 ---
from torch.utils.checkpoint import checkpoint

# recomputed: only `x` (the input) is kept; block internals are
# discarded on forward and regenerated during backward
x = checkpoint(block, x, use_reentrant=False)
