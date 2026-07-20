"""
The Modern Software Developer
Chapter 23: Classes of Software Vulnerabilities
Section: AI Testing, Security & Secure Vibe Coding

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/classes-of-vulnerabilities

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
@app.get("/invoice/{invoice_id}")
def get_invoice(invoice_id: int):
    return db.invoices.find_one({"id": invoice_id})

# --- block 2 ---
query = "SELECT * FROM users WHERE name = '" + username + "'"
db.execute(query)

# --- block 3 ---
OPENAI_API_KEY = "sk-proj-9f3a...real-key-here"
