"""
Vision-Language-Action & World Models for Robotics
Chapter 33: The Isaac Lab Training Pipeline
Section: Isaac Lab and Scalable Simulation

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/isaac-lab-training-pipeline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch

# --- block 1 ---
# one fused collect-and-train iteration, everything on-GPU
obs = env.reset()                      # (N, obs_dim), N worlds at once
for it in range(num_iters):
    with torch.no_grad():
        actions = expert_controller(obs)   # (N, action_dim): demo actions
    next_obs, _, done, _ = env.step(actions)   # step all N worlds together

    buffer.add(obs, actions)               # push the whole fleet's step
    obs = env.reset(done) if done.any() else next_obs

    if buffer.ready():                     # once we have enough chunks
        batch = buffer.sample_chunks(k)    # (B, k, action_dim) action chunks
        loss = act.loss(batch)             # L1 + β·KL, exactly as before
        loss.backward(); opt.step(); opt.zero_grad()
