"""
RLHF from Scratch
Chapter 19: Value Functions and the Advantage
Section: Policy Gradients and Advantage

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/value-functions-and-the-advantage

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# per-token policy-gradient term with an advantage weight
loss_t = -(advantage[t] * log_prob[t])   # minimize this == ascend the reward
