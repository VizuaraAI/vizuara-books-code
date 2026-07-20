"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 3: What Makes DeiT Data-Efficient
Section: Why DeiT?

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/what-makes-deit-data-efficient

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# # hard-label distillation loss (DeiT's default)
# loss = 0.5 * cross_entropy(psi(Zs), y)      # supervised by the true label
#      + 0.5 * cross_entropy(psi(Zs), y_t)     # supervised by the frozen CNN teacher
