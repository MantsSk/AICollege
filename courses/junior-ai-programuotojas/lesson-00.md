---
title: Pasiruošimas: aplinka, API raktas ir pirmoji API klaida
module: Pasiruošimas
order: 0
---

# Pasiruošimas: aplinka, API raktas ir pirmoji API klaida

Visi šio kurso projektai naudoja LLM API, todėl pirmiausia susitvarkome įrankius: virtualią aplinką, biblioteką ir raktą. Čia užstringa daugiausia pradedančiųjų — ne ties agentais, o ties `AuthenticationError`.

**Po šios pamokos galėsi:**

- paruošti Python aplinką su LiteLLM;
- gauti ir saugiai nustatyti API raktą;
- atpažinti tris dažniausias API klaidas ir žinoti, ką jos reiškia.

## 1. Aplinka

```bash
mkdir junior-ai && cd junior-ai
python3 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install litellm
```

## 2. API raktas

Užsiregistruok pas pasirinktą tiekėją (Anthropic, OpenAI ar Google) ir sukurk raktą. Nustatyk jį kaip aplinkos kintamąjį:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # macOS/Linux
# Windows PowerShell: $env:ANTHROPIC_API_KEY="sk-ant-..."
```

Raktas kode neturi atsirasti niekada: kodas keliauja į GitHub, o raktas — tik į aplinkos kintamuosius.

## 3. Pirmas kvietimas

Failas `test_api.py`:

```python
from litellm import completion

response = completion(
    model="claude-haiku-4-5-20251001",
    messages=[{"role": "user", "content": "Pasisveikink viena eilute."}],
)
print(response.choices[0].message.content)
```

Jei pamatei pasisveikinimą — aplinka paruošta.

## 4. Trys klaidos, kurias tikrai pamatysi

**`AuthenticationError`** — raktas nenustatytas arba neteisingas. Patikrink `echo $ANTHROPIC_API_KEY` ir ar terminalas naujas (kintamieji galioja tik tame lange, kur juos nustatei).

**`RateLimitError`** — per daug užklausų per trumpą laiką arba baigėsi kreditai. Palauk arba pasitikrink sąskaitą tiekėjo puslapyje.

**`ModuleNotFoundError: litellm`** — neaktyvuota virtuali aplinka. Pažiūrėk, ar prieš eilutę matai `(.venv)`.

## Pasitikrink save

**1. Kodėl raktas laikomas aplinkos kintamajame, o ne `test_api.py` faile?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Failai keliauja į GitHub, pokalbius ir ekrano nuotraukas. Nutekėjęs raktas leidžia svetimiems naudoti tavo sąskaitą, todėl jis gyvena tik aplinkoje.

</details>

**2. Ką pirmiausia tikrinti pamačius `AuthenticationError`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Ar raktas nustatytas šitame terminalo lange (`echo $ANTHROPIC_API_KEY`) ir ar jis nukopijuotas pilnas, be tarpų.

</details>

**3. Ką reiškia `ModuleNotFoundError: litellm`, jei `pip install` jau darei?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Greičiausiai diegei į vieną aplinką, o paleidi iš kitos — neaktyvuota virtuali aplinka. Aktyvuok `.venv` ir bandyk vėl.

</details>

## Mini užduotis

Paleisk `test_api.py` sėkmingai. Tada specialiai sugadink raktą (pakeisk vieną raidę), paleisk dar kartą ir perskaityk klaidą. Grąžink teisingą raktą.

> **Užduoties patikra:** nukopijuok gautą klaidos tekstą mentoriui ir paklausk: „Kaip iš šios klaidos suprasti, ar problema rakte, tinkle ar kode?“

> **Mentoriaus patarimas:** paklausk „Kuo skiriasi API raktas, tokenas ir slaptažodis? Kaip juos saugoti?“

Toliau: kaip naudoti DI mokantis programuoti — darbo eiga, kuri neišugdo priklausomybės.
