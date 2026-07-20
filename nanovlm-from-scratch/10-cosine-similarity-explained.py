"""
Build a NanoVLM from Scratch
Chapter 10: Cosine Similarity, Explained
Section: Embeddings & Similarity

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/cosine-similarity-explained

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
# cos(a, b) = (a · b) / (‖a‖ · ‖b‖)

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# a · b = (2)(4) + (1)(2) + (2)(4) = 8 + 2 + 8 = 18

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# ‖a‖ = √(2² + 1² + 2²) = √(4 + 1 + 4) = √9 = 3
# ‖b‖ = √(4² + 2² + 4²) = √(16 + 4 + 16) = √36 = 6

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# cos(a, b) = 18 / (3 × 6) = 18 / 18 = 1.0

# --- block 5 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# a · c = (2)(-1) + (1)(2) + (2)(0) = -2 + 2 + 0 = 0

# --- block 6 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# cos(â, b̂) = (â · b̂) / (1 × 1) = â · b̂

# --- block 7 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# â = [2/3, 1/3, 2/3]
# b̂ = [4/6, 2/6, 4/6] = [2/3, 1/3, 2/3]

# --- block 8 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# â · b̂ = (2/3)² + (1/3)² + (2/3)² = 4/9 + 1/9 + 4/9 = 9/9 = 1.0
