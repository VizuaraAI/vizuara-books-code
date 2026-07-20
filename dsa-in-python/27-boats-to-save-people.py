"""
Data Structures & Algorithms in Python
Chapter 27: Boats to Save People (Leetcode 881)
Section: Two Pointers & Sliding Window

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/boats-to-save-people

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def num_rescue_boats(people, limit):
    people.sort()                     # O(n log n): the price of admission
    light, heavy = 0, len(people) - 1
    boats = 0
    while light <= heavy:             # <= : the lone middle person still needs a boat
        if people[light] + people[heavy] <= limit:
            light += 1                # lightest gets a seat → advance from the left
        heavy -= 1                    # heaviest always leaves on THIS boat
        boats += 1
    return boats
