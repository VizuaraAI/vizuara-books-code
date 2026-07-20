"""
Vision-Language-Action & World Models for Robotics
Chapter 22: Deploying ACT on TurboPi
Section: From Simulation to the TurboPi Car

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/deploying-act-on-turbopi

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# what ACT gives us, conceptually
action_chunk = policy(image, qpos)   # image: (3,480,640), qpos: robot state
# action_chunk has shape (k, action_dim), e.g. (100, 2)

# --- block 2 ---
CHUNK = 100          # k actions per inference
HZ = 30              # control frequency
chunk = None
i = CHUNK            # force an inference on the first step

while driving:
    if i >= CHUNK:               # chunk exhausted → think again
        frame = camera.read()
        obs = preprocess(frame)  # SAME transform as training
        chunk = policy(obs, qpos())  # ~200 ms, once per ~3.3 s
        i = 0
    speed, turn = chunk[i]       # replay: cheap, no network
    set_motors(speed, turn)
    i += 1
    sleep(1 / HZ)

# --- block 3 ---
def set_motors(speed, turn):
    left  = speed - turn      # turn left  → left wheel slower
    right = speed + turn
    board.set_motor(LEFT_ID,  clamp(left  * MAX_PWM, -100, 100))
    board.set_motor(RIGHT_ID, clamp(right * MAX_PWM, -100, 100))
