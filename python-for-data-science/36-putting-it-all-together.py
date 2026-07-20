"""
Python for Data Science
Chapter 36: Putting It All Together
Section: Wrap-Up and Next Steps

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/putting-it-all-together

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://books.toscrape.com/")   # returns an HTTP response
soup = BeautifulSoup(resp.text, "html.parser")        # parse the HTML text

# check we actually got the page before touching it
if resp.status_code != 200:
    raise SystemExit(f"fetch failed: {resp.status_code}")

# --- block 2 ---
books = []
for card in soup.select("article.product_pod"):
    title = card.h3.a["title"]                 # a string
    price = float(card.select_one(".price_color").text[1:])  # strip "£", make it a float
    books.append({"title": title, "price": price})

# books is now:
# [{"title": "A Light in the Attic", "price": 51.77},
#  {"title": "Tipping the Velvet",   "price": 53.74},
#  {"title": "Soumission",           "price": 50.10}]

# --- block 3 ---
import pandas as pd

df = pd.DataFrame(books)          # list of dicts -> a 3-row, 2-column table
print(df.shape)                   # (3, 2)
print(df["price"].mean())         # 51.87  (a vectorized average)
expensive = df[df["price"] > 51]  # boolean filter -> 2 rows

# --- block 4 ---
import matplotlib.pyplot as plt

plt.bar(df["title"], df["price"])
plt.ylabel("Price (£)")
plt.title("Book prices")
plt.show()
