---
title: AI-Assisted Junior Developer Workflow
module: Workflow
order: 1
---

# AI-Assisted Junior Developer Workflow

For a junior programmer, AI is a major advantage when used as an explaining partner, not a blind code generator. The goal is to learn faster, understand errors better, and build small projects.

**After this lesson you will be able to:**

- use a six-step workflow with AI;
- ask for code explanations, not just code;
- turn an error message into learning material.

## Good Workflow

1. Define the problem yourself.
2. Ask AI to explain, not only write code.
3. Run the code locally.
4. Read errors and ask for explanations.
5. Write small tests.
6. Put on GitHub only what you understand.

## Code Explanation Prompt

```text
Explain this code to a beginner programmer.
Go line by line.
At the end, write:
- what this code does;
- possible mistakes;
- how to improve it.
```

## Error Prompt

```text
Help me understand this error.
Code:
[paste code]

Error:
[paste error]

Explain the cause simply.
Then suggest the smallest fix.
Do not rewrite the whole project unless needed.
```

## Check yourself

**1. What is the difference between "write me the code" and "explain the code to me"?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

The first gives you a result you may not understand and cannot fix. The second grows your understanding — and code you understand can be changed, tested, and defended in a job interview.

</details>

**2. Why does the error prompt ask for the "smallest fix"?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

So AI does not rewrite the whole project into code you no longer recognize. A small fix shows exactly what was wrong.

</details>

**3. What from this workflow belongs on GitHub?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Only what you understand and can explain. A portfolio's value is not the amount of code but your ability to defend it.

</details>

## Mini Project

Create a simple Python command-line "task helper" that lets you:

- add a task;
- show the task list;
- mark a task as done.

Use AI only for explanations and debugging. Understand each function yourself.

> **Task check:** paste your program to the mentor and ask: "Ask me 3 questions about my code as if you were an interviewer. Don't give the answers — test whether I understand."

> **Mentor tip:** Ask "Help me learn programming with AI without becoming dependent on copying."

Next: we will call an LLM API from Python.
