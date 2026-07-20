"""
Modern Robot Learning
Chapter 37: Evaluating Beyond Success Rate
Section: Training on Real Robots

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/evaluating-beyond-success-rate

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np

def path_length(traj):
    # traj: (T, n_joints) array of joint angles, one row per timestep
    steps = np.diff(traj, axis=0)          # (T-1, n_joints): per-step change
    return np.linalg.norm(steps, axis=1).sum()   # sum of step magnitudes

# --- block 2 ---
def mean_abs_jerk(traj, dt):
    vel  = np.diff(traj, axis=0) / dt      # velocity
    acc  = np.diff(vel,  axis=0) / dt      # acceleration
    jerk = np.diff(acc,  axis=0) / dt      # jerk (3rd derivative)
    return np.abs(jerk).mean()             # one scalar for the whole rollout
