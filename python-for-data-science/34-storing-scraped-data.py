"""
Python for Data Science
Chapter 34: Storing Scraped Data
Section: Project: Building a Web Scraper

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/storing-scraped-data

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- carried over from an earlier chapter (see context.py) ---
# `soup` is the parsed page built in chapter 33.
from context import soup

# --- block 1 ---
book = {"title": "The Silent Patient", "price": 12.99, "rating": 4}

# --- block 2 ---
books = []                                   # the growing list of rows

for card in soup.select("article.product"):  # one card = one book
    title  = card.find("h2").get_text(strip=True)
    price  = card.find("span", class_="price").get_text(strip=True)
    rating = card.find("p", class_="rating")["data-stars"]
    books.append({
        "title":  title,
        "price":  price,
        "rating": rating,
    })

# --- block 3 ---
import pandas as pd

df = pd.DataFrame(books)
print(df.head())
print(df.shape)      # (20, 3)  →  20 rows, 3 columns

# --- block 4 ---
df["price"]  = df["price"].str.replace("£", "", regex=False).astype(float)
df["rating"] = df["rating"].astype(int)

# --- block 5 ---
df.to_csv("books.csv", index=False)

# --- block 6 ---
df = pd.read_csv("books.csv")   # exactly the table you saved
