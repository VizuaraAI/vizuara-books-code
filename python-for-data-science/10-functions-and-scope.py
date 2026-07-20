"""
Python for Data Science
Chapter 10: Functions and Scope
Section: Python Fundamentals

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/functions-and-scope

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
c = 100
f = c * 9 / 5 + 32
print(f)          # 212.0

c = 37
f = c * 9 / 5 + 32
print(f)          # 98.6

c = 0
f = c * 9 / 5 + 32
print(f)          # 32.0

# --- block 2 ---
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

# --- block 3 ---
print(celsius_to_fahrenheit(100))   # 212.0
print(celsius_to_fahrenheit(37))    # 98.6
print(celsius_to_fahrenheit(0))     # 32.0

# --- block 4 ---
def greet(name, times):
    return f"Hello {name}! " * times

message = greet("Ada", 3)
print(message)   # Hello Ada! Hello Ada! Hello Ada!

# --- block 5 ---
result = print("hi")   # prints: hi
print(result)          # prints: None

# --- block 6 ---
def greet(name, times=1):
    return f"Hello {name}! " * times

print(greet("Ada"))       # Hello Ada!          (times defaults to 1)
print(greet("Ada", 3))    # Hello Ada! Hello Ada! Hello Ada!

# --- block 7 ---
# DON'T: the list is shared across calls
def add_item(item, basket=[]):
    basket.append(item)
    return basket

# DO: default to None, build a fresh list inside
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

# --- block 8 ---
x = 10                 # global x

def show():
    y = 5              # local y — exists only inside show()
    print(x + y)       # reads global x (10) and local y (5) -> 15

show()                 # prints 15
# NOTE: the next line is a deliberate error demo in the book - it shows that a
# local name does not survive outside its function. Commented out so this file
# runs; uncomment it to see the NameError the chapter is describing.
# print(y)               # NameError: y is not defined out here

# --- block 9 ---
count = 0

def increment():
    count = count + 1   # ERROR — see below
    return count

# --- block 10 ---
def increment(count):
    return count + 1

count = 0
count = increment(count)   # count is now 1
count = increment(count)   # count is now 2

# --- block 11 ---
def average(numbers, default=0.0):
    if not numbers:          # empty list is falsy
        return default
    return sum(numbers) / len(numbers)

print(average([2, 4, 6]))   # 4.0
print(average([]))          # 0.0  (the default kicks in)

# --- block 12 ---
def weekly_avg_fahrenheit(celsius_readings):
    mean_c = average(celsius_readings)          # reuse: one clear value out
    return celsius_to_fahrenheit(mean_c)        # feed it straight into the next

week = [20, 22, 21, 19, 23, 24, 22]
print(weekly_avg_fahrenheit(week))              # about 70.83
