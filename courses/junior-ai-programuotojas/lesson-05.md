---
title: Mažas agentas su įrankiais
module: Agentai
order: 5
---

# Mažas agentas su įrankiais

Agentas yra DI programa, kuri gali naudoti įrankius. Junior lygyje geriausia pradėti nuo labai saugių įrankių: skaičiuotuvo, failo skaitymo arba užduočių sąrašo.

**Po šios pamokos galėsi:**

- sukurti agentą su dviem saugiais įrankiais;
- apibrėžti, ko agentui daryti negalima, dar prieš rašant kodą;
- dokumentuoti agento ribas README faile.

## Projekto idėja

Sukurk agentą „study planner“, kuris gali:

- priimti mokymosi tikslą;
- sudaryti planą;
- išsaugoti planą į tekstinį failą;
- perskaityti esamą planą.

## Įrankių ribos

Pradžioje neleisk agentui:

- trinti failų;
- siųsti el. laiškų;
- daryti mokėjimų;
- vykdyti nežinomo kodo.

Agentų saugumas yra ne priedas, o pagrindinė funkcija.

## Paprasta įrankio funkcija

```python
def save_plan(filename: str, content: str) -> str:
    if not filename.endswith(".txt"):
        return "Galima saugoti tik .txt failus."
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Planas išsaugotas: {filename}"
```

## Pasitikrink save

**1. Kuo agentas skiriasi nuo chatboto?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Chatbotas tik atsako tekstu. Agentas gali atlikti veiksmus — kviesti funkcijas, rašyti failus, ieškoti — todėl jo klaidos turi realių pasekmių.

</details>

**2. Kodėl `save_plan` tikrina failo plėtinį?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Tai saugumo riba: agentas gali kurti tik `.txt` failus ir negali perrašyti, pvz., programos kodo ar sisteminių failų. Ribos dedamos į patį įrankį, ne tik į promptą.

</details>

**3. Kodėl agentų saugumas — „pagrindinė funkcija, o ne priedas“?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Modelis gali suklysti ar būti apgautas per įvestį. Jei įrankiai leidžia pavojingus veiksmus, klaida virsta ištrintais failais ar išsiųstais laiškais — todėl ribos projektuojamos pirmiausia.

</details>

## Mini projektas

Sukurk agentą su dviem įrankiais:

- `save_plan(filename, content)`;
- `read_plan(filename)`.

Tada aprašyk README faile:

- ką agentas daro;
- kokios jo ribos;
- kokių veiksmų jam specialiai neleidai.

> **Užduoties patikra:** įklijuok savo README mentoriui ir paklausk: „Ar mano agento ribos realiai apsaugo nuo žalos, ar tik deklaruojamos? Ką dar apribotum?“

> **Mentoriaus patarimas:** paklausk „Kokios saugumo ribos būtinos pradedančiojo agentui?“

Toliau: supakuosime projektą portfolio pristatymui.
