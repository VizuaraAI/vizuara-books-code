"""
Python for Data Science
Chapter 8: Control Flow: if / elif / else
Section: Python Fundamentals

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/control-flow-if-else

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
temperature = 38.5

if temperature > 37.5:
    print("Fever detected")
    print("See a doctor")

# --- block 2 ---
age = 15

if age >= 18:
    print("Access granted")
else:
    print("Access denied")

# --- block 3 ---
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(grade)     # B

# --- block 4 ---
names = []

if names:
    print(f"Processing {len(names)} names")
else:
    print("The list is empty, nothing to do")   # this runs

# --- block 5 ---
row = {"age": 40, "income": 55000}

if row["income"] > 50000:
    if row["age"] >= 35:
        print("Segment: established earner")
    else:
        print("Segment: rising earner")
else:
    print("Segment: entry level")
