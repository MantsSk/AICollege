---
title: Search, Embeddings, RAG, and Agents
module: Advanced Ideas
order: 7
---

# Search, Embeddings, RAG, and Agents

You do not need to be a programmer to understand the most important advanced AI ideas. They explain why some tools answer more accurately, how AI works with documents, and why some systems can take actions.

**After this lesson you will be able to:**

- explain embeddings, RAG, and agents in plain words;
- understand why RAG answer quality depends on retrieval, not just the model;
- name the boundaries agents need.

## Embeddings: meaning as numbers

An **embedding** turns text into a list of numbers that roughly captures meaning. Similar ideas end up close to each other.

```text
"how do I cancel my subscription"
and
"I want to stop my paid plan"

may be close in meaning even though the words are different.
```

That lets AI systems search by meaning, not only exact keywords.

## RAG: answers from your documents

**RAG** means retrieval-augmented generation. The system:

1. splits documents into chunks;
2. turns chunks into embeddings;
3. finds the most relevant chunks for your question;
4. places them into the model's context;
5. asks the model to answer using the found text.

This is useful when you want AI to answer from specific documents: course material, company policies, product manuals, or research.

## Why RAG is not magic

RAG quality depends on:

- document quality;
- how documents are split;
- whether search finds the right chunks;
- whether the model follows instructions to use sources;
- whether the answer includes references or quotes.

If search retrieves the wrong text, even a powerful model can answer badly.

## Agents: AI that can act

An **agent** is an AI system that does not only answer with text. It uses tools: search, calculators, calendars, email, code, databases.

A simple agent loop:

```text
Goal -> plan -> tool use -> result check -> next step
```

Agents are useful for multi-step tasks, but they need boundaries:

- a step limit;
- a list of allowed tools;
- human approval before risky actions;
- logs so you can see what the agent did.

## Check yourself

**1. What are embeddings for?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

They turn text into numbers that capture meaning, so a system can search by meaning ("cancel my subscription" ≈ "stop my paid plan") rather than exact words.

</details>

**2. Why can a powerful model with RAG still answer badly?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

If retrieval finds the wrong chunks, the model answers from the wrong text. RAG quality depends on the documents, how they are split, and the search — not just the model.

</details>

**3. How does an agent differ from a chat assistant, and what boundaries does it need?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

An agent does not only answer with text — it takes actions using tools. That is why it needs a step limit, an allowed-tool list, human approval before risky actions, and logs.

</details>

## Mini Exercise

Imagine an AI assistant that helps you in one area: learning, travel planning, budgeting, writing, fitness. Write down:

- what documents it should use;
- what tools it could have;
- which actions should require your approval.

> **Task check:** describe your imagined assistant to the mentor and ask: "Evaluate my assistant plan: are the boundaries enough, and what risks did I miss?"

> **Mentor tip:** Ask "Explain RAG and agents without technical terms, using an everyday example."

Next: we will connect everything into an everyday AI workflow.
