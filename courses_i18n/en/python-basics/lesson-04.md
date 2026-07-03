---
title: Functions
module: Functions
order: 4
---

# Functions

A **function** is a named, reusable block of code. It takes inputs and (optionally) returns an output.

**After this lesson you will be able to:**

- define a function with parameters and default values;
- understand what `return` gives back and when;
- call functions with keyword arguments.

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Aiste")
print(message)   # Hello, Aiste!
```

## Parameters and defaults

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25  (exponent defaults to 2)
print(power(2, 10))  # 1024
```

## Returning values

A function without an explicit `return` gives back `None`.

```python
def add(a, b):
    return a + b

total = add(3, 4)   # 7
```

## Why functions matter

They let you:

- **Avoid repetition** — write logic once, call it everywhere.
- **Name ideas** — `calculate_tax()` reads better than 5 lines of math.
- **Test small pieces** independently.

## Keyword arguments

You can pass arguments by name for clarity:

```python
def create_user(email, plan="free"):
    return {"email": email, "plan": plan}

create_user(email="a@b.com", plan="paid")
```

## Check yourself

**1. What does a function without `return` give back?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`None`. The function may print something, but without `return` you cannot assign its result to a variable or use it further.

</details>

**2. What does `print(power(3))` output if `def power(base, exponent=2)`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`9` — with the second argument omitted, the default `exponent=2` is used, so `3 ** 2`.

</details>

**3. Why put logic into functions instead of writing it inline?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

To avoid repetition, to give an idea a readable name, and to test small pieces independently.

</details>

## Mini Exercise

Write a function `bmi(weight_kg, height_m)` that returns the body-mass index, and a function `bmi_text(value)` that returns a label ("low", "normal", "high"). Combine them in one `print`.

> **Task check:** paste your functions to the mentor and ask: "How can I make these functions cleaner? Are the names and parameters well chosen?"

> **Mentor tip:** Paste a function you wrote and ask the AI Mentor "How can I make this function cleaner?"

Next: modeling real-world things with **classes**.
