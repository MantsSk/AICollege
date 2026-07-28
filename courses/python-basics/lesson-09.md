---
title: Pirmasis DI modelio kvietimas – prijunk OpenAI Responses API
module: DI asistento kūrimas
order: 9
---

# Pirmasis DI modelio kvietimas – prijunk OpenAI Responses API

> **Trukmė:** 6 akademinės valandos. Reikės OpenAI API projekto rakto ir nedidelio API biudžeto. Jei rakto nėra, atlik simuliacijos užduotis su pateiktais JSON pavyzdžiais.

> **Dokumentacijos data:** API pavyzdžiai patikrinti 2026-07-17 pagal oficialią OpenAI dokumentaciją. Modelis parenkamas per `OPENAI_MODEL`, kad kurso kodas nepasentų pakeitus rekomenduojamą modelį.

## Mokymosi rezultatai

Įdiegsi oficialų Python SDK, saugiai nuskaitysi raktą, iškviesi Responses API, paimsi `output_text`, suprasi įvesties, instrukcijų, modelio bei tokenų vaidmenį ir pakeisi taisyklinį atsakymą DI sugeneruotu.

## 1. Kas vyksta modelio kvietimo metu

```text
vartotojo tekstas → tavo Python patikra → Responses API → modelis → atsakymas → tavo Python pateikimas
```

Modelis nėra tavo Python proceso dalis. Programa siunčia duomenis į API, todėl galioja tinklo, kainos, privatumo ir klaidų valdymo principai iš ankstesnės pamokos.

## 2. Aplinkos paruošimas

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install openai python-dotenv
```

Windows PowerShell aktyvinimas:

```powershell
.venv\Scripts\Activate.ps1
```

`.env`:

```text
OPENAI_API_KEY=įklijuok_savo_raktą
OPENAI_MODEL=gpt-5.6-luna
```

Modelio pavadinimas yra konfigūracija, ne programos logika. Prieš realų darbą patikrink dabartinį prieinamumą ir kainodarą savo API projekte. `.env` būtinai įrašyk į `.gitignore`.

## 3. Minimalus veikiantis kvietimas

```python
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

model = os.getenv("OPENAI_MODEL")
if not model:
    raise RuntimeError(".env faile trūksta OPENAI_MODEL")

client = OpenAI()  # OPENAI_API_KEY nuskaitomas iš aplinkos

response = client.responses.create(
    model=model,
    input="Paaiškink Python kintamąjį vienu sakiniu lietuviškai.",
)

print(response.output_text)
```

`response` yra struktūruotas objektas. Patogus `output_text` surenka galutinį tekstinį atsakymą; nebandyk spėti giliai įdėtų indeksų iš seno pavyzdžio internete.

## 4. Instrukcijos ir vartotojo įvestis

```python
INSTRUCTIONS = """
Esi kantrus Python mokymosi asistentas.
Atsakyk lietuviškai, aiškiais trumpais sakiniais.
Pirmiausia pateik užuominą, ne visą namų darbo sprendimą.
Jei trūksta informacijos, užduok vieną tikslinantį klausimą.
Neapsimesk paleidęs kodą, jei jo nepaleidai.
""".strip()

question = input("Tu: ").strip()
if not question:
    raise ValueError("Klausimas negali būti tuščias")

response = client.responses.create(
    model=model,
    instructions=INSTRUCTIONS,
    input=question,
)
print(f"Asistentas: {response.output_text}")
```

Instrukcijos apibrėžia pastovų elgesį, o `input` – dabartinę vartotojo užduotį. Vartotojo tekstas neturi būti suklijuotas į instrukcijų vidurį kaip patikima taisyklė.

## 5. Neapibrėžtumas ir haliucinacijos

Modelis generuoja tikėtiną atsakymą, o ne automatiškai tikrina tiesą. Todėl:

- svarbius faktus grįsk pateiktu šaltiniu;
- prašyk aiškiai pažymėti nežinojimą;
- netikėk vien sklandžia formuluote;
- kodo pavyzdžius paleisk ir testuok;
- asmens, medicinos, teisės ar finansų sprendimams numatyk žmogaus peržiūrą.

## 6. Kaina ir tokenai

API naudojimas yra apskaitomas. Įvesties tekstas ir sugeneruotas atsakymas skaičiuojami tokenais; ilga istorija didina įvestį. Mokymuisi:

- pradėk nuo trumpų užklausų;
- nustatyk projekto biudžeto ribas;
- nerodyk begalinio automatinio kartojimo;
- loguok užklausų skaičių, bet ne paslaptis;
- modelį laikyk `.env`, kad galėtum rinktis ekonomiškesnį.

## 7. Klaidų vertimas vartotojui

```python
from openai import APIConnectionError, APIStatusError, RateLimitError

