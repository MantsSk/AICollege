---
title: Making Decisions with Conditions
module: Conditions
order: 2
---

# Making Decisions with Conditions

Programs become useful when they react to different situations. That is what **conditions** do.

**After this lesson you will be able to:**

- write `if` / `elif` / `else` branches;
- combine conditions with `and`, `or`, `not`;
- understand why `""`, `0`, and `[]` count as "falsy".

## if / elif / else

```python
score = 78

if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"

print(grade)  # B
```

Indentation matters in Python — the indented block belongs to the condition above it.

## Comparison operators

| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal |
| `>` `<` | greater / less than |
| `>=` `<=` | greater/less or equal |

## Combining conditions

Use `and`, `or`, `not`:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome in!")
```

## Truthiness

Empty things are "falsy": `""`, `0`, `[]`, `None`. Everything else is "truthy".

```python
name = ""
if not name:
    print("Please enter your name")
```

## Check yourself

**1. What grade does `score = 90` get in the example above?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`A` — the condition `score >= 90` is true, so the `elif` and `else` branches are never even checked. Python runs only the first true branch.

</details>

**2. What is the difference between `=` and `==`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`=` assigns a value to a variable; `==` compares two values and returns `True` or `False`. Mixing them up is one of the most common beginner mistakes.

</details>

**3. What does `if not "": print("empty")` output?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`empty` — the empty string `""` is falsy, so `not ""` is `True`.

</details>

## Mini Exercise

Write a program that prints a greeting based on the hour (0–23): "Good morning", "Good afternoon", or "Good evening".

> **Task check:** paste your solution to the mentor and ask: "Check my code: do the boundary values (0, 12, 18, 23) behave correctly? If not, don't give me the answer — give me a hint."

> **Mentor tip:** Ask the AI Mentor to give you 3 practice problems using `if`/`elif`/`else`.

Next: doing things *repeatedly* with loops.
