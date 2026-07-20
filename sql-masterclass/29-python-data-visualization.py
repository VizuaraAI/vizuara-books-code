"""
SQL Masterclass
Chapter 29: Visualizing SQL Data in Python
Section: SQL with Python and R

Read this chapter: https://books.vizuara.ai/read/sql-masterclass/python-data-visualization

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import pandas as pd

sql = """
SELECT c.name AS category, SUM(p.amount) AS revenue
FROM payment p
JOIN rental r      ON p.rental_id      = r.rental_id
JOIN inventory i   ON r.inventory_id   = i.inventory_id
JOIN film_category fc ON i.film_id     = fc.film_id
JOIN category c    ON fc.category_id   = c.category_id
GROUP BY c.name
ORDER BY revenue DESC;
"""
df = pd.read_sql_query(sql, conn)
print(df.head())

# --- block 2 ---
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(df["category"], df["revenue"], color="#4C78A8")
ax.invert_yaxis()                       # highest revenue on top
ax.set_xlabel("Revenue ($)")
ax.set_title("DVD rental revenue by film category")
plt.tight_layout()
plt.savefig("revenue_by_category.png", dpi=150)

# --- block 3 ---
import seaborn as sns

sns.set_theme(style="whitegrid")
ax = sns.barplot(data=df, x="revenue", y="category", color="#4C78A8")
ax.set(xlabel="Revenue ($)", ylabel="", title="Revenue by film category")
plt.tight_layout()

# --- block 4 ---
# df_raw has one row PER payment: columns [category, amount]
sns.barplot(data=df_raw, x="amount", y="category", estimator="mean", errorbar=("ci", 95))

# --- block 5 ---
sql = """
SELECT date_trunc('month', rental_date) AS month, COUNT(*) AS rentals
FROM rental
GROUP BY month
ORDER BY month;
"""
ts = pd.read_sql_query(sql, conn, parse_dates=["month"])
sns.lineplot(data=ts, x="month", y="rentals", marker="o")
