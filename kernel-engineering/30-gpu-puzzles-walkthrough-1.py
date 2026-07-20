"""
Kernel Engineering
Chapter 30: GPU Puzzles, walkthrough I
Section: The CUDA Programming Model

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/gpu-puzzles-walkthrough-1

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def call(out, a) -> None:
    local_i = cuda.threadIdx.x
    out[local_i] = a[local_i] + 10

# --- block 2 ---
def call(out, a, b) -> None:
    local_i = cuda.threadIdx.x
    out[local_i] = a[local_i] + b[local_i]

# --- block 3 ---
def call(out, a, size) -> None:
    local_i = cuda.threadIdx.x
    if local_i < size:
        out[local_i] = a[local_i] + 10

# --- block 4 ---
def call(out, a, size) -> None:
    i = cuda.threadIdx.x
    j = cuda.threadIdx.y
    if i < size and j < size:
        out[i, j] = a[i, j] + 10

# --- block 5 ---
def call(out, a, b, size) -> None:
    i = cuda.threadIdx.x
    j = cuda.threadIdx.y
    if i < size and j < size:
        out[i, j] = a[i, 0] + b[0, j]

# --- block 6 ---
def call(out, a, size) -> None:
    i = cuda.blockIdx.x * cuda.blockDim.x + cuda.threadIdx.x
    if i < size:
        out[i] = a[i] + 10

# --- block 7 ---
i = blockIdx.x * blockDim.x + threadIdx.x
if i < N:
    ...  # do this thread's work
