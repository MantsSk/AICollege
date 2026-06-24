---
title: Pokalbio sąsajos kūrimas
module: Pokalbio sąsaja
order: 2
---

# Pokalbio sąsajos kūrimas

Dabar API apgaubsime web sąsaja — tai tas pats principas, kurį šioje platformoje naudoja DI mentorius: **FastAPI + HTMX**, be sunkaus JavaScript frameworko.

## Idėja

- Forma nusiunčia vartotojo žinutę į serverį.
- Serveris kviečia LLM ir grąžina **HTML fragmentą** (naujas žinutes).
- HTMX įdeda tą fragmentą į puslapį. Puslapis pilnai nepersikrauna.

## Endpointas (FastAPI)

```python
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from litellm import completion

app = FastAPI()

@app.post("/chat", response_class=HTMLResponse)
def chat(message: str = Form(...)):
    reply = completion(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message}],
    ).choices[0].message.content

    return f"""
      <div class="msg user">{message}</div>
      <div class="msg assistant">{reply}</div>
    """
```

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

> **Mentoriaus patarimas:** paklausk „Kuo `hx-swap='beforeend'` skiriasi nuo numatytojo swap?“

Toliau: priversime asistentą *atsiminti* pokalbį — **atmintis**.
