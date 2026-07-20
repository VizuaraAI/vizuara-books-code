"""
Kernel Engineering
Chapter 52: FlashAttention I: tiling attention
Section: Kernels for Inference

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/flashattention-1

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
S = Q @ K.T              # (N, N)  every query dotted with every key
P = softmax(S, dim=-1)   # (N, N)  turn each row into a probability distribution
O = P @ V                # (N, d)  each output is a weighted average of values

# --- block 2 ---
m = max(x)                 # 1. the row's maximum
p = exp(x - m)             # 2. subtract max, then exponentiate
out = p / sum(p)           # 3. divide by the sum of exponentials

# --- block 3 ---
# One CTA (thread block) owns query block Q_i  (B_r x d), resident in SMEM/registers.
# m: (B_r,)   running max,  init -inf
# l: (B_r,)   running sum,  init 0
# O: (B_r, d) accumulator,  init 0
m = full(B_r, -inf); l = zeros(B_r); O = zeros(B_r, d)

for j in range(num_k_blocks):          # outer loop: stream over K/V blocks
    K_j = load(K, j)                   # (B_c, d) -> SMEM   (streamed in)
    V_j = load(V, j)                   # (B_c, d) -> SMEM

    S     = Q_i @ K_j.T                # (B_r, B_c)  scores — live in SMEM/regs, never HBM
    m_new = maximum(m, rowmax(S))      # (B_r,)      updated running max
    P     = exp(S - m_new[:, None])    # (B_r, B_c)  unnormalized weights
    alpha = exp(m - m_new)             # (B_r,)      the rescale factor from our by-hand example

    l = alpha * l + rowsum(P)          # rescale old sum,    then add this block
    O = alpha[:, None] * O + P @ V_j   # rescale old output, then add this block's P·V
    m = m_new

O = O / l[:, None]                     # ONE normalize, at the very end
store(O_i, O)                          # (B_r, d) -> HBM     (the only write!)
