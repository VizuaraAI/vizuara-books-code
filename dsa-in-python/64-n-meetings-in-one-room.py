"""
Data Structures & Algorithms in Python
Chapter 64: N Meetings in One Room
Section: Greedy Algorithms & Capstone

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/n-meetings-in-one-room

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def max_meetings(start, end):
    # Pair up each meeting, then sort by finish time (the second field).
    meetings = sorted(zip(start, end), key=lambda m: m[1])

    count = 0
    last_end = float("-inf")     # room is free before everything

    for s, e in meetings:
        if s >= last_end:        # this meeting doesn't overlap the last one taken
            count += 1
            last_end = e         # occupy the room until e
    return count

start = [1, 2, 4, 6, 5]
end   = [3, 5, 7, 8, 9]
print(max_meetings(start, end))   # -> 2
