---
title: Pokalbių robotas su istorija
module: Chatbotas
order: 3
---

# Pokalbių robotas su istorija

Vienkartinis API kvietimas atsako į vieną klausimą. Chatbotui reikia istorijos: ankstesnių vartotojo ir asistento žinučių.

**Po šios pamokos galėsi:**

- sukurti terminalo chatbotą su pokalbio istorija;
- paaiškinti, kodėl istorija būtina tęstiniam pokalbiui;
- įvardyti strategijas, kai istorija tampa per ilga.

## Žinučių sąrašas

```python
messages = [
    {"role": "system", "content": "Esi kantrus Python mentorius."},
    {"role": "user", "content": "Kas yra funkcija?"},
    {"role": "assistant", "content": "Funkcija yra pakartotinai naudojamas kodo blokas."},
    {"role": "user", "content": "Duok pavyzdį."},
]
```

Modelis mato visą sąrašą ir atsako pagal kontekstą.

## Terminalo chatbotas

```python
from litellm import completion

messages = [{"role": "system", "content": "Atsakyk kaip Python mentorius."}]

while True:
    user_text = input("Tu: ")
    if user_text.lower() in {"exit", "quit"}:
        break

    messages.append({"role": "user", "content": user_text})
    response = completion(model="claude-haiku-4-5-20251001", messages=messages)
    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    print("AI:", answer)
```

## Ribos

Istorija negali augti be galo. Ilgame pokalbyje reikės:

- trumpinti seną istoriją;
- saugoti tik svarbius faktus;
- riboti žinučių skaičių;
- naudoti duomenų bazę, jei kuri realią programą.

## Pasitikrink save

**1. Kodėl po kiekvieno atsakymo `messages.append` kviečiamas du kartus?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Į istoriją dedama ir vartotojo žinutė, ir asistento atsakymas. Jei asistento atsakymo nepridėsi, kitame ėjime modelis nematys, ką pats sakė.

</details>

**2. Kas nutiktų, jei kiekvieną kartą siųstum tik paskutinę žinutę?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Pokalbis prarastų tęstinumą: „duok pavyzdį“ modelis nesuprastų, nes nežinotų, apie ką kalbama. Kiekvienas kvietimas be istorijos yra naujas pokalbis.

</details>

**3. Kokios trys strategijos, kai istorija tampa per ilga?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Trumpinti (laikyti paskutines N žinučių), apibendrinti senas žinutes santrauka, saugoti žinutes duomenų bazėje ir įkelti tik dalį.

</details>

## Mini projektas

Sukurk „Python mokytojo“ chatbotą terminale. Jis turi:

- atsakyti lietuviškai;
- aiškinti pradedančiajam;
- duoti mažas užduotis;
- priimti komandą `summary`, kuri trumpai apibendrina, ką vartotojas mokėsi.

> **Užduoties patikra:** įklijuok savo chatbotą mentoriui ir paklausk: „Ar mano `summary` komanda teisingai naudoja istoriją? Kaip ją padaryčiau pigesnę tokenų prasme?“

> **Mentoriaus patarimas:** paklausk „Kaip išsaugoti chatbot istoriją į JSON failą?“

Toliau: darysime dokumentų klausimų atsakymų įrankį su RAG idėja.
