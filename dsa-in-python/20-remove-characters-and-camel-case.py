"""
Data Structures & Algorithms in Python
Chapter 20: Remove Occurrences & Camel-Case a Sentence
Section: Strings, Sets & Dictionaries

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/remove-characters-and-camel-case

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- placeholder added so this file runs standalone (not book code) ---
s = "banana"  # TODO: block 2 filters the chapter's running example string; the
              # book's blocks 1, 3 and 4 all use "banana" - see
              # https://books.vizuara.ai/read/dsa-in-python/remove-characters-and-camel-case

# --- block 1 ---
def remove_char(s, target):
    chars = list(s)          # immutable string -> mutable list, O(n)
    write = 0                # where the next kept char goes
    for read in range(len(chars)):     # read visits every position
        if chars[read] != target:
            chars[write] = chars[read] # keep it: copy back
            write += 1                 # advance the write cursor
    return "".join(chars[:write])      # the first `write` cells are the answer

remove_char("banana", "a")   # 'bnn'

# --- block 2 ---
"".join(ch for ch in s if ch != "a")        # 'bnn' — filter then join, O(n)

# --- block 3 ---
"banana".replace("a", "")                    # 'bnn' — replace target with empty, O(n)

# --- block 4 ---
"banana".translate(str.maketrans("", "", "aeiou"))   # 'bnn'

# --- block 5 ---
def to_camel_case(sentence):
    result = []              # collect chars, join once (never += in a loop)
    new_word = False         # first word stays lowercase, so start False
    for ch in sentence:
        if ch == " ":
            new_word = True          # drop the space, arm the flag
        elif new_word:
            result.append(ch.upper())  # first letter of a new word
            new_word = False           # disarm
        else:
            result.append(ch)          # ordinary letter, as-is
    return "".join(result)

to_camel_case("the quick brown fox")   # 'theQuickBrownFox'

# --- block 6 ---
def to_camel_case(sentence):
    words = sentence.split()                      # ['the','quick','brown','fox']
    return words[0] + "".join(w.capitalize() for w in words[1:])

to_camel_case("the quick brown fox")   # 'theQuickBrownFox'
