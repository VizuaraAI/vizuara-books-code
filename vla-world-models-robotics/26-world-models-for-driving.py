"""
Vision-Language-Action & World Models for Robotics
Chapter 26: World Models for Driving
Section: World Models

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/world-models-for-driving

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# toy numbers — a reward model r(s) scoring each imagined latent
plans = {
    "brake":  [ +2, +3, +8 ],   # slows, stops safely short of the obstacle
    "hold":   [ +1, -4, -20 ],  # closes the gap, then a predicted collision
    "swerve": [ -1, +2, +3 ],   # leaves the lane, recovers, mildly costly
}
for name, rewards in plans.items():
    print(name, "total imagined return =", sum(rewards))
# brake  total imagined return = 13
# hold   total imagined return = -23
# swerve total imagined return = 4
