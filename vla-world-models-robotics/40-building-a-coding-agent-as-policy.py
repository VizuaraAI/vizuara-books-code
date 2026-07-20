"""
Vision-Language-Action & World Models for Robotics
Chapter 40: Building a Coding-Agent-as-Policy
Section: Code as Policy and Capstone

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/building-a-coding-agent-as-policy

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# # The skill API handed to the LLM (perception returns values, actions command the car)
# class RobotAPI:
#     # --- perception (read the world) ---
#     def detect_objects(self) -> list[dict]: ...   # [{"label":"cone","x":0.4,"dist":1.2}, ...]
#     def lane_center_offset(self) -> float: ...     # metres; +right of centre, -left
#     def heading_error(self) -> float: ...          # radians; angle to the lane direction
#     def obstacle_ahead(self, within: float) -> bool: ...
#
#     # --- action (command the car) ---
#     def set_speed(self, v: float) -> None: ...     # m/s, clamped to [0, V_MAX]
#     def set_steering(self, angle: float) -> None:  # radians, clamped to [-A_MAX, A_MAX]
#     def stop(self) -> None: ...

# --- block 2 ---
def policy(robot):
    while True:
        if robot.obstacle_ahead(within=1.0):
            robot.stop()
            return
        offset = robot.lane_center_offset()
        robot.set_steering(-0.8 * offset)   # steer back toward centre
        robot.set_speed(0.6)
