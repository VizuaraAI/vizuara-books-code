"""
Kernel Engineering
Chapter 3: Speed-of-light thinking & the roofline
Section: Start Here

Read this chapter: https://books.vizuara.ai/read/kernel-engineering/speed-of-light-thinking

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def speed_of_light_us(flops, bytes_moved,
                      peak_flops=989e12, peak_bw=3.35e12):
    t_compute = flops / peak_flops        # seconds if the floor is the wall
    t_memory  = bytes_moved / peak_bw     # seconds if the belt is the wall
    return max(t_compute, t_memory) * 1e6 # microseconds — whichever wins
