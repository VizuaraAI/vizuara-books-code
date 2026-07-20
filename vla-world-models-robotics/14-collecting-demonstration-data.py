"""
Vision-Language-Action & World Models for Robotics
Chapter 14: Collecting Demonstration Data
Section: Building the Action Chunking Transformer

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/collecting-demonstration-data

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
trajectory = []                       # will hold (obs, action) pairs, in order
obs = env.reset()                     # start a fresh episode

while not done:
    action = expert(obs)              # human teleop OR scripted controller
    trajectory.append({
        "image":  obs["camera"],      # (3, H, W) uint8 RGB frame
        "state":  obs["state"],       # proprioception, e.g. [v_x, v_y, heading]
        "action": action,             # e.g. [forward_speed, turn_rate]
    })
    obs, done = env.step(action)      # apply the action, advance the sim

save_episode(trajectory)              # one file per episode, time order intact
