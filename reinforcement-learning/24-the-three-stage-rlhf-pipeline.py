"""
Reinforcement Learning
Chapter 24: The Three-Stage RLHF Pipeline
Section: RLHF from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/the-three-stage-rlhf-pipeline

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
# # SFT is just next-token prediction on curated (prompt, response) pairs.
# # Typically we mask the prompt tokens and only compute loss on the response y.
# loss = -sum( log p_theta(y_t | x, y_1..y_{t-1}) for t in range(T) )

# --- block 2 ---
# r_phi outputs one scalar per (prompt, response).
# Push the chosen score above the rejected score. Nothing else.
loss = -log( sigmoid( r_phi(prompt, chosen) - r_phi(prompt, rejected) ) )

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# # per token: earn reward, but pay beta for every step away from the reference
# adjusted_reward = r_phi(prompt, response) - beta * kl( policy || reference )
