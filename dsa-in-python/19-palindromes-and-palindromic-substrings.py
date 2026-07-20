"""
Data Structures & Algorithms in Python
Chapter 19: Palindrome String & Palindromic Substrings
Section: Strings, Sets & Dictionaries

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/palindromes-and-palindromic-substrings

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def is_palindrome_slice(s):
    return s == s[::-1]

is_palindrome_slice("racecar")   # True
is_palindrome_slice("hello")     # False

# --- block 2 ---
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False          # a single mismatch is a definitive NO
        left += 1
        right -= 1
    return True                   # never mismatched → symmetric

# --- block 3 ---
def is_palindrome_clean(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return is_palindrome(cleaned)          # same check, sanitized input

is_palindrome_clean("A man a plan a canal Panama")   # True

# --- block 4 ---
def count_palindromic_substrings(s):
    n = len(s)
    total = 0

    def expand(left, right):
        count = 0
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1                # this [left..right] is a new palindrome
            left -= 1                 # push outward
            right += 1
        return count

    for i in range(n):
        total += expand(i, i)         # odd-length center at i
        total += expand(i, i + 1)     # even-length center between i and i+1
    return total

count_palindromic_substrings("aaa")   # 6
count_palindromic_substrings("aba")   # 4
