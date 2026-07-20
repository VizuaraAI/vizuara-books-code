"""
Data Structures & Algorithms in Python
Chapter 42: Daily Temperatures
Section: Stacks & Queues

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/daily-temperatures

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def daily_temperatures_brute(T):
    n = len(T)
    answer = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if T[j] > T[i]:
                answer[i] = j - i
                break
    return answer

# --- block 2 ---
def daily_temperatures(T):
    n = len(T)
    answer = [0] * n
    stack = []                      # holds indices; temps decrease bottom→top
    for i in range(n):
        while stack and T[i] > T[stack[-1]]:
            j = stack.pop()         # day j finally has a warmer day
            answer[j] = i - j       # ...and it is exactly (i - j) days out
        stack.append(i)
    return answer
