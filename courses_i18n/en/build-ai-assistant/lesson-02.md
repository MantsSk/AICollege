---
title: Building a Chat Interface
module: Chat Interface
order: 2
---

# Building a Chat Interface

Now we wrap the API in a web interface — exactly the pattern the AI Mentor in this platform uses: **FastAPI + HTMX**, no heavy JavaScript framework.

**After this lesson you will be able to:**

- build a FastAPI endpoint that returns an HTML fragment;
- connect a form to the server with HTMX, no page reload;
- protect the interface from HTML injection with `html.escape`.

## The idea

- A form posts the user's message to the server.
- The server calls the LLM and returns an **HTML fragment** (the new messages).
- HTMX swaps that fragment into the page. The page never fully reloads.

## The endpoint (FastAPI)

```python
import html

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from litellm import completion

app = FastAPI()

@app.post("/chat", response_class=HTMLResponse)
def chat(message: str = Form(...)):
    reply = completion(
        model="claude-haiku-4-5-20251001",
        messages=[{"role": "user", "content": message}],
    ).choices[0].message.content

    return f"""
      <div class="msg user">{html.escape(message)}</div>
      <div class="msg assistant">{html.escape(reply)}</div>
    """
```

Note the `html.escape`: we are putting user (and model!) text into HTML, so it must be escaped. Without it, someone typing `<script>...</script>` would run code in other users' browsers — an XSS attack.

## The HTMX form

```html
<form hx-post="/chat" hx-target="#log" hx-swap="beforeend"
      hx-on::after-request="this.reset()">
  <input name="message" placeholder="Ask anything...">
  <button>Send</button>
</form>

<div id="log"></div>
```

`hx-post` sends the form, `hx-target` says where to put the response, `hx-swap="beforeend"` appends it to the log.

## Loading states

HTMX adds an `htmx-request` class during the call — show a "thinking…" indicator with CSS, no JS needed.

## Check yourself

**1. What does the server return to the browser in this design?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Not a full page and not JSON — an HTML fragment with the two new messages. HTMX swaps it into the `#log` element without a page reload.

</details>

**2. Why would the app be vulnerable without `html.escape`?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

User text goes straight into HTML. A `<script>` tag would be executed by the browser — an XSS attack. `html.escape` turns special characters into harmless text.

</details>

**3. What does `hx-swap="beforeend"` do?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

It appends the response HTML to the end of the target (instead of replacing its content), so chat messages accumulate one after another.

</details>

## Mini Exercise

Run this chat locally and deliberately type the message `<b>test</b>`. Make sure it renders as text, not bold — that means `html.escape` is doing its job.

> **Task check:** paste your endpoint code to the mentor and ask: "Is my interface safe? What other weaknesses could a chat endpoint like this have?"

> **Mentor tip:** Ask "How does hx-swap='beforeend' differ from the default swap?"

Next: making the assistant *remember* the conversation — **memory**.
