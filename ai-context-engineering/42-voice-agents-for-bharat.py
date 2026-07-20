"""
AI Context Engineering
Chapter 42: Building Conversational Voice Agents for Bharat
Section: Capstone Builds

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/voice-agents-for-bharat

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
SYSTEM = """You are a helpful voice assistant for Indian government schemes.
Speak the way people speak on a phone call:
- One or two short sentences per turn. Never lists or bullet points.
- Match the caller's language and their Hindi/English mix. Do not correct it.
- State a fact ONLY if it appears in the <context> block below. If it is not
  there, say you will check, and ask a clarifying question instead of guessing.
- Before any irreversible step (submitting a form), read back the details and
  wait for a yes.
"""
