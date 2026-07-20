"""
Python for Data Science
Chapter 14: Sets and Uniqueness
Section: Data Structures in Python

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/sets-and-uniqueness

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
rsvps = ["ana", "ravi", "ana", "meng", "ravi", "ravi"]

# --- block 2 ---
seen = []
for name in rsvps:
    if name not in seen:
        seen.append(name)
# seen == ["ana", "ravi", "meng"]

# --- block 3 ---
guests = set(rsvps)
# guests == {"ana", "ravi", "meng"}
len(guests)  # 3

# --- block 4 ---
type({})       # <class 'dict'>   ← surprise!
type(set())    # <class 'set'>    ← this is the empty set

# --- block 5 ---
primes = {2, 3, 5, 7}          # a set literal
chars  = set("banana")         # {"b", "a", "n"}  ← from a string's letters
empty  = set()                 # the one true empty set
primes.add(11)                 # {2, 3, 5, 7, 11}
primes.add(2)                  # no change — 2 is already present
primes.discard(4)              # removing an absent item is safe with discard

# --- block 6 ---
{1, "hi", (2, 3)}     # fine — all hashable
{[1, 2]}              # TypeError: unhashable type: 'list'

# --- block 7 ---
post_a = {"python", "data", "numpy"}
post_b = {"python", "pandas", "data", "sql"}

# --- block 8 ---
yesterday = {"u1", "u2", "u3", "u4"}
today     = {"u2", "u3", "u5"}

retained = yesterday & today   # {"u2", "u3"}   → in both days
new      = today - yesterday   # {"u5"}         → today only
churned  = yesterday - today   # {"u1", "u4"}   → gone today

# --- block 9 ---
yesterday = {"u1", "u2", "u3"}
today_list = ["u2", "u3", "u3"]          # a list, with a repeat
yesterday & today_list                   # TypeError (operator needs two sets)
yesterday.intersection(today_list)       # {"u2", "u3"}  ← method accepts the list
