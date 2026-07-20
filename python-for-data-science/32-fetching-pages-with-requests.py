"""
Python for Data Science
Chapter 32: Fetching Pages with requests
Section: Project: Building a Web Scraper

Read this chapter: https://books.vizuara.ai/read/python-for-data-science/fetching-pages-with-requests

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import requests

url = "https://example.com"
resp = requests.get(url)      # send an HTTP GET request
print(resp.status_code)       # -> 200
html = resp.text              # the raw HTML, as a string

# --- block 2 ---
resp = requests.get(url)

if resp.status_code == 200:
    html = resp.text          # safe: this is the real page
    # ... parse it in the next chapter ...
else:
    print(f"Skipping {url}: got {resp.status_code}")

# --- block 3 ---
headers = {"User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0)"}
resp = requests.get(url, headers=headers, timeout=10)

# --- stubs added to make this file runnable ---
# Block 4 is the polite-crawl loop. The chapter shows the loop but not the
# list it walks or the accumulator it fills.
urls = []   # TODO: the pages you want to fetch - see
            # https://books.vizuara.ai/read/python-for-data-science/fetching-pages-with-requests
pages = []  # TODO: collects the HTML of each page that came back 200

# --- block 4 ---
import time

for url in urls:
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code == 200:
        pages.append(resp.text)
    time.sleep(1)             # one polite second between requests
