"""
Kernel Engineering
Chapter 53: FlashAttention II: better work partitioning
Section: Kernels for Inference

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/flashattention-2

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# FA1 inner loop (conceptual): re-normalise the accumulator EVERY block
for j in key_blocks:
    S = Q @ K[j].T                     # tensor cores (fast)
    m_new = max(m, rowmax(S))          # slow
    P = exp(S - m_new)                 # slow
    correction = exp(m - m_new)        # slow
    l_new = correction * l + rowsum(P) # slow
    O = (correction * (l / l_new)) * O + (1 / l_new) * (P @ V[j])  # <-- /l EVERY j
    l, m = l_new, m_new

# FA2: keep O un-normalised; only the max-correction stays in the loop; divide ONCE
for j in key_blocks:
    S = Q @ K[j].T
    m_new = max(m, rowmax(S))
    P = exp(S - m_new)
    correction = exp(m - m_new)
    l = correction * l + rowsum(P)     # track the sum, don't divide by it yet
    O = correction * O + P @ V[j]      # only the max-rescale — no /l here
    m = m_new
O = O / l                              # the ONLY normalisation, once per output block

# --- block 2 ---
for i in query_blocks:                 # PARALLEL across SMs (change 2)
    for j in key_blocks:               # serial, keeps softmax state in registers
        if j * B_kv > (i + 1) * B_q:   # this key block is entirely above the diagonal
            continue                    # skip: all-masked, do zero work
        S = Q[i] @ K[j].T
        if on_diagonal(i, j):
            S = apply_causal_mask(S)    # only the diagonal block pays for masking
        # ... online softmax, un-normalised accumulate (change 1) ...
