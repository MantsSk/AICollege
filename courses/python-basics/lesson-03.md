---
title: Sąrašai ir ciklai – asistentas, kuris kalbasi ne vieną kartą
module: Python pagrindai
order: 3
---

# Sąrašai ir ciklai – asistentas, kuris kalbasi ne vieną kartą

> **Trukmė:** 8 akademinės valandos. Praktikai ir mini projektui skirk bent 5 valandas.

## Trumpa anotacija

Iki šiol asistentas atsakydavo į vieną klausimą ir baigdavo darbą – programa paleidžiama, `input()` gauna vieną žinutę, atspausdinamas atsakymas, ir failas baigiasi. Realus pokalbis taip neatrodo: žmogus užduoda kelis klausimus iš eilės, o programa turi prisiminti, kas jau buvo paklausta. Šioje pamokoje išmoksi saugoti kelias reikšmes viename sąraše (`list`), automatiškai apdoroti kiekvieną elementą su `for`, kartoti veiksmą, kol vartotojas pats nuspręs sustoti, su `while`, ir valdyti ciklo eigą komandomis `break` bei `continue`. Baigęs pamoką turėsi „Asistentą 0.2“ – programą, kuri kalbasi tol, kol išgirsta „baigti“, ir po pokalbio parodo visų užduotų klausimų sąrašą. Šie įgūdžiai – sąrašai ir ciklai – yra tas pats mechanizmas, kuriuo tikros AI sistemos apdoroja tūkstančius duomenų eilučių ir prisimena visą pokalbio istoriją.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- sukurti sąrašą (`list`) ir pasiekti jo elementus per teigiamą arba neigiamą indeksą;
- pridėti, pakeisti ir pašalinti sąrašo elementus su `append()`, `remove()` ir priskyrimu per indeksą;
- su `for` ciklu apdoroti kiekvieną sąrašo elementą ir su `enumerate()` pridėti numeraciją;
- naudoti `range()` fiksuotam pasikartojimų skaičiui arba indeksų sekai generuoti;
- filtruoti ir kaupti duomenis cikle, naudojant tuščią sąrašą kaip „kaupiklį“;
- parašyti `while` ciklą, kuris kartoja veiksmą, kol galioja sąlyga, ir teisingai jį užbaigti;
- valdyti ciklo eigą su `break` ir `continue`, aiškiai suprasdamas jų skirtumą;
- sukurti asistentą, kuris kalbasi tol, kol vartotojas pats nuspręs baigti pokalbį, ir saugo klausimų istoriją.

## Būtinos ankstesnės žinios

Prieš pradėdamas turėtum laisvai naudoti kintamuosius ir duomenų tipus iš pirmos pamokos bei sąlygas `if`/`elif`/`else`, palyginimo operatorius ir `and`/`or`/`not` iš antros pamokos. Ypač svarbu, kad mokėtum patikrinti tuščią įvestį (`if not message`) ir sunormalizuoti tekstą su `.lower()` bei `.strip()` – šiuos veiksmus dabar naudosime kiekviename cikle. Antroje pamokoje sukūrei „Asistentą 0.1“, kuris vieną kartą priima klausimą ir vieną kartą atsako. Jei tas failas dar neveikia savarankiškai, grįžk prie jo prieš tęsdamas – šioje pamokoje būtent jo `if`/`elif`/`else` sprendimų medį perkelsime į ciklą, kuris leis kalbėtis ne vieną, o daug kartų iš eilės.

## 1. Įtraukianti pradžia: kodėl asistentui reikia atminties apie *kelis* dalykus?

Kasdienis pavyzdys: pirkinių sąrašas telefone. Kiekvienai prekei nekuri naujo teksto pranešimo – turi vieną sąrašą, į kurį prekes prideda, pažymėtas išbraukia, ir bet kada gali peržiūrėti visas iš karto. Tas pats principas galioja ir pokalbio programai: ji turi prisiminti ne vieną, o daug klausimų.

Iki šiol vienas kintamasis saugojo vieną reikšmę: `age = 25`. Bet realaus asistento pokalbis susideda iš daugybės klausimų, o pirkinių programa – iš daugybės prekių. Tam reikia struktūros, kuri vienu vardu talpina kelias reikšmes – tai `list` (sąrašas).

```python
topics = ["kursai", "kaina", "kontaktai"]
print(topics[0])      # kursai
print(topics[-1])     # kontaktai
print(len(topics))    # 3
```

```text
kursai
kontaktai
3
```

> **Išbandyk pats:** nežiūrėdamas į paaiškinimą, pasakyk, ką atspausdintų `topics[1]`, ir kiek elementų grąžintų `len(topics)`, jei prie sąrašo pridėtum dar vieną temą.

## 2. Pagrindinės sąvokos

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| `list` (sąrašas) | Vienu vardu saugoma tvarkinga reikšmių seka | Pirkinių sąrašas telefone | Kai reikia saugoti kelias panašias reikšmes iš karto | Sąrašas supainiojamas su viena reikšme |
| Indeksas | Elemento vieta sąraše, skaičiuojama nuo 0 | Buto numeris daugiabutyje, kur pirmas butas – „0“ | Norint pasiekti konkretų elementą | Manoma, kad pirmas elementas turi indeksą 1 |
| `for` ciklas | Kodo blokas, automatiškai pakartojamas kiekvienam elementui | Konvejeris, kuriuo kiekvienas daiktas paeiliui patikrinamas | Kai reikia apdoroti visus žinomo rinkinio elementus | Pamirštama, kad ciklo kintamasis keičiasi kiekvieną apsisukimą |
| `range()` | Funkcija, generuojanti skaičių seką | Numeruotas bilietas eilėje nuo A iki B | Kai reikia pasikartoti fiksuotą skaičių kartų arba naudoti indeksą | Manoma, kad `range(5)` įtraukia skaičių 5 |
| `while` ciklas | Kodo blokas, kartojamas, kol sąlyga teisinga | Virdulio šildymas, kol vanduo neužverda | Kai kartojimų skaičius iš anksto nežinomas | Pamirštama atnaujinti sąlygos kintamąjį – gaunamas begalinis ciklas |
| `break` | Komanda, iškart nutraukianti visą ciklą | Signalas „gana, baigėme“ visai eilei | Kai pasiektas aiškus išėjimo taškas | Manoma, kad `break` praleidžia tik vieną apsisukimą |
| `continue` | Komanda, praleidžianti likusią ciklo dalį ir grąžinanti prie kito apsisukimo | „Šis atvejis netinka, imu kitą“ | Kai reikia praleisti netinkamus duomenis, bet tęsti ciklą | Manoma, kad `continue` baigia visą ciklą |

Trumpas bendras pavyzdys:

```python
numbers = [4, 8, 15, 16]

for number in numbers:
    if number == 15:
        continue
    if number == 16:
        break
    print(number)
```

```text
4
8
```

Skaičius `15` praleidžiamas su `continue` (ciklas tiesiog grįžta prie kito elemento), o pasiekus `16` suveikia `break` – ciklas nutrūksta dar prieš `print()`, todėl `16` niekada nepamatome.

## 3. Vizualūs paaiškinimai

### Vizualizacija A – sąrašas ir indeksai

```text
Indeksas:          0             1             2               3
                ┌────────┐   ┌────────┐   ┌───────────┐   ┌──────────────┐
topics    ───►  │ kursai │   │ kaina  │   │ kontaktai │   │ tvarkaraštis │
                └────────┘   └────────┘   └───────────┘   └──────────────┘
Neig. indeksas:    -4            -3            -2               -1
```

**Iliustracijos pavadinimas:** „Vienas sąrašas, du būdai skaičiuoti indeksą“
**Ką ji turi parodyti:** kad tą patį elementą galima pasiekti ir iš pradžios (teigiamu indeksu), ir nuo galo (neigiamu indeksu).
**Kokie elementai turi būti matomi:** keturios dėžutės su reikšmėmis, virš jų teigiami indeksai nuo `0`, po jais – neigiami indeksai nuo `-1`.
**Siūlomas vaizdo generavimo promptas:** „Minimalistinė edukacinė vektorinė schema lietuvių kalba: keturios dėžutės su tekstais kursai, kaina, kontaktai, tvarkaraštis; virš jų indeksai 0, 1, 2, 3, po jais indeksai -4, -3, -2, -1; aiškios etiketės, aukštas kontrastas.“

