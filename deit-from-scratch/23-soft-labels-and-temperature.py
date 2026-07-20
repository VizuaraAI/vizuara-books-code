"""
Build a Data-Efficient Image Transformer (DeiT) from Scratch
Chapter 23: Soft Labels and Temperature
Section: Knowledge Distillation

Read this chapter: https://books.vizuara.ai/read/deit-from-scratch/soft-labels-and-temperature

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
# softmax(z)[i] = exp(z[i]) / sum_j exp(z[j])

# --- block 2 ---
Zt = [8.0, 4.0, 3.5, -1.0]   # classes: cat, tiger, lynx, car

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# ψ(Zt) ≈ [0.9713, 0.0178, 0.0108, 0.00012]   # cat 97.1%, tiger 1.8%, lynx 1.1%, car 0.01%

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# softmax_T(z)[i] = exp(z[i] / T) / sum_j exp(z[j] / T)

# --- block 5 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# ψ(Zt / 4) ≈ [0.556, 0.205, 0.181, 0.059]   # cat 55.6%, tiger 20.5%, lynx 18.1%, car 5.9%
