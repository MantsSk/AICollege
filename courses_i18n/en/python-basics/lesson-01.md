---
title: Variables and Types
module: Variables
order: 1
---

# Variables and Types

A **variable** is a name that points to a value. You create one with the `=` sign.

**After this lesson you will be able to:**

- create variables and tell the four core types apart;
- check a value's type with `type()`;
- format text with f-strings.

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

## Check yourself

**1. What type is the value `19.99`? And `"19.99"`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`19.99` is a `float` (decimal number), while `"19.99"` is a `str` (text) because of the quotes. You cannot do math with text until you convert it to a number.

</details>

**2. What does `print(f"{name} is {age}")` output if `name = "Tomas"` and `age = 30`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`Tomas is 30` — the f-string substitutes variable values into the curly braces.

</details>

**3. Why doesn't Python require you to declare a variable's type?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Python determines the type automatically from the assigned value. The type belongs to the value, not the variable name — the same name can later point to a value of another type.

</details>

## Mini Exercise

Create variables for your name and your goal, then print a sentence:

```python
my_name = "..."
my_goal = "learn AI"
print(f"Hi, I am {my_name} and I want to {my_goal}.")
```

> **Task check:** paste your code to the mentor and ask: "Check my code and give me one extra variables exercise that is slightly harder."

> **Mentor tip:** Ask "Why does Python not need me to declare types?" and see how it explains it.

In the next lesson we make our programs *make decisions*.
