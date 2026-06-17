---
title: Making Decisions with Conditions
module: Conditions
order: 2
---

# Making Decisions with Conditions

Programs become useful when they react to different situations. That is what **conditions** do.

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

> **Mentor tip:** Ask the AI Mentor to give you 3 practice problems using `if`/`elif`/`else`.

Next: doing things *repeatedly* with loops.