### Vizualizacija B – `for` ciklas žingsnis po žingsnio

```text
questions = ["Kokia kaina?", "Kada prasideda?", "Ar gausiu pažymėjimą?"]

1 žingsnis:  question = "Kokia kaina?"          → print("Tikrinama: Kokia kaina?")
2 žingsnis:  question = "Kada prasideda?"        → print("Tikrinama: Kada prasideda?")
3 žingsnis:  question = "Ar gausiu pažymėjimą?"  → print("Tikrinama: Ar gausiu pažymėjimą?")
4 žingsnis:  sąrašas baigėsi → ciklas sustoja automatiškai, be papildomos sąlygos
```

**Iliustracijos pavadinimas:** „`for` ciklas kaip konvejeris“
**Ką ji turi parodyti:** kad kintamasis `question` kiekvieną žingsnį gauna kitą reikšmę iš sąrašo, o ciklas savaime sustoja, kai elementai baigiasi.
**Kokie elementai turi būti matomi:** trys eilės su žingsnio numeriu, einamąja reikšme ir atliekamu veiksmu, paskutinė eilė – sustojimo žyma.
**Siūlomas vaizdo generavimo promptas:** „Horizontali proceso diagrama lietuvių kalba, vaizduojanti konvejerio juostą su trimis dėžėmis (klausimais), kiekviena dėžė paeiliui patenka į patikros stotelę, paskutinis segmentas pažymėtas kaip 'ciklas baigtas'; aiškios rodyklės, švelni spalvų paletė.“

### Vizualizacija C – `while` ciklas su `break` ir `continue`

```text
                 ┌──────────────────────────┐
                 │      while True:          │
                 └────────────┬─────────────┘
                              ▼
                message = input("Tu: ").strip()
                              │
                 ┌────────────┴─────────────┐
                 │  message == "baigti" ?    │
                 └─────┬────────────────┬────┘
                     taip               ne
                       │                 │
                    break          ┌─────┴──────┐
               (išeina iš viso     │ message     │
                ciklo, programa    │ tuščias?    │
                tęsiasi toliau)    └───┬─────┬───┘
                                  taip      ne
                                    │        │
                                continue   apdoroti žinutę,
                             (grįžta į     parodyti atsakymą
                              ciklo        ir grįžti į
                              pradžią)     ciklo pradžią
```

**Iliustracijos pavadinimas:** „Kur ciklą nutraukia `break`, o kur tik praleidžia `continue`“
**Ką ji turi parodyti:** kad `break` veda tiesiai už ciklo ribų, o `continue` grąžina atgal į ciklo pradžią, nepasiekus paskutinės eilutės.
**Kokie elementai turi būti matomi:** ciklo pradžios blokas, du sprendimo rombai, aiškiai atskirtos `break` ir `continue` šakos su skirtingomis rodyklėmis.
**Siūlomas vaizdo generavimo promptas:** „Vertikali sprendimų medžio schema lietuvių kalba su romboidiniais sprendimo blokais 'message == baigti?' ir 'message tuščias?', viena šaka pažymėta žodžiu break ir rodykle už schemos ribų, kita šaka pažymėta žodžiu continue ir rodykle atgal į viršų; kontrastingos spalvos šakoms atskirti.“

## 4. Sąrašas: viena dėžė, daug reikšmių

Sąrašas (`list`) yra tvarkinga reikšmių seka, saugoma vienu vardu. Elementai gali kartotis, o jų tvarka išlieka tokia, kokia buvo įrašyta.

```python
topics = ["kursai", "kaina", "kontaktai"]
print(topics[0])      # kursai
print(topics[-1])     # kontaktai
print(len(topics))    # 3
```

```text
kursai
kontaktai
3
```

Eilutė po eilutės:

1. `topics = ["kursai", "kaina", "kontaktai"]` sukuria naują sąrašą su trimis tekstinėmis reikšmėmis ir susieja jį su vardu `topics`.
2. `print(topics[0])` paima elementą, esantį pirmoje pozicijoje (indeksas `0`) – tai `"kursai"`.
3. `print(topics[-1])` paima paskutinį elementą, skaičiuojant nuo galo, – tai `"kontaktai"`.
4. `print(len(topics))` suskaičiuoja, kiek elementų yra sąraše, – gauname `3`.

Indeksai visada prasideda nuo nulio. Jei paprašysi indekso, kurio sąraše nėra, gausi klaidą:

```python
topics = ["kursai", "kaina", "kontaktai"]
print(topics[5])
```

```text
Traceback (most recent call last):
  ...
IndexError: list index out of range
```

> **Dažna klaida:** manyti, kad pirmas elementas turi indeksą `1`. Python indeksai prasideda nuo `0`, todėl paskutinio elemento indeksas visada yra `len(sąrašas) - 1`, o ne pats sąrašo ilgis.

Sąrašą galima keisti – pridėti, pakeisti ar pašalinti elementus jį jau sukūrus:

```python
topics.append("tvarkaraštis")
topics.remove("kaina")
topics[0] = "mokymai"
print(topics)
```

```text
['mokymai', 'kontaktai', 'tvarkaraštis']
```

Eilutė po eilutės:

1. `topics.append("tvarkaraštis")` prideda naują elementą sąrašo pabaigoje.
2. `topics.remove("kaina")` suranda pirmą tokią reikšmę ir ją pašalina. Jei reikšmės sąraše nėra, Python sukels `ValueError`.
3. `topics[0] = "mokymai"` pakeičia elementą pagal indeksą – tai vadinama mutacija: pats sąrašas keičiamas vietoje, naujo sąrašo nesukuriama.
4. `print(topics)` parodo galutinę sąrašo būseną.

**Mini užduotis.** Sukurk penkių mėgstamų programų sąrašą. Atspausdink pirmą, paskutinę reikšmes ir elementų skaičių. Tada pridėk vieną naują programą, pakeisk antrą programą kita ir pašalink vieną iš pradinių.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
programs = ["VS Code", "Python", "Excel", "Figma", "Slack"]
print(programs[0])
print(programs[-1])
print(len(programs))

programs.append("Notion")
programs[1] = "PyCharm"
programs.remove("Excel")
print(programs)
```

```text
VS Code
Slack
5
['VS Code', 'PyCharm', 'Figma', 'Slack', 'Notion']
```

</details>

### Aiškūs sąrašų vardai

Sąrašo vardas turėtų nusakyti, kas jame saugoma, ir dažnai skamba daugiskaita: `topics`, `questions`, `history`, `products`. Tai padeda iš karto suprasti, kad kintamajame yra ne viena, o kelios reikšmės.

## 5. `for`: atlik su kiekvienu

`for` ciklas leidžia automatiškai pakartoti tą patį veiksmą su kiekvienu sąrašo elementu, nerašant to paties kodo kelis kartus.

```python
questions = ["Kokia kaina?", "Kada prasideda?", "Ar gausiu pažymėjimą?"]

for question in questions:
    print(f"Tikrinama: {question}")
```

```text
Tikrinama: Kokia kaina?
Tikrinama: Kada prasideda?
Tikrinama: Ar gausiu pažymėjimą?
```

Eilutė po eilutės:

1. `questions = [...]` sukuria sąrašą su trimis klausimais.
2. `for question in questions:` Python paima pirmą elementą, susieja jį su vardu `question`, įvykdo bloko eilutes, tada grįžta paimti kito elemento – ir taip iki pat sąrašo pabaigos.
3. `print(f"Tikrinama: {question}")` kiekvieną apsisukimą parodo einamąjį klausimą.

Kintamasis `question` kiekvieno apsisukimo metu gauna kitą sąrašo reikšmę. Jei prie kiekvieno elemento reikia ir numerio, naudok `enumerate()`:

```python
for number, question in enumerate(questions, start=1):
    print(f"{number}. {question}")
