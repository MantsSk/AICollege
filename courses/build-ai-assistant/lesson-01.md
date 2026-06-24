---
title: LLM API kvietimas
module: OpenAI API
order: 1
---

# LLM API kvietimas

Kiekvienas DI asistentas prasideda nuo vieno įgūdžio: nusiųsti žinutę modeliui ir gauti atsakymą. Naudosime **LiteLLM**, kuris suteikia vieną bendrą sąsają OpenAI, Gemini, Claude ir kitiems modeliams — būtent tai naudoja ši platforma.

## Pirmasis kvietimas

```python
from litellm import completion

response = completion(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Esi naudingas asistentas."},
        {"role": "user", "content": "Paaiškink rekursiją vienu sakiniu."},
    ],
)

print(response.choices[0].message.content)
```

## Kodėl LiteLLM

Pakeisk vieną eilutę ir perjungsi tiekėją, neperrašydamas kodo:

```python
model="gemini/gemini-1.5-flash"   # Google
model="claude-haiku-4-5-20251001" # Anthropic
model="gpt-4o-mini"               # OpenAI
```

Atitinkamą API raktą nustatyk kaip aplinkos kintamąjį (`OPENAI_API_KEY`, `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`).

## Žinučių formatas

Pokalbiai yra žinučių sąrašas, kuriame kiekviena žinutė turi `role`:

- `system` — pastovios instrukcijos / persona.
- `user` — ką pasakė žmogus.
- `assistant` — ką modelis atsakė anksčiau.

## Naudingi parametrai

```python
completion(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.3,   # mažiau = labiau susitelkęs atsakymas
    max_tokens=500,    # riboja atsakymo ilgį / kainą
)
```

> **Mentoriaus patarimas:** paklausk „Ką sistemos žinutė iš tikrųjų pakeičia atsakyme?“

Toliau: paversime tai interaktyvia **pokalbio sąsaja**.
