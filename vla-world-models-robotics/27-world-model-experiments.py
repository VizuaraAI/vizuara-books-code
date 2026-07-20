"""
Vision-Language-Action & World Models for Robotics
Chapter 27: World Model Experiments
Section: World Models

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/world-model-experiments

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def imagine(model, context_obs, future_actions):
    # 1. Encode the real context frames into a latent state.
    z, h = model.reset()
    for obs, act in context_obs:            # warm-up on REAL observations
        z = model.encode(obs)
        z, h = model.step(z, act, h)         # advance the dynamics

    # 2. Now imagine: no more real frames, feed predictions back in.
    imagined = []
    for act in future_actions:               # actions only from here on
        z, h = model.step(z, act, h)         # ẑ_{t+1} from the model's OWN ẑ_t
        imagined.append(model.decode(z))     # decode only for evaluation
    return imagined
