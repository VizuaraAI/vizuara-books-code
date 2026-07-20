"""
Vision-Language-Action & World Models for Robotics
Chapter 38: Code as Policy: The Idea
Section: Code as Policy and Capstone

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/code-as-policy-idea

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# The skill API we hand to the LLM (these are already implemented and tested)
def detect(name: str) -> list[Object]:   ...  # perception: returns detected objects
def dist(a: Object, b: Object) -> float: ...  # geometry helper
def is_left_of(obj: Object) -> bool:     ...  # is this object on the car's left?
def drive_to(obj: Object) -> None:       ...  # low-level controller → wheels

# --- block 2 ---
box  = detect("blue box")[0]
cones = detect("cone")
cones.sort(key=lambda c: dist(c, box))   # nearest first
second = cones[1]                         # second-closest
if is_left_of(second):
    drive_to(second)
