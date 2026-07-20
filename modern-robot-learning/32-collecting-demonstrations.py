"""
Modern Robot Learning
Chapter 32: Collecting Demonstrations
Section: Training on Real Robots

Read this chapter: https://books.vizuara.ai/read/modern-robot-learning/collecting-demonstrations

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Conceptually, LeRobot's record loop runs at a fixed rate (fps):
while recording_episode:
    obs = {
        "observation.images.top":   top_camera.read(),    # H x W x 3
        "observation.images.wrist": wrist_camera.read(),   # H x W x 3
        "observation.state":        follower.read_joints() # (6,) angles
    }
    action = leader.read_joints()          # (6,) the human's command = the label
    follower.set_joints(action)            # follower mirrors the leader
    dataset.add_frame(obs, action)         # write the (x, y) pair
    wait_until_next_tick(fps)              # hold the loop at, e.g., 50 Hz
