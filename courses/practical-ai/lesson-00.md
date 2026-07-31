---
title: Pirmasis geras promptas
module: 1 · Aiški užklausa
order: 0
---

# Pirmasis geras promptas

Promptas yra užduotis, kurią parašai dirbtiniam intelektui (DI). Kuo aiškiau paaiškini, ko nori, tuo naudingesnį atsakymą gali gauti.

Šioje pamokoje iš neaiškaus vieno sakinio sukursi konkretų promptą, kurį galėtum naudoti darbe ar mokydamasis.

## Ką išmoksi

Baigęs pamoką gebėsi:

- paaiškinti, kas yra promptas;
- atpažinti, kodėl užklausa yra per daug neaiški;
- promptui pateikti reikalingą kontekstą;
- nurodyti pageidaujamą atsakymo formatą;
- pasakyti DI, ką daryti, kai informacijos trūksta.

## 1. Kas yra promptas?

Promptas – tai tavo žinutė DI modeliui. Tai gali būti klausimas, nurodymas arba užduotis su papildoma informacija.

Paprastas promptas:

```text
Sutrumpink šį tekstą.
```

DI supranta bendrą veiksmą, bet jam lieka daug neatsakytų klausimų:

- kam skirtas rezultatas;
- koks turi būti jo ilgis;
- ką svarbiausia išsaugoti;
- kokiu formatu pateikti atsakymą;
- ką daryti su neaiškia informacija.

DI gali bandyti tai atspėti. Kartais atspės gerai, kartais – ne. Patikimesnis kelias yra svarbias sąlygas parašyti pačiame prompte.

## 2. Keturi gero prompto elementai

Pirmiems promptams naudok paprastą struktūrą:

```text
Užduotis + kontekstas + rezultato formatas + ribos
```

### Užduotis

Pasakyk, ką tiksliai turi padaryti DI.

```text
Iš susitikimo užrašų parenk trumpą santrauką.
```

Vartok konkretų veiksmą: `apibendrink`, `palygink`, `sugrupuok`, `paaiškink`, `pasiūlyk` arba `perrašyk`.

### Kontekstas

Pateik informaciją, kurios reikia užduočiai atlikti.

```text
Santrauka skirta projekto komandai, kuri nedalyvavo susitikime.
Žemiau pateikiu susitikimo užrašus.
```

DI nežino tavo situacijos, įmonės ar ankstesnių pokalbių, jei jų nepateikei šiame pokalbyje. Svarbų kontekstą geriau parašyti tiesiogiai.

### Rezultato formatas

Nurodyk, kaip turi atrodyti atsakymas.

```text
Pateik:
1. trijų punktų santrauką;
2. sutartų darbų sąrašą;
3. prie kiekvieno darbo nurodyk atsakingą žmogų ir terminą.
```

Formatas padeda gauti atsakymą, kurį lengva perskaityti ir panaudoti.

### Ribos

Pasakyk, ko DI negali daryti arba kaip elgtis, kai informacijos nepakanka.

```text
Naudok tik pateiktus užrašus. Nieko neišgalvok.
Jei trūksta atsakingo žmogaus ar termino, pažymėk „nenurodyta“.
```

Ši dalis negarantuoja tobulo atsakymo, tačiau aiškiai nustato tavo lūkesčius ir palengvina rezultato tikrinimą.

**Pasitikrink.** Prompte „Parašyk laišką klientui, kad užsakymas vėluoja“ – kurių iš keturių elementų labiausiai trūksta?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Užduotis aiški, tačiau trūksta **konteksto**, **formato** ir **ribų**: nenurodyta, kiek vėluoja užsakymas ir kokia nauja data, koks laiško tonas ir ilgis, ar galima siūlyti kompensaciją. Be šių dalių DI turės daug spėlioti, o rezultatą bus sunku patikrinti.

</details>

## 3. Nuo migloto iki naudingo prompto

Tarkime, turi tokius susitikimo užrašus:

```text
Tomas iki penktadienio atnaujins pagrindinio puslapio tekstą.
Rūta laukia naujų produkto nuotraukų.
Reklamos biudžetas dar nenuspręstas.
Kitas susitikimas – antradienį 10:00.
```

