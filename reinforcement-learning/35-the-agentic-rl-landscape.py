"""
Reinforcement Learning
Chapter 35: The Agentic RL Landscape
Section: Agentic Reinforcement Learning

Read this chapter: https://books.vizuara.ai/read/reinforcement-learning/the-agentic-rl-landscape

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
for question in dataset:                    # layer 3: the application
    group = []
    for _ in range(GROUP_SIZE):             # sample a group for GRPO's baseline
        traj, mask = [], []
        state = env.reset(question)         # layer 2: environment
        while not state.done:
            action = policy.generate(state) # model tokens  → mask = 1
            obs = env.step(action)          # tool output   → mask = 0
            traj += action + obs
            mask += [1]*len(action) + [0]*len(obs)
        reward = env.score(traj)            # e.g. exact-match: 1 or 0
        group.append((traj, mask, reward))
    advantages = group_relative(group)      # Â_i = (r_i − mean(r)) / std(r)
    grpo_update(policy, group, advantages)  # layer 1: the RL trainer
