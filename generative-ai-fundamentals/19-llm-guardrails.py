"""
Generative AI Fundamentals
Chapter 19: LLM Guardrails: Controlling Output
Section: Prompt Engineering

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/llm-guardrails

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
tools = [{
  "type": "function",
  "function": {
    "name": "log_ticket",
    "parameters": {
      "type": "object",
      "properties": {
        "category": {"type": "string", "enum": ["billing", "technical", "account"]},
        "urgency":  {"type": "integer", "minimum": 1, "maximum": 5}
      },
      "required": ["category", "urgency"]
    }
  }
}]

# --- block 2 ---
from pydantic import BaseModel, ValidationError, conint
from typing import Literal

class Ticket(BaseModel):
    category: Literal["billing", "technical", "account"]
    urgency: conint(ge=1, le=5)

def parse_ticket(raw: str) -> Ticket | None:
    try:
        return Ticket.model_validate_json(raw)   # parses JSON AND checks types/ranges
    except ValidationError as e:
        return None   # caller decides: retry, or send back e as a correction
