"""
Data Structures & Algorithms in Python
Chapter 22: Unique Characters & Pangram with Sets
Section: Strings, Sets & Dictionaries

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/unique-characters-and-pangram-with-sets

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def count_distinct_slow(s):
    seen = []
    for ch in s:
        if ch not in seen:      # scans the whole list — O(k)
            seen.append(ch)
    return len(seen)

# --- block 2 ---
def count_distinct(s):
    seen = set()
    for ch in s:
        seen.add(ch)        # duplicates are ignored automatically
    return len(seen)

# --- block 3 ---
len(set("BANANA"))      # 3

# --- block 4 ---
def is_pangram(sentence):
    letters = set(ch for ch in sentence.lower() if ch.isalpha())
    return len(letters) == 26

# --- block 5 ---
from string import ascii_lowercase   # 'abcdefghijklmnopqrstuvwxyz'

def is_pangram(sentence):
    return set(ascii_lowercase) <= set(sentence.lower())

# --- block 6 ---
def missing_letters(sentence):
    return set(ascii_lowercase) - set(sentence.lower())