```

```text
1. Kokia kaina?
2. Kada prasideda?
3. Ar gausiu pažymėjimą?
```

`enumerate(questions, start=1)` kiekvieną apsisukimą grąžina porą – numerį ir elementą. Parametras `start=1` sako, kad numeracija turi prasidėti nuo `1`, o ne nuo įprasto `0`.

Kartais reikia ne konkrečių elementų, o tiesiog pasikartoti tam tikrą skaičių kartų – tam skirtas `range()`. `range(5)` sugeneruoja `0, 1, 2, 3, 4` – penkis skaičius, bet pabaiga (`5`) neįtraukiama.

```python
for attempt in range(1, 4):
    print(f"Bandymas {attempt} iš 3")
```

```text
Bandymas 1 iš 3
Bandymas 2 iš 3
Bandymas 3 iš 3
```

`range(1, 4)` pradeda nuo `1` ir sustoja prieš `4`, todėl gauname `1, 2, 3` – tris bandymus, kaip ir norėjome.

> **Dažna klaida:** manoma, kad `range(1, 4)` grąžina ir `4`. Iš tikrųjų antrasis argumentas yra riba, kuri niekada neįtraukiama – paskutinė reikšmė visada yra „riba minus vienas“.

**Mini užduotis.** Su `for` ir `range()` parašyk ciklą, kuris nuo `1` iki `5` atspausdintų kiekvieno skaičiaus kvadratą tokiu pavidalu: `3^2 = 9`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
for number in range(1, 6):
    square = number ** 2
    print(f"{number}^2 = {square}")
```

```text
1^2 = 1
2^2 = 4
3^2 = 9
4^2 = 16
5^2 = 25
```

Kad kvadratai apimtų ir `5`, riba parašyta `6` – vienu daugiau nei paskutinis norimas skaičius.

</details>

## 6. Duomenų filtravimas

Dažna užduotis – iš „nešvarių“ duomenų surinkti tik tinkamas reikšmes. Tam naudojamas tuščias sąrašas kaip kaupiklis, į kurį per `for` ciklą renkame patikrintus rezultatus.

```python
messages = ["labas", "", "Kokia kaina?", "  ", "Iki!"]
valid_messages = []

for message in messages:
    cleaned = message.strip()
    if cleaned:
        valid_messages.append(cleaned)

print(valid_messages)
```

```text
['labas', 'Kokia kaina?', 'Iki!']
```

Eilutė po eilutės:

1. `messages` sąraše sumaišytos tikros žinutės ir „šiukšlės“ – tuščias tekstas bei vien tarpai.
2. `valid_messages = []` sukuria tuščią sąrašą, kuris veiks kaip kaupiklis geroms žinutėms.
3. `for message in messages:` pereina per kiekvieną pradinę žinutę.
4. `cleaned = message.strip()` pašalina tarpus teksto pradžioje ir pabaigoje.
5. `if cleaned:` patikrina, ar po valymo dar liko tekstas – tuščias tekstas sąlygoje laikomas `False`, todėl vien tarpų žinutė (`"  "` po `.strip()` tampa `""`) taip pat atmetama.
6. `valid_messages.append(cleaned)` prideda tik tinkamas, jau išvalytas žinutes į naują sąrašą.

Čia susijungia sąlygos, teksto metodai, sąrašas ir ciklas. Tokia grandinė – įprastas duomenų paruošimas prieš siunčiant tekstą DI modeliui: nė vienas realus sistemos komponentas nenori gauti tuščių ar vien tarpų sudarytų žinučių.

> **Dažna klaida:** filtruojant tikrinama originali žinutė be `.strip()`, todėl vien tarpų sudaryta žinutė klaidingai laikoma tinkama (`"  "` yra tiesa loginėje sąlygoje, nes tai netuščias tekstas – tik po išvalymo ji tampa tuščia).

**Mini užduotis.** Turėdamas sąrašą `["", "Ačiū", "   ", "Iki", ""]`, surašyk į naują sąrašą tik netuščias, jau išvalytas žinutes ir parodyk, kiek jų liko.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
raw_messages = ["", "Ačiū", "   ", "Iki", ""]
clean_messages = []

for message in raw_messages:
    cleaned = message.strip()
    if cleaned:
        clean_messages.append(cleaned)

print(clean_messages)
print(f"Tinkamų žinučių: {len(clean_messages)}")
```

```text
['Ačiū', 'Iki']
Tinkamų žinučių: 2
```

</details>

## 7. `while`: kartok, kol būsena pasikeis

`for` tinka, kai iš anksto žinai, per ką reikia pereiti. Bet pokalbis su vartotoju tęsiasi tol, kol jis pats nuspręs baigti – kartojimų skaičius iš anksto nežinomas. Tam skirtas `while`: jis kartoja bloką, kol nurodyta sąlyga yra teisinga.

```python
command = ""

while command != "baigti":
    command = input("Komanda (baigti – išeiti): ").strip().lower()
    print(f"Gauta: {command}")
```

Eilutė po eilutės:

1. `command = ""` prieš ciklą suteikia pradinę reikšmę – ji garantuotai nelygi `"baigti"`, todėl ciklas bent kartą įvykdomas.
2. `while command != "baigti":` prieš kiekvieną apsisukimą patikrina sąlygą – jei ji teisinga, blokas vykdomas dar kartą.
3. `command = input(...)` kiekviename apsisukime gauna naują vartotojo įvestį ir atnaujina `command` – būtent šis atnaujinimas leidžia ciklui kada nors sustoti.
4. `print(f"Gauta: {command}")` parodo, ką programa gavo.

Jei sąlyga niekada netaps `False`, gausime begalinį ciklą. Dialogo programoje visada aiškiai numatyk išėjimo komandą.

Dažniausiai naudojamas šablonas – `while True:` su rankiniu `break`:

```python
while True:
    message = input("Tu: ").strip()
    if message.lower() == "baigti":
        print("Iki!")
        break
    if not message:
        print("Įvesk klausimą.")
        continue
    print(f"Priėmiau: {message}")
```

`break` nutraukia visą ciklą – programa iškart tęsiasi už `while` bloko ribų. `continue` praleidžia tik dabartinį apsisukimą – Python grįžta į ciklo pradžią ir vėl tikrina sąlygą, nepasiekęs likusių eilučių.

> **Dažna klaida:** rašant `while True:` pamiršti kelią, kuriuo pasiekiamas `break`. Be aiškaus išėjimo taško programa niekada nesustos savarankiškai – ją teks stabdyti rankiniu būdu (pvz., `Ctrl+C`).

**Mini užduotis.** Parašyk `while` ciklą, kuris skaičiuoja atgal nuo `5` iki `1` ir po to parodo „Startas!“.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
count = 5

while count >= 1:
    print(count)
    count -= 1

print("Startas!")
```

```text
5
4
3
2
1
Startas!
```

Kiekviename apsisukime `count` sumažėja per vieną – būtent tai galiausiai padaro sąlygą `count >= 1` neteisingą, ir ciklas natūraliai sustoja.

</details>

## 8. Sąrašų analizė

Dažna cikle atliekama užduotis – suskaičiuoti sumą, vidurkį ar kitą apibendrinimą pereinant per visus sąrašo elementus.

```python
ratings = [8, 10, 7, 9, 6]
total = 0

for rating in ratings:
    total += rating

average = total / len(ratings)
print(f"Vidurkis: {average:.1f}")
```

```text
Vidurkis: 8.0
```

Eilutė po eilutės:

1. `ratings = [8, 10, 7, 9, 6]` – penki vertinimai.
2. `total = 0` – kaupiklis prasideda nuo nulio, nes dar nieko nesudėjome.
3. `for rating in ratings: total += rating` kiekviename apsisukime prie `total` prideda einamąjį vertinimą. `total += rating` yra trumpesnis užrašas, reiškiantis `total = total + rating`.
4. `average = total / len(ratings)` po ciklo bendrą sumą dalija iš elementų skaičiaus.
5. `f"Vidurkis: {average:.1f}"` suapvalina rezultatą iki vieno skaitmens po kablelio.

