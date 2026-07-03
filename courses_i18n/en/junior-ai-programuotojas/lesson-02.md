---
title: Your First LLM API Tool
module: API
order: 2
---

# Your First LLM API Tool

In this lesson, you will build a small Python tool that sends text to a model and receives an answer. This is the foundation for chatbots, document analyzers, and agents.

**After this lesson you will be able to:**

- build a command-line tool with an LLM call;
- pass arguments from the terminal into the program;
- handle errors so the user understands what happened.

## Project Idea

Create a command:

```bash
python ask_ai.py "Explain what an API is"
```

It should print the AI answer in the terminal.

## Minimal Code

```python
import sys
from litellm import completion


def ask_ai(question: str) -> str:
    response = completion(
        model="claude-haiku-4-5-20251001",
        messages=[
            {"role": "system", "content": "Answer briefly and clearly."},
            {"role": "user", "content": question},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    question = " ".join(sys.argv[1:])
    if not question:
        raise SystemExit("Please provide a question.")
    print(ask_ai(question))
```

## What you should understand

- Where the API key is stored.
- What `system` and `user` messages mean.
- Why limiting temperature can help.
- How to handle errors when there is no internet or API key.

## Check yourself

**1. What does `" ".join(sys.argv[1:])` do?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

It joins all the words typed after the program name into one question. `sys.argv[0]` is the program's own name, so it is skipped.

</details>

**2. Why is `temperature=0.3` chosen here?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

The tool answers questions rather than doing creative writing — low temperature gives more consistent, less random answers.

</details>

**3. What happens if you run the tool with no internet?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`completion` raises an exception (e.g., a connection error). A good program catches it with `try/except` and shows a human-friendly message instead of a long traceback.

</details>

## Mini Project

Extend the tool:

- add a `--short` mode;
- add a `--lithuanian` mode;
- show user-friendly error messages.

> **Task check:** paste your code to the mentor and ask: "Review my error handling: which situations am I still not catching?"

> **Mentor tip:** Ask "Explain this API call code so I understand every line."

Next: we will build a chatbot with conversation history.
