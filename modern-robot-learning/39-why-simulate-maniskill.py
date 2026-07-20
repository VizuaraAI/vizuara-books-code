"""
Modern Robot Learning
Chapter 39: Why Simulate? The ManiSkill Environment
Section: Simulation and Policy Gradients

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/why-simulate-maniskill

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import gymnasium as gym
import mani_skill.envs  # registers ManiSkill tasks

env = gym.make("PickCube-v1", obs_mode="state", num_envs=1)

obs, info = env.reset(seed=0)          # start a fresh episode
for t in range(50):
    action = policy(obs)               # our policy chooses an action
    obs, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
        obs, info = env.reset()        # cube lifted, or ran out of time
