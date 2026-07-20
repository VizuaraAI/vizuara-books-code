"""
SQL Masterclass
Chapter 27: Connecting Python to PostgreSQL with psycopg2
Section: SQL with Python and R

Read this chapter: https://books.vizuara.ai/read/sql-masterclass/connect-python-psycopg2

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="dvdrental",
    user="postgres",
    password="your_password",
    port=5432,
)

cur = conn.cursor()
cur.execute("SELECT first_name, last_name FROM actor LIMIT 5;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()

# --- block 2 ---
# WRONG — never do this
name = user_input
cur.execute("SELECT * FROM actor WHERE last_name = '" + name + "';")

# RIGHT — parameterized: %s is a placeholder, the value is passed separately
cur.execute("SELECT * FROM actor WHERE last_name = %s;", (name,))

# --- block 3 ---
cur.execute(
    "UPDATE actor SET last_name = %s WHERE actor_id = %s;",
    ("GUINESS-SMITH", 1),
)
conn.commit()   # <- without this line, the change vanishes

# --- block 4 ---
import psycopg2

with psycopg2.connect(
    host="localhost", dbname="dvdrental",
    user="postgres", password="your_password", port=5432,
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM film;")
        print(cur.fetchone())        # -> (1000,)
