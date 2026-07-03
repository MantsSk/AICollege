---
title: Pasiruošimas: aplinka, raktai ir pirmas serveris
module: Pasiruošimas
order: 0
---

# Pasiruošimas: aplinka, raktai ir pirmas serveris

Šiame kurse rašysime realų kodą: API kvietimus, web serverį, duomenų bazę. Prieš pradedant susitvarkykime aplinką — 15 minučių dabar sutaupys valandas vėliau.

**Po šios pamokos galėsi:**

- susikurti izoliuotą Python aplinką projektui;
- saugiai nustatyti API raktą kaip aplinkos kintamąjį;
- paleisti pirmą FastAPI serverį ir suprasti dažniausią jo klaidą.

## 1. Projekto aplanko ir virtualios aplinkos sukūrimas

```bash
mkdir ai-assistant && cd ai-assistant
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install litellm fastapi "uvicorn[standard]"
```

Virtuali aplinka (`.venv`) laiko projekto bibliotekas atskirai nuo sistemos. Jei terminale matai `(.venv)` prieš eilutę — ji aktyvi.

## 2. API raktas

Užsiregistruok pas pasirinktą tiekėją ir gauk raktą. Tada nustatyk jį kaip aplinkos kintamąjį — **niekada nerašyk rakto kode**:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # macOS/Linux
# Windows PowerShell: $env:ANTHROPIC_API_KEY="sk-ant-..."
```

Su LiteLLM tiekėją keisi viena eilute, todėl tinka bet kuris raktas: `OPENAI_API_KEY`, `GEMINI_API_KEY` ar `ANTHROPIC_API_KEY`.

## 3. Pirmas serveris

Sukurk failą `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "veikia"}
```

Paleisk:

```bash
uvicorn main:app --reload
```

Atsidaryk naršyklėje `http://127.0.0.1:8000` — turėtum pamatyti `{"status": "veikia"}`.

## 4. Pirmoji klaida (specialiai)

Sustabdyk serverį (`Ctrl+C`) ir paleisk `uvicorn app:main --reload` — sukeitęs žodžius vietomis. Gausi:

```text
ERROR: Error loading ASGI app. Could not import module "app".
```

Formatas yra `failo_vardas:kintamojo_vardas`. Ši klaida — dažniausia pirmos dienos FastAPI kliūtis, ir dabar jau žinai, ką ji reiškia.

## Pasitikrink save

**1. Kam reikalinga virtuali aplinka?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kad projekto bibliotekos būtų izoliuotos: skirtingi projektai gali naudoti skirtingas versijas, o sistema lieka švari. Aktyvuota aplinka matoma kaip `(.venv)` terminale.

</details>

**2. Kodėl API raktas laikomas aplinkos kintamajame, o ne kode?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kodas keliauja į git, ekrano nuotraukas ir pokalbius su DI — raktas neturi keliauti kartu. Nutekėjęs raktas leidžia kitiems naudoti tavo sąskaitą.

</details>

**3. Ką reiškia `uvicorn main:app`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

„Faile `main.py` rask kintamąjį `app` ir paleisk jį kaip serverį.“ Sukeitus dalis vietomis gaunama `Could not import module` klaida.

</details>

## Mini užduotis

Pridėk prie serverio antrą endpointą `/about`, kuris grąžina tavo vardą ir ką nori sukurti. Perkrauk naršyklę ir įsitikink, kad abu endpointai veikia.

> **Užduoties patikra:** įklijuok savo `main.py` mentoriui ir paklausk: „Ar mano FastAPI struktūra teisinga? Ką daryčiau, jei norėčiau endpointo su parametru, pvz., /hello/{name}?“

> **Mentoriaus patarimas:** paklausk „Kas atsitinka, kai uvicorn paleidžiamas su --reload, ir kodėl to nenaudoti produkcijoje?“

Toliau: pirmasis LLM API kvietimas.
