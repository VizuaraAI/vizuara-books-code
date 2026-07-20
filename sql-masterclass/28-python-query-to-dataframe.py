"""
SQL Masterclass
Chapter 28: From Query to DataFrame: Analyzing in Pandas
Section: SQL with Python and R

Read this chapter: https://books.vizuara.ai/read/sql-masterclass/python-query-to-dataframe

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
rows = cur.fetchall()            # [(1, 'Academy Dinosaur', 0.99), ...]
total = 0.0
for r in rows:
    total += r[2]                # rental_rate is the 3rd column... I think?
avg = total / len(rows)

# --- block 2 ---
import pandas as pd

query = """
    SELECT film_id, title, rental_rate, length
    FROM film
    ORDER BY film_id
    LIMIT 5;
"""
df = pd.read_sql_query(query, conn)

# --- block 3 ---
cur.execute(query)
rows = cur.fetchall()
cols = [d[0] for d in cur.description]     # column names live in cur.description
df = pd.DataFrame(rows, columns=cols)

# --- block 4 ---
df.describe()
#        film_id  rental_rate      length
# count      5.0      5.00000    5.000000
# mean       3.0      2.99000   86.200000
# std        ...      ...        ...
# min        1.0      0.99000   48.000000
# max        5.0      4.99000  130.000000

# --- block 5 ---
df[df['length'] > 100]        # boolean mask, keeps rows where length > 100

# --- block 6 ---
import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost", dbname="dvdrental",
    user="postgres", password="your_password", port=5432,
)

query = """
    SELECT rating, ROUND(AVG(rental_rate), 2) AS avg_rate, COUNT(*) AS n
    FROM film
    GROUP BY rating
    ORDER BY avg_rate DESC;
"""
df = pd.read_sql_query(query, conn)
conn.close()                      # get the rows first, then hang up

print(df.shape)                   # (5, 3) — one row per MPAA rating
print(df)
