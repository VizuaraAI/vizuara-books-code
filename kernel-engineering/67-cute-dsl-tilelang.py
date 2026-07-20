"""
Kernel Engineering
Chapter 67: CuTe, the DSL landscape & Triton
Section: The Frontier

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/cute-dsl-tilelang

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
@triton.jit
def softmax_kernel(out_ptr, in_ptr, n_cols, BLOCK: tl.constexpr):
    row  = tl.program_id(0)                       # one instance owns one row
    cols = tl.arange(0, BLOCK)
    ptrs = in_ptr + row * n_cols + cols
    x = tl.load(ptrs, mask=cols < n_cols, other=-float('inf'))
    x = x - tl.max(x, axis=0)                      # numerically stable
    num = tl.exp(x)
    y = num / tl.sum(num, axis=0)
    tl.store(out_ptr + row * n_cols + cols, y, mask=cols < n_cols)

# --- block 2 ---
@T.prim_func
def matmul(A, B, C):
    with T.Kernel(N // BN, M // BM, threads=128) as (bx, by):
        As = T.alloc_shared((BM, BK), "float16")     # YOU name + place this
        Bs = T.alloc_shared((BK, BN), "float16")     # YOU name + place this
        Cl = T.alloc_fragment((BM, BN), "float32")   # register accumulator
        T.clear(Cl)
        for k in T.Pipelined(K // BK, num_stages=3): # compiler FILLS the pipeline
            T.copy(A[by*BM, k*BK], As)               # global → SMEM
            T.copy(B[k*BK, bx*BN], Bs)
            T.gemm(As, Bs, Cl)                        # SMEM → tensor cores
        T.copy(Cl, C[by*BM, bx*BN])
