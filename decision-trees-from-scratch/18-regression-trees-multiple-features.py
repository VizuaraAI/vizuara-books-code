"""
Build Decision Trees from Scratch
Chapter 18: Regression Trees with Multiple Features
Section: Regression Trees

Read this chapter: https://books.vizuara.ai/read/decision-trees-from-scratch/regression-trees-multiple-features

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# best_score = float("inf")     # lower SSR is better; start impossibly high
# best_split = None             # (feature, threshold) of the champion so far
#
# for feature in range(n_features):                 # temp (0), then humidity (1)
#     values = sorted(set(rows[:, feature]))        # unique values in THIS node
#     for a, b in zip(values, values[1:]):          # adjacent sorted pairs
#         threshold = (a + b) / 2                    # the midpoint candidate
#         left  = rows[rows[:, feature] <= threshold, target]
#         right = rows[rows[:, feature] >  threshold, target]
#         score = ssr(left) + ssr(right)             # SSR(L) + SSR(R)
#         if score < best_score:                     # strictly better? take it
#             best_score, best_split = score, (feature, threshold)
#
# return best_split, best_score
