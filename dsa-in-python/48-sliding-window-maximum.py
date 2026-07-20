"""
Data Structures & Algorithms in Python
Chapter 48: Sliding Window Maximum
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/sliding-window-maximum

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def max_of_windows_brute(nums, k):
    out = []
    for i in range(len(nums) - k + 1):     # each window start
        out.append(max(nums[i:i + k]))     # scan k elements
    return out

# --- block 2 ---
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()          # holds INDICES, values decreasing front -> back
    out = []
    for i, val in enumerate(nums):
        # 1. drop the front if it has slid out of the window
        if dq and dq[0] <= i - k:
            dq.popleft()
        # 2. drop back indices whose values are <= the incoming value
        while dq and nums[dq[-1]] <= val:
            dq.pop()
        # 3. this index is a live candidate
        dq.append(i)
        # 4. once the first full window exists, record the front
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
