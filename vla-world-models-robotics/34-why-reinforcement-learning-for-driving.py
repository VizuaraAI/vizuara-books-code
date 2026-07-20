"""
Vision-Language-Action & World Models for Robotics
Chapter 34: Why Reinforcement Learning for Driving?
Section: Reinforcement Learning for Self-Driving

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/why-reinforcement-learning-for-driving

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Return of a trajectory: discounted sum of future rewards.
# gamma in [0,1) trades off immediate vs. long-term reward.
def return_of(rewards, gamma=0.99):
    G, total = 0.0, 0.0
    for t, r in enumerate(rewards):
        total += (gamma ** t) * r
    return total

# The RL objective: find policy pi that MAXIMIZES E[ return ]
#   over trajectories the policy itself generates.

# --- block 2 ---
def lane_reward(d, v, off_road):
    if off_road:
        return -10.0          # big penalty, ends the episode
    return v - 2.0 * abs(d)   # go fast, but pay for being off-center
