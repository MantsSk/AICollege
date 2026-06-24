---
title: Žinių bazės pridėjimas
module: Žinių bazė
order: 4
---

# Žinių bazės pridėjimas

Kad asistentas taptų ekspertu apie *tavo* medžiagą — dokumentus, DUK, kursą — duok jam **žinių bazę** naudodamas RAG principą iš DI pagrindų.

## 1 žingsnis — įkėlimas

Suskaidyk dokumentus į dalis ir vieną kartą sukurk jų įterpinius:

```python
from litellm import embedding

def embed(texts):
    resp = embedding(model="text-embedding-3-small", input=texts)
    return [d["embedding"] for d in resp["data"]]

chunks = split_into_chunks(my_docs)        # po ~300 tokenų
vectors = embed(chunks)
store(chunks, vectors)                      # išsaugoti vektorinėje DB
```

## 2 žingsnis — paieška

Kai gauni klausimą, sukurk jo įterpinį ir rask artimiausias dalis:

```python
def search(question, top_k=3):
    q = embed([question])[0]
    return nearest_chunks(q, top_k)          # kosinusinis panašumas
```

## 3 žingsnis — atsakymas su kontekstu

```python
context = "\n\n".join(search(question))
messages = [
    {"role": "system",
     "content": "Atsakyk naudodamas kontekstą. Jei atsakymo ten nėra, taip ir pasakyk."},
    {"role": "user",
     "content": f"Kontekstas:\n{context}\n\nKlausimas: {question}"},
]
answer = completion(model="gpt-4o-mini", messages=messages)
```

## Saugojimo pasirinkimai

- **pgvector** — pridėk vektorius į jau naudojamą PostgreSQL (puiku mažoms programoms).
- **Chroma** — paprasta lokali vektorių saugykla.
- **Pinecone / Qdrant** — valdoma infrastruktūra, tinka milijonams vektorių.

## Ši platforma kaip pavyzdys

DI mentorius įdeda **dabartinės pamokos markdown** kaip kontekstą ir liepia modeliui teikti jam pirmenybę. Tai sutelkta vieno dokumento žinių bazė — paprasta ir veiksminga.

> **Mentoriaus patarimas:** paklausk „Kaip pridėčiau pgvector į FastAPI + PostgreSQL programą?“

Toliau: paleidimas viešai — **diegimas**.
