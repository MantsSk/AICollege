---
title: Adding a Knowledge Base
module: Knowledge Base
order: 4
---

# Adding a Knowledge Base

To make your assistant an expert on *your* material — docs, FAQs, a course — give it a **knowledge base** using the RAG pattern.

**After this lesson you will be able to:**

- turn documents into embeddings and store them;
- retrieve the chunks most relevant to a question by meaning;
- put retrieved context into the prompt and constrain the answer to it.

## Step 1 — Ingest

Split documents into chunks and embed them once:

```python
from litellm import embedding

def embed(texts):
    resp = embedding(model="text-embedding-3-small", input=texts)
    return [d["embedding"] for d in resp["data"]]

chunks = split_into_chunks(my_docs)        # ~300 tokens each
vectors = embed(chunks)
store(chunks, vectors)                      # save to a vector DB
```

## Step 2 — Retrieve

At question time, embed the question and find the closest chunks:

```python
def search(question, top_k=3):
    q = embed([question])[0]
    return nearest_chunks(q, top_k)          # cosine similarity
```

## Step 3 — Answer with context

```python
context = "\n\n".join(search(question))
messages = [
    {"role": "system",
     "content": "Answer using the context. If it's not there, say so."},
    {"role": "user",
     "content": f"Context:\n{context}\n\nQuestion: {question}"},
]
answer = completion(model="claude-haiku-4-5-20251001", messages=messages)
```

## Storage options

- **pgvector** — add vectors to the PostgreSQL you already run (great for solo apps).
- **Chroma** — simple local vector store.
- **Pinecone / Qdrant** — managed, scales to millions of vectors.

## This platform as an example

The AI Mentor injects the **current lesson's markdown** as context and tells the model to prefer it. That's a focused, single-document knowledge base — simple and effective.

## Check yourself

**1. Why are document embeddings created once, but the question's embedding every time?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Documents do not change, so their vectors can be computed and stored ahead of time. Each question is new, so its embedding is computed at query time and compared against the stored ones.

</details>

**2. Why does the system message say "If it's not there, say so"?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Without it, a model that cannot find the answer in the context will fill the gap with general knowledge or a hallucination. That sentence gives it permission to say "I don't know".

</details>

**3. When is pgvector enough, and when is a managed vector DB worth it?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

If you already run PostgreSQL and have thousands to tens of thousands of vectors, pgvector is simplest. Managed services (Pinecone, Qdrant) pay off at millions of vectors or heavy traffic.

</details>

## Mini Exercise

Build a mini knowledge base from 5–10 of your own notes or FAQ entries, then ask a question whose answer is *not* there. Check whether the assistant admits it does not know or makes something up.

> **Task check:** describe the result to the mentor and ask: "My RAG answered like this. How do I improve the chunking or the prompt so answers are more reliable?"

> **Mentor tip:** Ask "How would I add pgvector to a FastAPI + PostgreSQL app?"

Next: getting it live — **deployment**.
