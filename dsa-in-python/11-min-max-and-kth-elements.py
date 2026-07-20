"""
Data Structures & Algorithms in Python
Chapter 11: Max, Min & K-th Smallest/Largest
Section: Arrays & Matrices

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/min-max-and-kth-elements

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def find_max(nums):
    best = nums[0]              # seed with a real element
    for x in nums[1:]:         # scan the rest
        if x > best:
            best = x           # crown the new champion
    return best

# --- block 2 ---
def kth_smallest_sorting(nums, k):
    return sorted(nums)[k - 1]     # 1-based k

# --- block 3 ---
import heapq

def kth_smallest_heap(nums, k):
    heap = []                       # max-heap via negated values
    for x in nums:
        heapq.heappush(heap, -x)
        if len(heap) > k:
            heapq.heappop(heap)     # drop the largest of the K+1
    return -heap[0]                 # root = K-th smallest

# --- block 4 ---
def kth_smallest_quickselect(nums, k):
    nums = nums[:]                 # copy: partition is in-place
    target = k - 1                 # 1-based k -> 0-based index

    def partition(lo, hi):
        pivot = nums[hi]           # last element as pivot
        i = lo                     # boundary of the "< pivot" region
        for j in range(lo, hi):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]   # pivot to its final spot
        return i                   # pivot's final index

    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        p = partition(lo, hi)
        if p == target:
            return nums[p]         # pivot is the K-th smallest
        elif p < target:
            lo = p + 1             # answer is to the right
        else:
            hi = p - 1             # answer is to the left
