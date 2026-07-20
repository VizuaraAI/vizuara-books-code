"""
Build Decision Trees from Scratch
Chapter 7: Gini Impurity: A Worked Example
Section: Classification Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/gini-impurity-worked-example

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def gini(labels):
    n = len(labels)
    if n == 0:
        return 0.0
    score = 1.0
    for c in set(labels):
        p = labels.count(c) / n        # fraction of THIS node in class c
        score -= p * p                 # subtract each squared fraction
    return score

def weighted_gini(left, right):
    n = len(left) + len(right)
    return (len(left) / n) * gini(left) + (len(right) / n) * gini(right)

gini(["cat", "cat", "cat"])                    # -> 0.0     (pure)
gini(["cat", "cat", "dog"])                    # -> 0.444   (mixed, 2/3-1/3)
weighted_gini(["cat","cat","dog"], ["cat","dog","dog"])  # -> 0.444 (the age<=2.5 split)
