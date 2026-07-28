---
title: File Search ir funkcijų kvietimas – prijunk žinių bazę bei veiksmus
module: DI asistento kūrimas
order: 11
---

# File Search ir funkcijų kvietimas – prijunk žinių bazę bei veiksmus

> **Trukmė:** 8 akademinės valandos. Tai tiltas nuo pokalbio roboto iki naudingo asistento: modelis gali rasti dokumentą ir paprašyti tavo kodo atlikti veiksmą.

## Mokymosi rezultatai

Suprasi RAG eigą, sukursi vector store, pridėsi `file_search`, apibrėši JSON Schema funkciją, apdorosi `function_call` ir grąžinsi `function_call_output`. Išmoksi nepasitikėti modelio argumentais be validacijos.

## 1. RAG eiga

Retrieval-Augmented Generation reiškia: pirmiausia surasti patikimą kontekstą, tada generuoti atsakymą jo pagrindu.

```text
failas → vector store → semantinė / raktažodinė paieška → citatos → atsakymas
```

File Search yra OpenAI valdomas Responses API įrankis. Programa sukuria vector store ir įkelia failus; kai modelis nusprendžia, įrankis automatiškai ieško nurodytoje bazėje.

## 2. Vector store paruošimas

```python
from openai import OpenAI

client = OpenAI()
vector_store = client.vector_stores.create(name="python-course")

with open("course-notes.md", "rb") as file:
    uploaded = client.files.create(file=file, purpose="assistants")

client.vector_stores.files.create(
    vector_store_id=vector_store.id,
    file_id=uploaded.id,
)
print(vector_store.id)
```

Prieš klausiant patikrink, kad vector store failo būsena `completed`. ID laikyk `.env` faile, o ne kode:

```text
OPENAI_VECTOR_STORE_ID=vs_...
```

## 3. File Search kvietimas

```python
response = client.responses.create(
    model=model,
    input="Kiek valandų trunka kursas? Atsakyk tik pagal įkeltus failus.",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store_id],
        "max_num_results": 4,
    }],
    include=["file_search_call.results"],
)
print(response.output_text)
```

Modelio atsakyme gali būti `file_search_call` ir `message` su failų citatomis. Jei dokumente informacijos nėra, instrukcija turi reikalauti aiškiai pasakyti „neradau“, o ne išgalvoti.

## 4. Funkcija kaip sutartis

Modelis pats nevykdo tavo Python funkcijos. Jis grąžina struktūruotą prašymą, tavo programa jį patikrina ir įvykdo, tada rezultatas grąžinamas modeliui.

```python
tools = [{
    "type": "function",
    "name": "calculate_course_price",
    "description": "Apskaičiuoja galutinę kainą pagal dalyvių skaičių.",
    "parameters": {
        "type": "object",
        "properties": {
            "participants": {"type": "integer", "minimum": 1, "maximum": 100},
            "unit_price": {"type": "number", "minimum": 0},
        },
        "required": ["participants", "unit_price"],
        "additionalProperties": False,
    },
    "strict": True,
}]
```

Schema mažina netinkamų argumentų tikimybę, bet nepašalina tavo validavimo pareigos.

## 5. Įrankio ciklas

```python
import json

def calculate_course_price(participants: int, unit_price: float) -> dict:
    if not 1 <= participants <= 100:
        raise ValueError("participants turi būti nuo 1 iki 100")
    if unit_price < 0:
        raise ValueError("unit_price negali būti neigiamas")
    return {"total": round(participants * unit_price, 2), "currency": "EUR"}

response = client.responses.create(model=model, input="Kiek kainuos 3 vietos po 20 eurų?", tools=tools)
tool_outputs = []
for item in response.output:
    if item.type == "function_call" and item.name == "calculate_course_price":
        args = json.loads(item.arguments)
        result = calculate_course_price(**args)
        tool_outputs.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": json.dumps(result),
        })

if tool_outputs:
    final = client.responses.create(
        model=model,
        previous_response_id=response.id,
        input=tool_outputs,
    )
    print(final.output_text)
```

