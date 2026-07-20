"""
Data Structures & Algorithms in Python
Chapter 40: Previous Smaller & Greater Element
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/previous-smaller-and-greater-element

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def previous_smaller_bruteforce(a):
    n = len(a)
    ans = [-1] * n
    for i in range(n):
        for j in range(i - 1, -1, -1):   # walk left from i-1
            if a[j] < a[i]:
                ans[i] = a[j]
                break
    return ans

# --- block 2 ---
def previous_smaller(a):
    stack = []              # values, kept strictly increasing bottom→top
    ans = []
    for x in a:
        while stack and stack[-1] >= x:   # pop everything not smaller than x
            stack.pop()
        ans.append(stack[-1] if stack else -1)
        stack.append(x)
    return ans

# previous_smaller([4, 5, 2, 10, 8]) -> [-1, 4, -1, 2, 2]

# --- block 3 ---
def previous_greater(a):
    stack = []
    ans = []
    for x in a:
        while stack and stack[-1] <= x:   # only strictly-greater survives
            stack.pop()
        ans.append(stack[-1] if stack else -1)
        stack.append(x)
    return ans

# previous_greater([4, 5, 2, 10, 8]) -> [-1, -1, 5, -1, 10]
