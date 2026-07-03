---
title: Vaizdai, garsas ir multimodalinis DI
module: Multimodalinis DI
order: 6
---

# Vaizdai, garsas ir multimodalinis DI

DI jau neapsiriboja tekstu. Daug modernių sistemų gali suprasti ar kurti vaizdus, garsą, vaizdo įrašus, lenteles ir dokumentus. Tai vadinama **multimodaliniu DI** — sistema dirba su daugiau nei viena informacijos rūšimi.

**Po šios pamokos galėsi:**

- panaudoti DI vaizdams, dokumentams ir garso įrašams suprasti;
- parašyti aiškesnį promptą vaizdui sukurti;
- žinoti, kur vaizdų analizė dažniausiai klysta.

## Ką gali multimodaliniai įrankiai

- Apibūdinti nuotrauką ar diagramą.
- Perskaityti tekstą paveikslėlyje.
- Padėti suprasti skaičiuoklę ar PDF.
- Sukurti iliustraciją pagal aprašymą.
- Perrašyti garso įrašą į tekstą.
- Išversti ar sutrumpinti vaizdo įrašo transkriptą.
- Padėti kurti skaidres, plakatus ar socialinių tinklų turinį.

## Vaizdų analizė

Kai įkeli vaizdą, DI gali pastebėti objektus, tekstą, išdėstymą ir kontekstą. Tačiau jis vis tiek gali klysti, ypač kai:

- vaizdas neryškus;
- svarbios smulkios detalės;
- reikia medicininės, teisinės ar techninės interpretacijos;
- prašai identifikuoti asmenį ar jautrią informaciją.

Geras promptas:

```text
Apibūdink, ką matai šiame paveikslėlyje.
Atskirk tai, ką tikrai matai, nuo spėjimų.
Jei tekstas neįskaitomas, taip ir pasakyk.
```

## Vaizdų kūrimas

Kuriant vaizdus svarbiausi yra:

- tema;
- stilius;
- kompozicija;
- apšvietimas;
- spalvos;
- formatas;
- ko vengti.

Pavyzdys:

```text
Sukurk šiltą, realistišką iliustraciją apie žmogų, kuris mokosi su DI asistentu prie virtuvės stalo.
Stilius: moderni redakcinė iliustracija, natūralios spalvos, aiški kompozicija.
Venk futuristinių robotų ir chaotiškų detalių.
```

## Garsas ir transkripcija

DI gali perrašyti susitikimą, paskaitą ar balso pastabą. Po transkripcijos gali prašyti:

- santraukos;
- veiksmų sąrašo;
- sprendimų ir atvirų klausimų;
- tono analizės;
- vertimo.

Svarbu: jei įraše yra kitų žmonių balsai, pagalvok apie sutikimą ir privatumo taisykles.

## Pasitikrink save

**1. Kada vaizdų analizė klysta dažniausiai?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kai vaizdas neryškus, svarbios smulkios detalės, reikia medicininės, teisinės ar techninės interpretacijos, arba prašoma identifikuoti asmenį.

</details>

**2. Kokie elementai svarbiausi prompte vaizdui sukurti?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Tema, stilius, kompozicija, apšvietimas, spalvos, formatas ir — dažnai pamirštama — ko vengti.

</details>

**3. Apie ką pagalvoti prieš transkribuojant susitikimo įrašą?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Apie kitų dalyvių sutikimą ir privatumo taisykles — įraše yra ne tik tavo balsas ir ne tik tavo informacija.

</details>

## Mini užduotis

Pasirink vieną vaizdą arba dokumentą ir paprašyk DI:

```text
Apibūdink turinį.
Išskirk svarbiausias detales.
Pažymėk, kur gali būti neaiškumų.
Pasiūlyk 3 klausimus, kuriuos turėčiau užduoti toliau.
```

> **Užduoties patikra:** DI apibūdinimą įklijuok mentoriui ir paklausk: „Kurios šio apibūdinimo dalys yra stebėjimas, o kurios — spėjimas, kurį reikėtų tikrinti?“

> **Mentoriaus patarimas:** paklausk „Kaip parašyti gerą promptą vaizdui sukurti, jei nežinau dizaino terminų?“

Toliau: suprasime, kaip DI randa informaciją dokumentuose ir kaip veikia RAG.
