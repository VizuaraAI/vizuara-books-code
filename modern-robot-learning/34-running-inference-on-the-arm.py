"""
Modern Robot Learning
Chapter 34: Running Inference on the Arm
Section: Training on Real Robots

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/running-inference-on-the-arm

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from lerobot.common.policies.act.modeling_act import ACTPolicy

# pulls weights + config + normalization stats from the Hub, builds the net
policy = ACTPolicy.from_pretrained("your-username/act_so101_pickplace")
policy.eval()          # inference mode: no dropout, no grad tracking
policy.to("cuda")      # or "cpu" — latency matters, see below

# --- block 2 ---
observation = {
    "observation.images.wrist": image_tensor,   # shape (1, 3, 480, 640), float, 0–1
    "observation.state":        joint_state,     # shape (1, 6): the current joint angles
}
action = policy.select_action(observation)       # shape (1, 6): the next command

# --- block 3 ---
import time

FPS = 30                          # target control frequency (Hz)
period = 1.0 / FPS                # 0.0333 s per tick

robot.connect()
for step in range(30 * FPS):      # run for ~30 seconds
    t0 = time.perf_counter()

    obs    = robot.get_observation()          # image + joint state from the arm
    action = policy.select_action(obs)        # the full ACT forward pass
    robot.send_action(action)                 # command the motors

    dt = time.perf_counter() - t0
    time.sleep(max(0.0, period - dt))         # hold the rhythm; don't run early
robot.disconnect()
