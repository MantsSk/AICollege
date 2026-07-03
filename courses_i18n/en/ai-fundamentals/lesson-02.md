---
title: How Do Language Models Work?
module: Language Models
order: 2
---

# How Do Language Models Work?

A large language model (LLM) is an AI system trained to predict text. In simple terms, it receives a sequence of words and word-pieces, then guesses what should come next. Repeating that process creates an answer.

This does not mean the model "thinks" exactly like a human. But at large scale, this prediction ability creates skills that look very intelligent: explanation, summarization, translation, coding, and argument building.

**After this lesson you will be able to:**

- explain tokens and the context window in plain words;
- understand why the same question can get different answers;
- recognize the situations where hallucinations are most likely.

## Tokens

A model does not read text exactly like a person. Text is split into **tokens**: words, word parts, or symbols.

```text
"Artificial intelligence changes learning"
may become:
["Artificial", " intelligence", " changes", " learning"]
```

Tokens matter because they affect:

- how much text the model can see at once;
- how API usage is priced;
- when a long conversation starts losing earlier context.

## Context Window

The **context window** is the model's short-term memory. It is the text the model can see while answering: your question, earlier conversation, documents, instructions.

If information is not in the context, the model may:

- rely on general knowledge;
- guess;
- say it does not know, if you ask it to;
- create a convincing but incorrect answer.

That is why good context is often more important than a "perfect" prompt.

## Temperature

**Temperature** controls randomness:

- low temperature is useful for facts, formatting, and correction;
- higher temperature is useful for ideas, creativity, and alternatives.

Casual users do not need to tune temperature often, but the principle matters: the same question can have different answers because the model is not a simple calculator.

## Why do models make mistakes?

A language model creates likely text. It does not automatically check reality. If it does not see a reliable source, it may fill gaps. This is called a **hallucination**.

Hallucinations are more likely when:

- you ask about very recent facts;
- the topic is narrow or niche;
- you ask for quotes, legal, medical, or academic answers without sources;
- you pressure the model to answer when it lacks information.

## A good usage principle

Give the model what you would give a human collaborator:

- a goal;
- background;
- examples;
- desired format;
- criteria for judging the result.

## Check yourself

**1. What is the context window?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

The model's short-term memory — everything it sees while answering: your question, the earlier conversation, documents, instructions. What is not in the context cannot be used.

</details>

**2. Why does AI "forget" the start of a long conversation?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

The context window is limited: once the conversation exceeds its size (measured in tokens), the oldest part no longer fits and the model can no longer see it.

</details>

**3. When are hallucinations most likely?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

When you ask for very recent or niche facts, quotes and sources, or pressure the model to answer without enough information. The model produces likely text — it does not check reality.

</details>

## Mini Exercise

Take a long text you need to read and ask AI:

```text
Summarize this text in 5 bullet points.
Then list 3 things I should verify myself.
If the text does not contain enough information, say so clearly.
```

> **Task check:** paste the summary you got to the mentor and ask: "Which claims in this summary are paraphrase and which are the model's interpretation I should verify myself?"

> **Mentor tip:** Ask "Explain tokens, context windows, and hallucinations to someone who has never used AI."

Next: we will learn how to write prompts that get better answers.
