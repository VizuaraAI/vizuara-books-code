"""
Python for Data Science
Chapter 35: Building the Full Scraper
Section: Project: Building a Web Scraper

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/building-the-full-scraper

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import requests

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; VizuaraScraper/1.0)"}

def fetch_page(url):
    resp = requests.get(url, headers=HEADERS, timeout=10)
    if resp.status_code != 200:
        print(f"Skipping {url}: got {resp.status_code}")
        return None
    return resp.text

# --- block 2 ---
from bs4 import BeautifulSoup

def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    books = soup.find_all("li", class_="book")
    rows = []
    for book in books:
        title, price = book.text.split(" — ")
        rows.append({"title": title.strip(), "price": price.strip()})
    return rows

# --- block 3 ---
import pandas as pd

def to_dataframe(rows):
    return pd.DataFrame(rows)

def save_csv(df, path):
    df.to_csv(path, index=False)
    print(f"Wrote {len(df)} rows to {path}")

# --- block 4 ---
def main():
    url = "https://example.com/books"
    html = fetch_page(url)
    if html is None:
        return                       # fetch failed; stop cleanly
    rows = parse_books(html)
    print(f"Parsed {len(rows)} books")
    df = to_dataframe(rows)
    save_csv(df, "books.csv")

if __name__ == "__main__":
    main()

# --- block 5 ---
import time

def main():
    urls = [
        "https://example.com/books?page=1",
        "https://example.com/books?page=2",
        "https://example.com/books?page=3",
    ]
    all_rows = []
    for url in urls:
        html = fetch_page(url)
        if html is None:
            continue                 # skip this page, keep going
        all_rows.extend(parse_books(html))
        time.sleep(1)                # one polite second between pages
    df = to_dataframe(all_rows)
    save_csv(df, "books.csv")

# --- block 6 ---
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; VizuaraScraper/1.0)"}

def fetch_page(url):
    resp = requests.get(url, headers=HEADERS, timeout=10)
    if resp.status_code != 200:
        print(f"Skipping {url}: got {resp.status_code}")
        return None
    return resp.text

def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for book in soup.find_all("li", class_="book"):
        title, price = book.text.split(" — ")
        rows.append({"title": title.strip(), "price": price.strip()})
    return rows

def scrape(urls, out_path="books.csv"):
    all_rows = []
    for url in urls:
        html = fetch_page(url)
        if html is None:
            continue
        all_rows.extend(parse_books(html))
        time.sleep(1)
    df = pd.DataFrame(all_rows)
    df.to_csv(out_path, index=False)
    print(f"Wrote {len(df)} rows to {out_path}")
    return df

if __name__ == "__main__":
    scrape(["https://example.com/books"])