Python turi ir įmontuotą `sum(ratings)`, tačiau rankinis variantas leidžia suprasti kaupiklio principą – kintamąjį, kuris po kiekvieno apsisukimo saugo jau apdorotų elementų tarpinį rezultatą. Šis principas vėliau pravers skaičiuojant užklausų kiekį, testų rezultatus ar pokalbio statistiką.

## 9. Įvairūs kodo pavyzdžiai

### Minimalus pavyzdys

**Problema:** apdoroti tris pasisveikinimus be pasikartojančio kodo.

```python
greetings = ["Labas", "Sveiki", "Sveikas"]

for greeting in greetings:
    print(f"{greeting}!")
```

```text
Labas!
Sveiki!
Sveikas!
```

**Patobulinimas:** pridėk ketvirtą pasisveikinimą – kodo keisti nereikės, ciklas jį apdoros automatiškai.

### Kasdienis pavyzdys – savaitės mokymosi planas

```python
days = ["Pirmadienis", "Antradienis", "Trečiadienis"]

for day in days:
    print(f"{day}: mokausi Python 1 valandą")
```

```text
Pirmadienis: mokausi Python 1 valandą
Antradienis: mokausi Python 1 valandą
Trečiadienis: mokausi Python 1 valandą
```

**Patobulinimas:** naudok `enumerate()`, kad kiekviena diena būtų sunumeruota.

### Darbo pavyzdys – sąskaitos eilutės

```python
items = ["Konsultacija", "Ataskaita", "Palaikymas"]
prices = [50.0, 80.0, 20.0]
total = 0

for index in range(len(items)):
    print(f"{items[index]}: {prices[index]} Eur")
    total += prices[index]

print(f"Iš viso: {total} Eur")
```

```text
Konsultacija: 50.0 Eur
Ataskaita: 80.0 Eur
Palaikymas: 20.0 Eur
Iš viso: 150.0 Eur
```

**Patobulinimas:** kai išmoksi `zip()`, tą patį rezultatą gausi be `range(len(...))` – tiesiog surišdamas abu sąrašus `for item, price in zip(items, prices):`.

### Automatizavimo pavyzdys – užduočių eilė

```python
tasks = ["atsakyti į el. laiškus", "paruošti ataskaitą", "atnaujinti sąrašą"]
completed = []

for task in tasks:
    print(f"Vykdoma: {task}")
    completed.append(task)

print(f"Atlikta {len(completed)} užduočių.")
```

```text
Vykdoma: atsakyti į el. laiškus
Vykdoma: paruošti ataskaitą
Vykdoma: atnaujinti sąrašą
Atlikta 3 užduočių.
```

**Patobulinimas:** pridėk sąlygą, kuri su `continue` praleidžia užduotis, pažymėtas kaip jau atliktas.

### Duomenų ir AI pavyzdys – žinučių paketo apdorojimas

```python
messages = ["Kaina?", "", "Kontaktai?", "  ", "Ačiū"]
processed = []

for message in messages:
    cleaned = message.strip()
    if not cleaned:
        continue
    processed.append(cleaned)

print(f"Iš {len(messages)} žinučių tinkamos: {len(processed)}")
print(processed)
```

```text
Iš 5 žinučių tinkamos: 3
['Kaina?', 'Kontaktai?', 'Ačiū']
```

**Patobulinimas:** prieš siunčiant žinutes AI modeliui, papildomai apkirpk per ilgas žinutes iki tam tikro simbolių skaičiaus.

### Klaidingas pavyzdys – pataisyk

```python
items = ["obuolys", "bananas", "kriaušė"]

for i in range(len(items)):
    print(items[i + 1])
```

```text
bananas
kriaušė
Traceback (most recent call last):
  ...
IndexError: list index out of range
```

Kai `i` pasiekia paskutinę reikšmę (`2`), kodas bando pasiekti `items[3]`, kurio sąraše nėra – gauname `IndexError`.

Pataisymas:

```python
items = ["obuolys", "bananas", "kriaušė"]

for i in range(len(items)):
    print(items[i])
```

```text
obuolys
bananas
kriaušė
```

## 10. Interaktyvios veiklos

### 1. Nuspėk rezultatą

```python
letters = ["a", "b", "c"]
for letter in letters:
    if letter == "b":
        continue
    print(letter)
```

A. `a`, `b`, `c`
B. `a`, `c`
C. `a`, `b`
D. Klaida

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Kai `letter` lygus `"b"`, suveikia `continue`, ir eilutė `print(letter)` tą apsisukimą praleidžiama. `"a"` ir `"c"` spausdinami įprastai.

</details>

### 2. Užpildyk trūkstamą kodą

```python
numbers = [10, 20, 30]
total = 0

for number in numbers:
    total ____ number

print(total)
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
total += number
```

`total += number` reiškia `total = total + number` – kiekviename apsisukime prie kaupiklio pridedama nauja reikšmė. Rezultatas – `60`.

</details>

### 3. Surask klaidą

```python
values = [1, 2, 3]
for value in range(values):
    print(value)
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

`range()` laukia skaičiaus, o ne sąrašo – gauname `TypeError: 'list' object cannot be interpreted as an integer`. Norint tiesiog pereiti per elementus, `range()` čia iš viso nereikia:

```python
values = [1, 2, 3]
for value in values:
    print(value)
```

</details>

### 4. Sudėliok teisinga tvarka

```text
print(cleaned_messages)
cleaned_messages = []
for message in raw_messages:
    cleaned_messages.append(message.strip())
raw_messages = ["labas ", " kaina"]
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
raw_messages = ["labas ", " kaina"]
cleaned_messages = []
for message in raw_messages:
    cleaned_messages.append(message.strip())
print(cleaned_messages)
```

Pirmiausia turi egzistuoti pradinis sąrašas, tada – tuščias kaupiklis, tik po to – ciklas, kuris jį užpildo, ir galiausiai – rezultato spausdinimas.

</details>

### 5. Pasirink tinkamą sprendimą

Reikia pakartoti veiksmą lygiai penkis kartus, nepriklausomai nuo jokios vartotojo įvestos reikšmės. Kuris variantas tinka geriausiai?

A. `while True:` su `break`, kai vartotojas parašo tam tikrą žodį
B. `for i in range(5):`
C. `while count <= 5:` be `count` atnaujinimo cikle

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Kai pasikartojimų skaičius žinomas iš anksto ir yra fiksuotas, aiškiausias ir saugiausias pasirinkimas yra `for i in range(5):`. A variantas priklauso nuo vartotojo elgesio, o C sukurtų begalinį ciklą, nes `count` niekada nesikeičia.

</details>

### 6. Parašyk pats

Paprašyk vartotojo įvesti keturias mėgstamas dainas (keturis atskirus `input()` kvietimus, sudedamus į sąrašą). Tada su `enumerate()` parodyk sunumeruotą sąrašą.

### 7. Patobulink kodą

```python
lst = [3, 1, 4, 1, 5]
s = 0
for x in lst:
    s = s + x
print(s)
```

Pakeisk kintamųjų vardus taip, kad kodas paaiškintų pats save: `lst` tegul tampa `numbers`, `s` – `total`, `x` – `number`.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
numbers = [3, 1, 4, 1, 5]
total = 0
for number in numbers:
    total = total + number
print(total)
```

Logika visiškai nepakito – pasikeitė tik vardai. Bet dabar kodą skaitantis žmogus iš karto supranta, kad `total` yra kaupiama suma, o ne paslaptinga raidė `s`.

</details>

## 11. Žinių patikrinimas prieš platformos testą

Pirmiausia atsakyk neužleisdamas atsakymų.

