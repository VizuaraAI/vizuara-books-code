"""
Modern Robot Learning
Chapter 28: Action Chunking Explained
Section: The ACT Policy

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/action-chunking-explained

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# single-step (naive behavioral cloning): 400 queries over the task
for t in range(400):
    obs    = robot.observe()          # look every single step
    action = policy(obs)              # predict ONE action, shape (7,)
    robot.execute(action)             # ... then look again  → 400 re-decisions

# action chunking: ~4 queries over the same task
k = 100
t = 0
while t < 400:
    obs   = robot.observe()           # look ONCE per chunk
    chunk = policy(obs)               # predict k actions, shape (k, 7)
    for a in chunk:                   # execute the whole plan open-loop
        robot.execute(a)
        t += 1                        # ... only 4 re-decisions total
