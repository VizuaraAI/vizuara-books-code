"""
LLM Finetuning
Chapter 13: Tokenizing and Formatting the Data
Section: Instruction Finetuning from Scratch

Read this chapter: https://books.vizuara.ai/read/llm-finetuning/tokenizing-and-formatting

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
ids = [2, 7, 4, 3, 9, 4, 5, 11, 8]
#      └──────── prompt ────────┘ └─ response ─┘
#      Instruction:Capitalize.Input:cat Response: CAT

# --- block 2 ---
inputs  = ids[:-1]   # [2, 7, 4, 3, 9, 4, 5, 11]   what the model reads
targets = ids[1:]    # [7, 4, 3, 9, 4, 5, 11, 8]    what it must predict next

# --- block 3 ---
# targets before masking:  [7, 4, 3, 9, 4,  5, 11, 8]
# mask the prompt region → set the first 5 target positions to -100
targets_masked =           [-100, -100, -100, -100, -100,  5, 11, 8]
#                          └──────── ignored by loss ───────┘└ graded ┘

# --- block 4 ---
def encode_example(text, prompt_len, tokenizer, ignore_index=-100):
    ids = tokenizer.encode(text)              # string  -> list[int]
    inputs  = ids[:-1]                         # shift: model reads these
    targets = ids[1:]                          # shift: model predicts these
    # mask every target position that lies in the prompt region:
    targets = [ignore_index if i < prompt_len - 1 else t
               for i, t in enumerate(targets)]
    return inputs, targets                      # later: pad + stack into a batch
