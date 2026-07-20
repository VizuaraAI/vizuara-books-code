"""
The Modern Software Developer
Chapter 25: AI-Assisted Manual Code Review
Section: AI Testing, Security & Secure Vibe Coding

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/manual-code-review-with-agents

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
@app.post("/checkout")
def checkout(body: dict, session: Session):
    item_id  = body["item_id"]
    price    = body["price"]        # <-- trusted from the client
    quantity = body["quantity"]
    total    = price * quantity
    charge_card(session.user, total)
    fulfill(item_id, quantity)
    return {"charged": total}
