---
title: Setup: Python, Your First File, and Your First Error
module: Setup
order: 0
---

# Setup: Python, Your First File, and Your First Error

Before learning variables, you need one thing most courses skip: a working environment and the courage to read an error message. This lesson is about exactly that. It is less exciting than the others, but without it you will get stuck on the very first evening.

**After this lesson you will be able to:**

- check whether Python works on your computer;
- create and run your first `.py` file;
- read an error message and know where to start fixing it.

## 1. Is Python already installed?

Open a terminal (macOS: the "Terminal" app; Windows: "PowerShell") and type:

```bash
python3 --version
```

If you see `Python 3.10` or newer, you are set. If the command is not found, download Python from [python.org/downloads](https://www.python.org/downloads/) — and on Windows, make sure to tick **Add Python to PATH** during installation. That checkbox is the single most common beginner obstacle.

## 2. Your first file

Create a folder for this course and inside it a file called `hello.py` with a single line:

```python
print("It works!")
```

Run it in the terminal:

```bash
python3 hello.py
```

If `It works!` appeared on screen — you just wrote and ran a program. Seriously, that is the whole essence of programming: a file, a command, a result.

## 3. Your first error (on purpose)

Now break the program. Change `print` to `printt` and run it again:

```text
Traceback (most recent call last):
  File "hello.py", line 1, in <module>
    printt("It works!")
NameError: name 'printt' is not defined. Did you mean: 'print'?
```

Learn to read this message from the bottom up:

- the **last line** says *what* happened (`NameError` — an unknown name) and often even suggests the fix;
- the **lines above** show *where* it happened (the file and line number).

An error message is not a punishment — it is an instruction. Programmers see dozens of them every day.

## Check yourself

**1. What should you do if `python3 --version` says "command not found"?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Install Python from python.org, and on Windows tick "Add Python to PATH" during installation. Then open a new terminal window and try again.

</details>

**2. From which end should you read a long error message?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

From the bottom: the last line tells you the error type and cause, and the lines above show the file and line where it happened.

</details>

**3. What is the difference between writing a file and running it?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

A file is just text. It becomes a program when you run `python3 filename.py` in the terminal and Python executes the commands inside it.

</details>

## Mini Exercise

Create a file `about_me.py` that prints three lines: your name, why you are learning to program, and one thing you want to build. Then break it on purpose, run it, and read the message.

> **Task check:** copy the error message to the mentor and ask: "Explain this error message line by line: what happened, where, and why?"

> **Mentor tip:** Ask "What are the 3 most common mistakes beginners make in their first Python week, and how do I recognize them?"

Next: variables and types — the first real building blocks of programming.
