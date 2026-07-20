"""
Kernel Engineering
Chapter 70: Monkeys & search: test-time scaling
Section: AI × Kernels

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/test-time-scaling-and-search

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
archive = []                          # every correct kernel we have ever found
seeds   = [pytorch_reference]         # round 0 starts from the reference itself

for round in range(NUM_ROUNDS):
    children = []
    for seed in top_k(seeds, K):                      # branch from the current best
        ideas = model.propose_ideas(seed, profile_of(seed))   # STEP 1: NL, diverse
        for idea in ideas:                            # fan out: one idea -> many impls
            for _ in range(SAMPLES_PER_IDEA):
                kernel = model.write_code(seed, idea) # STEP 2: idea -> code
                if not compiles(kernel):            continue   # gate 1
                if not correct(kernel, tol=1e-2):   continue   # gate 2
                kernel.speed = benchmark(kernel)               # fitness
                children.append(kernel)
                archive.append(kernel)                # remember EVERYTHING that worked
    seeds = children                  # survivors seed the next round

best = max(archive, key=lambda k: k.speed)
