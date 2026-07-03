---
title: Pirmas LLM API įrankis
module: API
order: 2
---

# Pirmas LLM API įrankis

Šioje pamokoje sukursi mažą Python įrankį, kuris siunčia tekstą modeliui ir gauna atsakymą. Tai pamatas chatbotams, dokumentų analizatoriams ir agentams.

**Po šios pamokos galėsi:**

- sukurti komandų eilutės įrankį su LLM kvietimu;
- perduoti argumentus iš terminalo į programą;
- tvarkyti klaidas taip, kad vartotojas suprastų, kas nutiko.

## Projekto idėja

Sukurk komandą:

```bash
python ask_ai.py "Paaiškink kas yra API"
```

Ji turi išvesti DI atsakymą terminale.

## Minimalus kodas

```python
import sys
from litellm import completion


def ask_ai(question: str) -> str:
    response = completion(
        model="claude-haiku-4-5-20251001",
        messages=[
            {"role": "system", "content": "Atsakyk trumpai ir aiškiai lietuviškai."},
            {"role": "user", "content": question},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    question = " ".join(sys.argv[1:])
    if not question:
        raise SystemExit("Pateik klausimą.")
    print(ask_ai(question))
```

## Ką turi suprasti

- Kur saugomas API raktas.
- Kas yra `system` ir `user` žinutės.
- Kodėl verta riboti temperatūrą.
- Kaip tvarkyti klaidas, kai nėra interneto ar rakto.

## Pasitikrink save

**1. Ką daro `" ".join(sys.argv[1:])`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Sujungia visus terminale po programos pavadinimo įrašytus žodžius į vieną klausimą. `sys.argv[0]` yra pačios programos vardas, todėl jis praleidžiamas.

</details>

**2. Kodėl čia pasirinkta `temperature=0.3`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Įrankis skirtas atsakymams į klausimus, ne kūrybai — žema temperatūra duoda nuoseklesnius, mažiau atsitiktinius atsakymus.

</details>

**3. Kas nutiks, jei paleisi įrankį be interneto?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`completion` mes išimtį (pvz., ryšio klaidą). Gera programa ją pagauna su `try/except` ir parodo žmogui suprantamą žinutę vietoj ilgo traceback.

</details>

## Mini projektas

Papildyk įrankį:

- pridėk `--short` režimą;
- pridėk `--english` režimą;
- klaidas parodyk aiškia žinute vartotojui.

> **Užduoties patikra:** įklijuok savo kodą mentoriui ir paprašyk: „Peržiūrėk mano klaidų tvarkymą: kokių situacijų dar nepagaunu?“

> **Mentoriaus patarimas:** paklausk „Paaiškink šį API kvietimo kodą taip, kad suprasčiau kiekvieną eilutę.“

Toliau: kursime pokalbių robotą su atmintimi.
