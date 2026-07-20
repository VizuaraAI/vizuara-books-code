"""
Reinforcement Learning
Chapter 13: From Q-Tables to Q-Networks
Section: Deep Q-Networks

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/from-q-tables-to-q-networks

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
Q[s, a] = Q[s, a] + alpha * (r + gamma * max(Q[s_next]) - Q[s, a])
