"""
Vision-Language-Action & World Models for Robotics
Chapter 42: Capstone: Your Own Self-Driving Car
Section: Code as Policy and Capstone

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/capstone-your-own-self-driving-car

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# run_car.py — the single documented entry point for the capstone
import torch
from act_policy import ACTPolicy          # our CVAE decoder
from turbopi import Camera, Motors         # the command layer
from telemetry import Logger

policy = ACTPolicy.load("checkpoint.pt")   # pinned weights
policy.eval()                              # z -> prior mean, deterministic
cam, motors, log = Camera(), Motors(), Logger("run.jsonl")

with torch.no_grad():
    while True:
        frame = cam.read()                 # (3, H, W) tensor
        chunk = policy(frame)              # action chunk, k = 100
        action = chunk[0]                  # temporal ensemble handles the rest
        motors.apply(action)               # map to PWM and drive
        log.step(frame_id=cam.i, action=action, latency=cam.dt)
