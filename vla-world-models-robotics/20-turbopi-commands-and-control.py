"""
Vision-Language-Action & World Models for Robotics
Chapter 20: TurboPi Commands and Control
Section: From Simulation to the TurboPi Car

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/turbopi-commands-and-control

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def action_to_pwm(action, v_max=0.5, w_max=2.0, L=0.08, kv=200.0):
    # 1. un-normalize the policy's [-1, 1] output into physical units
    v = action[0] * v_max          # forward velocity  (m/s)
    w = action[1] * w_max          # yaw rate          (rad/s)

    # 2. inverse kinematics: body command -> per-side wheel speed (m/s)
    w_left  = v - w * L
    w_right = v + w * L

    # 3. speed -> raw PWM duty, then clamp to the motor's range
    def to_duty(speed):
        duty = kv * speed          # kv maps m/s -> duty counts
        return max(-100, min(100, int(round(duty))))

    return to_duty(w_left), to_duty(w_right)
