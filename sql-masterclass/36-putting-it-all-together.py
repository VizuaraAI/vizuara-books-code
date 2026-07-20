"""
SQL Masterclass
Chapter 36: Putting It All Together
Section: Capstone and Interview Prep

Read this chapter: https://books.vizuara.ai/read/sql-masterclass/putting-it-all-together

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(host="localhost", dbname="dvdrental",
                        user="postgres", password="secret", port=5432)

sql = """SELECT c.name, SUM(p.amount) AS revenue
         FROM payment p JOIN category c USING (category_id)
         GROUP BY c.name ORDER BY revenue DESC;"""

df = pd.read_sql_query(sql, conn)   # straight into a DataFrame
df.plot.bar(x="name", y="revenue")
plt.show()
conn.close()
