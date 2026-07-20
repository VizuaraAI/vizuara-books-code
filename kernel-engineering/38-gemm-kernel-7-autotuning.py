"""
Kernel Engineering
Chapter 38: Kernel 7: Autotuning the tiles
Section: The GEMM Worklog

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/gemm-kernel-7-autotuning

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- imports (added by the generator) ---
# The chapter uses these modules but introduces them earlier in the
# book, so the import lines are not repeated in its own code blocks.
import itertools

# --- block 1 ---
BM  = [64, 128, 256]
BN  = [64, 128, 256]
BK  = [8, 16, 32, 64]
TM  = [4, 8, 16]
TN  = [4, 8, 16]

def legal(BM, BN, BK, TM, TN, smem_cap=228*1024, max_regs=255):
    nthreads = (BM * BN) // (TM * TN)
    if not (64 <= nthreads <= 1024):            # block-size limits
        return False
    if (BM * BN) % (TM * TN) != 0:              # tile must divide evenly
        return False
    # vectorized float4 SMEM loads: each thread loads whole float4s
    if (BM * BK) % (4 * nthreads) != 0:         # A slab is float4-loadable
        return False
    if (BK * BN) % (4 * nthreads) != 0:         # B slab is float4-loadable
        return False
    smem = (BM * BK + BK * BN) * 4              # bytes, single-buffered
    if smem > smem_cap:
        return False
    est_regs = TM * TN + 8                      # accumulators + overhead
    return est_regs <= max_regs

configs = [c for c in itertools.product(BM, BN, BK, TM, TN) if legal(*c)]

# --- block 2 ---
best = None
for cfg in configs:
    binary = compile_kernel(cfg)              # -DBM=... -DBN=... etc.
    for _ in range(warmup): binary.run(A, B, C)
    ts = [time(lambda: binary.run(A, B, C)) for _ in range(iters)]
    tflops = flops(N) / median(ts)
    if best is None or tflops > best.tflops:
        best = Result(cfg, tflops)
