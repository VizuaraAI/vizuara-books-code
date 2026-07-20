"""
The Modern Software Developer
Chapter 24: Static & Dependency Scanning
Section: AI Testing, Security & Secure Vibe Coding

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/static-and-dependency-scans

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# app.py
from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/user")
def get_user():
    name = request.args.get("name")
    conn = sqlite3.connect("app.db")
    # BUG: user input glued straight into SQL
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return str(conn.execute(query).fetchall())

# --- block 2 ---
    query = "SELECT * FROM users WHERE name = ?"
    return str(conn.execute(query, (name,)).fetchall())
