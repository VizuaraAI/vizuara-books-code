"""
Data Structures & Algorithms in Python
Chapter 24: Frequency Counting: Vowels, Uniques & Pangram
Section: Strings, Sets & Dictionaries

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/frequency-counting-with-dictionaries

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def char_frequency(s):
    freq = {}
    for c in s:
        if c in freq:            # (1) the explicit way
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

char_frequency("banana")   # {'b': 1, 'a': 3, 'n': 2}

# --- block 2 ---
from collections import defaultdict

def char_frequency(s):
    freq = defaultdict(int)      # missing keys default to 0
    for c in s:
        freq[c] += 1             # no KeyError — the key springs into existence at 0
    return dict(freq)

# --- block 3 ---
def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for c in s.lower():          # normalize so 'A' and 'a' both count
        if c in vowels:
            count += 1
    return count

count_vowels("Education")   # 5  ->  E, u, a, i, o

# --- block 4 ---
from collections import Counter

def unique_chars(s):
    freq = Counter(s)                         # {'b': 1, 'a': 3, 'n': 2}
    return [c for c, n in freq.items() if n == 1]

unique_chars("banana")   # ['b']

# --- block 5 ---
import string

def is_pangram(s):
    letters = set(c for c in s.lower() if c.isalpha())
    return len(letters) == 26

is_pangram("The quick brown fox jumps over the lazy dog")   # True
is_pangram("Hello world")                                    # False

# --- block 6 ---
from collections import Counter

def pangram_report(s):
    freq = Counter(c for c in s.lower() if c.isalpha())
    missing = [c for c in string.ascii_lowercase if c not in freq]
    return {"is_pangram": len(missing) == 0, "missing": missing}

# --- block 7 ---
from collections import Counter

def is_anagram(a, b):
    return Counter(a) == Counter(b)

is_anagram("listen", "silent")   # True
is_anagram("aab", "abb")         # False
