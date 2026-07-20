"""
Kernel Engineering
Chapter 31: GPU Puzzles, walkthrough II
Section: The CUDA Programming Model

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/gpu-puzzles-walkthrough-2

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def call(out, a) -> None:
    shared = cuda.shared.array(TPB, numba.float32)
    i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    local_i = cuda.threadIdx.x

    if i < a.size:
        shared[local_i] = a[i]        # 1. every thread loads its element
    cuda.syncthreads()                 # 2. barrier: wait for ALL loads
    if i < a.size:
        out[i] = shared[local_i] + 10  # 3. now safe to read shared

# --- block 2 ---
def call(out, a, b) -> None:
    shared_a = cuda.shared.array(TPB + CONV - 1, numba.float32)
    shared_b = cuda.shared.array(CONV, numba.float32)
    i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    local_i = cuda.threadIdx.x

    if i < a.size:
        shared_a[local_i] = a[i]
    if local_i < CONV:                       # a few threads fetch the halo + kernel
        shared_a[TPB + local_i] = a[i + TPB] if i + TPB < a.size else 0
        shared_b[local_i] = b[local_i]
    cuda.syncthreads()

    if i < out.size:
        acc = 0.0
        for j in range(CONV):
            acc += shared_a[local_i + j] * shared_b[j]  # window from shared only
        out[i] = acc

# --- block 3 ---
def call(out, a, b) -> None:
    shared = cuda.shared.array(TPB, numba.float32)
    i = cuda.threadIdx.x
    shared[i] = a[i] * b[i]     # elementwise product into shared
    cuda.syncthreads()

    stride = TPB // 2
    while stride > 0:
        if i < stride:
            shared[i] += shared[i + stride]   # add partner `stride` away
        cuda.syncthreads()                    # barrier EVERY round
        stride //= 2

    if i == 0:
        out[0] = shared[0]     # thread 0 writes the answer

# --- block 4 ---
def call(out, a, b, size) -> None:
    shared_a = cuda.shared.array((TPB, TPB), numba.float32)
    shared_b = cuda.shared.array((TPB, TPB), numba.float32)
    i = cuda.blockIdx.y * cuda.blockDim.y + cuda.threadIdx.y   # global row
    j = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x   # global col
    ti, tj = cuda.threadIdx.y, cuda.threadIdx.x

    acc = 0.0
    for k0 in range(0, size, TPB):                # slide over k, tile by tile
        if i < size and k0 + tj < size:
            shared_a[ti, tj] = a[i, k0 + tj]
        if j < size and k0 + ti < size:
            shared_b[ti, tj] = b[k0 + ti, j]
        cuda.syncthreads()                        # tile fully loaded
        for k in range(TPB):
            acc += shared_a[ti, k] * shared_b[k, tj]
        cuda.syncthreads()                        # done reading before reload
    if i < size and j < size:
        out[i, j] = acc
