---
title: Patikrink DI atsakymą: faktai ir spėjimai
module: 2 · Patikimas atsakymas
order: 1
---

# Patikrink DI atsakymą: faktai ir spėjimai

Praeitoje pamokoje išmokai parašyti aiškų promptą. Bet net ir į gerą užklausą DI gali atsakyti įtikinamai, o kartu ir neteisingai. Todėl antras svarbus įgūdis – **patikrinti atsakymą** prieš juo pasikliaunant.

Šioje pamokoje išmoksi atskirti, kas atsakyme paremta tavo pateikta informacija, o kas yra modelio spėjimas, ir kaip promptu sumažinti klaidų riziką.

## Ką išmoksi

Baigęs pamoką gebėsi:

- paaiškinti, kas yra DI „haliucinacija“;
- atskirti faktą (paremtą šaltiniu) nuo spėjimo;
- promptu leisti DI pasakyti „nežinau“;
- paprašyti citatų iš šaltinio;
- apriboti DI tik pateikta informacija;
- greitai patikrinti atsakymą pagal paprastą sąrašą.

## 1. Kodėl DI kartais „prasimano“

Net pažangiausi kalbos modeliai kartais sugeneruoja tekstą, kuris yra faktiškai neteisingas arba neatitinka pateikto konteksto. Šis reiškinys vadinamas **haliucinacija**.

Svarbiausia suprasti štai ką: DI rašo sklandų, užtikrintą tekstą nepriklausomai nuo to, ar jis teisingas. Todėl **įtikinamas tonas nėra teisingumo įrodymas**. Atsakymas gali skambėti profesionaliai ir vis tiek turėti prasimanytą skaičių, datą ar vardą.

## 2. Faktas ar spėjimas?

Pagrindinis tikrinimo įgūdis – žiūrėti į atsakymą teiginys po teiginio ir klausti: *ar tai galiu rasti man pateiktame šaltinyje?*

Tark, davei DI tokius susitikimo užrašus:

```text
Susitikimas vyko antradienį 10:00.
Tomas iki penktadienio atnaujins pagrindinio puslapio tekstą.
Reklamos biudžetas dar nenuspręstas.
```

O DI santraukoje parašė:

```text
1. Susitikimas vyko antradienį.
2. Tomas iki penktadienio atnaujins pagrindinį puslapį.
3. Reklamos biudžetas patvirtintas – 5000 eurų.
```

Pirmi du teiginiai **paremti šaltiniu**. Trečias yra **spėjimas**: šaltinyje parašyta priešingai – biudžetas dar nenuspręstas. Toks sakinys skamba konkrečiai (net su suma!), bet informacijos jam nėra. Būtent tokius teiginius reikia pastebėti.

## 3. Leisk DI pasakyti „nežinau“

Pagal Anthropic rekomendacijas, viena paprasčiausių priemonių – **aiškiai leisti modeliui pripažinti nežinojimą**. Be tokio leidimo DI linkęs užpildyti spragą spėjimu.

Pridėk į promptą sakinį:

```text
Jei informacijos nepakanka, parašyk „Neturiu pakankamai informacijos“, o ne spėk.
```

Tada vietoj išgalvoto atsakymo dažniau gausi sąžiningą „nežinau“, o tai daug lengviau pastebėti ir sutvarkyti nei paslėptą prasimanymą.

## 4. Prašyk citatų iš šaltinio

Kita rekomenduojama priemonė – **paremti atsakymą tiksliomis citatomis**. Paprašyk, kad prie kiekvieno teiginio DI pateiktų ištrauką iš šaltinio, o jei citatos nėra – teiginio neįtrauktų.

```text
Naudok tik pateiktus užrašus, ne savo bendrąsias žinias.
Prie kiekvieno teiginio pateik tikslią citatą iš užrašų.
Jei tinkamos citatos nerandi, to teiginio nerašyk.
```

Šis būdas veikia dviem kryptimis: jis grąžina DI prie tikro teksto ir kartu palieka tau lengvą būdą pasitikrinti – tiesiog žiūri, ar citata iš tikrųjų yra šaltinyje.

## 5. Greita atsakymo patikra

Prieš pasikliaudamas DI atsakymu, pereik keturis klausimus:

1. Ar kiekvieną teiginį galiu rasti šaltinyje?
2. Ar yra konkrečių skaičių, datų ar vardų, kurių šaltinyje nemačiau?
3. Ar DI kur nors pažymėjo „nežinau“ arba informacijos spragą?
4. Ar svarbiam sprendimui pasitikrinčiau dar ir nepriklausomu šaltiniu?

Jei bent vienas atsakymas kelia abejonių, teiginį reikia patikrinti, o ne priimti kaip faktą.

## 6. Net su gerais promptais tikrink pats

Pačioje Anthropic dokumentacijoje pabrėžiama: šios priemonės **gerokai sumažina** haliucinacijas, bet jų **visiškai nepašalina**. Ypač svarbiam ar rizikingam sprendimui kritinę informaciją visada patikrink pats.

Todėl DI naudinga laikyti greitu juodraščio rašytoju, o ne galutiniu žinių šaltiniu. Sprendimą ir atsakomybę pasilieki sau.

## 7. Praktinė užduotis

Laboratorijoje gausi trumpą šaltinį ir jo pagrindu parašytą DI atsakymą. Kiekvieną atsakymo teiginį suskirstysi į **paremtą šaltiniu** arba **modelio spėjimą**. Tada iš dviejų prompto papildymų pasirinksi tą, kuris labiausiai sumažina prasimanymų riziką.

> **Užduoties patikra:** nukopijuok DI atsakymą mentoriui ir paklausk „Kaip patikrinčiau, ar šie teiginiai paremti šaltiniu?“

## Svarbiausia iš šios pamokos

- DI gali rašyti įtikinamai ir kartu neteisingai – tai vadinama haliucinacija.
- Kiekvieną teiginį verta patikrinti: ar jį galiu rasti šaltinyje?
- Leidimas pasakyti „nežinau“ padeda pastebėti informacijos spragas.
- Prašymas pateikti citatas leidžia lengvai patikrinti atsakymą.
- Apribojimas tik pateikta informacija sumažina prasimanymus.
- Priemonės mažina, bet nepašalina klaidų – svarbią informaciją visada tikrink pats.

Kitoje pamokoje šias taisykles surašysime į vieną aiškią asistento instrukciją su ribomis ir rezultato formatu.
