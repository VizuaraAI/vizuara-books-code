"""
Python for Data Science
Chapter 24: Visualizing Data with Matplotlib
Section: The Data Science Toolkit

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/visualizing-data-with-matplotlib

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales  = [120, 135, 128, 160, 185]

plt.plot(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales (units)")
plt.title("Monthly sales")
plt.show()

# --- stubs added to make this file runnable ---
# Block 2 plots two years against the same `months`, but the chapter never
# lists the two series. Supply your own, one value per month.
sales_2024 = None  # TODO: a sales series aligned with `months` - see
                   # https://books.vizuara.ai/read/python-for-data-science/visualizing-data-with-matplotlib
sales_2025 = None  # TODO: same, for the second year

# --- block 2 ---
plt.plot(months, sales_2024, label="2024")
plt.plot(months, sales_2025, label="2025")
plt.legend()
plt.show()

# --- block 3 ---
regions = ["North", "South", "East", "West"]
totals  = [230, 185, 310, 260]

plt.bar(regions, totals)
plt.ylabel("Total sales (units)")
plt.title("Sales by region")
plt.show()

# --- block 4 ---
hours  = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [52, 55, 61, 64, 70, 72, 79, 85]

plt.scatter(hours, scores)
plt.xlabel("Hours studied")
plt.ylabel("Exam score")
plt.title("Study time vs. score")
plt.show()
