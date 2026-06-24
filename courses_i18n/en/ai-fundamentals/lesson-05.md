---
title: AI Agents
module: AI Agents
order: 5
---

# AI Agents

An **agent** is an LLM that can *decide* and *act* — not just answer. You give it a goal and a set of **tools**, and it loops: think → choose a tool → observe the result → repeat, until the goal is done.

## Chatbot vs Agent

| | Chatbot | Agent |
|--|---------|-------|
| Output | text reply | text **and actions** |
| Tools | none | search, code, APIs, DB |
| Steps | one turn | many, autonomously |

## Tools (function calling)

You describe functions to the model; it picks which to call and with what arguments.

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]
```

The model replies "call `get_weather(city='Vilnius')`", your code runs it, and you feed the result back.

## The agent loop

```text
goal -> LLM thinks -> calls tool -> gets result
     -> LLM thinks again -> ... -> final answer
```

## Where agents shine — and where they don't

✅ Multi-step research, coding tasks, workflow automation.
⚠️ Add **guardrails**: step limits, allowed tools, human approval for risky actions. Unbounded agents can loop or take wrong actions.

## What you've learned

You now understand the full modern AI stack: models, prompting, embeddings, RAG, and agents. In the next course, **Build Your Own AI Assistant**, you'll combine all of it into a real product.

> **Mentor tip:** Ask "What is the simplest possible agent I could build as a first project?"
