"""
AI Context Engineering
Chapter 10: Structured Output and Formatting Contracts
Section: The Instructional Layer

Read this chapter: https://books.vizuara.ai/read/ai-context-engineering/structured-output-and-formatting

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
from pydantic import BaseModel
from typing import Literal

class Order(BaseModel):
    order_id: str
    amount: float
    status: Literal["shipped", "pending", "cancelled"]

# raw is the model's text output
order = Order.model_validate_json(raw)   # raises if the shape is wrong
