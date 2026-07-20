"""
Data Structures & Algorithms in Python
Chapter 25: The Two-Pointers Technique
Section: Two Pointers & Sliding Window

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/two-pointers-technique

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False       # one mismatch → definitively NOT a palindrome
        left += 1
        right -= 1
    return True

# --- block 2 ---
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left, right]     # found it
        elif total < target:
            left += 1                # too small → need a bigger value on the left
        else:
            right -= 1               # too big → need a smaller value on the right
    return []                        # no pair sums to target

# --- block 3 ---
def dedupe_preview(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]    # place the next unique value
    return slow + 1                    # count of uniques
