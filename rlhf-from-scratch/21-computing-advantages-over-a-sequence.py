"""
RLHF from Scratch
Chapter 21: Computing Advantages Over a Sequence
Section: Policy Gradients and Advantage

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/computing-advantages-over-a-sequence

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def compute_gae(rewards, values, gamma=1.0, lam=0.95):
    # rewards[t], values[t] for t = 0..T-1 ; append 0 for the terminal bootstrap
    T = len(rewards)
    values = values + [0.0]          # V(s_T) = 0  (the terminal bootstrap)
    advantages = [0.0] * T
    gae = 0.0                        # running accumulator, starts at 0
    for t in reversed(range(T)):     # BACKWARD: last token first
        delta = rewards[t] + gamma * values[t + 1] - values[t]
        gae = delta + gamma * lam * gae
        advantages[t] = gae
    return advantages
