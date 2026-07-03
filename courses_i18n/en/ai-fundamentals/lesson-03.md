---
title: Prompts That Work
module: Prompt Engineering
order: 3
---

# Prompts That Work

A prompt is your instruction to an AI model. A good prompt is not long for the sake of being long. It clearly says what you want, what context matters, what format you need, and how quality should be judged.

**After this lesson you will be able to:**

- structure a prompt with the formula: goal, context, role, format, criteria, constraints;
- recognize why a weak prompt produces a generic, one-size-fits-nobody answer;
- iterate on an answer instead of settling for the first draft.

## A simple formula

Use this structure:

```text
Goal: what do I want?
Context: what does AI need to know?
Role: what perspective should it answer from?
Format: how should the answer look?
Quality criteria: what counts as a good result?
Constraints: what should it avoid?
```

## Weak and stronger prompts

Weak:

```text
Write me a resume.
```

The weak prompt usually gets an answer like this:

```text
Name Surname
An ambitious and motivated professional with excellent communication
skills and the ability to work in a team...
```

Notice what happened: the model knows nothing about you, so it filled the resume with impressive-sounding but empty phrases that recruiters see hundreds of times a day. That is not the model's fault — it did the best it could without context.

Stronger:

```text
Help me create a one-page resume for a junior data analyst role.
Context: I have 6 months of self-study, know Excel, SQL basics, and beginner Python.
Tone: professional but simple.
Format: sections called Profile, Skills, Projects, Experience, Learning.
Do not invent facts. If information is missing, ask questions.
```

With this prompt, a good model will usually start with questions rather than a resume: what projects do you have, what job are you targeting, what should stand out. That is exactly what we want — an answer built on your facts, not invented qualities.

## Five techniques

**1. Ask for questions before the answer.**

If the task is unclear:

```text
Before answering, ask up to 5 questions that would help you produce a better result.
```

**2. Give an example.**

If you want a specific style, paste an example and ask it to follow the rhythm, length, or tone.

**3. Ask for alternatives.**

```text
Give me 3 versions: conservative, creative, and very short.
```

**4. Ask for critique.**

```text
Evaluate your answer: what is weak, unclear, or should be verified?
```

**5. Iterate.**

The first answer is often a draft. Continue:

```text
Make it more specific.
Cut it in half.
Add examples.
Remove jargon.
Adapt it for a beginner.
```

## Useful prompt templates

For learning:

```text
Explain [topic] as if I were a beginner.
Then give an analogy, one practical example, and 3 self-check questions.
```

For decisions:

```text
Help me compare [A] and [B].
Create a table using these criteria: cost, effort, risk, long-term value.
End with a recommendation and when that recommendation would be wrong.
```

For writing:

```text
Rewrite this text so it is clearer and warmer.
Keep my meaning, but shorten it by 30%.
Avoid an exaggerated marketing tone.
```

## Check yourself

**1. Why does the weak prompt "Write me a resume" produce an empty, generic result?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

The model has no context about you, so it fills the gaps with the most generic phrases. The less context you give, the closer the answer is to the average of everything on the internet.

</details>

**2. What are the six parts of the prompt formula?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Goal, context, role, format, quality criteria, and constraints.

</details>

**3. What should you do if the first answer is not good?**

<details class="selfcheck" markdown="1">
<summary>Show answer</summary>

Iterate: ask for more specific, shorter, with examples, without jargon, adapted to the audience. The first answer is a draft, not the final result.

</details>

## Mini Exercise

Take one weak prompt of your own and rewrite it using the formula: goal, context, role, format, criteria, constraints.

> **Task check:** paste both versions to the mentor and ask: "Compare these two prompts: which parts of the formula are still missing from the second one, and how can it be improved?"

> **Mentor tip:** Paste your prompt and ask "Rewrite this so the answer is more specific and easier to verify."

Next: we will learn how to verify AI answers and avoid mistakes.
