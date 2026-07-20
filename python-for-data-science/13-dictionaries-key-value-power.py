"""
Python for Data Science
Chapter 13: Dictionaries: Key-Value Power
Section: Data Structures in Python

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/dictionaries-key-value-power

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
contacts = [
    ("Ada", "555-0100"),
    ("Grace", "555-0199"),
    ("Alan", "555-0142"),
]

# --- block 2 ---
phone = {"Ada": "555-0100", "Grace": "555-0199", "Alan": "555-0142"}

# --- block 3 ---
phone["Grace"]     # -> '555-0199'

# --- block 4 ---
student = {"name": "Grace", "age": 21, "grades": [88, 92, 79]}

student["name"]           # read   -> 'Grace'
student["age"] = 22       # update in place
student["city"] = "London"  # add a brand-new key

# --- block 5 ---
"phone" in student        # membership test -> False (fast, average O(1))
student.get("phone")      # -> None instead of raising KeyError
student.get("phone", "n/a")  # -> 'n/a', a default you choose

# --- block 6 ---
for key, value in student.items():
    print(f"{key}: {value}")
# name: Grace
# age: 22
# grades: [88, 92, 79]

# --- block 7 ---
counts = {}
for letter in "banana":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)   # {'b': 1, 'a': 3, 'n': 2}

# --- block 8 ---
records = [("Ada", "London"), ("Grace", "London"), ("Alan", "Manchester")]

by_city = {}
for name, city in records:
    by_city.setdefault(city, []).append(name)

print(by_city)   # {'London': ['Ada', 'Grace'], 'Manchester': ['Alan']}
