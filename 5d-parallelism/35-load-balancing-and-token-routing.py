"""
5D Parallelism for Large Model Training
Chapter 35: Load Balancing and Token Routing
Section: Expert Parallelism and MoE

Read this chapter: https://books.vizuara.ai/read/5d-parallelism/load-balancing-and-token-routing

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
capacity = capacity_factor * (num_tokens / num_experts)

# --- block 2 ---
aux_loss = alpha * E * sum(f[i] * P[i] for i in range(E))
