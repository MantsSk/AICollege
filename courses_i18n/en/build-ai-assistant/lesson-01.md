---
title: Calling the LLM API
module: OpenAI API
order: 1
---

# Calling the LLM API

Every AI assistant starts with one skill: sending a message to a model and getting a reply. We'll use **LiteLLM**, which gives one unified interface to OpenAI, Gemini, Claude, and more — exactly what this platform uses.

## Your first call

```python
from litellm import completion

response = completion(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain recursion in one sentence."},
    ],
)

print(response.choices[0].message.content)
```

## Why LiteLLM

Change one string to switch providers — no code rewrite:

```python
model="gemini/gemini-1.5-flash"   # Google
model="claude-haiku-4-5-20251001" # Anthropic
model="gpt-4o-mini"               # OpenAI
```

Set the matching API key as an environment variable (`OPENAI_API_KEY`, `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`).

## The message format

Conversations are a list of messages, each with a `role`:

- `system` — persistent instructions / persona.
- `user` — what the person said.
- `assistant` — what the model previously replied.

## Useful parameters

```python
completion(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.3,   # lower = more focused
    max_tokens=500,    # cap the reply length / cost
)
```

> **Mentor tip:** Ask "What does the system message actually change in the output?"

Next: turning this into an interactive **chat interface**.
