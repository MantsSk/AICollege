---
title: Embeddings
module: Embeddings
order: 3
---

# Embeddings

An **embedding** turns text into a list of numbers (a *vector*) that captures its meaning. Texts with similar meaning produce vectors that are close together.

```text
"dog"   -> [0.21, -0.08, 0.55, ...]
"puppy" -> [0.19, -0.05, 0.58, ...]   ← close to "dog"
"car"   -> [-0.40, 0.71, 0.02, ...]   ← far away
```

## Why this is powerful

Computers can't compare *meaning* directly, but they can compare *numbers*. With embeddings you can:

- **Search by meaning**, not keywords ("how to cancel my plan" finds "subscription management").
- **Cluster** similar documents.
- **Recommend** related content.
- Power **RAG** (next lesson).

## Measuring similarity

The standard tool is **cosine similarity** — it measures the angle between two vectors. Closer to `1` means more similar.

```python
# pseudo-code
score = cosine_similarity(embed("cancel plan"), embed(doc))
```

## Generating an embedding

```python
from litellm import embedding

resp = embedding(model="text-embedding-3-small", input=["Learn AI with Python"])
vector = resp["data"][0]["embedding"]
print(len(vector))  # e.g. 1536 numbers
```

## Vector databases

When you have thousands of documents, you store their vectors in a **vector database** (e.g. pgvector, Chroma, Pinecone) so you can find the closest matches in milliseconds.

> **Mentor tip:** Ask "Why is cosine similarity used instead of plain distance?"

Next: combining search + LLMs to answer from *your own* data — **RAG**.
