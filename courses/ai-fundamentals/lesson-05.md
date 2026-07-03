---
title: Privatumas, etika ir saugus naudojimas
module: Atsakingas DI
order: 5
---

# Privatumas, etika ir saugus naudojimas

DI įrankiai tampa kasdieniai, todėl lengva pamiršti, kad jiems dažnai perduodame tekstą, dokumentus, nuotraukas, vardus, darbo informaciją ar jautrius planus. Atsakingas naudojimas prasideda nuo klausimo: ką aš duodu sistemai?

**Po šios pamokos galėsi:**

- atskirti, kokių duomenų į DI įrankius kelti nereikėtų;
- anonimizuoti jautrų tekstą prieš siųsdamas jį modeliui;
- prieš naudodamas DI darbe pasitikrinti organizacijos taisykles.

## Ko geriau nekelti į DI

Be aiškios priežasties ir tinkamų nustatymų nekelk:

- slaptažodžių, API raktų, prisijungimų;
- asmens kodų, banko duomenų, medicininių dokumentų;
- konfidencialių darbo dokumentų;
- kitų žmonių privačių duomenų be leidimo;
- dokumentų, kurių negalėtum parodyti pašaliniam žmogui.

Jei reikia pagalbos su jautriu tekstu, dažnai galima informaciją **anonimizuoti**:

```text
Vietoj tikrų vardų naudok: Klientas A, Darbuotojas B, Įmonė C.
Pašalink adresus, kodus, telefono numerius ir tikslias datas.
```

## Duomenų naudojimo klausimai

Skirtingi DI įrankiai turi skirtingas taisykles: vieni gali naudoti pokalbius modeliams gerinti, kiti leidžia tai išjungti, dar kiti skirti verslui su griežtesnėmis apsaugomis.

Prieš naudodamas DI darbui, pasitikrink:

- ar organizacija leidžia naudoti tokį įrankį;
- ar galima kelti vidinius dokumentus;
- ar pokalbiai naudojami mokymui;
- kur saugomi duomenys;
- ar reikia sutarties ar verslo plano.

## Šališkumas

Modeliai mokosi iš žmonių sukurtų duomenų, todėl gali perimti stereotipus, nevienodą reprezentaciją ar kultūrines prielaidas.

Naudingas promptas:

```text
Peržiūrėk atsakymą dėl galimo šališkumo.
Ar yra grupių, kurios nepagrįstai ignoruojamos?
Ar formuluotės gali būti neteisingai suprastos?
Pasiūlyk neutralesnę versiją.
```

## Autorystė ir sąžiningumas

DI gali padėti rašyti, bet verta aiškiai atskirti:

- tavo idėjas;
- DI pasiūlytą formą;
- faktus iš šaltinių;
- citatas ar duomenis, kuriuos būtina nurodyti.

Mokymesi pavojinga naudoti DI taip, kad jis pakeistų mąstymą. Geriau naudok jį kaip trenerį: tegul klausia, aiškina, duoda užuominas, peržiūri tavo bandymą.

## Saugaus naudojimo kontrolinis sąrašas

Prieš siųsdamas tekstą DI, paklausk:

- ar čia yra jautrių duomenų?
- ar turiu teisę šią informaciją kelti?
- ar atsakymas gali paveikti sveikatą, pinigus, teisę ar reputaciją?
- kaip patikrinsiu rezultatą?
- ar reikia žmogaus peržiūros?

## Pasitikrink save

**1. Kokių duomenų niekada nekelti į DI įrankius be aiškios priežasties?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Slaptažodžių ir API raktų, asmens kodų ir banko duomenų, konfidencialių darbo dokumentų, kitų žmonių privačių duomenų be jų leidimo.

</details>

**2. Kas yra anonimizavimas ir kada jis padeda?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Tikrų vardų, adresų, kodų ir tikslių datų pakeitimas bendriniais žymenimis (Klientas A, Įmonė B). Padeda, kai reikia DI pagalbos su jautriu tekstu, bet pačių duomenų atskleisti nereikia.

</details>

**3. Ką pasitikrinti prieš naudojant DI darbo dokumentams?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Ar organizacija leidžia tokį įrankį, ar galima kelti vidinius dokumentus, ar pokalbiai naudojami modelių mokymui, kur saugomi duomenys.

</details>

## Mini užduotis

Paimk vieną realų tekstą, kurį norėtum duoti DI, ir sukurk anonimizuotą versiją. Pašalink asmens duomenis, įmonių pavadinimus, tikslias sumas ar datas, jei jos nebūtinos.

> **Užduoties patikra:** įklijuok anonimizuotą versiją mentoriui ir paklausk: „Ar šiame tekste dar liko detalių, iš kurių būtų galima atpažinti asmenį ar įmonę?“

> **Mentoriaus patarimas:** paklausk „Padėk man anonimizuoti šį tekstą prieš naudojant DI, bet nekeisk pagrindinės prasmės.“

Toliau: pažvelgsime į vaizdus, garsą ir kitus multimodalinius DI įrankius.
