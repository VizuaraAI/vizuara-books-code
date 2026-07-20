"""
Data Structures & Algorithms in Python
Chapter 17: Introduction to Strings
Section: Strings, Sets & Dictionaries

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/introduction-to-strings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholder added so this file runs standalone (not book code) ---
text = ""  # TODO: blocks 5 and 6 scan an input string the reader supplies - see
           # https://books.vizuara.ai/read/dsa-in-python/introduction-to-strings

# --- block 1 ---
s = "PYTHON"
s[0]        # 'P'   — first character, O(1)
s[-1]       # 'N'   — last character
s[1:4]      # 'YTH' — a slice, characters 1,2,3
len(s)      # 6

# --- block 2 ---
s = "PYTHON"
s[0] = "J"      # TypeError: 'str' object does not support item assignment

# --- block 3 ---
s = "CAT"
s = s[0] + "O" + s[2]   # builds a NEW 3-char string "COT"

# --- block 4 ---
a = "hello"
b = "hel" + "lo"        # same characters, built at runtime
a == b                  # True  (same TEXT, always correct)
a is b                  # may be True OR False (same OBJECT?)

# --- block 5 ---
result = ""
for ch in text:
    if ch.isalpha():
        result += ch        # looks like appending — it is NOT

# --- block 6 ---
parts = []
for ch in text:
    if ch.isalpha():
        parts.append(ch)     # O(1) amortized, list is mutable
result = "".join(parts)      # ONE pass, O(n) total

# --- block 7 ---
s = "  Hello, World  "
s.strip()            # 'Hello, World'  — returns new; s is UNCHANGED
s.lower()            # 'hello, world'  — new string
s.replace("l", "L")  # '  HeLLo, WorLd  ' — new string
s = s.strip().lower()   # to actually keep it, REBIND

# --- block 8 ---
chars = list("hello")   # ['h','e','l','l','o'] — now mutable
chars[0] = "H"          # fine!
"".join(chars)          # 'Hello'
