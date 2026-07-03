---
title: Small Agent With Tools
module: Agents
order: 5
---

# Small Agent With Tools

An agent is an AI program that can use tools. At junior level, start with safe tools: a calculator, file reading, or a task list.

**After this lesson you will be able to:**

- build an agent with two safe tools;
- define what the agent must not do before writing code;
- document the agent's boundaries in a README.

## Project Idea

Create a "study planner" agent that can:

- accept a learning goal;
- create a plan;
- save the plan to a text file;
- read an existing plan.

## Tool Boundaries

At first, do not let the agent:

- delete files;
- send emails;
- make payments;
- execute unknown code.

Agent safety is not an add-on. It is a core feature.

## Simple Tool Function

```python
def save_plan(filename: str, content: str) -> str:
    if not filename.endswith(".txt"):
        return "Only .txt files are allowed."
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Plan saved: {filename}"
```

## Check yourself

**1. How does an agent differ from a chatbot?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

A chatbot only replies with text. An agent takes actions — calls functions, writes files, searches — so its mistakes have real consequences.

</details>

**2. Why does `save_plan` check the file extension?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

It is a safety boundary: the agent can only create `.txt` files and cannot overwrite, say, source code or system files. Boundaries belong in the tool itself, not only in the prompt.

</details>

**3. Why is agent safety "a core feature, not an add-on"?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

The model can make mistakes or be tricked through its input. If the tools allow dangerous actions, a mistake becomes deleted files or sent emails — so boundaries are designed first.

</details>

## Mini Project

Create an agent with two tools:

- `save_plan(filename, content)`;
- `read_plan(filename)`.

Then describe in the README:

- what the agent does;
- its limits;
- which actions you intentionally disallowed.

> **Task check:** paste your README to the mentor and ask: "Do my agent's boundaries actually prevent harm, or are they only declared? What else would you restrict?"

> **Mentor tip:** Ask "What safety boundaries are necessary for a beginner agent?"

Next: we will package the project for a portfolio.
