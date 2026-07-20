"""
Reinforcement Learning
Chapter 9: Temporal Difference Learning
Section: The Three Pillars of Classical RL

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/temporal-difference-learning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
V[s] = V[s] + alpha * (G_t - V[s])

# --- block 2 ---
V[s] = V[s] + alpha * (R + gamma * V[s_next] - V[s])