1. Ką grąžintų `topics[-2]`, jei `topics = ["a", "b", "c", "d"]`?
2. Kuo skiriasi `sarasas.append(x)` nuo `sarasas[0] = x`?
3. Kodėl `for item in items:` dažniausiai patogesnis nei `for i in range(len(items)): item = items[i]`?
4. Kada verta rinktis `while`, o ne `for`?
5. Kas atsitiks, jei `while` cikle pamirši atnaujinti sąlygos kintamąjį?
6. Kuo `break` poveikis kaupikliui (pvz., `total`) skiriasi nuo `continue` poveikio?
7. Kodėl prieš tikrinant, ar žinutė tuščia, verta naudoti `.strip()`?
8. Kokia klaida įvyks, jei bandysi pasiekti `topics[10]`, kai sąraše yra tik 3 elementai?
9. Kodėl asistento pokalbio klausimus verta laikyti sąraše `history`, o ne atskiruose kintamuosiuose `question1`, `question2`, `question3`?
10. Kas nutinka, kai `.remove()` bandoma pašalinti reikšmę, kurios sąraše nėra?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymus ir paaiškinimus</summary>

1. `"c"` – neigiamas indeksas `-2` reiškia „antras nuo galo“.
2. `append(x)` prideda naują elementą sąrašo pabaigoje ir sąrašas pailgėja; `sarasas[0] = x` pakeičia jau esantį elementą, ir sąrašo ilgis nesikeičia.
3. `for item in items:` iškart duoda patį elementą ir yra sunkiau suklysti su indeksais; `range(len(items))` reikalingas tik tada, kai papildomai reikia ir indekso.
4. `while` renkamasi, kai kartojimų skaičius iš anksto nežinomas ir priklauso nuo besikeičiančios sąlygos (pvz., vartotojo įvesties).
5. Sąlyga niekada netaps `False`, ir gausime begalinį ciklą.
6. `break` iškart nutraukia ciklą, tad kaupiklis nebepapildomas likusiais elementais; `continue` tik praleidžia dabartinį elementą, o kaupiklis toliau papildomas kitais apsisukimais.
7. Nes tekstas, sudarytas vien iš tarpų, be `.strip()` sąlygoje laikomas netuščiu (tiesa), nors iš tikrųjų naudingos informacijos jame nėra.
8. `IndexError: list index out of range`.
9. Nes sąrašas leidžia bet kiek klausimų saugoti vienu vardu, juos suskaičiuoti su `len()` ir pereiti su `for` – su atskirais kintamaisiais tektų iš anksto žinoti tikslų klausimų skaičių ir rašyti atskirą eilutę kiekvienam.
10. Python sukelia `ValueError`, nurodydamas, kad tokios reikšmės sąraše nėra.

</details>

## 12. Praktinės užduotys

### A lygis – pirkinių sąrašas

**Sąlyga:** rink produktus į sąrašą tol, kol jame atsiras penki tinkami (netušti) produktai. Tuščios įvesties nepridėk – paprašyk įvesties dar kartą. Pabaigoje parodyk sunumeruotą sąrašą.
**Pavyzdinė įvestis:** `duonos`, `pieno`, `kiaušinių`, `` (tuščia), `obuolių`, `sūrio`.
**Laukiamas rezultatas:**

```text
Pirkinių sąrašas:
1. duonos
2. pieno
3. kiaušinių
4. obuolių
5. sūrio
```

**Užuomina:** naudok `while len(products) < 5:` ir prie sąrašo prideda tik netuščią, jau išvalytą įvestį.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
products = []

while len(products) < 5:
    product = input("Įrašyk produktą: ").strip()
    if not product:
        print("Tuščias produktas nepridedamas, bandyk dar kartą.")
        continue
    products.append(product)

print("Pirkinių sąrašas:")
for number, product in enumerate(products, start=1):
    print(f"{number}. {product}")
```

`while len(products) < 5:` tikrina ne fiksuotą kartojimų skaičių, o realų sąrašo ilgį – tai reiškia, kad tuščia įvestis niekada neužims vietos tarp penkių produktų. **Papildomas iššūkis:** neleisk pridėti to paties produkto du kartus, prieš tai patikrinęs `if product in products:`.

</details>

### B lygis – pažymių analizė

**Sąlyga:** turėdamas bent 8 pažymių sąrašą, suskaičiuok vidurkį, kiek pažymių yra teigiami (`>= 5`), didžiausią ir mažiausią pažymį. Pirmiausia atlik viską ciklu su kaupikliais, tada patikrink rezultatą su `sum()`, `min()` ir `max()`.
**Pavyzdinė įvestis:** `grades = [10, 4, 7, 9, 5, 6, 3, 8]`.
**Laukiamas rezultatas:** vidurkis `6.5`, teigiamų pažymių `6`, didžiausias `10`, mažiausias `3`.
**Užuomina:** kaupiklius `highest` ir `lowest` prieš ciklą inicijuok pirmuoju sąrašo elementu, o ne `0`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
grades = [10, 4, 7, 9, 5, 6, 3, 8]

total = 0
passing_count = 0
highest = grades[0]
lowest = grades[0]

for grade in grades:
    total += grade
    if grade >= 5:
        passing_count += 1
    if grade > highest:
        highest = grade
    if grade < lowest:
        lowest = grade

average = total / len(grades)

print(f"Vidurkis: {average:.1f}")
print(f"Teigiamų pažymių: {passing_count}")
print(f"Didžiausias: {highest}")
print(f"Mažiausias: {lowest}")

print("--- Patikra su įmontuotomis funkcijomis ---")
print(f"Vidurkis: {sum(grades) / len(grades):.1f}")
print(f"Didžiausias: {max(grades)}")
print(f"Mažiausias: {min(grades)}")
```

```text
Vidurkis: 6.5
Teigiamų pažymių: 6
Didžiausias: 10
Mažiausias: 3
--- Patikra su įmontuotomis funkcijomis ---
Vidurkis: 6.5
Didžiausias: 10
Mažiausias: 3
```

Jei `highest` ir `lowest` būtų inicijuoti nuliu, o visi pažymiai būtų neigiami arba visi didesni už nulį, rezultatas galėtų būti klaidingas – todėl saugiausia pradėti nuo pirmojo tikro elemento. **Papildomas iššūkis:** papildomai suskaičiuok, kiek pažymių yra lygiai `10`.

</details>

### C lygis – komandų meniu

**Sąlyga:** komandos `pridėti`, `rodyti`, `šalinti`, `baigti` turi valdyti užduočių sąrašą. Neleisk pašalinti neegzistuojančio numerio.
**Pavyzdinė sąveika:**

```text
Komandos: pridėti, rodyti, šalinti, baigti
Komanda: pridėti
Užduotis: Parašyti laišką
Pridėta.
Komanda: pridėti
Užduotis: Sutvarkyti stalą
Pridėta.
Komanda: rodyti
1. Parašyti laišką
2. Sutvarkyti stalą
Komanda: šalinti
Numeris: 5
Tokio numerio nėra.
Komanda: šalinti
Numeris: 1
Pašalinta: Parašyti laišką
Komanda: baigti
Iki!
```

**Laukiamas rezultatas:** po pavyzdinės sąveikos sąraše lieka tik „Sutvarkyti stalą“.
**Užuomina:** numerį, kurį įvedė vartotojas, prieš naudojant kaip indeksą sumažink vienetu (`index = int(number_text) - 1`) ir patikrink, ar jis patenka tarp `0` ir `len(tasks) - 1`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
tasks = []

print("Komandos: pridėti, rodyti, šalinti, baigti")

while True:
    command = input("Komanda: ").strip().lower()

    if command == "baigti":
        print("Iki!")
        break
    elif command == "pridėti":
        task = input("Užduotis: ").strip()
        if not task:
            print("Tuščios užduoties nepridėsiu.")
            continue
        tasks.append(task)
        print("Pridėta.")
    elif command == "rodyti":
        if not tasks:
            print("Sąrašas tuščias.")
            continue
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")
    elif command == "šalinti":
        number_text = input("Numeris: ").strip()
        if not number_text.isdigit():
            print("Įvesk skaičių.")
            continue
        index = int(number_text) - 1
        if index < 0 or index >= len(tasks):
            print("Tokio numerio nėra.")
            continue
        removed = tasks.pop(index)
        print(f"Pašalinta: {removed}")
    else:
        print("Nežinoma komanda.")
