"""
Machine Learning & Deep Learning Mastery
Chapter 44: Splitting on Numerical Data
Section: CNNs & Decision Trees

Read this chapter: https://books.vizuara.ai/read/ml-dl-mastery/splitting-on-numerical-data

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
    p1 = sum(labels) / n          # fraction of positives (labels are 0/1)
    return 1 - (p1**2 + (1 - p1)**2)

def best_numeric_split(values, labels):
    # pair up, sort by feature value
    rows = sorted(zip(values, labels))
    xs = [v for v, _ in rows]
    ys = [y for _, y in rows]
    n = len(xs)

    best_t, best_score = None, float("inf")
    for i in range(1, n):
        if xs[i] == xs[i - 1]:
            continue                      # no gap → no new split
        t = (xs[i] + xs[i - 1]) / 2       # midpoint threshold
        left, right = ys[:i], ys[i:]      # already sorted, so a clean cut
        score = (len(left)/n) * gini(left) + (len(right)/n) * gini(right)
        if score < best_score:
            best_t, best_score = t, score
    return best_t, best_score
