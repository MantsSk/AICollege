---
title: Retrieval-Augmented Generation (RAG)
module: RAG
order: 4
---

# Retrieval-Augmented Generation (RAG)

LLMs don't know your private documents and can hallucinate facts. **RAG** fixes both by *retrieving* relevant text and putting it into the prompt before the model answers.

## The RAG pipeline

```text
1. INGEST   Split your docs into chunks, embed them, store vectors.
2. RETRIEVE For a question, embed it and find the closest chunks.
3. AUGMENT  Insert those chunks into the prompt as context.
4. GENERATE Ask the LLM to answer using only that context.
```

## A minimal example

```python
question = "How do I cancel my subscription?"

# 1+2: find the most relevant chunks
chunks = vector_search(question, top_k=3)
context = "\n\n".join(chunks)

# 3+4: ground the model in your content
prompt = f"""Answer using ONLY the context below.
If the answer isn't there, say you don't know.

Context:
{context}

Question: {question}"""

answer = llm(prompt)
```

## Why this matters here

The **AI Mentor** in this platform is a form of RAG: it receives the current lesson's content as context and is instructed to *prefer the course material* when answering. That's why it stays on-topic and accurate for the lesson you're reading.

## Practical tips

- **Chunk well** — too big wastes context, too small loses meaning (~200–500 tokens is common).
- **Retrieve enough** — top 3–5 chunks usually beats one.
- **Cite sources** so users can verify.

> **Mentor tip:** Ask "How is the AI Mentor in this lesson using RAG ideas?"

Next: letting AI *take actions* — **agents**.
