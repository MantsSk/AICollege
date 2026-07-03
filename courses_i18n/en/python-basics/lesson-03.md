---
title: Loops and Repetition
module: Loops
order: 3
---

# Loops and Repetition

Loops let you repeat work without copying code.

**After this lesson you will be able to:**

- iterate over lists with `for` and generate numbers with `range()`;
- use `while`, `break`, and `continue`;
- grow a list in a loop and write the same thing shorter with a list comprehension.

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

## Check yourself

**1. What does `for i in range(3): print(i)` output?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`0`, `1`, `2` — `range(3)` starts at zero and stops at 2 (the end value is excluded).

</details>

**2. When should you pick `while` over `for`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

When you do not know how many repetitions you need — you repeat *while* a condition holds (e.g., until the user types a valid answer). `for` fits when you walk through a known collection or number sequence.

</details>

**3. What is the difference between `break` and `continue`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

`break` stops the whole loop; `continue` skips only the current round and moves to the next one.

</details>

## Mini Exercise

Write a loop over the numbers 1 to 20 that prints only those divisible by 3. Then rewrite it as a list comprehension.

> **Task check:** paste both versions to the mentor and ask: "Does my list comprehension really match the loop? When does a comprehension become too complex and a loop is better?"

> **Mentor tip:** Ask "What is the difference between a for loop and a while loop, with a real example?"

Next: packaging logic into reusable **functions**.
