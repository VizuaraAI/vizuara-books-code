"""
The Modern Software Developer
Chapter 19: The Dev Skill and Test-Driven Development
Section: PRD-Driven Agentic Engineering

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/the-dev-skill-and-tdd

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# test_split.py
from billing import split_bill

def test_even_split_sums_to_total():
    shares = split_bill(100.00, 3)
    assert shares == [33.34, 33.33, 33.33]   # leftover paisa goes to payer #1
    assert round(sum(shares), 2) == 100.00   # not a paisa is lost

def test_clean_division():
    assert split_bill(10.00, 2) == [5.00, 5.00]

# --- block 2 ---
# billing.py
def split_bill(total, people):
    cents = round(total * 100)            # work in the smallest unit — integers
    base, leftover = divmod(cents, people)
    shares = [base + (1 if i < leftover else 0) for i in range(people)]
    return [c / 100 for c in shares]      # back to rupees
