"""
Data Structures & Algorithms in Python
Chapter 2: Setting Up Python: Interpreter & REPL
Section: Foundations & Python Refresher

Read this chapter: https://books.vizuara.ai/read/dsa-in-python/python-setup-repl-and-interpreter

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import dis

def add(a, b):
    return a + b

dis.dis(add)
#   2  LOAD_FAST    a
#      LOAD_FAST    b
#      BINARY_OP    + 
#      RETURN_VALUE

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# >>> 2 + 3          # a plain expression
# 5                  # the REPL prints the value for you
# >>> x = 10         # an assignment is a statement — it produces no value
# >>> x * x          # ...so nothing prints. But now we can use x:
# 100
# >>> nums = [4, 1, 7, 3]
# >>> len(nums)      # ask a question, get an answer instantly
# 4
# >>> sorted(nums)   # experiment — does this mutate nums, or return a copy?
# [1, 3, 4, 7]
# >>> nums           # check: the original is untouched — good to know!
# [4, 1, 7, 3]

# --- block 3 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# >>> 6 * 7
# 42
# >>> _ + 8          # _ is 42, the previous result
# 50

# --- block 4 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# >>> for i in range(3):    # ends in ':' → REPL shows ... and waits
# ...     print(i * i)      # 4-space indent, still inside the block
# ...                       # <- press Enter on an EMPTY line to finish
# 0
# 1
# 4

# --- block 5 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# >>> import timeit
# >>> # append to the END of a 10,000-element list, 1000 times
# >>> timeit.timeit('a.append(0)', setup='a=list(range(10000))', number=1000)
# 0.00008          # ~0.08 milliseconds total
# >>> # insert at the FRONT of the same list, 1000 times
# >>> timeit.timeit('a.insert(0,0)', setup='a=list(range(10000))', number=1000)
# 0.012            # ~12 milliseconds total — about 150× slower
