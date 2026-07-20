"""
Vision-Language-Action & World Models for Robotics
Chapter 32: ACT Implementation in Isaac Lab
Section: Isaac Lab and Scalable Simulation

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/act-implementation-in-isaac-lab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import torch
import torch.nn.functional as F

# --- block 1 ---
def act_step(policy, obs, chunk_size):
    # obs from Isaac Lab: images (N, H, W, 3), state (N, state_dim)
    img = obs["camera"].permute(0, 3, 1, 2).float() / 255.0   # -> (N, 3, H, W)
    state = obs["state"]                                        # (N, state_dim)

    # z is the CVAE style latent. At INFERENCE we zero it (prior mean)
    # so the same obs always yields the same chunk. See below.
    z = torch.zeros(img.shape[0], policy.latent_dim, device=img.device)

    chunk = policy(img, state, z)      # (N, chunk_size, action_dim)
    return chunk

# --- block 2 ---
pred_chunk = policy(img, state, z_sampled)          # (B, k, action_dim)
recon = F.l1_loss(pred_chunk, target_chunk)         # imitate the demo
kl    = kl_divergence(mu, logvar).mean()            # keep z near N(0, I)
loss  = recon + beta * kl                           # beta is small (~10)
