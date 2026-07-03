---
title: Document Q&A Tool
module: RAG Project
order: 4
---

# Document Q&A Tool

RAG means the model receives relevant text from a document before answering. For a junior project, a simple version is enough: the user provides text and the program answers only from it.

**After this lesson you will be able to:**

- ground a model's answer in a specific document;
- write a prompt that forbids answering without context;
- explain how this tool differs from full RAG.

## Project Idea

Create a tool:

```bash
python doc_qa.py notes.txt "What are the most important points?"
```

The program:

1. reads the file;
2. places the text into a prompt;
3. asks the model to answer only from the document.

## Simple Prompt

```python
prompt = f"""
Answer only using the provided document.
If the answer is not there, write: "I did not find the answer in the document."

Document:
{document_text}

Question:
{question}
"""
```

## Why this is not full RAG yet

Full RAG would split the document into chunks, create embeddings, and search for the most relevant parts. But this mini project already teaches the key principle: the model should be grounded in specific context.

## Check yourself

**1. Why does the prompt specify the exact phrase "I did not find the answer in the document"?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

A clear instruction for what to say when the answer is missing reduces hallucination risk — the model gets a permitted "exit" instead of guessing.

</details>

**2. What is missing before this counts as full RAG?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Splitting the document into chunks, embeddings, and search by meaning. Here the whole document goes into the prompt — that only works for small files.

</details>

**3. When does this simple version stop working?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

When the document exceeds the context window or becomes too expensive to send with every question. Then you need chunking and retrieval.

</details>

## Mini Project

Create `doc_qa.py` that:

- accepts a file path and question;
- answers clearly;
- refuses to answer if the file is empty;
- ends with "Check the original document before making a decision."

> **Task check:** test your tool with a question whose answer is not in the document, then tell the mentor: "Here is how my tool answered. Is my prompt strict enough?"

> **Mentor tip:** Ask "How can I turn this simple document Q&A tool into a real RAG project?"

Next: we will connect tools and create a small agent.
