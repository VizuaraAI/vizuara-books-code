"""
Python for Data Science
Chapter 18: Coding Challenge One
Section: Problem-Solving with Coding Challenges

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/coding-challenge-one

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Buggy first attempt — wrong order
for n in range(1, 101):
    if n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    elif n % 15 == 0:
        print("FizzBuzz")
    else:
        print(n)

# --- block 2 ---
# Correct FizzBuzz
for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
