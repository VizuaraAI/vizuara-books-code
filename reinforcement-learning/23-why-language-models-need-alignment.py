"""
Reinforcement Learning
Chapter 23: Why Language Models Need Alignment
Section: RLHF from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/why-language-models-need-alignment

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# r_chosen, r_rejected are scalar scores from the reward model r_phi(response)
# We want P(chosen beats rejected) to be high, so we minimize:
loss = -log(sigmoid(r_chosen - r_rejected))

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# # per-token: chase reward, but stay close to the frozen reference policy
# adjusted_reward = r_phi(response) - beta * kl(policy || reference)
