"""
Memory in AI Systems
Chapter 14: Summary Memory
Section: The Memory Taxonomy

Read this chapter: https://books.vizuara.ai/read/memory-workshop/summary-memory

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
SUMMARY_PROMPT = """You maintain a running summary of a conversation.
Given the CURRENT SUMMARY and the NEW LINES of dialogue, produce an
UPDATED SUMMARY that folds in the new information. Keep durable facts
about the user (name, preferences, goals, decisions). Stay under 100
words. Drop small talk.

CURRENT SUMMARY:
{summary}

NEW LINES:
{new_turns}

UPDATED SUMMARY:"""

def update_summary(summary, new_turns, llm):
    prompt = SUMMARY_PROMPT.format(summary=summary, new_turns=new_turns)
    return llm(prompt).strip()          # the new running summary
