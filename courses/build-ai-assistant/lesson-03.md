---
title: Adding Memory
module: Memory
order: 3
---

# Adding Memory

By default each API call is stateless — the model forgets everything. **Memory** means feeding past messages back so the conversation has continuity.

## Short-term memory: the message history

Keep a list and append every turn:

```python
history = [{"role": "system", "content": "You are a study tutor."}]

def ask(user_text):
    history.append({"role": "user", "content": user_text})
    reply = completion(model="gpt-4o-mini", messages=history)\
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

> **Mentor tip:** Ask "When should I summarize history instead of just truncating it?"

Next: grounding answers in your own documents — a **knowledge base**.
