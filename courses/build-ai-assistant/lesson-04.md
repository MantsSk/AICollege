---
title: Žinių bazės pridėjimas
module: Žinių bazė
order: 4
---

# Žinių bazės pridėjimas

Kad asistentas taptų ekspertu apie *tavo* medžiagą — dokumentus, DUK, kursą — duok jam **žinių bazę** naudodamas RAG principą.

**Po šios pamokos galėsi:**

- paversti dokumentus įterpiniais ir juos išsaugoti;
- rasti klausimui aktualiausias dalis pagal prasmę;
- sudėti rastą kontekstą į promptą ir apriboti atsakymą juo.

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
answer = completion(model="claude-haiku-4-5-20251001", messages=messages)
```

## Saugojimo pasirinkimai

- **pgvector** — pridėk vektorius į jau naudojamą PostgreSQL (puiku mažoms programoms).
- **Chroma** — paprasta lokali vektorių saugykla.
- **Pinecone / Qdrant** — valdoma infrastruktūra, tinka milijonams vektorių.

## Ši platforma kaip pavyzdys

DI mentorius įdeda **dabartinės pamokos markdown** kaip kontekstą ir liepia modeliui teikti jam pirmenybę. Tai sutelkta vieno dokumento žinių bazė — paprasta ir veiksminga.

## Pasitikrink save

**1. Kodėl dokumentų įterpiniai kuriami vieną kartą, o klausimo — kiekvieną kartą?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Dokumentai nesikeičia, todėl jų vektorius galima paskaičiuoti ir išsaugoti iš anksto. Klausimas kaskart naujas, todėl jo įterpinys kuriamas užklausos metu ir lyginamas su išsaugotais.

</details>

**2. Kam sistemos žinutėje sakinys „Jei atsakymo ten nėra, taip ir pasakyk“?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Be jo modelis, neradęs atsakymo kontekste, užpildys spragą bendromis žiniomis ar haliucinacija. Šis sakinys duoda jam leidimą pasakyti „nežinau“.

</details>

**3. Kada užtenka pgvector, o kada verta valdomos vektorių DB?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Jei jau naudoji PostgreSQL ir vektorių tūkstančiai ar dešimtys tūkstančių — pgvector paprasčiausia. Valdomos paslaugos (Pinecone, Qdrant) apsimoka nuo milijonų vektorių ar didelio srauto.

</details>

## Mini užduotis

Sukurk mini žinių bazę iš 5–10 savo užrašų ar DUK įrašų ir užduok klausimą, kurio atsakymo ten *nėra*. Patikrink, ar asistentas prisipažįsta nežinąs, ar išsigalvoja.

> **Užduoties patikra:** aprašyk mentoriui rezultatą ir paklausk: „Mano RAG atsakė štai taip. Kaip pagerinti suskaidymą ar promptą, kad atsakymai būtų patikimesni?“

> **Mentoriaus patarimas:** paklausk „Kaip pridėčiau pgvector į FastAPI + PostgreSQL programą?“

Toliau: paleidimas viešai — **diegimas**.