```

Kiekviena komanda tikrinama atskiroje `elif` šakoje, o klaidingas numeris niekada nepasiekia `tasks.pop(index)` – prieš tai jį sustabdo ribų patikra. **Papildomas iššūkis:** pridėk komandą `išvalyti`, kuri vienu veiksmu pašalina visas užduotis (`tasks.clear()`).

</details>

## 13. Mini projektas: Asistentas 0.2

### 1. Projekto situacija

Mokymų centras nori, kad asistentas galėtų kalbėtis su lankytoju ilgiau nei vieną kartą – priimti kelis klausimus iš eilės ir prisiminti, kas per pokalbį jau buvo klausta, kol lankytojas pats nuspręs baigti.

### 2. Galutinis tikslas

Sukurti `assistant_v02.py`, kuris veikia begaliniame cikle tol, kol vartotojas parašo „baigti“, kaupia visus klausimus sąraše ir pokalbio pabaigoje parodo juos sunumeruotus.

### 3. Funkciniai reikalavimai

Programa turi:

1. tęsti pokalbį begaliniame `while True:` cikle, kol vartotojas neparašo „baigti“;
2. ignoruoti tuščią įvestį ir su `continue` iš karto grąžinti vartotoją prie naujo klausimo, neįrašant jos į istoriją;
3. saugoti kiekvieną netuščią klausimą originaliu (nepakeistu registru) pavidalu sąraše `history`;
4. atpažinti temas apie kursą, kainą ir kontaktus nepriklausomai nuo raidžių registro, tikrindama jau sunormalizuotą (mažosiomis raidėmis) žinutę;
5. baigus pokalbį parodyti, į kiek klausimų buvo atsakyta (`len(history)`), ir naudoti `break`, kad išeitų iš ciklo;
6. po ciklo su `for` ir `enumerate()` parodyti sunumeruotą visų užduotų klausimų sąrašą.

### 4. Pavyzdinė sąveika

```text
Asistentas 0.2. Parašyk „baigti“, kai norėsi išeiti.
Tu: Labas
Asistentas: Galiu atsakyti apie kursą, kainą ir kontaktus.
Tu: 
Asistentas: Parašyk klausimą.
Tu: Kokia kaina?
Asistentas: Dėl kainos kreipkis į koordinatorių.
Tu: baigti
Asistentas: Iki! Atsakiau į 2 klausimus.
```

### 5. Pavyzdinis rezultatas

```text
Asistentas 0.2. Parašyk „baigti“, kai norėsi išeiti.
Tu: Labas
Asistentas: Galiu atsakyti apie kursą, kainą ir kontaktus.
Tu: 
Asistentas: Parašyk klausimą.
Tu: Kokia kaina?
Asistentas: Dėl kainos kreipkis į koordinatorių.
Tu: baigti
Asistentas: Iki! Atsakiau į 2 klausimus.
Pokalbio klausimai:
1. Labas
2. Kokia kaina?
```

Atkreipk dėmesį: tuščia įvestis (antra eilutė pavyzdyje) į `history` nepatenka ir neskaičiuojama – ji tik parodo priminimą ir per `continue` grąžina prie naujo klausimo.

### 6. Projekto kūrimo etapai

1. Sukurk tuščią sąrašą `history` ir sąrašą `known_topics` su galimomis temomis.
2. Parodyk pasisveikinimo žinutę su instrukcija, kaip baigti pokalbį.
3. Parašyk `while True:` ciklą, jame priimk žinutę su `input()`.
4. Sunormalizuok žinutę į `message`, bet originalią versiją pasilik atskirame kintamajame `original`.
5. Patikrink, ar žinutė yra „baigti“ – jei taip, parodyk atsisveikinimą su `len(history)` ir naudok `break`.
6. Patikrink, ar žinutė tuščia – jei taip, paprašyk klausimo dar kartą ir naudok `continue`.
7. Įrašyk `original` į `history`.
8. Su `if`/`elif`/`else` grandine parink atsakymą pagal raktažodžius `kurs`, `kain`, `kontakt`.
9. Parodyk parinktą atsakymą.
10. Po ciklo su `for` ir `enumerate()` parodyk visus klausimus sunumeruotus.

### 7. Pseudokodas

```text
SUKURK tuščią istorijos sąrašą
SUKURK žinomų temų sąrašą
PARODYK pasisveikinimą

KARTOK, kol nenutrūksta:
    PRIIMK žinutę
    SUNORMALIZUOK žinutę mažosiomis raidėmis

    JEI žinutė yra "baigti":
        PARODYK atsisveikinimą su klausimų skaičiumi
        NUTRAUK ciklą

    JEI žinutė tuščia:
        PARAŠYK, kad reikia klausimo
        PEREIK PRIE KITO APSISUKIMO

    ĮTRAUK originalią žinutę į istoriją
    PARINK atsakymą pagal raktažodį
    PARODYK atsakymą

PO CIKLO parodyk sunumeruotą klausimų sąrašą
```

> **Užuomina:** jei kodas „užstringa“ neišeidamas iš ciklo, patikrink, ar sąlyga `message == "baigti"` tikrai pasiekiama – dažniausia priežastis yra tai, kad `message` lyginamas su originaliu, nesunormalizuotu tekstu.

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

```python
history = []
known_topics = ["kurs", "kain", "kontakt"]

print("Asistentas 0.2. Parašyk „baigti“, kai norėsi išeiti.")

while True:
    original = input("Tu: ").strip()
    message = original.lower()

    if message == "baigti":
        print(f"Asistentas: Iki! Atsakiau į {len(history)} klausimus.")
        break
    if not message:
        print("Asistentas: Parašyk klausimą.")
        continue

    history.append(original)

    if "kurs" in message:
        answer = "Python programa trunka 88 akademines valandas."
    elif "kain" in message:
        answer = "Dėl kainos kreipkis į koordinatorių."
    elif "kontakt" in message:
        answer = "El. paštas: mokymai@example.lt."
    else:
        answer = "Galiu atsakyti apie kursą, kainą ir kontaktus."

    print(f"Asistentas: {answer}")

print("Pokalbio klausimai:")
for number, question in enumerate(history, start=1):
    print(f"{number}. {question}")
```

`history` pradžioje tuščias ir per kiekvieną tinkamą apsisukimą papildomas originaliu (nepakeistu registru) tekstu – taip pokalbio istorija atrodo natūraliai, net jei atsakymai buvo parinkti pagal sunormalizuotą `message`. `while True:` su dviem ankstyvais išėjimais (`break` ir `continue`) leidžia programai kalbėtis tiek kartų, kiek reikia, o `if`/`elif`/`else` grandinė iš antros pamokos čia veikia visiškai taip pat kaip „Asistente 0.1“ – tik dabar ji vykdoma kiekvieną ciklo apsisukimą, o ne vieną kartą. Paskutinis `for` su `enumerate()` paverčia sukauptą sąrašą į tvarkingą, sunumeruotą suvestinę.

</details>

### 8. Galimi patobulinimai

- pridėti komandą `istorija`, kuri parodytų iki šiol užduotus klausimus, nenutraukiant paties pokalbio;
- pridėti komandą `valyti`, kuri išvalytų sukauptą istoriją;
- atskirti pasisveikinimo ir padėkos atsakymus nuo bendro „nesupratau“ atsakymo;
- skaičiuoti, kiek kartų asistentas negalėjo atpažinti temos (nežinomų užklausų skaitiklis);
- kitoje pamokoje šią atsakymų parinkimo logiką perkelsime į atskirą funkciją, kad kodas nesikartotų ir jį būtų lengviau testuoti.

### 9. `README.md` šablonas

```text
# Asistentas 0.2

Interaktyvus konsolės asistentas, kuris kalbasi tol, kol vartotojas parašo „baigti“.

## Funkcijos
- Tęsia pokalbį begaliniame cikle
- Ignoruoja tuščią įvestį
- Atpažįsta klausimus apie kursą, kainą ir kontaktus
- Saugo visų klausimų istoriją ir ją parodo pabaigoje

## Paleidimas
python3 assistant_v02.py

## Pavyzdys
Rašyk klausimus vieną po kito; baik pokalbį parašęs „baigti“.

