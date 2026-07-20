"""
Build a Diffusion Language Model from Scratch
Chapter 26: The Coherence vs Speed Tradeoff
Section: Inference and Unmasking Strategies

Read this chapter: https://books.vizuara.ai/read/diffusion-lm-from-scratch/coherence-speed-tradeoff

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Sweep step counts and watch quality flatten out.
step_grid = [2, 4, 8, 16, 32, 64]      # few steps (fast) → many steps (slow)
N = 64                                  # target sequence length

for S in step_grid:
    samples = [generate(prompt, num_steps=S) for prompt in eval_prompts]
    ppl = mean_perplexity(samples, scorer)          # local fluency (lower better)
    lat = S                                          # sequential passes ≈ latency
    print(f"steps={S:>3}  k≈{N//S:>2}  perplexity={ppl:6.1f}  passes={lat}")
