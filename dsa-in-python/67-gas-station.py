"""
Data Structures & Algorithms in Python
Chapter 67: Gas Station
Section: Greedy Algorithms & Capstone

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/gas-station

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def can_complete_brute(gas, cost):
    n = len(gas)
    for start in range(n):          # try each start
        tank = 0
        for step in range(n):       # simulate a full loop
            i = (start + step) % n
            tank += gas[i] - cost[i]
            if tank < 0:            # ran dry mid-leg
                break
        else:                       # never broke → made it around
            return start
    return -1

# --- block 2 ---
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

# --- block 3 ---
net = [-2, -2, -2, 3, 3]

# --- block 4 ---
def can_complete_circuit(gas, cost):
    total = 0        # sum of all nets → feasibility check
    tank = 0         # net since the current candidate start
    start = 0        # current candidate

    for i in range(len(gas)):
        net = gas[i] - cost[i]
        total += net
        tank += net
        if tank < 0:        # candidate s..i all fail
            start = i + 1   # jump the whole failed prefix
            tank = 0        # fresh tank from the new candidate
    return start if total >= 0 else -1