## Ką išmokau
list, for, while, range(), break, continue, enumerate()

## Tolimesni patobulinimai
Komandos /help, /history, /clear, atskiri klausimų ir atsakymų sąrašai
```

## 14. Derinimo laboratorija

Realiame darbe klaidos su sąrašais ir ciklais kartojasi dažniausiai dviem pavidalais: neteisinga indekso riba ir pamirštas sąlygos kintamojo atnaujinimas. Surask ir ištaisyk abu žemiau pateiktus pavyzdžius.

```python
items = ["a", "b", "c"]
for i in range(1, len(items) + 1):
    print(items[i])
```

```python
message = ""
while message != "stop":
    print("Laukiu...")
```

Pirmu atveju indeksai nesutampa su sąrašo ribomis, antru – ciklo viduje `message` niekada neatnaujinamas.

Ištaisyti variantai:

```python
items = ["a", "b", "c"]
for i in range(len(items)):
    print(items[i])
```

```python
message = ""
while message != "stop":
    message = input("Įvesk komandą arba 'stop': ")
    print("Laukiu...")
```

Pirmame taisyme riba pakeista iš `len(items) + 1` į `len(items)`, todėl paskutinis naudojamas indeksas yra `len(items) - 1` – tiksliai sąrašo paskutinis elementas. Antrame taisyme prieš `print()` pridėtas `input()`, kuris kiekvieną apsisukimą atnaujina `message` – tik tada sąlyga `message != "stop"` kada nors gali tapti klaidinga.

## 15. Gilioji laboratorija: pasirink tinkamą kolekciją

### 15.1. Keturios kolekcijos, keturios paskirtys

```python
topics = ["python", "api", "python", "testai"]
coordinates = (54.6872, 25.2797)
unique_topics = {"python", "api", "testai"}
course = {"title": "Python", "hours": 88}
```

`list` išlaiko tvarką ir pasikartojimus, `tuple` tinka nekintamai porai, `set` pašalina dublikatus, o `dict` sieja prasmingą raktą su reikšme. Prie kiekvienos struktūros parašyk vieną asistento naudojimo pavyzdį.

**Mini užduotis.** Sugalvok po vieną „Asistento 0.2“ naudojimo atvejį kiekvienai iš keturių kolekcijų.

<details class="selfcheck" markdown="1"><summary>Rodyti pavyzdinį atsakymą</summary>

```python
# list – saugome pokalbio klausimų istoriją (tvarka ir pasikartojimai svarbūs)
history = ["Kokia kaina?", "Kokia kaina?", "Kur vyksta paskaitos?"]

# tuple – saugome nekintamą asistento versijos numerį
version = (0, 2)

# set – saugome unikalias vartotojo paminėtas temas be pasikartojimų
mentioned_topics = {"kaina", "kursas"}

# dict – siejame raktažodį su jį atitinkančiu atsakymu
responses = {"kaina": "Dėl kainos kreipkis į koordinatorių."}
```

`history` tyčia leidžia pasikartojimus – vartotojas gali du kartus paklausti to paties. `mentioned_topics` kaip `set` automatiškai sujungtų pasikartojančias temas į vieną įrašą.

</details>

### 15.2. Mutacija ir netikėtas bendrinimas

```python
original = ["kursas", "kaina"]
alias = original
alias.append("kontaktai")
print(original)
```

`alias` nėra kopija – abu vardai rodo į tą patį sąrašą, todėl pakeitimas per `alias` matomas ir per `original`. Atskirai kopijai naudok `original.copy()`. Parašyk testą, kuris įrodo, ar tavo pagalbinė funkcija sąrašą keičia, ar grąžina naują.

> **Dažna klaida:** manoma, kad `b = a` sukuria naują, nepriklausomą sąrašą. Iš tikrųjų sukuriamas tik antras vardas tam pačiam sąrašui atmintyje.

### 15.3. Sąrašo generatorius ir ciklo invariantas

```python
raw = [" Kursas ", "", " API ", "  "]
cleaned = [item.strip().lower() for item in raw if item.strip()]
print(cleaned)
```

Rezultatas yra `['kursas', 'api']`. Generatorius tinkamas trumpai taisyklei, bet sudėtingą logiką rašyk įprastu `for`. Kaupiklio invariantas: po kiekvieno apsisukimo `total` yra jau aplankytų elementų suma. Užrašyk šį sakinį prieš skaičiuodamas pokalbio statistiką.

### 15.4. Derinimo iššūkis

```python
history = []
saved = history
for message in ["labas", "kaina"]:
    saved = saved + [message]
print(history)
```

`history` liks tuščias, nes `+` sukuria naują sąrašą, o `saved` po kiekvieno apsisukimo pradeda rodyti į tą naują sąrašą – ne į pradinį `history`. Palygink su `saved.append(message)`, kuris keistų tą patį sąrašą, į kurį rodo ir `history`, ir paaiškink, kada mutacija padeda, o kada klaidina.

### 15.5. Kontrolinis taškas

Sukurk `choose_collection.py`, kuris priima penkis raktažodžius ir parodo originalią seką, unikalius raktažodžius, jų dažnius žodyne bei asistento istoriją. Kontrolinis klausimas: kodėl istorijai pasirinkai `list`, o dažniams – `dict`?

## 16. Dažniausios klaidos

| Klaida | Kodėl ji atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| `IndexError` dėl netinkamos ribos | `range()` riba parašyta per didelė | `for i in range(1, len(items)+1): items[i]` | `for i in range(len(items)): items[i]` | Ribą tikrink su `len()` ir prisimink, kad indeksai prasideda nuo 0 |
| Begalinis `while` ciklas | Sąlygos kintamasis niekada neatsinaujina | `while message != "stop": print(...)` | `while message != "stop": message = input(...); print(...)` | Kiekviename apsisukime atnaujink kintamąjį, nuo kurio priklauso sąlyga |
| `break` ir `continue` sukeičiami | Neaišku, kuris nutraukia, kuris praleidžia | naudojamas `continue`, kai reikėjo baigti visą ciklą | naudok `break`, kai reikia išeiti visam laikui | Prisimink: `break` = išeiti, `continue` = praleisti šį kartą |
| Tuščia žinutė laikoma tinkama | Pamirštas `.strip()` prieš tikrinant tuštumą | `if message:`, kai `message = "  "` | `if message.strip():` arba iš anksto `message = message.strip()` | Prieš tikrindamas tuštumą visada išvalyk tarpus |
| Sąrašas keičiamas per aliasą netyčia | Priskyrimas `b = a` nekopijuoja sąrašo | `alias = original; alias.append(x)` keičia ir `original` | `alias = original.copy()` | Kai reikia atskiros kopijos, naudok `.copy()` |
| `.remove()` sukelia `ValueError` | Bandoma pašalinti sąraše neesančią reikšmę | `topics.remove("nera")` | prieš tai `if "nera" in topics: topics.remove("nera")` | Prieš `.remove()` patikrink reikšmės buvimą su `in` |
| Sąrašas keičiamas ciklo metu, kol per jį einama | Elementų šalinimas ar pridėjimas `for` metu praleidžia arba pakartoja elementus | `for item in items: items.remove(item)` | rink šalinamus elementus į atskirą sąrašą arba eik per `items.copy()` | Naujus ar šalinamus elementus rink atskirai, o patį sąrašą keisk po ciklo |

## 17. Profesionali praktika

- Sąrašo vardą rink daugiskaita ir pagal turinį: `topics`, `history`, `questions`, o ne `data` ar `lst`.
- Rinkis `for item in items:` vietoj `for i in range(len(items)):`, nebent tikrai reikia ir paties indekso.
- `while True:` visada projektuok kartu su aiškiu `break` – prieš rašydamas pagalvok, kokia tiksliai sąlyga išves iš ciklo.
- Kaupiklius (`total`, `history`, `valid_messages`) inicijuok prieš ciklą ir aiškiai įsivardyk, ką jie reiškia po kiekvieno apsisukimo.
- Prieš keisdamas sąrašą per aliasą, pagalvok, ar tikrai nori paveikti ir originalą – jei ne, naudok `.copy()`.
- Testuok ciklus su kraštutiniais atvejais: tuščiu sąrašu, vienu elementu ir tuščia įvestimi.
- Sudėtingą filtravimo ar kaupimo logiką pirmiausia parašyk įprastu `for`, o sąrašo generatorių naudok tik trumpoms, aiškioms taisyklėms.

## 18. Kodėl tai svarbu mokantis AI?

AI sistemos beveik niekada neapdoroja vienos reikšmės – jos dirba su sąrašais duomenų eilučių, žinučių ar pokalbio ėjimų, o cikle apdoroja kiekvieną iš jų nuosekliai. Tavo `history` sąrašas Asistente 0.2 yra supaprastinta versija to paties principo, kurį naudoja tikri pokalbių modeliai – jie gauna visą pokalbio istoriją kaip sąrašą, kad „prisimintų“ kontekstą.

```python
conversation_history = [
    {"role": "user", "text": "Kokia kaina?"},
    {"role": "assistant", "text": "Dėl kainos kreipkis į koordinatorių."},
]

