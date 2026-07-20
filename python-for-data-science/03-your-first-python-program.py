"""
Python for Data Science
Chapter 3: Your First Python Program
Section: Getting Started

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/your-first-python-program

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
print("Hello, world!")

# --- block 2 ---
# NOTE: the second line here is a deliberate error demo in the book - it shows
# that dropping the quotes turns text into a name lookup and raises
# NameError: name 'Hello' is not defined. Commented out so this file runs;
# uncomment it to see the error the chapter is describing.
print("Hello")
# print(Hello)

# --- block 3 ---
print("first")
print("second")

# --- block 4 ---
name = "Ada"
print("Hello, " + name)
age = 30 + 6
print(age)

# --- block 5 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# print("line one")
#     print("line two")

# --- block 6 ---
print("3" + "4")
print(3 + 4)
