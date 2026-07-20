"""
Python for Data Science
Chapter 33: Parsing HTML with BeautifulSoup
Section: Project: Building a Web Scraper

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/parsing-html-with-beautifulsoup

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- carried over from an earlier chapter (see context.py) ---
# `resp` is the response fetched in chapter 32.
from context import resp

# --- block 1 ---
from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "html.parser")

# --- block 2 ---
soup.find("h1")                    # <h1>Books</h1>  — the first h1
soup.find_all("li")                # [<li>…Dune…</li>, <li>…Neuromancer…</li>]
soup.find_all("li", class_="book") # same two — filtered by class

# --- block 3 ---
soup.select("li")            # every <li>            (tag)
soup.select(".book")         # every class="book"    (. = class)
soup.select_one("#catalog")  # the id="catalog" node (# = id)
soup.select("ul.book li")    # descendant li inside a ul with class book

# --- block 4 ---
soup.find("h1").text          # "Books"
soup.select_one(".book").text # "Dune — $12"

# --- block 5 ---
link = soup.find("a")
link["href"]        # "/dune"
link.get("href")    # "/dune"  — safer: returns None if missing

# --- block 6 ---
from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "html.parser")

books = soup.find_all("li", class_="book")   # a list of 2 nodes
print(len(books))                            # 2

for book in books:
    title, price = book.text.split(" — ")    # "Dune — $12" → ["Dune", "$12"]
    print(title, price)
# Dune $12
# Neuromancer $9
