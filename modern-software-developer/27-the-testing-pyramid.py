"""
The Modern Software Developer
Chapter 27: The Testing Pyramid
Section: AI Testing, Security & Secure Vibe Coding

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/the-testing-pyramid

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
def order_total(prices, discount_pct, tax_pct):
    subtotal = sum(prices)
    discounted = subtotal * (1 - discount_pct / 100)
    return round(discounted * (1 + tax_pct / 100), 2)

# --- block 2 ---
def test_order_total_basic():
    assert order_total([100.0], 0, 0) == 100.0

def test_order_total_with_discount_and_tax():
    # 100 - 10% = 90, then +8% tax = 97.20
    assert order_total([100.0], 10, 8) == 97.20

def test_order_total_empty_cart():
    assert order_total([], 10, 8) == 0.0

# --- block 3 ---
def test_checkout_persists_order(test_db):
    save_order(test_db, prices=[100.0], discount_pct=10, tax_pct=8)
    row = test_db.query("SELECT total FROM orders").fetchone()
    assert row["total"] == 97.20

# --- block 4 ---
def test_checkout_flow(page):
    page.goto("http://localhost:8000")
    page.click("text=Add sample item")
    page.click("text=Checkout")
    assert page.locator("#total").inner_text() == "$97.20"
