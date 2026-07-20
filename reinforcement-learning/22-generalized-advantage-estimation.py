"""
Reinforcement Learning
Chapter 22: Generalized Advantage Estimation
Section: Policy Gradient Methods from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/generalized-advantage-estimation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def compute_gae(rewards, values, gamma=0.99, lam=0.95):
    # values has one extra entry: V(S_T) for the final/terminal state
    advantages = [0.0] * len(rewards)
    gae = 0.0
    for t in reversed(range(len(rewards))):
        delta = rewards[t] + gamma * values[t + 1] - values[t]
        gae = delta + gamma * lam * gae          # Â_t = δ_t + γλ·Â_{t+1}
        advantages[t] = gae
    return advantages
