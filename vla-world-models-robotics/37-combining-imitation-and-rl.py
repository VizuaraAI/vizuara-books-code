"""
Vision-Language-Action & World Models for Robotics
Chapter 37: Combining Imitation and RL
Section: Reinforcement Learning for Self-Driving

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/combining-imitation-and-rl

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Stage 1 — imitation pre-training (supervised, on demonstrations)
policy = ACTPolicy()
for images, expert_action_chunk in demo_loader:      # human demos
    pred_chunk = policy(images)
    loss = reconstruction_loss(pred_chunk, expert_action_chunk)
    loss.backward(); opt.step()                       # copy the human

# Stage 2 — RL fine-tuning (same weights, now driven by reward)
for episode in range(N):
    traj = rollout(policy, env)                        # policy drives itself
    rewards = [reward_fn(s, a) for s, a in traj]       # shaped reward
    advantages = compute_advantages(rewards, values)   # PPO-style
    loss = ppo_objective(policy, traj, advantages)     # push past the ceiling
    loss.backward(); opt.step()
