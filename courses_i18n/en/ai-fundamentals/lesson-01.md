---
title: What Are Large Language Models?
module: LLMs
order: 1
---

# What Are Large Language Models?

A **Large Language Model (LLM)** is a program trained to predict the next piece of text. That sounds simple, but at scale it produces something remarkable: the ability to write, reason, summarize, translate, and code.

## How they work, intuitively

1. Text is broken into **tokens** (roughly word-pieces).
2. The model has read enormous amounts of text and learned statistical patterns.
3. Given some tokens, it predicts the most likely next token — one at a time.
4. Repeating this produces fluent paragraphs.

```text
Input:  "The capital of Lithuania is"
Output: " Vilnius."   ← highest-probability continuation
```

## Key terms you will hear

- **Token** — a chunk of text. ~4 characters in English. Pricing is per token.
- **Context window** — how much text the model can "see" at once (e.g. 128k tokens).
- **Temperature** — randomness. `0` = focused/deterministic, `1`+ = creative.
- **Parameters** — the learned weights. More is not always better.

## What they are good and bad at

✅ Drafting, explaining, transforming, coding, brainstorming.
⚠️ Not a database — they can **hallucinate** confident but wrong facts.
⚠️ No live knowledge unless you give it (we fix this later with **RAG**).

## Why this matters

Every tool you will build in this platform — the AI Mentor included — is an LLM with good instructions and the right context. Understanding the model removes the magic and replaces it with control.

> **Mentor tip:** Ask "Explain tokens and context windows using a simple analogy."

Next: how to actually *talk* to these models — **prompt engineering**.
