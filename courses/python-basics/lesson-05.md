---
title: Classes and Objects
module: Classes
order: 5
---

# Classes and Objects

A **class** is a blueprint. An **object** is a thing built from that blueprint. Classes bundle *data* and *behavior* together.

```python
class Student:
    def __init__(self, name, plan="free"):
        self.name = name
        self.plan = plan
        self.completed_lessons = 0

    def complete_lesson(self):
        self.completed_lessons += 1

    def is_subscribed(self):
        return self.plan == "paid"
```

## Creating objects

```python
aiste = Student("Aiste", plan="paid")
aiste.complete_lesson()
aiste.complete_lesson()

print(aiste.completed_lessons)  # 2
print(aiste.is_subscribed())    # True
```

## The key parts

- `__init__` is the **constructor** — it runs when you create the object.
- `self` refers to *this specific object*.
- **Attributes** (`self.name`) store data.
- **Methods** (`complete_lesson`) are functions that belong to the object.

## Why classes matter for AI work

Most AI libraries are class-based. When you write:

```python
client = OpenAI()
response = client.chat.completions.create(...)
```

…you are creating an object (`client`) and calling its methods. Understanding classes makes every AI SDK feel familiar.

> **Mentor tip:** Ask the AI Mentor to model a `BankAccount` class with deposit and withdraw methods, then explain each line.

Congratulations — you now have the Python foundation needed for the **AI Fundamentals** course.
