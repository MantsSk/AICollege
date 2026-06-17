---
title: Loops and Repetition
module: Loops
order: 3
---

# Loops and Repetition

Loops let you repeat work without copying code.

## The for loop

Iterate over a collection:

```python
courses = ["Python", "AI Fundamentals", "AI Assistant"]

for course in courses:
    print(f"Studying {course}")
```

`range()` generates numbers:

```python
for i in range(3):
    print(i)   # 0, 1, 2
```

## The while loop

Repeat *while* a condition is true:

```python
attempts = 0
while attempts < 3:
    print("Trying...")
    attempts += 1
```

Be careful: if the condition never becomes false, the loop runs forever.

## Useful tools

`break` stops a loop early, `continue` skips to the next round:

```python
for n in range(10):
    if n == 5:
        break        # stop entirely
    if n % 2 == 0:
        continue     # skip even numbers
    print(n)         # 1, 3
```

## Lists grow with loops

```python
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)  # [1, 4, 9, 16, 25]
```

A shorter version (a *list comprehension*):

```python
squares = [n * n for n in range(1, 6)]
```

> **Mentor tip:** Ask "What is the difference between a for loop and a while loop, with a real example?"

Next: packaging logic into reusable **functions**.
