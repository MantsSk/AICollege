---
title: Promptai, kurie veikia
module: Promptų inžinerija
order: 3
---

# Promptai, kurie veikia

Promptas yra tavo instrukcija DI modeliui. Geras promptas nėra ilgas dėl ilgio. Jis aiškiai pasako, ko nori, kokiame kontekste, kokiu formatu ir pagal kokius kriterijus.

**Po šios pamokos galėsi:**

- sudėlioti promptą pagal formulę: tikslas, kontekstas, vaidmuo, formatas, kriterijai, apribojimai;
- atpažinti, kodėl silpnas promptas duoda bendrą, niekam nepritaikytą atsakymą;
- iteruoti atsakymą, o ne pasitenkinti pirmu juodraščiu.

## Paprasta formulė

Naudok šią struktūrą:

```text
Tikslas: ką noriu gauti?
Kontekstas: ką DI turi žinoti?
Vaidmuo: iš kokios perspektyvos atsakyti?
Formatas: kaip pateikti atsakymą?
Kokybės kriterijai: kas bus laikoma geru rezultatu?
Apribojimai: ko vengti?
```

## Silpnas ir stiprus promptas

Silpnas:

```text
Parašyk man CV.
```

Į silpną promptą modelis paprastai atsako maždaug taip:

```text
Vardas Pavardė
Ambicingas ir motyvuotas specialistas, turintis puikius komunikacijos
įgūdžius ir gebėjimą dirbti komandoje...
```

Pastebėk, kas įvyko: modelis nieko apie tave nežino, todėl užpildė CV skambiomis, bet tuščiomis frazėmis, kurias darbdaviai mato šimtus kartų per dieną. Tai ne modelio klaida — jis padarė geriausia, ką galėjo be konteksto.

Stipresnis:

```text
Padėk man sukurti vieno puslapio CV jaunesniojo duomenų analitiko pozicijai.
Kontekstas: turiu 6 mėn. savarankiško mokymosi patirties, moku Excel, SQL pagrindus ir Python pradmenis.
Tonas: profesionalus, bet paprastas.
Formatas: skyriai „Profilis“, „Įgūdžiai“, „Projektai“, „Patirtis“, „Mokymasis“.
Nesugalvok faktų. Jei trūksta informacijos, užduok klausimus.
```

Su šiuo promptu geras modelis dažniausiai pradės ne nuo CV, o nuo klausimų: kokių projektų turi, kokio darbo ieškai, ką nori paryškinti. Būtent to ir norime — atsakymo, pagrįsto tavo faktais, o ne išgalvotomis savybėmis.

## Penkios technikos

**1. Paprašyk klausimų prieš atsakymą.**

Jei užduotis neaiški:

```text
Prieš atsakydamas užduok iki 5 klausimų, kurie padėtų tau parengti geresnį rezultatą.
```

**2. Duok pavyzdį.**

Jei nori konkretaus stiliaus, įklijuok pavyzdį ir paprašyk laikytis jo ritmo, ilgio ar tono.

**3. Paprašyk alternatyvų.**

```text
Pateik 3 variantus: konservatyvų, kūrybišką ir labai trumpą.
```

**4. Paprašyk kritikos.**

```text
Įvertink savo atsakymą: kas silpna, kas neaišku, ką reikėtų patikrinti?
```

**5. Iteruok.**

Pirmas atsakymas dažnai yra juodraštis. Tęsk:

```text
Padaryk konkrečiau.
Sutrumpink per pusę.
Pridėk pavyzdžių.
Pašalink žargoną.
Pritaikyk pradedančiajam.
```

## Naudingi promptų šablonai

Mokymuisi:

```text
Paaiškink [tema] taip, lyg būčiau pradedantysis.
Tada duok analogiją, vieną praktinį pavyzdį ir 3 klausimus pasitikrinimui.
```

Sprendimams:

```text
Padėk palyginti [A] ir [B].
Sudaryk lentelę pagal kriterijus: kaina, pastangos, rizika, ilgalaikė vertė.
Pabaigoje pateik rekomendaciją ir kada ji būtų neteisinga.
```

Rašymui:

```text
Perrašyk tekstą aiškiau ir šilčiau.
Išlaikyk mano mintis, bet sutrumpink 30%.
Nenaudok perdėto marketingo tono.
```

## Pasitikrink save

**1. Kodėl silpnas promptas „Parašyk man CV“ duoda tuščią, šabloninį rezultatą?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Modelis neturi jokio konteksto apie tave, todėl užpildo spragas bendriausiomis frazėmis. Kuo mažiau konteksto duodi, tuo labiau atsakymas panašus į vidurkį visų internete matytų tekstų.

</details>

**2. Iš kokių šešių dalių susideda prompto formulė?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Tikslas, kontekstas, vaidmuo, formatas, kokybės kriterijai ir apribojimai.

</details>

**3. Ką daryti, jei pirmas atsakymas nepatinka?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Iteruoti: prašyti konkrečiau, trumpiau, su pavyzdžiais, be žargono, pritaikyti auditorijai. Pirmas atsakymas — juodraštis, ne galutinis rezultatas.

</details>

## Mini užduotis

Paimk vieną savo silpną promptą ir perrašyk jį pagal formulę: tikslas, kontekstas, vaidmuo, formatas, kriterijai, apribojimai.

> **Užduoties patikra:** įklijuok abu variantus mentoriui ir paprašyk: „Palygink šiuos du promptus: kurių formulės dalių trūksta antrajame ir kaip jį dar patobulinti?“

> **Mentoriaus patarimas:** įklijuok savo promptą ir paklausk „Perrašyk jį taip, kad atsakymas būtų konkretesnis ir lengviau patikrinamas.“

Toliau: mokysimės tikrinti DI atsakymus ir saugotis klaidų.