Svarbiausi laukai: `name`, JSON tekstas `arguments`, `call_id` ir atgal siunčiamas `function_call_output`. Nevykdyk nežinomo funkcijos vardo.

## 6. Saugumo ribos įrankiams

Įrankių kvietimas gali pakeisti duomenis ar išleisti pinigus, todėl:

- skaitymo ir rašymo funkcijas atskirk;
- `delete`, mokėjimui ar el. laiškui reikalauk patvirtinimo;
- ribok skaičių, sumą, eilutės ilgį ir leidžiamus ID;
- funkcijai perduok tik reikiamus laukus;
- loguok funkcijos pavadinimą ir rezultatų santrauką, ne slaptus argumentus;
- jei validacija nepraeina, grąžink saugią klaidą modeliui.

## 7. Praktika trimis lygiais

### A lygis – File Search tyrimas

Įkelk kurso programą, užduok 8 klausimus, prie kiekvieno pažymėk, ar atsakymas remiasi failu. Išbandyk klausimą, kurio faile nėra.

### B lygis – saugi skaičiuoklės funkcija

Apibrėžk `calculate_course_price` ir `search_topic`. Parašyk testus validiems, ribiniams ir netinkamiems argumentams. Modelio nenaudok testams.

### C lygis – keli įrankiai

Pridėk `get_course_schedule` (tik skaito JSON) ir `save_feedback` (rašo CSV). Aprašyk, kada kiekvieną įrankį leisti, ir parodyk, kaip vartotojas patvirtina įrašymą.

## 8. Mini projektas: Asistentas 0.9

Sujunk vietinį `knowledge.json` su File Search pasirinktinai ir pridėk vieną saugų įrankį – kainos skaičiavimą. Asistentas turi:

- atsakyti iš patikimo dokumento, kai klausimas apie kursą;
- skaičiuoti kainą tik su validuotais skaičiais;
- parodyti, kada naudojo įrankį;
- neįvykdyti vartotojo prašymo paleisti savavališką kodą;
- turėti testinį netikrą klientą, kad įrankių ciklą būtų galima patikrinti be API.

## Santrauka ir namų darbas

RAG suteikia modelio atsakymui šaltinį, o function calling – kontroliuojamą ryšį su tavo kodu. Namų darbui pateik File Search įkėlimo instrukciją, dviejų funkcijų JSON Schema, 12 saugumo testų ir vieną atvejį, kai modelio argumentai atmetami.

## 9. Gilioji laboratorija: nuo tool call iki patikimo rezultato

Įkėlus failą neperšok iškart į klausimą. Užrašyk būsenas `uploaded`, `in_progress`, `completed`, `failed` ir sukurk laukimo ciklą su laiko limitu. Jei failas nepasiekia `completed`, vartotojui rodyk, kad žinių bazė neparuošta.

Viename atsakyme gali būti daugiau nei vienas `function_call`. Iteruok per visą `response.output`, išsaugok modelio output elementus ir kiekvienam `call_id` grąžink atskirą rezultatą. Reasoning modeliams būtina perduoti ir susijusius reasoning output elementus, kaip nurodo oficialus Function Calling srautas.

Sukurk maršrutizatorių su aiškiu leidžiamų įrankių rinkiniu. Jei modelis grąžina nežinomą pavadinimą arba blogą JSON, jo nevykdyk. Skaitymo įrankis gali veikti automatiškai, o laiškas, trynimas, mokėjimas ar įrašymas turi grąžinti „reikia vartotojo patvirtinimo“.

Kontrolinis taškas: netikras modelio atsakymas su dviem tool call, vienu nežinomu vardu ir blogu JSON turi būti apdorotas be šalutinio veiksmo.

Oficialūs šaltiniai: [File Search](https://developers.openai.com/api/docs/guides/tools-file-search), [Function calling](https://developers.openai.com/api/docs/guides/function-calling).
