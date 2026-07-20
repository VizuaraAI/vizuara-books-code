"""
Kernel Engineering
Chapter 17: Occupancy: the balancing act
Section: The GPU, From Silicon Up

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/occupancy

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# H100 SM budgets (sm_90)
MAX_REGS    = 65536          # 32-bit registers per SM
MAX_SMEM    = 228 * 1024     # usable shared-memory carve-out
MAX_THREADS = 2048           # = 64 warps
MAX_WARPS   = 64

# what kernel 3 asks for
regs_per_thread = 37
smem_per_block  = 8192 + 1024        # tiles + runtime reservation
threads_per_blk = 1024               # = 32 warps

# how many blocks each resource permits
by_regs    = MAX_REGS    // (regs_per_thread * threads_per_blk)   # -> 1
by_smem    = MAX_SMEM    // smem_per_block                        # -> 25
by_threads = MAX_THREADS // threads_per_blk                       # -> 2

blocks_per_sm = min(by_regs, by_smem, by_threads)                 # -> 1
warps         = blocks_per_sm * (threads_per_blk // 32)           # -> 32
occupancy     = warps / MAX_WARPS                                 # -> 0.50
