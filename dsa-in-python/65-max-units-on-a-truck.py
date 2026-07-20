"""
Data Structures & Algorithms in Python
Chapter 65: Maximum Units on a Truck
Section: Greedy Algorithms & Capstone

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/max-units-on-a-truck

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
boxTypes = [[1, 3], [2, 2], [3, 1]]   # [count, units-per-box]
truckSize = 4                          # the truck holds 4 boxes total

# --- block 2 ---
def maximum_units(boxTypes, truckSize):
    # Sort by units-per-box, DESCENDING (richest first).
    boxTypes.sort(key=lambda b: b[1], reverse=True)

    total = 0
    remaining = truckSize
    for boxes, units in boxTypes:
        take = min(boxes, remaining)   # never load more than the truck can hold
        total += take * units
        remaining -= take
        if remaining == 0:             # truck is full — no reason to keep looking
            break
    return total

boxTypes = [[1, 3], [2, 2], [3, 1]]
print(maximum_units(boxTypes, 4))      # -> 8
