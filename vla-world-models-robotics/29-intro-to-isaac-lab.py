"""
Vision-Language-Action & World Models for Robotics
Chapter 29: Introduction to Isaac Lab
Section: Isaac Lab and Scalable Simulation

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/intro-to-isaac-lab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# classic single-env loop — one thing at a time
obs = env.reset()                 # shape (obs_dim,)
for step in range(N):
    action = policy(obs)          # shape (action_dim,)
    obs, reward, done = env.step(action)

# Isaac Lab — a whole batch every step, on the GPU
obs = env.reset()                 # shape (num_envs, obs_dim)  e.g. (2048, obs_dim)
for step in range(N):
    action = policy(obs)          # shape (num_envs, action_dim)
    obs, reward, done = env.step(action)   # reward: (num_envs,), done: (num_envs,)
