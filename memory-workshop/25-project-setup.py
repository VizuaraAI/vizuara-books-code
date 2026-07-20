"""
Memory in AI Systems
Chapter 25: Project Setup: A Bare LLM Loop
Section: Coding Memory Layers from Scratch

Read this chapter: https://books.vizuara.ai/read/memory-workshop/project-setup

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- resolved names (added so this file passes a static check) ---
# The names below are used by this chapter but not defined in it.
# Imports point at context.py, which copies the earlier chapter verbatim.
# Stubs are deliberately empty: the book expects YOU to supply them.
user_text_as_message = None  # TODO: the book never defines this - block 3 below shows the fix
# --- end resolved names ---

# --- block 1 ---
from openai import OpenAI
client = OpenAI()

def llm(messages):
    # messages: a list of {"role", "content"} dicts
    # returns: one assistant message (a string)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    return resp.choices[0].message.content

# --- block 2 ---
SYSTEM = {"role": "system", "content": "You are a friendly assistant."}

while True:
    user_text = input("you > ")
    if user_text.strip() == "/quit":
        break
    reply = llm([SYSTEM, user_text_as_message(user_text)])
    print("bot >", reply)

# --- block 3 ---
history = [SYSTEM]

while True:
    user_text = input("you > ")
    if user_text.strip() == "/quit":
        break
    history.append({"role": "user", "content": user_text})
    reply = llm(history)                       # pass the WHOLE history
    history.append({"role": "assistant", "content": reply})
    print("bot >", reply)
