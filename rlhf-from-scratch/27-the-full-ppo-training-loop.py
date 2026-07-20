"""
RLHF from Scratch
Chapter 27: The Full PPO Training Loop
Section: Proximal Policy Optimization

Read this chapter: https://books.vizuara.ai/read/rlhf-from-scratch/the-full-ppo-training-loop

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
# per minibatch, inside the K inner epochs
ratio = torch.exp(new_logp - old_logp)                 # π_θ / π_old, per token
unclipped = ratio * advantages
clipped   = torch.clamp(ratio, 1 - eps, 1 + eps) * advantages
policy_loss = -torch.min(unclipped, clipped).mean()    # maximize L^CLIP → minimize its negative

returns = advantages + values                          # target for the critic
value_loss  = F.mse_loss(new_values, returns)          # regression: fit V toward returns

entropy_bonus = -new_dist.entropy().mean()             # encourage exploration (small)

loss = policy_loss + c1 * value_loss + c2 * entropy_bonus
loss.backward()                                        # ONE backward pass updates actor + critic

# --- block 2 ---
policy, value = make_actor_critic()          # trainable
reward_model, ref_model = frozen_reward(), frozen_ref()   # frozen anchors

for iteration in range(N_ITERATIONS):
    # ---- PHASE 1: rollout (no gradients) ----
    prompts = sample_prompts(batch_size)
    answers, old_logp = policy.generate(prompts)          # cache old log-probs
    ref_logp  = ref_model.logprobs(prompts, answers)
    values    = value(prompts, answers)                   # V(s_t) per token
    scores    = reward_model(prompts, answers)            # one scalar per answer

    rewards    = shape_reward(scores, old_logp, ref_logp, beta)  # KL-shaped, per token
    advantages = compute_gae(rewards, values, gamma, lam)        # backward sweep
    advantages = normalize(advantages)                          # batch mean/std

    # ---- PHASE 2: optimize (gradients, reuse the batch) ----
    for epoch in range(K_EPOCHS):
        for mb in minibatches(answers, old_logp, advantages, values):
            new_logp, new_values, ent = policy_value_forward(mb)
            loss = ppo_loss(new_logp, mb.old_logp, mb.adv,
                            new_values, mb.adv + mb.values, ent)
            loss.backward(); optimizer.step(); optimizer.zero_grad()
    # snapshot: the updated policy becomes π_old for the next iteration