def ask_model(client: OpenAI, model: str, question: str) -> str:
    try:
        response = client.responses.create(
            model=model,
            instructions=INSTRUCTIONS,
            input=question,
        )
        answer = response.output_text.strip()
        return answer or "Modelis negrąžino tekstinio atsakymo."
    except RateLimitError as exc:
        raise RuntimeError("Pasiektas užklausų limitas. Pabandyk vėliau.") from exc
    except APIConnectionError as exc:
        raise RuntimeError("Nepavyko prisijungti prie DI paslaugos.") from exc
    except APIStatusError as exc:
        raise RuntimeError(f"DI paslauga grąžino klaidą {exc.status_code}.") from exc
```

Klaidos klasės ir SDK gali keistis – projekto diegimo metu remkis įdiegtos versijos ir oficialia dokumentacija.

## 8. Praktika trimis lygiais

### A lygis – trys rolės

Tą patį klausimą išbandyk su trimis instrukcijomis: kantrus dėstytojas, lakoniškas techninis redaktorius, viktorinos vedėjas. Palygink toną, struktūrą ir faktinį turinį.

### B lygis – promptų bandymų lentelė

Paruošk 12 klausimų: aiškūs, dviprasmiški, už temos ribų ir bandantys pakeisti asistento rolę. Užrašyk tikėtiną elgesį, faktinį elgesį ir patobulintą instrukciją.

### C lygis – testuojamas adapteris

`ask_model()` neturi `input()` ar `print()`. Testuose perduok netikrą klientą, kurio `responses.create()` grąžina objektą su `output_text`. Patikrink normalų, tuščią ir klaidos atvejį nesiųsdamas mokamos užklausos.

## 9. Mini projektas: Asistentas 0.7

Pakeisk ankstesnės versijos nežinomo klausimo šaką: pirmiausia ieškok vietinėje DUK bazėje, o neradęs – tik gavęs vartotojo patvirtinimą klausk DI modelio. Atsakyme pažymėk šaltinį `Vietinė žinių bazė` arba `DI modelis`.

Baigimo kriterijai:

- raktas nėra kode ar Git istorijoje;
- modelis gaunamas iš `OPENAI_MODEL`;
- tuščia įvestis nesiunčiama;
- klaidos pateikiamos suprantamai;
- naudotojas žino, kada atsakė modelis;
- yra bent 10 elgesio scenarijų;
- README paaiškina galimas API išlaidas.

## Santrauka ir namų darbas

Sukūrei pirmą tikrą DI integraciją per Responses API. Namų darbui užbaik Asistentą 0.7, pateik `.env.example`, išlaidų saugiklius, 12 promptų vertinimo lentelę ir vieno neteisingo modelio atsakymo analizę.

## 10. Gilioji laboratorija: API kvietimas turi veikti ir be rakto

Sukurk konfigūracijos funkciją, kuri grąžina `OPENAI_MODEL` ir kuria klientą tik tada, kai pasirinktas realus režimas. Testuose perduok fake klientą, o ne tikrą API raktą. Asistentas turi turėti vietinį kelią: klausimą apie `knowledge.json` atsakyti be tinklo ir aiškiai parodyti šaltinį.

Patikrink tris atsakymo būsenas: normalų `output_text`, tuščią tekstą ir SDK klaidą. Kiekvienai būsenai parašyk vartotojui rodomą žinutę. Paruošk 20 klausimų paketą, suskirstytą į trumpus, vidutinius ir ilgus; prie jo nurodyk užklausų limitą ir ką darysi jį pasiekus.

Kontrolinis taškas: veikia vietinis režimas be rakto, fake klientas testuose ir realus klientas su `.env`. Modelio ID laikomas konfigūracijoje, o diegimo metu tikrinama oficiali modelių dokumentacija.

Oficialūs šaltiniai: [OpenAI API greita pradžia](https://developers.openai.com/api/docs/quickstart), [modelių pasirinkimas](https://developers.openai.com/api/docs/guides/latest-model), [Responses API](https://developers.openai.com/api/docs/api-reference/responses).
