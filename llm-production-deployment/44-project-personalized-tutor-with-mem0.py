"""
LLM Production & Deployment
Chapter 44: Project: Personalized Tutor with Mem0
Section: Agents & Memory

Read this chapter: https://books.vizuara.ai/read/llm-production-deployment/project-personalized-tutor-with-mem0

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
import numpy as np
from sentence_transformers import SentenceTransformer

embed = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

class MemoryLayer:
    def __init__(self):
        self.texts, self.vecs = [], []          # parallel lists: fact + its vector

    def write(self, fact: str):
        self.texts.append(fact)
        self.vecs.append(embed.encode(fact, normalize_embeddings=True))

    def retrieve(self, query: str, k: int = 3):
        if not self.texts:
            return []
        q = embed.encode(query, normalize_embeddings=True)
        scores = np.array(self.vecs) @ q          # cosine sim (vectors are unit-norm)
        top = scores.argsort()[::-1][:k]          # k highest, descending
        return [self.texts[i] for i in top]

# --- block 2 ---
def tutor_reply(mem, student_msg, llm):
    facts = mem.retrieve(student_msg, k=3)
    context = "\n".join(f"- {f}" for f in facts) or "(no memories yet)"
    system = f"You are a patient tutor. What you remember about this student:\n{context}"
    return llm.chat(system=system, user=student_msg)   # a stateless LLM call

# --- block 3 ---
from mem0 import Memory

mem = Memory()   # backed by a vector DB + an LLM for extraction

# WRITE: hand it the raw turn; Mem0 extracts + dedupes + updates for you
mem.add(
    [{"role": "user", "content": "I finally understand recursion, but pointers still confuse me"}],
    user_id="student_42",
)

# RETRIEVE: same semantic search, now persistent and per-user
hits = mem.search("what should I review with this student?", user_id="student_42")

# --- block 4 ---
def tutor_turn(mem, llm, user_id, message):
    memories = mem.search(message, user_id=user_id)          # 1. retrieve
    facts = "\n".join(f"- {m['memory']}" for m in memories["results"])
    system = ("You are a patient, personalized tutor. Adapt to what you know:\n"
              f"{facts or '(new student — learn about them)'}")
    reply = llm.chat(system=system, user=message)            # 2. stateless generation
    mem.add([{"role": "user", "content": message},           # 3. write the exchange back
             {"role": "assistant", "content": reply}], user_id=user_id)
    return reply
