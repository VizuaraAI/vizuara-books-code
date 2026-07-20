"""
The Modern Software Developer
Chapter 26: Security Hardening: From v1 to v2
Section: AI Testing, Security & Secure Vibe Coding

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/security-hardening-v1-to-v2

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# v1 — login route (looks fine, is not)
import sqlite3

API_KEY = "sk-proj-8Qd3...redacted"   # OpenAI key, pasted right here

def login(username, password):
    conn = sqlite3.connect("app.db")
    q = f"SELECT * FROM users WHERE name='{username}' AND pw='{password}'"
    row = conn.execute(q).fetchone()
    return row is not None

# --- block 2 ---
# v2 — parameterized query (input can never become SQL)
q = "SELECT * FROM users WHERE name=? AND pw=?"
row = conn.execute(q, (username, password)).fetchone()

# --- block 3 ---
# v2 — secret comes from the environment, never the source
import os
API_KEY = os.environ["OPENAI_API_KEY"]   # set in .env / deployment secrets, git-ignored
