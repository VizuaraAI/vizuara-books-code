"""
The Modern Software Developer
Chapter 6: The Anatomy of a Coding Agent
Section: Coding Agents & Claude Code

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/anatomy-of-a-coding-agent

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
{
  "name": "run_shell",
  "description": "Run a shell command in the project directory and return its output.",
  "parameters": {
    "command": {"type": "string", "description": "e.g. 'pytest test_auth.py'"}
  }
}

# --- block 2 (DOES NOT COMPILE - COMMENTED OUT) ---
# Tagged python in the book, but it is not compilable Python here:
# either prose/pseudo-code, or a fragment shown out of its context
# (e.g. a bare `return`). Kept verbatim; the generator does not
# guess at what the missing context was.
# context = [user_request, CLAUDE_md]        # the room's starting contents
# while True:
#     reply = model(context)                 # 1. model reasons over everything so far
#     if reply.wants_tool:                    # 2. did it ask to act?
#         result = run_tool(reply.tool_call)  # 3. the harness actually acts
#         context.append(reply)               # 4. remember what it asked
#         context.append(result)              #    ...and what came back
#     else:
#         return reply                        # 5. no tool wanted → it's finished
