"""
Data Structures & Algorithms in Python
Chapter 18: All Substrings & Reverse a String
Section: Strings, Sets & Dictionaries

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/all-substrings-and-reverse-a-string

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholder added so this file runs standalone (not book code) ---
s = "abcd"  # TODO: block 4 reverses the chapter's example string; the book's
            # own blocks 1-2 use "abcd" - see
            # https://books.vizuara.ai/read/dsa-in-python/all-substrings-and-reverse-a-string

# --- block 1 ---
def all_substrings(s):
    result = []
    n = len(s)
    for i in range(n):            # start index
        for j in range(i, n):     # end index, never before the start
            result.append(s[i:j+1])
    return result

all_substrings("abcd")
# ['a', 'ab', 'abc', 'abcd',
#  'b', 'bc', 'bcd',
#  'c', 'cd',
#  'd']

# --- block 2 ---
def reverse(s):
    return s[::-1]

reverse("abcd")   # 'dcba'

# --- block 3 ---
def reverse_slow(s):
    result = ""
    for ch in s:
        result = ch + result      # prepend each character... looks innocent
    return result

# --- block 4 ---
s[::-1]                    # extended slice — idiomatic, one allocation
"".join(reversed(s))       # reversed() yields chars right-to-left, join builds once
"".join(list(s)[::-1])     # materialise, reverse the list, join — most explicit
