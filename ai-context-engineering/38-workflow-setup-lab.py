"""
AI Context Engineering
Chapter 38: Workflow Setup Lab
Section: Setting Up the Build Workflow

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/workflow-setup-lab

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# src/todo.py
import json, pathlib

STORE = pathlib.Path("tasks.json")

def _load():
    return json.loads(STORE.read_text()) if STORE.exists() else []

def add_task(text):
    tasks = _load()
    new_id = (max((t["id"] for t in tasks), default=0)) + 1
    tasks.append({"id": new_id, "text": text, "done": False})
    STORE.write_text(json.dumps(tasks))
    return new_id

def list_tasks():
    return _load()
