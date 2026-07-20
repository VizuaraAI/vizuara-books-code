"""
Build a NanoVLM from Scratch
Chapter 23: Temperature and Logit Scaling
Section: Contrastive Learning

Read this chapter: https://books.vizuara.ai/read/nanovlm-from-scratch/temperature-and-logit-scaling

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- companion-repo scaffolding (not book code) ---
from torch import clamp, exp

S = None            # TODO: (N, N) cosine similarity matrix
temperature = 0.07  # the chapter's worked value
t = None            # TODO: the learnable log-temperature parameter


# --- block 1 ---
logits = S / temperature      # temperature is a small positive scalar, e.g. 0.07

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# p_correct = 2.46 / 6.14 = 0.40

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# p_correct = 6.05 / 10.58 = 0.57

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# p_correct ≈ 4.0×10⁵ / (4.0×10⁵ + 96) ≈ 0.9998

# --- block 5 ---
logit_scale = exp(t)              # exp guarantees a positive multiplier
logits = logit_scale * S          # multiply, don't divide

# --- block 6 ---
logit_scale = clamp(exp(t), max=100)   # equivalently, temperature never drops below 0.01
