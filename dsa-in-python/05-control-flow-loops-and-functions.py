"""
Data Structures & Algorithms in Python
Chapter 5: Control Flow: Conditionals, Loops & Functions
Section: Foundations & Python Refresher

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/control-flow-loops-and-functions

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
n = -4

if n < 0:
    print("negative")
elif n == 0:
    print("zero")
else:
    print("positive")

# --- block 2 ---
nums = [3, 1, 4, 1, 5]
total = 0
for x in nums:
    total += x        # 3, then 4, then 8, then 9, then 14
print(total)          # 14

# --- block 3 ---
n = 100
steps = 0
while n > 0:
    n = n // 2        # 100 → 50 → 25 → 12 → 6 → 3 → 1 → 0
    steps += 1
print(steps)          # 7

# --- block 4 ---
def find(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i          # found it — leave right now
    return -1                 # scanned everything, not present

# --- block 5 ---
def add(a, b):
    result = a + b
    return result

x = add(3, 4)     # a=3, b=4 → returns 7, bound to x
y = add(10, 5)    # same code, new arguments → 15

# --- block 6 ---
def maximum(nums):
    best = nums[0]            # assume the first is largest
    for x in nums[1:]:        # loop over the rest
        if x > best:          # decide: is this one bigger?
            best = x          # update the running best
    return best              # hand back the answer

maximum([3, 1, 4, 1, 5])     # → 5
