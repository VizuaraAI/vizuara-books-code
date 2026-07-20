"""
Reinforcement Learning
Chapter 10: Q-Learning and SARSA
Section: The Three Pillars of Classical RL

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/q-learning-and-sarsa

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
Q[s, a] = Q[s, a] + alpha * (R + gamma * max(Q[s_next]) - Q[s, a])

# --- block 2 ---
if random() < epsilon:
    a = random_action()        # explore: 10% of the time
else:
    a = argmax(Q[s])           # exploit: 90% of the time
