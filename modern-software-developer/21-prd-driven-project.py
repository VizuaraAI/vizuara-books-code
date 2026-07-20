"""
The Modern Software Developer
Chapter 21: Idea to Product: A Full PRD-Driven Build
Section: PRD-Driven Agentic Engineering

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/prd-driven-project

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def test_shorten_returns_6_char_code(client):
    r = client.post("/shorten", json={"url": "https://vizuara.ai"})
    assert r.status_code == 200
    assert len(r.json()["code"]) == 6      # from acceptance criterion #1

# --- block 2 ---
def test_same_url_returns_same_code(client):
    a = client.post("/shorten", json={"url": "https://vizuara.ai"}).json()["code"]
    b = client.post("/shorten", json={"url": "https://vizuara.ai"}).json()["code"]
    assert a == b       # criterion #4: no duplicate codes for the same URL
