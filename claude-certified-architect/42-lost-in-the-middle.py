"""
Claude Certified Architect (CCAF)
Chapter 42: Lost in the Middle
Section: Context Engineering and Reliability (Domain 5)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/lost-in-the-middle

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
prompt = f"""{system_instructions}

<case_facts>
- Plan type: enterprise
- Enterprise refund window: 30 days   # the load-bearing fact, pinned at the top
</case_facts>

{top_3_ranked_documents}   # only the relevant ones, best chunk LAST

REMINDER: answer using the enterprise policy in <case_facts>, not the consumer default.

User question: {user_question}
"""
