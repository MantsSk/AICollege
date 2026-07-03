---
title: LLM API kvietimas
module: LLM API
order: 1
---

# LLM API kvietimas

Kiekvienas DI asistentas prasideda nuo vieno įgūdžio: nusiųsti žinutę modeliui ir gauti atsakymą. Naudosime **LiteLLM**, kuris suteikia vieną bendrą sąsają OpenAI, Gemini, Claude ir kitiems modeliams — būtent tai naudoja ši platforma.

**Po šios pamokos galėsi:**

- iškviesti LLM iš Python kodo ir atspausdinti atsakymą;
- paaiškinti tris žinučių roles: `system`, `user`, `assistant`;
- valdyti atsakymą per `temperature` ir `max_tokens`.

## Pirmasis kvietimas

```python
from litellm import completion

response = completion(
    model="claude-haiku-4-5-20251001",
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
    model="claude-haiku-4-5-20251001",
    messages=messages,
    temperature=0.3,   # mažiau = labiau susitelkęs atsakymas
    max_tokens=500,    # riboja atsakymo ilgį / kainą
)
```

## Pasitikrink save

**1. Kuo skiriasi `system` ir `user` rolės?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`system` — pastovios instrukcijos ir asistento persona, kurias nustato programuotojas. `user` — konkreti žmogaus žinutė. Sistemos žinutė veikia visą pokalbį, vartotojo — vieną ėjimą.

</details>

**2. Kam skirtas `max_tokens`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Riboja atsakymo ilgį, taigi ir kainą bei laukimo laiką. Per mažas limitas nukirs atsakymą vidury sakinio.

</details>

**3. Ką reikia pakeisti kode, norint naudoti kito tiekėjo modelį per LiteLLM?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Tik `model` parametrą (ir turėti to tiekėjo API raktą aplinkos kintamajame). Visa kita — žinučių formatas, atsakymo struktūra — lieka tas pats.

</details>

## Mini užduotis

Parašyk skriptą, kuris tą patį klausimą užduoda su `temperature=0` ir `temperature=1` po tris kartus ir atspausdina visus šešis atsakymus. Palygink, kuo jie skiriasi.

> **Užduoties patikra:** įklijuok savo pastebėjimus mentoriui ir paklausk: „Ar teisingai supratau, ką daro temperature? Kada rinkčiausi 0, o kada 1?“

> **Mentoriaus patarimas:** paklausk „Ką sistemos žinutė iš tikrųjų pakeičia atsakyme?“

Toliau: paversime tai interaktyvia **pokalbio sąsaja**.
