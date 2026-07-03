---
title: Classes and Objects
module: Classes
order: 5
---

# Classes and Objects

A **class** is a blueprint. An **object** is a thing built from that blueprint. Classes bundle *data* and *behavior* together.

**After this lesson you will be able to:**

- define a class with `__init__`, attributes, and methods;
- create objects and call their methods;
- recognize classes in AI library code.

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

## Check yourself

**1. What is the difference between a class and an object?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

A class is a blueprint (a description); an object is a concrete instance built from it. From one `Student` class you can create many different students.

</details>

**2. What does `self` mean inside a method?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

The specific object the method was called on. Inside `aiste.complete_lesson()`, `self` is `aiste`, so it is her `completed_lessons` that changes.

</details>

**3. What does `print(aiste.completed_lessons)` output after two `complete_lesson()` calls?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`2` — each call increments the attribute by one, and the state lives inside the object itself.

</details>

## Mini Exercise

Create a class `Course` with attributes `title` and `lessons_done`, plus methods `complete()` (increments the counter) and `progress_text()` (returns e.g. "Python Basics: 3 lessons done"). Create two courses and show their progress.

> **Task check:** paste your class to the mentor and ask: "Review my class: are the attributes and methods sensibly split? What would you add to make it useful in a real app?"

> **Mentor tip:** Ask the AI Mentor to model a `BankAccount` class with deposit and withdraw methods, then explain each line.

Congratulations — you now have the Python foundation needed for the next courses: **Junior AI Developer Projects** and **Build Your Own AI Assistant**.
