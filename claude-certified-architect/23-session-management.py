"""
Claude Certified Architect (CCAF)
Chapter 23: Session Management and Stale Context
Section: Agentic Architecture and Orchestration (Domain 1)

Read this chapter: https://books.vizuara.ai/read/claude-certified-architect/session-management

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# One expensive setup run establishes shared context
base = client.sessions.create(prompt="Analyze this 400-page contract")

# Fork it three ways — each child inherits the analysis, then diverges
liability = client.sessions.fork(base.id, prompt="Draft the liability summary")
payment   = client.sessions.fork(base.id, prompt="Draft the payment-terms summary")
risks     = client.sessions.fork(base.id, prompt="List the top 5 risks")
