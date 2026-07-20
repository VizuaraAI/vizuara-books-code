"""
Vision-Language-Action & World Models for Robotics
Chapter 31: Massively Parallel Simulation
Section: Isaac Lab and Scalable Simulation

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/massively-parallel-simulation

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from isaaclab.envs import ManagerBasedRLEnv

# one scene definition, N copies laid out as a batched tensor on the GPU
env = ManagerBasedRLEnv(cfg=turbopi_cfg, num_envs=4096, device="cuda")

obs = env.reset()                      # obs shape: (4096, obs_dim), all on GPU
for _ in range(1000):
    actions = policy(obs["policy"])    # (4096, act_dim) — one forward pass, whole batch
    obs, reward, done, info = env.step(actions)   # steps ALL 4096 cars at once
    # reward: (4096,)   done: (4096,) bool
