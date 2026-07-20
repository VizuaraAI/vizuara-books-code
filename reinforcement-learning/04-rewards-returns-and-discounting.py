"""
Reinforcement Learning
Chapter 4: Rewards, Returns and Discounting
Section: Foundations of Reinforcement Learning

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/rewards-returns-and-discounting

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def discounted_return(rewards, gamma):
    # rewards = [R_{t+1}, R_{t+2}, ...] from time t onward
    G = 0.0
    for k, r in enumerate(rewards):
        G += (gamma ** k) * r          # direct definition: Σ γ^k R_{t+k+1}
    return G

def return_recursive(rewards, gamma):
    G = 0.0
    for r in reversed(rewards):        # walk backwards
        G = r + gamma * G              # G_t = R_{t+1} + γ · G_{t+1}
    return G

rewards = [-0.3, -0.3, -0.3, 100.0]
print(discounted_return(rewards, 1.0))   # 99.1
print(return_recursive(rewards, 1.0))    # 99.1  — same number, computed backwards