for turn in conversation_history:
    print(f"{turn['role']}: {turn['text']}")
```

```text
user: Kokia kaina?
assistant: Dėl kainos kreipkis į koordinatorių.
```

Čia nėra tikro modelio – tik jo naudojamos duomenų struktūros imitacija. `while` ciklas su `break` taip pat atitinka realų modelį: pokalbis tęsiasi tol, kol vartotojas jį baigia, o ne fiksuotą skaičių kartų. Vėlesniuose moduliuose tą pačią sąrašo su žodynais struktūrą naudosi siųsdamas pokalbio istoriją tikram AI modeliui.

## 19. Pamokos santrauka

- Sąrašas (`list`) leidžia vienu vardu saugoti kelias reikšmes, pasiekiamas per indeksą nuo `0`.
- `for` automatiškai pereina per kiekvieną žinomo rinkinio elementą; `enumerate()` prideda numeraciją.
- `range()` generuoja skaičių seką, kurioje galinė riba niekada neįtraukiama.
- `while` kartoja bloką, kol galioja sąlyga – tinka, kai kartojimų skaičius iš anksto nežinomas.
- `break` visiškai nutraukia ciklą, `continue` praleidžia tik dabartinį apsisukimą.
- Kaupiklio šablonas (tuščias sąrašas ar `0` prieš ciklą, papildomas kiekviename apsisukime) yra pagrindas filtravimui, sumavimui ir istorijos saugojimui.

**Atmintinė:**

```python
items = []
items.append("pirma")
items.append("antra")

for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

while True:
    command = input("Komanda: ").strip().lower()
    if command == "baigti":
        break
    if not command:
        continue
    print(f"Priimta: {command}")
```

**Sąrašai kartu su `for` ir `while` ciklais paverčia programą iš vienkartinio atsakymo į nuolat veikiantį, duomenis kaupiantį pašnekovą.**

## 20. Savirefleksija

1. Ką dabar galiu padaryti, ko negalėjau prieš pamoką?
2. Kuri dalis buvo sunkiausia: indeksavimas, `while` ciklo sąlyga ar `break`/`continue` skirtumas?
3. Kokią klaidą dabar mokėčiau atpažinti vien pažiūrėjęs į kodą?
4. Kur šias žinias – sąrašus ir kartojimą, kol vartotojas nesustabdo – galėčiau pritaikyti realiame projekte?
5. Ar galėčiau kitam žmogui paaiškinti, kodėl `alias = original` nesukuria atskiros sąrašo kopijos?

## 21. Namų darbas

### Privaloma – Asistentas 0.2 su atskira klausimų ir atsakymų istorija

Papildyk „Asistentą 0.2“: saugok ne tik klausimą, bet ir atsakymą – dviejuose atskiruose, vienodo ilgio sąrašuose (`questions` ir `answers`). Pridėk komandas `/help` (parodo galimas komandas), `/history` (parodo iki šiol užduotus klausimus su atsakymais, nenutraukiant pokalbio), `/clear` (išvalo istoriją) ir `/quit` (baigia pokalbį lygiai taip pat, kaip dabartinė komanda „baigti“). Sudaryk bent 12 rankinių testų lentelę: įvestis, tikėtinas atsakymas ar veiksmas, faktinis rezultatas, ar testas pavyko.

**Vertinimas (10 taškų):** `questions` ir `answers` visada lieka vienodo ilgio – 3; visos keturios komandos veikia teisingai – 4; 12 rankinių testų lentelė užpildyta – 2; kodas paleidžiamas be klaidų – 1.

### Pasirenkama – nežinomų užklausų skaitiklis

Prie namų darbo pridėk skaitiklį, kuris skaičiuoja, kiek kartų asistentas negalėjo atpažinti temos (pateko į `else` šaką). Pridėk komandą `/stats`, kuri parodo šį skaičių ir bendrą klausimų kiekį.

**Vertinimas (5 taškai):** skaitiklis atnaujinamas tik tinkamu atveju – 2; `/stats` rodo teisingą informaciją – 2; kodas aiškiai pavadintas – 1.

### Kūrybinis iššūkis – savo temos asistentas

Sukurk asistentą kita tema (pvz., restorano meniu klausimai, sporto klubo tvarkaraštis ar bibliotekos knygų paieška) su bent keturiomis atpažįstamomis temomis. Naudok `history` sąrašą pokalbiui saugoti ir parašyk bent 10 rankinių testų.

**Vertinimas (5 taškai):** reali, savarankiškai pasirinkta tema – 1; bent keturios temos atpažįstamos teisingai – 2; aiškūs kintamųjų vardai ir tvarkinga išvestis – 1; 10 testų lentelė – 1.

## 22. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Sąrašai: kūrimas, indeksai, metodai | 40 min. | Iš karto parodyti `IndexError`, kad mokiniai suprastų indeksų ribas |
| `for` ciklas ir `range()` | 45 min. | Painiava tarp `range(5)` ir „penkto elemento“ – tikrinti atskirai |
| Duomenų filtravimas | 35 min. | Akcentuoti `.strip()` prieš tuštumo patikrą |
| `while`, `break`, `continue` | 50 min. | Daugiausia klaidų – begalinis ciklas; turėti paruoštą `Ctrl+C` demonstraciją |
| Sąrašų analizė (kaupiklis, vidurkis) | 35 min. | Palyginti rankinį variantą su `sum()`, `min()`, `max()` |
| Trijų lygių praktika | 60 min. | C lygio meniu tikrinti su keliomis komandų sekomis iš karto |
| Mini projektas: Asistentas 0.2 | 75 min. | Kodo tikslumą (ypač `break`/`continue` vietas) tikrinti rankiniu būdu |
| Derinimo laboratorija | 30 min. | Abu pavyzdžius pirmiausia paleisti be taisymo, kad klaida taptų akivaizdi |
| Gilioji laboratorija: kolekcijos | 70 min. | Aliasingo pavyzdį parodyti gyvai, sekant kintamųjų būseną žingsnis po žingsnio |
| Interaktyvios veiklos ir testas | 40 min. | Fiksuoti, kurios klaidų kategorijos (indeksai, begalinis ciklas, `break`/`continue`) kartojasi dažniausiai |

Suminė trukmė – 480 minučių (8 akademinės valandos). Animacija labiausiai padėtų ties `while True → break/continue` sprendimų medžiu ir aliasingo (`alias = original`) pavyzdžiu – šios dvi vietos kelia daugiausiai nesusipratimų. Interaktyvų Python redaktorių verta įterpti po sąrašo metodų bloko, po `break`/`continue` pavyzdžio, klaidingame `range(len(items)+1)` pavyzdyje ir mini projekte. Platformoje verta fiksuoti atliktas mini užduotis, pirmą sėkmingą `while True` su `break` paleidimą, `IndexError` bei begalinio ciklo dažnį, testo rezultatą, mini projekto užbaigimą ir savirefleksijos pasirinkimą – tai leis kitose pamokose grįžti būtent prie tų vietų, kur mokiniai stringa dažniausiai.
