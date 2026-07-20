"""
Reinforcement Learning
Chapter 1: What Is Reinforcement Learning?
Section: Foundations of Reinforcement Learning

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/what-is-reinforcement-learning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import random

def epsilon_greedy(Q, epsilon=0.1):
    # Q: dict of action -> estimated value, e.g. {"A": 0.75, "B": 0.50}
    if random.random() < epsilon:
        return random.choice(list(Q))        # explore: try a random arm
    return max(Q, key=Q.get)                 # exploit: take the current best
