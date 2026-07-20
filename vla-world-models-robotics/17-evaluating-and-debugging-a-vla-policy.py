"""
Vision-Language-Action & World Models for Robotics
Chapter 17: Evaluating and Debugging a VLA Policy
Section: Building the Action Chunking Transformer

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/evaluating-and-debugging-a-vla-policy

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Open-loop sanity check: does the policy reproduce a demo it was trained on?
# No simulator, no car — the cheapest, most decisive test you can run.
import numpy as np

policy.eval()
errors = []
for img, state, expert_action in logged_demo:          # one held-out trajectory
    img_n   = normalize(img)                            # MUST match training exactly
    pred    = policy(img_n, state)                      # predicted action chunk
    a_hat   = unnormalize(pred[0])                      # first action, back to real units
    errors.append(np.abs(a_hat - expert_action).mean())

errors = np.array(errors)
print(f"open-loop MAE      : {errors.mean():.3f}")
print(f"error trend (slope): {np.polyfit(np.arange(len(errors)), errors, 1)[0]:+.4f}")
# tiny + flat  -> model & data are fine; hunt the loop / compounding error
# large        -> the model never learned this demo; fix data or training
# small + rising slope -> the seed of compounding error; shorten the chunk horizon
