"""
Vision-Language-Action & World Models for Robotics
Chapter 23: Closing the Loop: The First Autonomous Drive
Section: From Simulation to the TurboPi Car

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/closing-the-loop-first-drive

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import time

# --- block 1 ---
CHUNK, HZ = 100, 30
chunk, i = None, CHUNK          # force inference on step 0
t0 = time.time()

while driving:
    if i >= CHUNK:                       # chunk exhausted → think
        frame = camera.read()
        obs   = preprocess(frame)        # SAME transform as training
        t = time.time()
        chunk = policy(obs, qpos())      # ~200 ms, once per ~3.3 s
        infer_ms = (time.time() - t) * 1000
        i = 0
        log(f"{time.time()-t0:6.2f}s  INFER {infer_ms:5.1f}ms")
    speed, turn = chunk[i]
    set_motors(speed, turn)
    log(f"{time.time()-t0:6.2f}s  act[{i:3d}] speed={speed:+.2f} turn={turn:+.2f}")
    i += 1
    time.sleep(1 / HZ)
