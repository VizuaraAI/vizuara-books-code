"""
Vision-Language-Action & World Models for Robotics
Chapter 36: Training a Driving Policy with RL
Section: Reinforcement Learning for Self-Driving

Read this chapter: https://books.vizuara.ai/read/vla-world-models-robotics/training-a-driving-policy-with-rl

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# The policy-gradient estimator, for one trajectory:
#   grad J(θ) = sum_t [ G_t * grad_theta log pi_theta(a_t | s_t) ]
#
#   G_t   = return that FOLLOWED action a_t  (how the drive turned out)
#   log pi = log-probability the policy assigned to the action it took

# --- block 2 ---
for iteration in range(NUM_ITERS):
    # 1. COLLECT: run the current policy in the sim, recording everything.
    states, actions, logps, rewards = rollout(policy, envs, horizon=T)

    # 2. EVALUATE: turn rewards into returns, then advantages via the critic.
    returns    = discounted_returns(rewards, gamma=0.99)   # G_t per step
    values     = critic(states)                            # V(s_t) baseline
    advantages = returns - values.detach()                 # A_t = G_t - V(s_t)
    advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

    # 3. UPDATE: one gradient step on actor + critic.
    policy_loss = -(logps * advantages).mean()             # REINFORCE-with-baseline
    value_loss  = ((values - returns) ** 2).mean()         # critic regresses to G_t
    loss = policy_loss + 0.5 * value_loss
    optimizer.zero_grad(); loss.backward(); optimizer.step()
