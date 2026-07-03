---
title: Pokalbio sąsajos kūrimas
module: Pokalbio sąsaja
order: 2
---

# Pokalbio sąsajos kūrimas

Dabar API apgaubsime web sąsaja — tai tas pats principas, kurį šioje platformoje naudoja DI mentorius: **FastAPI + HTMX**, be sunkaus JavaScript frameworko.

**Po šios pamokos galėsi:**

- sukurti FastAPI endpointą, kuris grąžina HTML fragmentą;
- sujungti formą su serveriu per HTMX be puslapio perkrovimo;
- apsaugoti sąsają nuo HTML injekcijos su `html.escape`.

## Idėja

- Forma nusiunčia vartotojo žinutę į serverį.
- Serveris kviečia LLM ir grąžina **HTML fragmentą** (naujas žinutes).
- HTMX įdeda tą fragmentą į puslapį. Puslapis pilnai nepersikrauna.

## Endpointas (FastAPI)

```python
import html

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from litellm import completion

app = FastAPI()

@app.post("/chat", response_class=HTMLResponse)
def chat(message: str = Form(...)):
    reply = completion(
        model="claude-haiku-4-5-20251001",
        messages=[{"role": "user", "content": message}],
    ).choices[0].message.content

    return f"""
      <div class="msg user">{html.escape(message)}</div>
      <div class="msg assistant">{html.escape(reply)}</div>
    """
```

Atkreipk dėmesį į `html.escape`: vartotojo (ir modelio!) tekstą dedame į HTML, todėl jį būtina apsaugoti. Be šito kas nors įvedęs `<script>...</script>` įvykdytų kodą kitų vartotojų naršyklėse — tai vadinama XSS ataka.

## HTMX forma

```html
<form hx-post="/chat" hx-target="#log" hx-swap="beforeend"
      hx-on::after-request="this.reset()">
  <input name="message" placeholder="Klausk bet ko...">
  <button>Siųsti</button>
</form>

<div id="log"></div>
```

`hx-post` išsiunčia formą, `hx-target` nurodo, kur įdėti atsakymą, o `hx-swap="beforeend"` prideda jį pokalbio gale.

## Krovimo būsenos

Kvietimo metu HTMX prideda `htmx-request` klasę, todėl gali rodyti „galvoja...“ indikatorių su CSS, be papildomo JS.

## Pasitikrink save

**1. Ką serveris grąžina naršyklei šiame sprendime?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Ne visą puslapį ir ne JSON, o HTML fragmentą — dvi naujas žinutes. HTMX įdeda jį į `#log` elementą be puslapio perkrovimo.

</details>

**2. Kodėl be `html.escape` programa būtų pažeidžiama?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Vartotojo tekstas patenka tiesiai į HTML. Įvedus `<script>` žymą, naršyklė ją įvykdytų — tai XSS ataka. `html.escape` paverčia specialius simbolius nekenksmingu tekstu.

</details>

**3. Ką daro `hx-swap="beforeend"`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Prideda atsakymo HTML į taikinio pabaigą (vietoj turinio pakeitimo), todėl pokalbio žinutės kaupiasi viena po kitos.

</details>

## Mini užduotis

Paleisk šį chatą lokaliai ir specialiai įvesk žinutę `<b>testas</b>`. Įsitikink, kad ji rodoma kaip tekstas, o ne paryškinama — tada `html.escape` veikia.

> **Užduoties patikra:** įklijuok savo endpointo kodą mentoriui ir paklausk: „Ar mano sąsauga saugi? Kokių dar spragų gali turėti toks chat endpointas?“

> **Mentoriaus patarimas:** paklausk „Kuo `hx-swap='beforeend'` skiriasi nuo numatytojo swap?“

Toliau: priversime asistentą *atsiminti* pokalbį — **atmintis**.
