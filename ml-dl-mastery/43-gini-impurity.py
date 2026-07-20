"""
Machine Learning & Deep Learning Mastery
Chapter 43: Gini Impurity: Choosing the Best Split
Section: CNNs & Decision Trees

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/gini-impurity

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from collections import Counter

def gini(labels):
    """Gini impurity of a list of class labels."""
    n = len(labels)
    if n == 0:
        return 0.0
    counts = Counter(labels)
    return 1.0 - sum((c / n) ** 2 for c in counts.values())

def split_gain(parent, left, right):
    """How much this split reduces weighted impurity."""
    n = len(parent)
    weighted_child = (len(left) / n) * gini(left) + (len(right) / n) * gini(right)
    return gini(parent) - weighted_child

parent = ["A"]*6 + ["O"]*4
left   = ["A"]*5 + ["O"]*1     # answered "is it red?" = yes
right  = ["A"]*1 + ["O"]*3     # answered "is it red?" = no

print(gini(parent))            # 0.48
print(split_gain(parent, left, right))   # 0.163...
