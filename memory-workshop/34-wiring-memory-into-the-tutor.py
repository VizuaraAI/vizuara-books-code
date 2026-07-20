"""
Memory in AI Systems
Chapter 34: Wiring Memory into the Tutor Loop
Section: Building with Mem0

Read this chapter: https://books.vizuara.ai/read/memory-workshop/wiring-memory-into-the-tutor

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from openai import OpenAI

client = OpenAI()

SYSTEM = "You are a patient AI tutor. Explain simply and check for understanding."

def tutor_reply(user_msg):
    messages = [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": user_msg},
    ]
    resp = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return resp.choices[0].message.content

while True:
    user_msg = input("you › ")
    print("tutor ›", tutor_reply(user_msg))

# --- block 2 ---
from mem0 import Memory

memory = Memory()          # local vector store + LLM extractor, out of the box

def recall(user_msg, user_id):
    hits = memory.search(query=user_msg, user_id=user_id, limit=5)
    return [m["memory"] for m in hits["results"]]

# --- block 3 ---
def build_messages(user_msg, memories):
    memory_block = "\n".join(f"- {m}" for m in memories)
    system = SYSTEM
    if memory_block:
        system += f"\n\nWhat you remember about this learner:\n{memory_block}"
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user_msg},
    ]

# --- block 4 ---
def tutor_turn(user_msg, user_id):
    memories = recall(user_msg, user_id)                 # 1. READ
    messages = build_messages(user_msg, memories)        # 2. AUGMENT
    reply = client.chat.completions.create(              # 3. GENERATE
        model="gpt-4o-mini", messages=messages
    ).choices[0].message.content
    memory.add(                                          # 4. WRITE
        [{"role": "user", "content": user_msg},
         {"role": "assistant", "content": reply}],
        user_id=user_id,
    )
    return reply

# --- block 5 ---
from openai import OpenAI
from mem0 import Memory

client = OpenAI()
memory = Memory()
SYSTEM = "You are a patient AI tutor. Explain simply and check for understanding."

def tutor_turn(user_msg, user_id):
    hits = memory.search(query=user_msg, user_id=user_id, limit=5)   # READ
    mems = [m["memory"] for m in hits["results"]]
    system = SYSTEM + ("\n\nWhat you remember about this learner:\n" +
                       "\n".join(f"- {m}" for m in mems) if mems else "")
    reply = client.chat.completions.create(                          # AUGMENT + GENERATE
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": user_msg}],
    ).choices[0].message.content
    memory.add([{"role": "user", "content": user_msg},               # WRITE
                {"role": "assistant", "content": reply}], user_id=user_id)
    return reply

while True:
    print("tutor ›", tutor_turn(input("you › "), user_id="aditya"))
