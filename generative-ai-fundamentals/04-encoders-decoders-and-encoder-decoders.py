"""
Generative AI Fundamentals
Chapter 4: Encoders, Decoders, and Encoder-Decoders
Section: Foundations of Generative AI

Read this chapter: https://books.vizuara.ai/read/generative-ai-fundamentals/encoders-decoders-and-encoder-decoders

GENERATED FILE - extracted automatically from the book's own text by
tools/build_companion_repo.py. Do not hand-edit; edit the book instead.
Code blocks appear in the order they appear in the chapter, and may
assume names defined in earlier blocks or earlier chapters.
"""

# --- block 1 ---
# Encoder-style usage: text -> vectors -> a task head
tokens   = tokenizer("The film was a masterpiece")
hidden   = bert(tokens)          # (seq_len, 768): one vector per token
cls_vec  = hidden[0]             # the [CLS] summary vector for the whole sequence
label    = classifier_head(cls_vec)   # -> "positive"
