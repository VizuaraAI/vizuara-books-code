"""
Harness Engineering
Chapter 2: Why 'just call the API' fails
Section: Start Here

Read this chapter: https://books.vizuara.ai/read/harness-engineering/why-just-call-the-api-fails

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import anthropic
client = anthropic.Anthropic()          # reads ANTHROPIC_API_KEY from the env

def ask(request):
    reply = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": request}],
    )
    return reply.content[0].text

# --- block 2 ---
ask("The test test_parser.py::test_dates is failing. Fix it.")
