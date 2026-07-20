"""
Claude Certified Architect (CCAF)
Chapter 36: Lab: Design and Break MCP Tools
Section: Tool Design and MCP Integration (Domain 2)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/lab-design-and-break-mcp-tools

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
search_orders = {
    "name": "search_orders",
    "description": (
        "Look up what a customer PURCHASED: order status, shipping, "
        "delivery dates, items in an order. Use for 'where is my package', "
        "'did my order ship'. NOT for complaints or refunds — for those "
        "use search_tickets. Input: customer_id (required), order_id (optional)."
    ),
    "input_schema": { "type": "object",
        "properties": {"customer_id": {"type": "string"},
                       "order_id": {"type": ["string", "null"]}},
        "required": ["customer_id"] }
}

search_tickets = {
    "name": "search_tickets",
    "description": (
        "Look up support TICKETS a customer FILED: complaints, bug reports, "
        "refund requests, and their resolution status. NOT for order or "
        "shipping questions — for those use search_orders. "
        "Input: customer_id (required), status (optional enum)."
    ),
    "input_schema": { "type": "object",
        "properties": {"customer_id": {"type": "string"},
                       "status": {"type": ["string", "null"],
                                  "enum": ["open", "closed", "escalated", None]}},
        "required": ["customer_id"] }
}

# --- block 2 ---
def search_orders_impl(customer_id, order_id=None):
    if not is_authorized(customer_id):
        return mcp_error("permission", retryable=False,
                         msg="Caller not authorized for this customer's orders.")
    try:
        rows = db.query(customer_id, order_id)
    except TimeoutError:
        return mcp_error("transient", retryable=True,
                         msg="Order DB timed out; safe to retry.")
    if not rows:
        return mcp_error("business", retryable=False,
                         msg=f"No orders for customer {customer_id}. "
                             f"Confirm the ID with the user.")
    return {"content": rows}

def mcp_error(category, retryable, msg):
    return {"isError": True, "errorCategory": category,
            "isRetryable": retryable, "content": msg}

# --- block 3 ---
CASES = [
    ("where is my package?",              "search_orders"),
    ("this app keeps crashing",           "search_tickets"),
    ("where is my stuff",                 "search_orders"),   # ambiguous
    ("I never received my refund",        "search_tickets"),  # trap: 'received' -> orders?
    ("cancel my subscription",            None),              # neither -> must NOT force a call
]

for prompt, expected in CASES:
    resp = client.messages.create(model="claude-sonnet-4-5", max_tokens=512,
        tools=[search_orders, search_tickets],
        tool_choice={"type": "auto"},          # let it choose — this is the test
        messages=[{"role": "user", "content": prompt}])
    picked = next((b.name for b in resp.content if b.type == "tool_use"), None)
    print("OK " if picked == expected else "FAIL", repr(prompt), "->", picked)
