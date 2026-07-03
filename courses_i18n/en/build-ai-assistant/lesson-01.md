---
title: Calling the LLM API
module: LLM API
order: 1
---

# Calling the LLM API

Every AI assistant starts with one skill: sending a message to a model and getting a reply. We'll use **LiteLLM**, which gives one unified interface to OpenAI, Gemini, Claude, and more — exactly what this platform uses.

**After this lesson you will be able to:**

- call an LLM from Python and print the reply;
- explain the three message roles: `system`, `user`, `assistant`;
- steer the reply with `temperature` and `max_tokens`.

## Your first call

```python
from litellm import completion

response = completion(
    model="claude-haiku-4-5-20251001",
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
    model="claude-haiku-4-5-20251001",
    messages=messages,
    temperature=0.3,   # lower = more focused
    max_tokens=500,    # cap the reply length / cost
)
```

## Check yourself

**1. How do the `system` and `user` roles differ?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`system` holds persistent instructions and the assistant's persona, set by the developer. `user` is the person's actual message. The system message shapes the whole conversation; the user message is one turn.

</details>

**2. What is `max_tokens` for?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

It caps the reply length, and therefore the cost and latency. Too low a cap will cut the answer mid-sentence.

</details>

**3. What do you change in the code to use another provider's model via LiteLLM?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Only the `model` parameter (plus having that provider's API key in an environment variable). Everything else — message format, response structure — stays the same.

</details>

## Mini Exercise

Write a script that asks the same question three times with `temperature=0` and three times with `temperature=1`, printing all six answers. Compare how they differ.

> **Task check:** paste your observations to the mentor and ask: "Did I understand temperature correctly? When would I pick 0 and when 1?"

> **Mentor tip:** Ask "What does the system message actually change in the output?"

Next: turning this into an interactive **chat interface**.
