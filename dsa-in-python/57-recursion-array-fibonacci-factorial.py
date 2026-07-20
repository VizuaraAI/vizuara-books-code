"""
Data Structures & Algorithms in Python
Chapter 57: Recursive Traversal, Fibonacci & Factorial
Section: Recursion & Backtracking

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/recursion-array-fibonacci-factorial

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def array_sum(nums, i=0):
    if i == len(nums):      # base case: past the end, nothing left to add
        return 0
    return nums[i] + array_sum(nums, i + 1)   # first + sum(rest)

# --- block 2 ---
def factorial(n):
    if n <= 1:          # base case: 0! and 1! are both 1
        return 1
    return n * factorial(n - 1)   # n × (n-1)!

# --- block 3 ---
def fib(n):
    if n < 2:                 # two base cases: F(0)=0, F(1)=1
        return n
    return fib(n - 1) + fib(n - 2)

# --- block 4 ---
def fib(n, memo={}):
    if n < 2:
        return n
    if n in memo:                 # already solved? return the cached answer
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
