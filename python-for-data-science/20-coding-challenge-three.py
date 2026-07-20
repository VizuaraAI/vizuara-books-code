"""
Python for Data Science
Chapter 20: Coding Challenge Three
Section: Problem-Solving with Coding Challenges

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/coding-challenge-three

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
text = "The cat sat. The CAT ran!"

# --- block 2 ---
# 1. lowercase the whole text
# 2. split into words on whitespace
# 3. for each word: strip leading/trailing punctuation
#      -> if the word is now empty, skip it
# 4. tally it in a dict: counts[word] = counts.get(word, 0) + 1
# 5. sort the dict items by count, descending
# 6. return the sorted list of (word, count) pairs

# --- block 3 ---
# Buggy first attempt — no lowercasing, no punctuation stripping
def word_counts(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

word_counts("The cat sat. The CAT ran!")
# {'The': 1, 'cat': 1, 'sat.': 1, 'CAT': 1, 'ran!': 1}

# --- block 4 ---
import string

def word_counts(text):
    counts = {}
    for word in text.lower().split():        # 1 + 2: lowercase, then split
        word = word.strip(string.punctuation)  # 3: shave punctuation off both ends
        if not word:                           # guard: skip anything left empty
            continue
        counts[word] = counts.get(word, 0) + 1  # 4: tally, get()-with-default
    return counts

# --- block 5 ---
def top_words(text):
    counts = word_counts(text)
    return sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

top_words("The cat sat. The CAT ran!")
# [('the', 2), ('cat', 2), ('sat', 1), ('ran', 1)]
