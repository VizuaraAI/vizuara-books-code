"""
Data Structures & Algorithms in Python
Chapter 66: Minimum Arrows to Burst Balloons
Section: Greedy Algorithms & Capstone

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/minimum-arrows-to-burst-balloons

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def find_min_arrows(balloons):
    if not balloons:
        return 0
    # 1. sort by end coordinate
    balloons.sort(key=lambda b: b[1])
    arrows = 1
    arrow = balloons[0][1]          # fire the first arrow at the first end
    # 2. sweep left to right
    for start, end in balloons[1:]:
        if start > arrow:           # balloon starts past our arrow → needs a new one
            arrows += 1
            arrow = end             # plant it at this balloon's end
        # else: start <= arrow, already burst, do nothing
    return arrows
