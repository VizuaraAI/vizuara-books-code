"""
Reinforcement Learning
Chapter 5: OpenAI Gymnasium: Your First Environment
Section: Foundations of Reinforcement Learning

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/openai-gymnasium-your-first-environment

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
observation, reward, terminated, truncated, info = env.step(action)

# --- block 2 ---
import gymnasium as gym

env = gym.make("CartPole-v1")        # build the environment
observation, info = env.reset(seed=42)   # S_0, plus an info dict

action = env.action_space.sample()   # a random legal action: 0 or 1
observation, reward, terminated, truncated, info = env.step(action)

print(observation)   # e.g. [ 0.027  0.191  0.041 -0.288 ]  -> the new S_1
print(reward)        # 1.0
print(terminated)    # False
print(truncated)     # False

# --- block 3 ---
import gymnasium as gym

env = gym.make("CartPole-v1")
observation, info = env.reset(seed=0)

total_reward = 0.0
for t in range(500):                         # CartPole caps at 500 steps
    action = env.action_space.sample()       # <- a real agent decides here
    observation, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    if terminated or truncated:
        break

print("episode length / return:", total_reward)
env.close()
