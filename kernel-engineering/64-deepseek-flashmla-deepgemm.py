"""
Kernel Engineering
Chapter 64: DeepSeek's open kernels: FlashMLA & DeepGEMM
Section: The Frontier

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/deepseek-flashmla-deepgemm

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# FlashMLA decode, one query token, streaming over KV pages
acc = 0            # output accumulator, per head
denom = 0          # running softmax denominator
m = -inf           # running max, for numerically-stable softmax
for page in kv_pages(seq):          # scattered physical pages
    latent = load(page)             # low-rank cached vector (small!)
    K, V = up_project(latent)       # reconstruct per-head K, V on-chip
    s = q @ K.T * scale             # attention logits
    m_new = max(m, rowmax(s))       # online softmax rescale
    p = exp(s - m_new)
    acc = acc * exp(m - m_new) + p @ V
    denom = denom * exp(m - m_new) + rowsum(p)
    m = m_new
out = acc / denom

# --- block 2 ---
# grouped MoE GEMM — one launch for all active experts
# tokens are sorted by expert; group_offsets marks each expert's slice
deep_gemm.grouped_gemm_fp8(
    lhs        = tokens_fp8,       # [num_tokens, hidden], block-scaled
    rhs        = expert_w_fp8,     # [num_experts, hidden, inter], FP8/FP4
    out        = y,               # [num_tokens, inter], FP32 accumulate
    group_offs = group_offsets,   # per-expert row ranges (masked layout)
    scales     = block_scales,    # fine-grained scale per tile
)
