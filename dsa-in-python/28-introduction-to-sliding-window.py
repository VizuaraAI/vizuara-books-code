"""
Data Structures & Algorithms in Python
Chapter 28: The Sliding-Window Technique
Section: Two Pointers & Sliding Window

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-sliding-window

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def max_sum_bruteforce(nums, k):
    best = float("-inf")
    for start in range(len(nums) - k + 1):   # each window start
        window_sum = 0
        for i in range(start, start + k):     # re-sum k elements
            window_sum += nums[i]
        best = max(best, window_sum)
    return best

# --- block 2 ---
def max_sum_window(nums, k):
    window_sum = sum(nums[:k])        # prime the first window: O(k), once
    best = window_sum
    for right in range(k, len(nums)):  # slide the right edge across the rest
        window_sum += nums[right]      # add the element entering on the right
        window_sum -= nums[right - k]  # drop the element leaving on the left
        best = max(best, window_sum)
    return best

# --- block 3 ---
# NOTE: this block is prose in the book, not runnable code.
# It is the variable-size sliding-window TEMPLATE: `window_is_invalid()` and the
# "running state" lines are placeholders the reader fills in per problem, so the
# block is kept verbatim but commented out.
# def longest_window(nums):
#     left = 0
#     best = 0
#     # ... running state describing the window, e.g. a sum or a count ...
#     for right in range(len(nums)):
#         # 1. include nums[right] — the window just grew on the right
#         while window_is_invalid():        # 2. property broke?
#             # remove nums[left] from the running state
#             left += 1                      #    shrink from the left
#         best = max(best, right - left + 1) # 3. record this valid window's length
#     return best
