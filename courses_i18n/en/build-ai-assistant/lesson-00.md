---
title: Setup: Environment, Keys, and Your First Server
module: Setup
order: 0
---

# Setup: Environment, Keys, and Your First Server

In this course we write real code: API calls, a web server, a database. Before starting, let's set up the environment — 15 minutes now will save hours later.

**After this lesson you will be able to:**

- create an isolated Python environment for the project;
- set an API key safely as an environment variable;
- run your first FastAPI server and understand its most common error.

## 1. Project folder and virtual environment

```bash
mkdir ai-assistant && cd ai-assistant
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install litellm fastapi "uvicorn[standard]"
```

The virtual environment (`.venv`) keeps the project's libraries separate from your system. If you see `(.venv)` at the start of your terminal prompt, it is active.

## 2. The API key

Sign up with your chosen provider and get a key. Then set it as an environment variable — **never write the key in code**:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # macOS/Linux
# Windows PowerShell: $env:ANTHROPIC_API_KEY="sk-ant-..."
```

With LiteLLM you switch providers with one line, so any key works: `OPENAI_API_KEY`, `GEMINI_API_KEY`, or `ANTHROPIC_API_KEY`.

## 3. Your first server

Create a file `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "working"}
```

Run it:

```bash
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000` in your browser — you should see `{"status": "working"}`.

## 4. Your first error (on purpose)

Stop the server (`Ctrl+C`) and run `uvicorn app:main --reload` — with the words swapped. You will get:

```text
ERROR: Error loading ASGI app. Could not import module "app".
```

The format is `file_name:variable_name`. This error is the most common first-day FastAPI obstacle, and now you know what it means.

## Check yourself

**1. What is a virtual environment for?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

To isolate the project's libraries: different projects can use different versions, and your system stays clean. An active environment shows as `(.venv)` in the terminal.

</details>

**2. Why does the API key live in an environment variable, not in code?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Code travels to git, screenshots, and AI chats — the key must not travel with it. A leaked key lets others spend on your account.

</details>

**3. What does `uvicorn main:app` mean?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

"In the file `main.py`, find the variable `app` and run it as a server." Swapping the parts produces the `Could not import module` error.

</details>

## Mini Exercise

Add a second endpoint `/about` to the server that returns your name and what you want to build. Reload the browser and make sure both endpoints work.

> **Task check:** paste your `main.py` to the mentor and ask: "Is my FastAPI structure correct? What would I do for an endpoint with a parameter, like /hello/{name}?"

> **Mentor tip:** Ask "What happens when uvicorn runs with --reload, and why shouldn't I use it in production?"

Next: your first LLM API call.
