"""
Vision-Language-Action & World Models for Robotics
Chapter 35: Reward Shaping for Autonomous Control
Section: Reinforcement Learning for Self-Driving

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/reward-shaping-for-autonomous-control

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
r_t = ( w_speed   * forward_speed
      - w_center  * dist_from_lane_center
      - w_heading * abs(heading_error)
      - w_jerk    * abs(steer_t - steer_prev)
      - w_crash   * crashed )
