"""
RLHF from Scratch
Chapter 16: The Policy Gradient Objective
Section: Policy Gradients and Advantage

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/the-policy-gradient-objective

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
# # three possible responses to one prompt, with reward-model returns
# R(A) = +5.0     # a great summary
# R(B) = +1.0     # a mediocre summary
# R(C) = -2.0     # an off-topic ramble

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# π_θ(A) = 0.2     # good answer, but under-produced
# π_θ(B) = 0.3
# π_θ(C) = 0.5     # bad answer, but the policy loves it

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# # after one small step of policy improvement
# π_θ(A) = 0.5     # up from 0.2
# π_θ(B) = 0.3     # unchanged
# π_θ(C) = 0.2     # down from 0.5
#
# J(θ) = 0.5·(+5.0) + 0.3·(+1.0) + 0.2·(-2.0)
#      = 2.5        + 0.3        + (-0.4)
#      = +2.4

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# θ ← θ + α · ∇_θ J(θ)     # α = learning rate; note the PLUS: we ASCEND
