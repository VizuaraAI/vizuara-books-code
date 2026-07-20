"""
Reinforcement Learning
Chapter 14: Experience Replay and Target Networks
Section: Deep Q-Networks

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/experience-replay-and-target-networks

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import random

# --- block 1 ---
Transition = (state, action, reward, next_state, done)
#              S       A       R       S'          terminal?

# --- block 2 ---
buffer.append((s, a, r, s_next, done))        # 1. remember this single step
batch = random.sample(buffer, 32)             # 2. learn from 32 random old steps

# --- block 3 ---
buffer.append((s, a, r, s_next, done))            # remember
batch = random.sample(buffer, 32)                 # decorrelate  (cure 1)
target = r + gamma * target_net(s_next).max(1)[0] * (1 - done)   # frozen label (cure 2)
loss   = (target - online_net(s).gather(1, a))**2               # regress
loss.mean().backward(); optimizer.step()          # update ONLINE net only
if step % 10_000 == 0:                            # sync the target
    target_net.load_state_dict(online_net.state_dict())
