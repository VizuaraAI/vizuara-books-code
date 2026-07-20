"""
Kernel Engineering
Chapter 42: Benchmarking without lying to yourself
Section: The GEMM Worklog

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/gemm-benchmark-methodology

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
flops = 2 * M * N * K
tflops = flops / (time_ms * 1e-3) / 1e12

# --- block 2 ---
ref  = cublas_gemm(A, B)                       # trusted reference
out  = my_kernel(A, B)
err  = (out - ref).abs().max() / ref.abs().max()
assert err < 1e-2, f"kernel wrong: rel err {err:.2e}"
