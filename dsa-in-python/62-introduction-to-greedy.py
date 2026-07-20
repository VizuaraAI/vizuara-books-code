"""
Data Structures & Algorithms in Python
Chapter 62: Introduction to Greedy: Chocolate Distribution
Section: Greedy Algorithms & Capstone

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-greedy

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
packets = [7, 3, 2, 4, 9, 12, 56]   # chocolates per packet
m = 3                               # number of children

# --- block 2 ---
[2, 3, 4, 7, 9, 12, 56]

# --- block 3 ---
def min_unfairness(packets, m):
    n = len(packets)
    if m == 0 or m > n:            # no valid distribution
        return 0 if m == 0 else None

    packets.sort()                # O(n log n) — this is the expensive step

    best = float("inf")
    for i in range(n - m + 1):    # every window start, O(n) of them
        # window is packets[i : i + m]; sorted, so ends are min and max
        spread = packets[i + m - 1] - packets[i]
        best = min(best, spread)
    return best

print(min_unfairness([7, 3, 2, 4, 9, 12, 56], 3))   # -> 2
