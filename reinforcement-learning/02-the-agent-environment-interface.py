"""
Reinforcement Learning
Chapter 2: The Agent-Environment Interface
Section: Foundations of Reinforcement Learning

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/the-agent-environment-interface

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def step(state, action):
    # state: an int in {1,2,3,4}; action: "LEFT" or "RIGHT"
    if action == "RIGHT":
        next_state = min(state + 1, 4)
    else:  # "LEFT"
        next_state = max(state - 1, 1)

    if next_state == 4:
        reward, done = +10, True      # reached the goal, episode ends
    else:
        reward, done = -1, False      # every other step costs 1
    return next_state, reward, done
