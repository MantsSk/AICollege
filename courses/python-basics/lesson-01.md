---
title: Variables and Types
module: Variables
order: 1
---

# Variables and Types

A **variable** is a name that points to a value. You create one with the `=` sign.

```python
name = "Aiste"
age = 28
price = 19.99
is_subscribed = True
```

Python figures out the *type* automatically — you never declare it.

## The core types

| Type | Example | Meaning |
|------|---------|---------|
| `str` | `"hello"` | text |
| `int` | `42` | whole number |
| `float` | `3.14` | decimal number |
| `bool` | `True` / `False` | yes/no value |

Check a type with `type()`:

```python
print(type("hello"))   # <class 'str'>
print(type(42))        # <class 'int'>
```

## Working with text

Strings can be combined and formatted. **f-strings** are the modern way:

```python
name = "Aiste"
lessons = 12
print(f"{name} completed {lessons} lessons.")
# Aiste completed 12 lessons.
```

## A small exercise

Create variables for your name and your goal, then print a sentence:

```python
my_name = "..."
my_goal = "learn AI"
print(f"Hi, I am {my_name} and I want to {my_goal}.")
```

> **Try it with the AI Mentor:** Ask "Why does Python not need me to declare types?" and see how it explains it.

In the next lesson we make our programs *make decisions*.
