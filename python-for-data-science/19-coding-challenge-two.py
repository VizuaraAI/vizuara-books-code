"""
Python for Data Science
Chapter 19: Coding Challenge Two
Section: Problem-Solving with Coding Challenges

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/coding-challenge-two

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def normalize(text):
    text = text.lower()
    cleaned = ""
    for ch in text:
        cleaned += ch if ch.isalpha() or ch == " " else " "
    return cleaned

def tokenize(text):
    return normalize(text).split()   # split() on no args splits on any run of whitespace

# --- block 2 ---
def count_words(tokens):
    counts = {}
    for word in tokens:
        counts[word] = counts.get(word, 0) + 1
    return counts

# --- block 3 ---
def top_n(counts, n=3):
    ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
    return ranked[:n]

# --- block 4 ---
text = "The cat sat. The cat ran!"
tokens = tokenize(text)          # normalize + split
counts = count_words(tokens)     # the dict tally
print(top_n(counts, 3))          # -> [('the', 2), ('cat', 2), ('sat', 1)]
