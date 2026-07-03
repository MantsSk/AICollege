---
title: Chatbot With History
module: Chatbot
order: 3
---

# Chatbot With History

A one-time API call answers one question. A chatbot needs history: previous user and assistant messages.

**After this lesson you will be able to:**

- build a terminal chatbot with conversation history;
- explain why history is required for a continuous conversation;
- name strategies for when the history grows too long.

## Message List

```python
messages = [
    {"role": "system", "content": "You are a patient Python mentor."},
    {"role": "user", "content": "What is a function?"},
    {"role": "assistant", "content": "A function is a reusable block of code."},
    {"role": "user", "content": "Give me an example."},
]
```

The model sees the whole list and answers using context.

## Terminal Chatbot

```python
from litellm import completion

messages = [{"role": "system", "content": "Answer as a Python mentor."}]

while True:
    user_text = input("You: ")
    if user_text.lower() in {"exit", "quit"}:
        break

    messages.append({"role": "user", "content": user_text})
    response = completion(model="claude-haiku-4-5-20251001", messages=messages)
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    print("AI:", answer)
```

## Limits

History cannot grow forever. In long conversations, you will need to:

- summarize old history;
- keep only important facts;
- limit the number of messages;
- use a database for a real app.

## Check yourself

**1. Why is `messages.append` called twice per turn?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Both the user's message and the assistant's reply go into history. If you skip the assistant's reply, the model will not see what it said itself on the next turn.

</details>

**2. What would happen if you sent only the latest message each time?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

The conversation would lose continuity: the model would not understand "give me an example" because it would not know what it refers to. Every call without history is a brand-new conversation.

</details>

**3. What are three strategies when history gets too long?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Truncate (keep the last N messages), summarize old messages, or store messages in a database and load only part of them.

</details>

## Mini Project

Create a terminal "Python teacher" chatbot. It should:

- answer simply;
- explain for beginners;
- give small exercises;
- accept a `summary` command that summarizes what the user learned.

> **Task check:** paste your chatbot to the mentor and ask: "Does my `summary` command use the history correctly? How would I make it cheaper in tokens?"

> **Mentor tip:** Ask "How can I save chatbot history to a JSON file?"

Next: we will build a document question-answering tool with the core RAG idea.
