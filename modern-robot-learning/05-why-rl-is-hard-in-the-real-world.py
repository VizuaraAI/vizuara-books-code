"""
Modern Robot Learning
Chapter 5: Why RL Is Hard in the Real World
Section: Foundations of Robot Learning

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/why-rl-is-hard-in-the-real-world

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def reward(state):
    return 1.0 if cube_is_grasped(state) else 0.0

# --- block 2 ---
def shaped_reward(state):
    r  = -distance(gripper, cube)        # get closer → less negative
    r += 0.5 if in_contact(state) else 0 # touching is progress
    r += lift_height(cube)               # lifting is more progress
    return r
