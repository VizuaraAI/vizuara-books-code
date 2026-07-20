"""
Vision-Language-Action & World Models for Robotics
Chapter 1: Why Vision Alone Is Not Enough
Section: Foundations: Perception, Language, Action

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/why-vision-alone-is-not-enough

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# What a detector gives you: pixels -> labels
def perceive(frame):
    return {"obstacle": 1, "green_light": 1}   # facts, not a plan

# What driving actually needs: situation -> action
def decide(facts):
    if facts["obstacle"]:
        return "SLOW" if facts["green_light"] else "STOP"
    return "GO" if facts["green_light"] else "STOP"
