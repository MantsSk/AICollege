---
title: Adding Memory
module: Memory
order: 3
---

# Adding Memory

By default each API call is stateless — the model forgets everything. **Memory** means feeding past messages back so the conversation has continuity.

**After this lesson you will be able to:**

- accumulate conversation history and send it with every call;
- design message storage in a database;
- manage growing history by truncating or summarizing.

## Short-term memory: the message history

Keep a list and append every turn:

```python
history = [{"role": "system", "content": "You are a study tutor."}]

def ask(user_text):
    history.append({"role": "user", "content": user_text})
    reply = completion(model="claude-haiku-4-5-20251001", messages=history)\
        .choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply
```

Now "and explain it simpler" works, because the model sees what came before.

## Persisting memory in a database

In-memory lists vanish on restart. Store messages in tables — exactly what this platform does:

```text
chat_conversations  (id, user_id, lesson_id)
chat_messages       (id, conversation_id, role, content, created_at)
```

On each request: load the conversation's messages, send them to the LLM, then save the new user + assistant messages.

## Watch the context window

Long histories cost tokens and can overflow the context window. Strategies:

- **Truncate** — keep only the last N messages.
- **Summarize** — replace old turns with a short summary.

```python
recent = history[-10:]   # keep the last 10 turns
```

## Check yourself

**1. Why doesn't "explain it simpler" work without history?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Each API call is stateless: the model only sees what is sent in that call. Without the earlier messages in the list, it does not know what to explain more simply.

</details>

**2. Why store messages in a database instead of a Python list?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

A list lives in the process and vanishes when the server restarts. In a database, conversations persist and can be linked to a user and a lesson.

</details>

**3. What is the difference between truncating and summarizing history?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Truncating drops old messages (simple, but facts are lost). Summarizing replaces them with a short summary — more expensive (an extra LLM call) but keeps the essence.

</details>

## Mini Exercise

Extend your terminal chat so it sends only the last 6 messages — but always keeps the system message. Verify that the start of a long conversation is "forgotten" while the assistant's persona survives.

> **Task check:** paste your code to the mentor and ask: "Did I separate the system message from the truncated history correctly? How would I add a summarization strategy?"

> **Mentor tip:** Ask "When should I summarize history instead of just truncating it?"

Next: grounding answers in your own documents — a **knowledge base**.
