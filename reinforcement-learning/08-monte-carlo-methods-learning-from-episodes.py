"""
Reinforcement Learning
Chapter 8: Monte Carlo Methods: Learning from Episodes
Section: The Three Pillars of Classical RL

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/monte-carlo-methods-learning-from-episodes

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# incremental mean update after observing return G for state s
N[s] += 1                       # one more visit counted
V[s] += (1 / N[s]) * (G - V[s]) # nudge V toward the new return
