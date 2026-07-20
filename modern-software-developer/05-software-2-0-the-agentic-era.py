"""
The Modern Software Developer
Chapter 5: Software 2.0: The Agentic Era
Section: The New Era of Software Development

Read this chapter: https://books.vizuara.ai/read/modern-software-developer/software-2-0-the-agentic-era

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
context = [user_goal]
while not done:
    action = model(context)          # model decides the next step
    if action.is_tool_call:
        result = run_tool(action)    # e.g. run the tests, read a file
        context.append(result)       # feed the result back in
    else:
        done = True                  # model says the task is finished
