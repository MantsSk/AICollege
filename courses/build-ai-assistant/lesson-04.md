---
title: Adding a Knowledge Base
module: Knowledge Base
order: 4
---

# Adding a Knowledge Base

To make your assistant an expert on *your* material — docs, FAQs, a course — give it a **knowledge base** using the RAG pattern from AI Fundamentals.

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
answer = completion(model="gpt-4o-mini", messages=messages)
```

## Storage options

- **pgvector** — add vectors to the PostgreSQL you already run (great for solo apps).
- **Chroma** — simple local vector store.
- **Pinecone / Qdrant** — managed, scales to millions of vectors.

## This platform as an example

The AI Mentor injects the **current lesson's markdown** as context and tells the model to prefer it. That's a focused, single-document knowledge base — simple and effective.

> **Mentor tip:** Ask "How would I add pgvector to a FastAPI + PostgreSQL app?"

Next: getting it live — **deployment**.
