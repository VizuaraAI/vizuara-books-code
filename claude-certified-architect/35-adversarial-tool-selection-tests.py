"""
Claude Certified Architect (CCAF)
Chapter 35: Adversarial Tool-Selection Tests
Section: Tool Design and MCP Integration (Domain 2)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/adversarial-tool-selection-tests

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
cases = [
    {"prompt": "Where's my stuff? email jo@x.com",              "expected": "search_orders"},
    {"prompt": "cancel my last order and give me my money back", "expected": "issue_refund"},
    {"prompt": "did order 8842 ship yet?",                        "expected": "check_order_status"},
    # ... one or two prompts per pairwise seam
]

def routed_tool(prompt):
    resp = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=256,
        tools=TOOLS,
        tool_choice={"type": "any"},          # force a choice; we measure WHICH
        messages=[{"role": "user", "content": prompt}],
    )
    for block in resp.content:
        if block.type == "tool_use":
            return block.name                  # the routing decision
    return None

results = [(c["prompt"], c["expected"], routed_tool(c["prompt"])) for c in cases]
passed  = sum(exp == act for _, exp, act in results)
print(f"routing accuracy: {passed}/{len(results)}")
for p, exp, act in results:
    if exp != act:
        print(f"  MISMATCH  {exp} != {act}   :: {p}")
