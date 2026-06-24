---
title: Functions
module: Functions
order: 4
---

# Functions

A **function** is a named, reusable block of code. It takes inputs and (optionally) returns an output.

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

> **Mentor tip:** Paste a function you wrote and ask the AI Mentor "How can I make this function cleaner?"

Next: modeling real-world things with **classes**.
