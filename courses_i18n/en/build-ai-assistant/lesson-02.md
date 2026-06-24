---
title: Building a Chat Interface
module: Chat Interface
order: 2
---

# Building a Chat Interface

Now we wrap the API in a web interface — exactly the pattern the AI Mentor in this platform uses: **FastAPI + HTMX**, no heavy JavaScript framework.

## The idea

- A form posts the user's message to the server.
- The server calls the LLM and returns an **HTML fragment** (the new messages).
- HTMX swaps that fragment into the page. The page never fully reloads.

## The endpoint (FastAPI)

```python
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from litellm import completion

app = FastAPI()

@app.post("/chat", response_class=HTMLResponse)
def chat(message: str = Form(...)):
    reply = completion(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
    ).choices[0].message.content

    return f"""
      <div class="msg user">{message}</div>
      <div class="msg assistant">{reply}</div>
    """
```

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

> **Mentor tip:** Ask "How does hx-swap='beforeend' differ from the default swap?"

Next: making the assistant *remember* the conversation — **memory**.
