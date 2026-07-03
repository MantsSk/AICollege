---
title: Setup: Environment, API Key, and Your First API Error
module: Setup
order: 0
---

# Setup: Environment, API Key, and Your First API Error

Every project in this course uses an LLM API, so first we set up the tools: a virtual environment, the library, and a key. This is where most beginners get stuck — not on agents, but on `AuthenticationError`.

**After this lesson you will be able to:**

- prepare a Python environment with LiteLLM;
- obtain and safely set an API key;
- recognize the three most common API errors and know what they mean.

## 1. The environment

```bash
mkdir junior-ai && cd junior-ai
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install litellm
```

## 2. The API key

Sign up with your chosen provider (Anthropic, OpenAI, or Google) and create a key. Set it as an environment variable:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # macOS/Linux
# Windows PowerShell: $env:ANTHROPIC_API_KEY="sk-ant-..."
```

The key must never appear in code: code travels to GitHub, keys only travel to environment variables.

## 3. Your first call

File `test_api.py`:

```python
from litellm import completion

response = completion(
    model="claude-haiku-4-5-20251001",
    messages=[{"role": "user", "content": "Say hello in one line."}],
)
print(response.choices[0].message.content)
```

If you saw a greeting — your environment is ready.

## 4. Three errors you will definitely meet

**`AuthenticationError`** — the key is missing or wrong. Check `echo $ANTHROPIC_API_KEY` and whether this is a new terminal window (variables only live in the window where you set them).

**`RateLimitError`** — too many requests in a short time, or your credits ran out. Wait, or check your account on the provider's site.

**`ModuleNotFoundError: litellm`** — the virtual environment is not active. Check whether your prompt shows `(.venv)`.

## Check yourself

**1. Why does the key live in an environment variable rather than in `test_api.py`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Files travel to GitHub, chats, and screenshots. A leaked key lets strangers spend on your account, so it lives only in the environment.

</details>

**2. What do you check first when you see `AuthenticationError`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Whether the key is set in this terminal window (`echo $ANTHROPIC_API_KEY`) and whether it was copied in full, without spaces.

</details>

**3. What does `ModuleNotFoundError: litellm` mean if you already ran `pip install`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Most likely you installed into one environment and are running from another — the virtual environment is not active. Activate `.venv` and try again.

</details>

## Mini Exercise

Run `test_api.py` successfully. Then break the key on purpose (change one letter), run again, and read the error. Restore the correct key.

> **Task check:** copy the error text to the mentor and ask: "How do I tell from this error whether the problem is the key, the network, or the code?"

> **Mentor tip:** Ask "What is the difference between an API key, a token, and a password? How do I store each?"

Next: how to use AI while learning to code — a workflow that does not create dependency.
