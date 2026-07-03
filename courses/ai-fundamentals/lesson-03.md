---
title: Įterpiniai
module: Įterpiniai
order: 3
---

# Įterpiniai

**Įterpinys** tekstą paverčia skaičių sąrašu (*vektoriumi*), kuris užfiksuoja jo prasmę. Panašios prasmės tekstai sukuria arti vienas kito esančius vektorius.

```text
"dog"   -> [0.21, -0.08, 0.55, ...]
"puppy" -> [0.19, -0.05, 0.58, ...]   ← arti "dog"
"car"   -> [-0.40, 0.71, 0.02, ...]   ← toli
```

## Kodėl tai galinga

Kompiuteriai negali tiesiogiai palyginti *prasmės*, bet gali palyginti *skaičius*. Su įterpiniais gali:

- **Ieškoti pagal prasmę**, ne pagal raktažodžius („kaip atšaukti planą“ randa „prenumeratos valdymą“).
- **Grupuoti** panašius dokumentus.
- **Rekomenduoti** susijusį turinį.
- Įgalinti **RAG** (kita pamoka).

## Panašumo matavimas

Standartinis įrankis yra **kosinusinis panašumas** — jis matuoja kampą tarp dviejų vektorių. Kuo arčiau `1`, tuo panašiau.

```python
# pseudo-code
score = cosine_similarity(embed("cancel plan"), embed(doc))
```

## Įterpinio generavimas

```python
from litellm import embedding

resp = embedding(model="text-embedding-3-small", input=["Mokykis DI su Python"])
vector = resp["data"][0]["embedding"]
print(len(vector))  # pvz., 1536 skaičiai
```

## Vektorinės duomenų bazės

Kai turi tūkstančius dokumentų, jų vektorius saugai **vektorinėje duomenų bazėje** (pvz., pgvector, Chroma, Pinecone), kad artimiausius atitikmenis rastum per milisekundes.

> **Mentoriaus patarimas:** paklausk „Kodėl naudojamas kosinusinis panašumas, o ne paprastas atstumas?“

Toliau: paiešką ir LLM sujungsime atsakymams iš *tavo pačių* duomenų — **RAG**.