Per trumpas promptas:

```text
Sutvarkyk šiuos užrašus.
```

Žodis „sutvarkyk“ nepaaiškina, kokio rezultato tikiesi. DI gali perrašyti tekstą, sutrumpinti jį arba pakeisti jo toną.

Aiškesnis promptas:

```text
Užduotis: iš pateiktų susitikimo užrašų parenk santrauką projekto komandai.

Rezultatas:
- svarbiausi sprendimai;
- sutarti darbai su atsakingu žmogumi ir terminu;
- neatsakyti klausimai.

Taisyklės: naudok tik pateiktą informaciją. Jei atsakingas žmogus arba
terminas nenurodytas, rašyk „nenurodyta“. Nieko neišgalvok.

Užrašai:
Tomas iki penktadienio atnaujins pagrindinio puslapio tekstą.
Rūta laukia naujų produkto nuotraukų.
Reklamos biudžetas dar nenuspręstas.
Kitas susitikimas – antradienį 10:00.
```

Antrasis variantas ilgesnis ne dėl grožio. Kiekviena jo dalis padeda valdyti atsakymą:

- aiški užduotis pasako, ką atlikti;
- auditorija paaiškina, kam skirtas rezultatas;
- formatas nurodo atsakymo struktūrą;
- taisyklės neleidžia tyliai užpildyti spragų spėjimais;
- užrašai pateikia medžiagą darbui.

## 4. Ar visada reikia ilgo prompto?

Ne. Paprastam klausimui gali pakakti vieno sakinio:

```text
Paaiškink, kas yra Python kintamasis, vienu sakiniu.
```

Promptą verta detalizuoti, kai:

- pirmas atsakymas nėra toks, kokio tikėjaisi;
- svarbus konkretus formatas;
- DI reikia tavo dokumento ar situacijos konteksto;
- atsakyme negalima spėlioti;
- tą pačią užduotį kartosi ne vieną kartą.

Tikslas nėra parašyti kuo ilgesnį promptą. Tikslas – pašalinti svarbiausias dviprasmybes.

## 5. Tobulink po vieną dalį

Jei DI atsakymas netinka, nereikia visko pradėti iš naujo. Pirmiausia įvardyk, kas blogai:

- per ilgas atsakymas → nurodyk apimtį;
- trūksta struktūros → nurodyk formatą;
- netinkamas tonas → įvardyk auditoriją ir toną;
- atsirado išgalvotų faktų → pateik šaltinį ir taisyklę nespėlioti;
- praleista svarbi dalis → aiškiai įtrauk ją į užduotį.

Pavyzdžiui:

```text
Sutrumpink atsakymą iki penkių punktų. Prie kiekvieno punkto pridėk
vieną citatą iš pateiktų užrašų.
```

Tai vadinama iteravimu: pamatai rezultatą, pakeiti vieną prompto dalį ir bandai dar kartą.

## 6. Praktinė užduotis

Laboratorijoje gausi tuos pačius netvarkingus susitikimo užrašus. Iš keturių dalių sudėsi savo promptą:

1. aiški užduotis;
2. reikalingas kontekstas;
3. atsakymo formatas;
4. taisyklė, kaip elgtis su trūkstama informacija.

Pildant laukus dešinėje iškart matysi visą savo promptą. Baigęs galėsi jį nukopijuoti ir išbandyti pasirinktame DI pokalbyje.

> **Užduoties patikra:** nukopijuok savo promptą mentoriui ir paklausk „Kurią mano prompto dalį reikėtų patikslinti?“

## Svarbiausia iš šios pamokos

- Promptas yra užduotis arba klausimas, kurį pateiki DI.
- Geras promptas turi aiškią užduotį ir reikalingą kontekstą.
- Nurodytas rezultato formatas sumažina netikėtų atsakymų.
- Ribos pasako, ką DI daryti, kai informacijos trūksta.
- Geras promptas nebūtinai ilgas – jame tiesiog neturi trūkti svarbių sąlygų.
- Pirmą atsakymą galima gerinti keičiant po vieną prompto dalį.

Kitoje pamokoje mokysimės tikrinti DI atsakymą: atskirsime pateiktus faktus nuo modelio spėjimų.
