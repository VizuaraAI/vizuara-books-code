"""
Reinforcement Learning
Chapter 11: Project: Landing a Lunar Lander
Section: The Three Pillars of Classical RL

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/project-landing-a-lunar-lander

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def bin_index(value, low, high, n_bins=8):
    # clip to range, then map linearly to an integer bin 0 .. n_bins-1
    value = np.clip(value, low, high)
    frac = (value - low) / (high - low)
    return min(int(frac * n_bins), n_bins - 1)

# a state like y = 0.35, vy = -0.60 becomes a discrete key:
key = (bin_index(0.35, -0.5, 1.5),   # -> bin 2
       bin_index(-0.60, -2.0, 2.0))  # -> bin 2
# key = (2, 2)  ->  one row in the Q-table

# --- block 2 ---
G = 0.0
for (state, action, reward) in reversed(episode):   # walk backwards
    G = reward + gamma * G                           # accumulate the return
    N[state][action] += 1
    Q[state][action] += (1 / N[state][action]) * (G - Q[state][action])

# --- block 3 ---
state = discretize(env.reset(seed=0)[0])
for t in range(max_steps):
    action = epsilon_greedy(Q, state, epsilon)
    obs, reward, terminated, truncated, info = env.step(action)
    next_state = discretize(obs)
    target = reward if terminated else reward + gamma * np.max(Q[next_state])
    Q[state][action] += alpha * (target - Q[state][action])   # update EVERY step
    state = next_state
    if terminated or truncated:
        break
