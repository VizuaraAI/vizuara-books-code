"""
The Modern Software Developer
Chapter 22: The Risks of Vibe Coding
Section: AI Testing, Security & Secure Vibe Coding

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/why-secure-vibe-coding

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
@app.get("/search")
def search(name: str):
    # find users whose name matches
    query = f"SELECT * FROM users WHERE name = '{name}'"
    rows = db.execute(query).fetchall()
    return {"results": [dict(r) for r in rows]}
