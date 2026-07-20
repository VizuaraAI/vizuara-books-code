"""
RLHF from Scratch
Chapter 9: Generation as a Trajectory
Section: The LLM as an RL Agent

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/generation-as-a-trajectory

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
# # probability the policy assigned to each token it actually chose
# p(" time"  | "Once upon a")              = 0.62
# p(" there" | "Once upon a time")         = 0.30
# p(" was"   | "Once upon a time there")   = 0.71

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# r_0 = 0        # reward after " time"
# r_1 = 0        # reward after " there"
# r_2 = 0        # reward after " was"
# r_T = 2.4      # reward model scores the COMPLETED story: +2.4 (nicely positive)
#
# R(τ) = 0 + 0 + 0 + ... + 2.4 = 2.4
