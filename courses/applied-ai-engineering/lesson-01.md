---
title: Nuo modelių prie produktų — DI inžinieriaus mąstysena
module: Pagrindai
order: 1
---

# Nuo modelių prie produktų — DI inžinieriaus mąstysena

Modelis pats savaime nėra produktas. „ChatGPT“ langas yra produktas; už jo — modelis, sistemos promptas, atmintis, įrankiai ir daugybė inžinerinių sprendimų. Šis kursas yra apie tą **inžineriją**: kaip iš galingo, bet nenuspėjamo modelio sukurti patikimą programą.

## Kuo DI inžinerija skiriasi nuo įprastos

Įprastoje programoje tas pats įėjimas duoda tą patį išėjimą. Su LLM:

- atsakymas yra **tikimybinis** — tas pats promptas gali duoti skirtingus rezultatus;
- modelis gali **haliucinuoti** — užtikrintai pateikti klaidą;
- elgesį valdai ne `if/else`, o **kontekstu ir instrukcijomis**.

Todėl DI inžinieriaus darbas — ne „parašyti teisingą promptą vieną kartą“, o **sukurti sistemą, kuri lieka teisinga net kai modelis klysta**.

## Trys svertai, kuriuos valdai

Kiekvienai užduočiai turi tris įtakos taškus:

1. **Modelis** — kurį pasirinkti (greitas ir pigus vs. galingas ir brangus).
2. **Kontekstas** — ką modelis mato: sistemos promptą, pavyzdžius, ištrauktus dokumentus, pokalbio istoriją.
3. **Apribojimai** — kaip suvaržai išėjimą: struktūrizuotas formatas, įrankiai, validacija, pakartotiniai bandymai.

> 90 % kokybės problemų sprendžiamos ne keičiant modelį, o gerinant **kontekstą** ir **apribojimus**.

## Kaip atrodo gamybinė DI programa

```text
Vartotojas → [Programa]
                ├─ surenka kontekstą (DB, dokumentai, istorija)
                ├─ sudaro promptą (sistema + kontekstas + įvestis)
                ├─ kviečia modelį (su parametrais ir įrankiais)
                ├─ validuoja išėjimą (formatas, taisyklės)
                └─ grąžina / kartoja / perduoda žmogui
```

Visa šio kurso esmė — užpildyti šias dėžutes tikru, veikiančiu kodu.

## Mūsų darbinis įrankis

Pavyzdžiuose naudosime **LiteLLM** — biblioteką, leidžiančią tuo pačiu kodu kalbėti su „Claude“, „Gemini“ ar GPT, keičiant tik modelio pavadinimą. Būtent ją naudoja ir ši platforma.

```python
from litellm import completion

resp = completion(
    model="claude-haiku-4-5-20251001",
    messages=[{"role": "user", "content": "Pasisveikink viena eilute."}],
)
print(resp.choices[0].message.content)
```

## Ką sukursi iki kurso pabaigos

Suprasi visą kelią nuo prompto iki gamybos: struktūrizuotus atsakymus, įrankių iškvietimą, RAG, agentus, vertinimą, saugą ir kaštų valdymą — viską su kodu.

> **Mentoriaus patarimas:** paklausk „Kodėl LLM programos yra tikimybinės ir ką tai keičia projektuojant?“

Toliau: kaip modelis iš tikrųjų „mato“ tekstą — **tokenai, konteksto langas ir įterpiniai**.
