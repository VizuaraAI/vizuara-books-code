"""
Reinforcement Learning
Chapter 20: REINFORCE with a Baseline
Section: Policy Gradient Methods from Scratch

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/reinforce-with-a-baseline

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# One episode of REINFORCE with a learned value baseline
states, actions, returns = rollout(policy)          # run π_θ, compute G_t for each step

for s_t, a_t, G_t in zip(states, actions, returns):
    baseline = value_net(s_t)                        # V_w(s_t): "par" for this state
    advantage = G_t - baseline.detach()              # detach: baseline is a CONSTANT to the policy

    # (1) Policy update: gradient ASCENT, weighted by advantage
    policy_loss = -log_prob(policy, s_t, a_t) * advantage

    # (2) Value update: regression, pull V_w(s_t) toward the observed return
    value_loss  = (baseline - G_t) ** 2

    (policy_loss + value_loss).backward()
    optimizer.step()
