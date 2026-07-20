"""
Python for Data Science
Chapter 7: Strings and Formatting
Section: Python Fundamentals

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/strings-and-formatting

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
word = "Python"
print(word[0])   # P
print(word[1])   # y
print(word[5])   # n

# --- block 2 ---
word = "Python"
print(word[0:3])   # Pyt
print(word[2:5])   # tho

# --- block 3 ---
print(word[:3])    # Pyt   — from the start up to (not including) index 3
print(word[3:])    # hon   — from index 3 to the end
print(word[:])     # Python — a full copy

# --- block 4 ---
raw = "  Ada Lovelace  "

print(raw.strip())            # "Ada Lovelace"  — trims whitespace off both ends
print(raw.strip().lower())    # "ada lovelace"  — then lowercases
print(raw.strip().upper())    # "ADA LOVELACE"
print("data,science,python".split(","))   # ['data', 'science', 'python']
print("Ada Lovelace".replace("Ada", "Grace"))  # "Grace Lovelace"

# --- block 5 ---
name = "Ada"
score = 92
print("Student " + name + " scored " + str(score) + " points.")

# --- block 6 ---
name = "Ada"
score = 92
print(f"Student {name} scored {score} points.")

# --- block 7 ---
price = 19.5
qty = 3
print(f"Total: {price * qty} for {qty} items")   # Total: 58.5 for 3 items
print(f"Hi {name.upper()}!")                       # Hi ADA!

# --- block 8 ---
avg = 91.66666666
print(f"Average: {avg:.2f}")   # Average: 91.67

# --- block 9 ---
row = "  ada lovelace ,  92  , 1815 "

parts = row.split(",")                 # ['  ada lovelace ', '  92  ', ' 1815 ']
name  = parts[0].strip().title()       # 'Ada Lovelace'
score = int(parts[1].strip())          # 92  (a real integer now)
year  = parts[2].strip()               # '1815'

print(f"{name} scored {score} in {year}.")
# Ada Lovelace scored 92 in 1815.
