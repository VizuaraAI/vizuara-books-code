"""
Reinforcement Learning
Chapter 37: Putting It All Together
Section: From Learner to Researcher

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/putting-it-all-together

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# DQN target uses the frozen network θ⁻ for the bootstrap
target = R + gamma * Q_target(S_next).max(dim=1).values   # γ max_a' Q(S',a'; θ⁻)
loss   = ((target - Q_online(S).gather(1, A)) ** 2).mean()
