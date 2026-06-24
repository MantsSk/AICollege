---
title: Paieška papildyta generacija (RAG)
module: RAG
order: 4
---

# Paieška papildyta generacija (RAG)

LLM nežino tavo privačių dokumentų ir gali haliucinuoti faktus. **RAG** sprendžia abi problemas: *suranda* aktualų tekstą ir įdeda jį į promptą prieš modeliui atsakant.

## RAG eiga

```text
1. ĮKĖLIMAS     Suskaidyk dokumentus į dalis, sukurk įterpinius, saugok vektorius.
2. PAIEŠKA      Klausimą paversk įterpiniu ir rask artimiausias dalis.
3. PAPILDYMAS   Įdėk tas dalis į promptą kaip kontekstą.
4. GENERAVIMAS  Paprašyk LLM atsakyti naudojant tik tą kontekstą.
```

## Minimalus pavyzdys

```python
question = "Kaip atšaukti prenumeratą?"

# 1+2: rasti aktualiausias dalis
chunks = vector_search(question, top_k=3)
context = "\n\n".join(chunks)

# 3+4: pagrįsti modelį tavo turiniu
prompt = f"""Atsakyk naudodamas TIK žemiau pateiktą kontekstą.
Jei atsakymo ten nėra, pasakyk, kad nežinai.

Kontekstas:
{context}

Klausimas: {question}"""

answer = llm(prompt)
```

## Kodėl tai svarbu čia

Šios platformos **DI mentorius** yra RAG forma: jis gauna dabartinės pamokos turinį kaip kontekstą ir instrukciją atsakymuose *teikti pirmenybę kurso medžiagai*. Todėl jis lieka prie temos ir tiksliai padeda su skaitoma pamoka.

## Praktiniai patarimai

- **Gerai skaidyk** — per didelės dalys švaisto kontekstą, per mažos praranda prasmę (dažnai tinka ~200–500 tokenų).
- **Surask pakankamai** — 3–5 geriausios dalys paprastai geriau nei viena.
- **Cituok šaltinius**, kad vartotojai galėtų patikrinti.

> **Mentoriaus patarimas:** paklausk „Kaip šios pamokos DI mentorius naudoja RAG idėjas?“

Toliau: leisime DI *imtis veiksmų* — **agentai**.
