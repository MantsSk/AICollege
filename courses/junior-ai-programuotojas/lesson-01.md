---
title: AI-assisted junior programuotojo workflow
module: Darbo eiga
order: 1
---

# AI-assisted junior programuotojo workflow

Junior programuotojui DI yra didelis pranašumas, bet tik tada, kai jis naudojamas kaip paaiškinantis partneris, o ne kaip aklas kodo generatorius. Tikslas: greičiau mokytis, geriau suprasti klaidas ir kurti mažus projektus.

**Po šios pamokos galėsi:**

- naudoti šešių žingsnių darbo eigą su DI;
- prašyti kodo paaiškinimo, o ne tik kodo;
- paversti klaidos pranešimą mokymosi medžiaga.

## Gera darbo eiga

1. Pats suformuluok problemą.
2. Paprašyk DI paaiškinti, ne tik parašyti kodą.
3. Paleisk kodą lokaliai.
4. Skaityk klaidas ir prašyk paaiškinimo.
5. Rašyk mažus testus.
6. Į GitHub kelk tai, ką supranti.

## Promptas kodo aiškinimui

```text
Paaiškink šį kodą pradedančiam programuotojui.
Eik eilutė po eilutės.
Pabaigoje parašyk:
- ką šis kodas daro;
- kokios galimos klaidos;
- kaip jį patobulinti.
```

## Promptas klaidai

```text
Padėk suprasti šią klaidą.
Kodas:
[įklijuok kodą]

Klaida:
[įklijuok klaidą]

Paaiškink priežastį paprastai.
Tada pasiūlyk mažiausią pataisymą.
Neperrašyk viso projekto, jei nebūtina.
```

## Pasitikrink save

**1. Kuo skiriasi „parašyk man kodą“ nuo „paaiškink man kodą“?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Pirmasis duoda rezultatą, kurio gali nesuprasti ir negalėsi pataisyti. Antrasis augina tavo supratimą — o suprastą kodą gali keisti, testuoti ir paaiškinti pokalbyje dėl darbo.

</details>

**2. Kodėl klaidos prompte prašoma „mažiausio pataisymo“?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kad DI neperrašytų viso projekto kodu, kurio nebeatpažinsi. Mažas pataisymas leidžia supranti, kas tiksliai buvo blogai.

</details>

**3. Ką iš šios darbo eigos verta kelti į GitHub?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Tik tai, ką supranti ir gali paaiškinti. Portfolio vertė — ne kodo kiekis, o gebėjimas jį apginti.

</details>

## Mini projektas

Sukurk paprastą Python komandų eilutės programą „task helper“, kuri leidžia:

- pridėti užduotį;
- parodyti užduočių sąrašą;
- pažymėti užduotį atlikta.

DI naudok tik paaiškinimams ir klaidų taisymui. Kiekvieną funkciją suprask pats.

> **Užduoties patikra:** įklijuok savo programą mentoriui ir paprašyk: „Užduok man 3 klausimus apie mano kodą, tarsi būtum interviuotojas. Nesakyk atsakymų — patikrink, ar suprantu.“

> **Mentoriaus patarimas:** paklausk „Padėk man mokytis programuoti su DI taip, kad netapčiau priklausomas nuo kopijavimo.“

Toliau: kviesime LLM API iš Python.
