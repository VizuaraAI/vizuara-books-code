"""
Data Structures & Algorithms in Python
Chapter 63: Minimum Platforms
Section: Greedy Algorithms & Capstone

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/minimum-platforms

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
arrivals   = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]

# --- block 2 ---
arrivals.sort()
departures.sort()

# --- block 3 ---
arrivals   = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1120, 1130, 1200, 1900, 2000]

# --- block 4 ---
def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    n = len(arrivals)

    i = j = 0
    platforms = 0
    max_platforms = 0

    while i < n and j < n:
        if arrivals[i] <= departures[j]:   # next event is an arrival
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:                              # next event is a departure
            platforms -= 1
            j += 1

    return max_platforms
