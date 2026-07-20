"""
Vision-Language-Action & World Models for Robotics
Chapter 10: The VLA 3D Simulator Platform
Section: Introduction to Vision-Language-Action

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/the-vla-3d-simulator

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
obs = env.reset()                 # obs = (image (3,84,84), state (4,))
done = False
while not done:
    action = my_policy(obs)       # -> [steer, throttle], each in [-1, 1]
    obs, reward, done = env.step(action)   # world advances one tick
    env.render()                  # draw it so a human can watch
