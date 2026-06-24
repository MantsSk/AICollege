---
title: Prompt Engineering
module: Prompt Engineering
order: 2
---

# Prompt Engineering

**Prompt engineering** is the craft of writing instructions that get reliable, high-quality output from an LLM. It is the highest-leverage skill in applied AI.

## The anatomy of a good prompt

1. **Role** — who the model should act as.
2. **Task** — what to do, specifically.
3. **Context** — the material to work from.
4. **Format** — how the answer should look.
5. **Constraints** — what to avoid.

```text
You are a senior Python tutor.        (role)
Explain list comprehensions           (task)
to a complete beginner who knows       (context)
only for-loops.
Use one short example, then a 2-line    (format)
summary. Avoid jargon.                  (constraints)
```

## Techniques that reliably help

- **Be specific.** "Summarize in 3 bullet points" beats "summarize".
- **Show an example** (one-shot / few-shot) when format matters.
- **Ask it to think step by step** for reasoning tasks.
- **Give it an out:** "If you are unsure, say so" reduces hallucination.

## System vs user messages

Most APIs separate a **system** message (persistent instructions / persona) from **user** messages (the actual request). Our AI Mentor uses a system prompt that says *"prefer the course content, explain simply, stay focused on learning."*

## Iterate

Treat prompting like debugging. If the output is wrong, the fix is usually a clearer prompt — not a different model.

> **Mentor tip:** Paste a vague prompt and ask the Mentor to rewrite it using the role/task/context/format structure.

Next: how machines understand *meaning* — **embeddings**.
