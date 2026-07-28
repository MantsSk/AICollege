---
title: Sąlygos ir loginiai sprendimai – išmokyk programą pasirinkti
module: Python pagrindai
order: 2
---

# Sąlygos ir loginiai sprendimai – išmokyk programą pasirinkti

> **Trukmė:** 6 akademinės valandos. Mažiausiai 4 valandas skirk kodo rašymui ir bandymams.

## Trumpa anotacija

Iki šiol tavo programos visada darydavo tą patį – priimdavo duomenis, apskaičiuodavo rezultatą ir jį parodydavo. Šioje pamokoje programa pirmą kartą pati **pasirinks**, ką daryti: palygins reikšmes, sujungs kelias sąlygas su `and`, `or`, `not` ir nuves vykdymą vienu iš kelių kelių naudodama `if`, `elif`, `else`. Išmoksi tvarkingai tikrinti vartotojo tekstą (tuščią įvestį, raidžių registrą, tarpus) ir pamokos pabaigoje sukursi **Asistentą 0.1** – pirmą savo sprendimų medžiu paremtą pokalbių robotuką, kuris atpažins kelias temas ir tinkamai sureaguos net į nesuprastą klausimą. Tai tas pats mechanizmas, kuris vėliau nuspręs, kada atsakymą duoti iš karto, o kada kreiptis į AI modelį.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- palyginti reikšmes operatoriais `==`, `!=`, `>`, `<`, `>=`, `<=` ir suprasti, kad rezultatas visada yra `bool`;
- parašyti `if`, `elif`, `else` sprendimų medį teisinga tvarka (nuo konkrečiausios sąlygos iki bendriausios);
- sujungti kelias sąlygas su `and`, `or`, `not` ir paaiškinti, kuo jos skiriasi;
- prieš lygindamas vartotojo tekstą, jį pritaikyti su `.strip()` ir `.lower()`;
- atpažinti ir tvarkingai apdoroti tuščią ar per trumpą įvestį be `try/except`;
- suskaidyti sudėtingą sąlygą į aiškiai pavadintus tarpinius `bool` kintamuosius;
- sukurti ir išbandyti pirmąją asistento versiją (Asistentas 0.1), kuris raktažodžiais atpažįsta kelias temas;
- sudaryti testinių žinučių lentelę ir ja įrodyti, kad sprendimų medis veikia numatytu būdu.

## Būtinos ankstesnės žinios

Turėtum laisvai kurti kintamuosius, atskirti `str`, `int`, `float` ir `bool` reikšmes, priimti vartotojo įvestį su `input()`, konvertuoti ją su `int()` arba `float()` ir sudaryti aiškią žinutę su f-string – visa tai išmokai antroje pamokoje „Kintamieji ir duomenų tipai“. Jei jautiesi nesaugiai, prieš tęsdamas peržiūrėk tos pamokos atmintinę ir mini projektą `quote_calculator.py` – [antra pamoka](lesson-01). Šios pamokos sąlygos tikrins būtent tokius pat kintamuosius, kokius jau moki sukurti.

## 1. Programa, kuri ne tik skaičiuoja

Kintamieji yra programos atmintis, o sąlygos – sprendimų priėmimas. Durų kodas tikrinamas taip: **jei** kodas teisingas – atrakinti, **kitu atveju** – neįleisti. Praeitoje pamokoje `quote_calculator.py` visada atlikdavo tą pačią formulę nepriklausomai nuo įvesties. Dabar programa pati nuspręs, kurią eilutę parodyti.

```python
pin = input("Įvesk PIN: ")

if pin == "1234":
    print("Prieiga suteikta")
else:
    print("Neteisingas PIN")
```

Atkreipk dėmesį: `=` priskiria reikšmę, o `==` palygina. Po sąlygos rašomas dvitaškis, o vykdomos eilutės atitraukiamos keturiais tarpais.

Eilutė po eilutės:

1. `pin = input("Įvesk PIN: ")` – programa parodo klausimą ir vartotojo atsakymą (visada kaip `str`) išsaugo kintamajame `pin`.
2. `if pin == "1234":` – Python patikrina, ar `pin` reikšmė **tiksliai** sutampa su tekstu `"1234"`; rezultatas yra `True` arba `False`.
3. Jei sąlyga teisinga, vykdoma tik įtraukta eilutė `print("Prieiga suteikta")`, o `else` blokas praleidžiamas.
4. Jei sąlyga klaidinga, Python peršoka tiesiai į `else:` ir įvykdo `print("Neteisingas PIN")`.

> **Išbandyk pats:** paleisk kodą ir įvesk `1234`, tada paleisk dar kartą ir įvesk bet ką kitą. Prieš antrą paleidimą nuspėk, kurią eilutę pamatysi ekrane, ir tik tada patikrink.

## 2. Pagrindinės sąvokos

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| Sąlyga (`if`) | Kodo blokas, vykdomas tik kai išraiška yra `True` | Skėtis imamas tik jei lyja | Kai programa turi elgtis skirtingai priklausomai nuo duomenų | Pamirštamas dvitaškis po sąlygos |
| Palyginimo operatorius (`==`, `!=`, `>`, `<`, `>=`, `<=`) | Dviejų reikšmių sugretinimas, grąžinantis `bool` | Svarstyklės, rodančios, kas sunkesnis | Renkantis tarp kelių galimybių pagal skaičių ar tekstą | `=` naudojamas vietoj `==` |
| `elif` | Papildoma sąlyga, tikrinama tik jei ankstesnė buvo neteisinga | Antras klausimas, užduodamas tik negavus atsakymo į pirmą | Kai galimybių daugiau nei dvi | Konkreti sąlyga parašoma per vėlai grandinėje |
| `else` | Blokas, vykdomas kai visos ankstesnės sąlygos neteisingos | „Kitu atveju“ punktas instrukcijoje | Numatytajam, „visų kitų“ atvejui aprašyti | Manoma, kad `else` irgi turi turėti savo sąlygą |
| `and` | Sujungia dvi sąlygas – abi turi būti teisingos | Įleidžiama tik jei turi bilietą IR esi pilnametis | Kai reikalavimų yra kelios ir visos privalomos vienu metu | Sumaišomas su `or`, kai reikalavimas turėtų būti griežtesnis |
| `or` | Sujungia dvi sąlygas – pakanka bent vienos | Nuolaida taikoma studentams ARBA pensininkams | Kai tinka bet kuri iš kelių sąlygų | Naudojamas ten, kur logiškai reikėtų `and` |
| `not` | Apverčia loginę reikšmę priešinga | Jungiklis, kuris atrakina duris, kai yra IŠJUNGTAS | Tikrinant priešingą būseną arba tuščią įvestį | Dvigubas neigimas (`not not x`) apsunkina skaitymą |
| `in` | Tikrina, ar reikšmė yra tekste ar rinkinyje | Ieškai konkretaus žodžio laiške | Atpažįstant raktažodį vartotojo žinutėje | Nepatikrinamas raidžių registras prieš `in` |

Trumpas bendras pavyzdys:

```python
message = "Klausiu apie KAINĄ"
normalized = message.strip().lower()
is_price_question = "kain" in normalized
print(is_price_question)
```

```text
True
```

## 3. Vizualūs paaiškinimai

### Vizualizacija A – sprendimų medis

```text
                     score >= 9 ?
                    ┌─────┴─────┐
                  taip          ne
                    │            │
              "Puikiai"     score >= 7 ?
                            ┌─────┴─────┐
                          taip          ne
                            │            │
                       "Gerai"     score >= 5 ?
                                   ┌─────┴─────┐
                                 taip          ne
                                   │            │
                          "Patenkinamai"  "Reikia pakartoti"
```

**Iliustracijos pavadinimas:** „Vienas kelias iš kelių“
**Ką ji turi parodyti:** kad `if`/`elif`/`else` grandinėje vykdoma tik viena šaka – ta, kurios sąlyga pirma pasitvirtina.
**Kokie elementai turi būti matomi:** keturi galimi rezultatai, sąlygų klausimai, „taip“/„ne“ šakos ir aiškiai pažymėtas vienintelis pasiektas galutinis mazgas.
**Siūlomas vaizdo generavimo promptas:** „Minimalistinė edukacinė vektorinė medžio diagrama lietuvių kalba: šaknyje klausimas score >= 9, dvi šakos taip/ne, po jų dar du panašūs sąlygų mazgai, keturi galutiniai lapeliai su tekstu Puikiai, Gerai, Patenkinamai, Reikia pakartoti; vienas kelias paryškintas.“

### Vizualizacija B – `and` ir `or` tiesos lentelės

```text
   AND (abi turi būti True)        OR (pakanka bent vienos)
   ┌───────┬───────┬────────┐      ┌───────┬───────┬───────┐
   │   A   │   B   │ A and B│      │   A   │   B   │ A or B│
   ├───────┼───────┼────────┤      ├───────┼───────┼───────┤
   │ True  │ True  │  True  │      │ True  │ True  │ True  │
   │ True  │ False │  False │      │ True  │ False │ True  │
   │ False │ True  │  False │      │ False │ True  │ True  │
   │ False │ False │  False │      │ False │ False │ False │
   └───────┴───────┴────────┘      └───────┴───────┴───────┘
```

**Iliustracijos pavadinimas:** „Dvi skirtingos logikos“
**Ką ji turi parodyti:** kad `and` reikalauja abiejų sąlygų, o `or` – bent vienos; tos pačios reikšmės `A` ir `B` duoda skirtingą rezultatą priklausomai nuo operatoriaus.
**Kokie elementai turi būti matomi:** dvi greta esančios lentelės su vienodais `A`/`B` stulpeliais, bet skirtingu trečiu stulpeliu, ir aiškus vizualus kontrastas tarp jų.
**Siūlomas vaizdo generavimo promptas:** „Dvi greta esančios mokomosios tiesos lentelės lietuvių kalba pavadinimais AND ir OR, keturios eilutės su True/False reikšmėmis, paskutinis stulpelis spalvotai paryškintas pagal rezultatą.“

### Vizualizacija C – teksto normalizavimo kelias

```text
Vartotojas įrašo „  LABAS  “
          │
          ▼
input() grąžina "  LABAS  "
          │
          ▼ .strip()
       "LABAS"
          │
          ▼ .lower()
       "labas"
          │
          ▼ == "labas"
         True
```

**Iliustracijos pavadinimas:** „Nuo netvarkingo teksto iki patikimo palyginimo“
**Ką ji turi parodyti:** kodėl prieš lyginant vartotojo tekstą reikia jį išvalyti nuo tarpų ir suvienodinti raidžių registrą.
**Kokie elementai turi būti matomi:** klaviatūra ar teksto laukas, tarpai aplink žodį, `.strip()`, `.lower()`, galutinis palyginimas su `True`.
**Siūlomas vaizdo generavimo promptas:** „Vertikali mokomoji proceso diagrama lietuvių kalba: vartotojas įveda tekstą su tarpais ir didžiosiomis raidėmis, strip pašalina tarpus, lower pakeičia raides mažosiomis, galiausiai lyginama su etalonu ir gaunamas True; kiekvienas žingsnis kitos spalvos.“

## 4. Palyginimai ir loginės reikšmės (bool)

Palyginimo rezultatas visada yra `True` arba `False` – trečios galimybės nėra.

```python
message = "Labas, padėk rasti kursą"
normalized = message.lower()

print("labas" in normalized)   # True
print(len(message) > 10)       # True
```

`lower()` nekeičia pradinio teksto – jis grąžina **naują** tekstą mažosiomis raidėmis, o originalas `message` lieka nepakitęs. Tai ypač naudinga atpažįstant `Labas`, `LABAS` ir `labas` kaip tą pačią intenciją.

> **Dažna klaida:** `"AI" == "ai"` grąžina `False`, nes Python palygina raides tiksliai, tarp jų ir registrą. Prieš lygindamas vartotojo tekstą, visada pritaikyk `.lower()` (o kartais ir `.strip()`).

### Greita praktika

**Mini užduotis.** Prieš paleisdamas nuspėk keturių eilučių rezultatus.

```python
print(12 >= 12)
print("AI" == "ai")
print("python" in "Mokausi python")
print(5 != 3)
```

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```text
True
False
True
True
```

`12 >= 12` teisinga, nes reikšmės lygios. `"AI" == "ai"` klaidinga dėl skirtingo raidžių registro. `"python" in "Mokausi python"` teisinga, nes žodis randamas tekste. `5 != 3` teisinga, nes reikšmės skiriasi.

</details>

## 5. Keli keliai su `elif`

```python
score = int(input("Įvertinimas nuo 0 iki 10: "))

if score >= 9:
    print("Puikiai")
elif score >= 7:
    print("Gerai")
elif score >= 5:
    print("Patenkinamai")
else:
    print("Reikia pakartoti")
```

Eilutė po eilutės:

1. `score = int(input(...))` – tekstinę įvestį paverčiame sveiku skaičiumi, kad galėtume jį lyginti su skaičiais.
2. `if score >= 9:` – tikrinama pati griežčiausia (siauriausia) riba pirmiausia.
3. Jei ji neteisinga, Python pereina prie `elif score >= 7:`, tada prie `elif score >= 5:` – kiekviena tikrinama tik jei visos ankstesnės buvo `False`.
4. `else:` pagauna visus likusius atvejus, kuriems netiko nė viena aukščiau esanti sąlyga.

Python tikrina nuo viršaus ir vykdo **tik pirmą** tinkamą šaką. Todėl griežčiausią ribą rašome pirmiausia. Jei pradėtume nuo `score >= 5`, devynetas niekada nepasiektų šakos `score >= 9`, nes `9 >= 5` jau būtų teisinga ir programa sustotų ties „Patenkinamai“.

> **Dažna klaida:** sąlygų grandinėje parašius plačiausią ribą pirmą (`score >= 5` prieš `score >= 9`), konkretesnės šakos niekada nepasieksi. Visada rikiuok nuo konkrečiausios prie bendriausios.

**Mini užduotis.** Parašyk sprendimų medį, kuris pagal temperatūrą (`int`) pasako, kaip rengtis: `>= 25` → „Karšta“, `>= 15` → „Šilta“, `>= 5` → „Vėsu“, kitu atveju – „Šalta“.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
temperature = int(input("Temperatūra (°C): "))

if temperature >= 25:
    print("Karšta")
elif temperature >= 15:
    print("Šilta")
elif temperature >= 5:
    print("Vėsu")
else:
    print("Šalta")
```

Tvarka ta pati kaip pažymių pavyzdyje: nuo griežčiausios ribos iki numatytojo atvejo.

</details>

## 6. Sudėtinės sąlygos: `and`, `or`, `not`

- `and` – abi sąlygos turi būti teisingos;
- `or` – pakanka bent vienos;
- `not` – apverčia rezultatą.

```python
age = int(input("Amžius: "))
has_ticket = input("Ar turi bilietą? (taip/ne): ").lower() == "taip"

if age >= 16 and has_ticket:
    print("Gali dalyvauti")
else:
    print("Patikrink amžių arba bilietą")
```

> **Profesinė taisyklė:** sudėtingą sąlygą suskaidyk į prasmingai pavadintus `bool` kintamuosius. Kodą bus lengviau patikrinti.

```python
is_adult = age >= 18
has_long_question = len(message) >= 10
can_continue = is_adult and has_long_question
```

> **Dažna klaida:** rašant `age >= 16 and has_ticket or has_parent` be skliaustų, sunku iškart pasakyti, kuri dalis vykdoma pirmiau. Skliaustais parodyk ketinimą: `(age >= 16 and has_ticket) or has_parent`.

**Mini užduotis.** Sukurk kintamuosius `is_member = True` ir `cart_total = 45.0`, tada parašyk sąlygą, kuri parodo „Nemokamas pristatymas“, jei klientas yra narys ARBA suma bent 50.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
is_member = True
cart_total = 45.0

if is_member or cart_total >= 50:
    print("Nemokamas pristatymas")
else:
    print("Pristatymas mokamas")
```

Kadangi `is_member` yra `True`, visa `or` išraiška jau yra teisinga, net jei `cart_total` nesiekia 50 – todėl spausdinama „Nemokamas pristatymas“.

</details>

## 7. Įvesties ribos ir paprasti patikrinimai

Vartotojas gali įvesti tuščią tekstą ar per trumpą klausimą. Kol dar nesimokėme `try`/`except`, bent patikrinkime paprastas ribas:

```python
question = input("Klausimas: ").strip()

if not question:
    print("Klausimas negali būti tuščias.")
elif len(question) < 5:
    print("Parašyk šiek tiek išsamiau.")
else:
    print("Klausimas priimtas.")
```

`strip()` pašalina tarpus teksto pradžioje ir pabaigoje. Tuščias tekstas sąlygoje laikomas `False`, todėl `not question` aptinka ir `""`, ir tekstą, kuris po `strip()` liko tuščias (pvz., vien tarpai).

> **Dažna klaida:** tikrinant tik `question == ""`, praleidžiamas atvejis, kai vartotojas įveda vien tarpus (`"   "`). Prieš tikrindamas tuštumą, visada pirma pritaikyk `.strip()`.

**Mini užduotis.** Papildyk kodą taip, kad jis taip pat priimtų vardą (`name`) ir atmestų jį, jei jame yra mažiau nei 2 simboliai.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
name = input("Vardas: ").strip()

if not name:
    print("Vardas negali būti tuščias.")
elif len(name) < 2:
    print("Vardas per trumpas.")
else:
    print("Vardas priimtas.")
```

Struktūra identiška klausimo pavyzdžiui – tik pakeistas kintamojo vardas ir riba.

</details>

## 8. Įvairūs kodo pavyzdžiai

### Minimalus pavyzdys

**Problema:** patikrinti, ar skaičius lyginis.

```python
number = int(input("Įvesk skaičių: "))

if number % 2 == 0:
    print("Lyginis")
else:
    print("Nelyginis")
```

```text
Įvesk skaičių: 7
Nelyginis
```

**Patobulinimas:** pridėk atskirą pranešimą, jei skaičius lygus 0.

### Kasdienis pavyzdys – apranga pagal orą

```python
temperature = int(input("Kiek laipsnių lauke? "))

if temperature >= 20:
    print("Vilkėk marškinėlius")
elif temperature >= 10:
    print("Vilkėk švarką")
else:
    print("Vilkėk striukę")
```

```text
Kiek laipsnių lauke? 8
Vilkėk striukę
```

**Patobulinimas:** pridėk papildomą sąlygą lietui – naudok antrą `input()` klausimą ir `and`.

### Darbo pavyzdys – sąskaitos būsena

```python
days_overdue = int(input("Kiek dienų vėluoja mokėjimas? "))

if days_overdue <= 0:
    status = "Apmokėta laiku"
elif days_overdue <= 7:
    status = "Lengvas vėlavimas"
else:
    status = "Reikia priminimo"

print(f"Sąskaitos būsena: {status}")
```

```text
Kiek dienų vėluoja mokėjimas? 10
Sąskaitos būsena: Reikia priminimo
```

**Patobulinimas:** apskaičiuok delspinigius už kiekvieną vėlavimo dieną virš 7.

### Automatizavimo pavyzdys – laiškų rūšiavimas

```python
subject = input("Laiško tema: ").strip().lower()

if "sąskaita" in subject or "invoice" in subject:
    folder = "Finansai"
elif "susitikimas" in subject:
    folder = "Kalendorius"
else:
    folder = "Bendras"

print(f"Laiškas perkeliamas į aplanką: {folder}")
```

```text
Laiško tema: Sąskaita už spalio mėnesį
Laiškas perkeliamas į aplanką: Finansai
```

**Patobulinimas:** raktažodžius sudėk į atskirą sąrašą ir tikrink su keliais `in`, kad juos būtų lengviau papildyti.

### Duomenų ir AI pavyzdys – modelio patikimumo riba

```python
predicted_topic = "pristatymas"
confidence = 0.62

if confidence >= 0.8:
    action = "Atsakyti automatiškai"
elif confidence >= 0.5:
    action = "Peržiūrėti prieš siunčiant"
else:
    action = "Perduoti žmogui"

print(f"Tema: {predicted_topic}, veiksmas: {action}")
```

```text
Tema: pristatymas, veiksmas: Peržiūrėti prieš siunčiant
```

**Patobulinimas:** pridėk atvejį, kai `confidence` yra lygiai `0.8` – patikrink, kuriai šakai jis priskiriamas.

### Klaidingas pavyzdys – pataisyk

**Šis kodas nepasileis – jame yra sąmoninga klaida (`SyntaxError`). Rask ją prieš skaitydamas paaiškinimą.**

```python
age = 20
if age = 18:
    print("Pilnametis")
```

Klaida: sąlygoje naudojamas priskyrimo operatorius `=` vietoj palyginimo `==` (ar `>=`). Python tokios sintaksės nepriims ir programa nepasileis.

Pataisymas:

```python
age = 20
if age >= 18:
    print("Pilnametis")
```

```text
Pilnametis
```

## 9. Interaktyvios veiklos

### 1. Nuspėk rezultatą

```python
score = 6

if score >= 9:
    result = "A"
elif score >= 7:
    result = "B"
elif score >= 5:
    result = "C"
else:
    result = "D"

print(result)
```

A. `A`
B. `B`
C. `C`
D. `D`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**C.** `6` nėra `>= 9`, nėra `>= 7`, bet yra `>= 5`, todėl vykdoma trečia šaka ir spausdinama `"C"`.

</details>

### 2. Užpildyk trūkstamą kodą

```python
age = 17
has_permission = True

if age >= 18 ____ has_permission:
    print("Įleidžiama")
else:
    print("Neįleidžiama")
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
if age >= 18 or has_permission:
```

Norime įleisti nepilnametį, jei jis turi leidimą, todėl reikia `or` – pakanka bent vienos sąlygos.

</details>

### 3. Surask klaidą

```python
temperature = 5

if temperature > 0
    print("Virš nulio")
else:
    print("Šalta arba nulis")
```

Nustatyk klaidą, paaiškink ir pataisyk.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Trūksta dvitaškio po sąlygos.

```python
temperature = 5

if temperature > 0:
    print("Virš nulio")
else:
    print("Šalta arba nulis")
```

</details>

### 4. Sudėliok teisinga tvarka

```text
elif "laik" in topic:
topic = input("Klausimas: ").strip().lower()
    print("Kalbame apie laiką")
if "kain" in topic:
    print("Kalbame apie kainą")
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
topic = input("Klausimas: ").strip().lower()
if "kain" in topic:
    print("Kalbame apie kainą")
elif "laik" in topic:
    print("Kalbame apie laiką")
```

Pirma turi būti gauta ir sunormalizuota įvestis, tik tada – sąlygų grandinė.

</details>

### 5. Pasirink tinkamą sprendimą

Kuris variantas teisingai patikrina, ar klausimas po `strip()` liko tuščias?

A. `if question == None:`
B. `if not question:`
C. `if question = "":`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Tuščias tekstas sąlygoje laikomas `False`, todėl `not question` teisingai aptinka tuščią įvestį. Variantas A tikrina netinkamą dalyką, o C yra sintaksės klaida (priskyrimas vietoj palyginimo).

</details>

### 6. Parašyk pats

Parašyk sprendimų medį, kuris pagal krepšelio prekių skaičių parodo skirtingą pranešimą apie pristatymo laiką: `0` prekių – „Krepšelis tuščias“; `1`–`5` – „Pristatymas per 2 dienas“; daugiau nei `5` – „Pristatymas per 5 dienas“.

### 7. Patobulink kodą

```python
x = input("a: ")
if x == "taip":
    print("ok")
if x == "ne":
    print("neok")
if x != "taip" and x != "ne":
    print("?")
```

Perrašyk naudodamas `elif` ir prasmingus vardus.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
answer = input("Ar sutinki? (taip/ne): ").strip().lower()

if answer == "taip":
    print("Sutikimas gautas")
elif answer == "ne":
    print("Sutikimas negautas")
else:
    print("Atsakyk 'taip' arba 'ne'")
```

`elif` grandinė aiškiai parodo, kad tikrinamas tas pats kintamasis, o ne trys nepriklausomi `if` blokai.

</details>

## 10. Žinių patikrinimas prieš platformos testą

Pirmiausia atsakyk neužleisdamas atsakymų.

1. Kuo skiriasi `if` ir `elif` naudojimo tikslas sprendimų grandinėje?
2. Kodėl `"Labas" == "labas"` grąžina `False`?
3. Kas nutinka, jei `if` sąlyga neteisinga ir nėra nei `elif`, nei `else`?
4. Kam naudojamas `strip()` prieš tikrinant vartotojo įvestį?
5. Kuo `in` skiriasi nuo `==`, tikrinant tekstą?
6. Kodėl verta sudėtingą sąlygą suskaidyti į atskirus, aiškiai pavadintus `bool` kintamuosius?
7. Ar `if not message:` ir `if message == "":` visada duoda tą patį rezultatą?
8. Kiek šakų iš `if`/`elif`/…/`else` grandinės gali suveikti per vieną programos vykdymą?
9. Kodėl `if age = 18:` (su vienu lygybės ženklu) sukelia klaidą dar prieš programai pasileidžiant?
10. Kada geriau rinktis `and`, o kada `or`, jungiant dvi privalomas sąlygas?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymus ir paaiškinimus</summary>

1. `if` pradeda grandinę ir tikrinamas visada; `elif` tikrinamas tik jei visos ankstesnės grandinės sąlygos buvo `False`.
2. Python palygina raides tiksliai, tarp jų ir registrą, todėl skirtingo registro tekstai laikomi skirtingomis reikšmėmis.
3. Programa tiesiog nieko nevykdo tame bloke ir tęsia kitą kodo eilutę po jo.
4. `strip()` pašalina atsitiktinius tarpus įvesties pradžioje/pabaigoje, kad, pvz., `" taip "` būtų atpažinta kaip `"taip"`.
5. `==` reikalauja visiško sutapimo, o `in` tikrina, ar viena reikšmė yra platesnės sekos (pvz., sakinio) dalis.
6. Aiškiai pavadinti tarpiniai `bool` kintamieji (pvz. `is_adult`) leidžia kiekvieną sąlygos dalį patikrinti atskirai ir sumažina klaidų riziką skaitant sudėtingą išraišką.
7. Ne visada. Su paprastu `input()` rezultatu abu variantai praktiškai sutampa, bet `not message` taip pat laikytų „tuščiu“ ir kitas reikšmes (pvz. `None`), o `message == ""` tikrina tik tikslų tuščią tekstą.
8. Tik viena – pirmoji, kurios sąlyga teisinga; likusios šakos praleidžiamos, net jei jų sąlygos taip pat būtų teisingos.
9. Nes `=` Python kalboje yra priskyrimo, o ne palyginimo operatorius, ir tokia sintaksė sąlygoje neleidžiama – klaidą Python aptinka analizuodamas kodą dar prieš vykdymą.
10. `and`, kai reikalingos visos sąlygos vienu metu (griežtesnis reikalavimas); `or`, kai pakanka bet kurios iš jų (švelnesnis reikalavimas).

</details>

## 11. Praktinės užduotys

### 1 lygis – nuolaidos taisyklė

#### Užduotis 1. Krepšelio nuolaida

**Sąlyga:** paprašyk krepšelio sumos. Jei suma bent 100 – taikyk 15 % nuolaidą, jei bent 50 – 10 %, kitu atveju nuolaidos nėra. Parodyk galutinę sumą suapvalintą iki dviejų skaitmenų po kablelio.
**Pavyzdinė įvestis:** `120`.
**Laukiamas rezultatas:** `Galutinė suma: 102.0 Eur`.
**Užuomina:** griežčiausią ribą (`>= 100`) tikrink pirmiausia; suapvalinti padeda funkcija `round(reikšmė, 2)`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
cart_total = float(input("Krepšelio suma: "))

if cart_total >= 100:
    discount_rate = 0.15
elif cart_total >= 50:
    discount_rate = 0.10
else:
    discount_rate = 0.0

final_total = round(cart_total - cart_total * discount_rate, 2)
print(f"Galutinė suma: {final_total} Eur")
```

`round(reikšmė, 2)` suapvalina skaičių iki dviejų skaitmenų po kablelio. **Papildomas iššūkis:** parodyk ir taikomos nuolaidos procentą kaip atskirą f-string reikšmę.

</details>

### 2 lygis – prisijungimo patikra

#### Užduotis 2. Prisijungimo patikra

**Sąlyga:** paprašyk vartotojo vardo ir slaptažodžio. Įleisk tik jei vardas `studentas`, o slaptažodis `python88`. Atskirai pranešk, ar nežinomas vartotojas, ar neteisingas slaptažodis. Tikroje sistemoje slaptažodžių kode nelaikytume – čia tik sąlygų pratimas.
**Pavyzdinė įvestis:** vardas `studentas`, slaptažodis `python88`.
**Laukiamas rezultatas:** `Prisijungimas sėkmingas.`
**Užuomina:** pirma patikrink vardą, tik tada slaptažodį – taip atskirsi dvi skirtingas klaidas.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
username = input("Vartotojo vardas: ")
password = input("Slaptažodis: ")

if username != "studentas":
    print("Nežinomas vartotojas.")
elif password != "python88":
    print("Neteisingas slaptažodis.")
else:
    print("Prisijungimas sėkmingas.")
```

Jei vardas neteisingas, apie slaptažodį net nesprendžiama – `elif` toliau netikrinamas. **Papildomas iššūkis:** pridėk trečią bandymą su teisingu vardu, bet tuščiu slaptažodžiu, ir patikrink, koks pranešimas parodomas.

</details>

### 3 lygis – užklausos maršrutizatorius

#### Užduotis 3. Užklausos maršrutizatorius

**Sąlyga:** programa turi atpažinti žodžius `kaina`, `laikas`, `kontaktai`, `pagalba`. Neatpažinus – mandagiai išvardyti galimas temas. Turi veikti nepriklausomai nuo raidžių registro ir papildomų tarpų.
**Pavyzdinė įvestis:** `Kiek KAINUOJA kursas?`.
**Laukiamas rezultatas:** `Kaina priklauso nuo pasirinkto kurso.`
**Užuomina:** prieš tikrindamas `in`, visada pritaikyk `.strip().lower()`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
topic = input("Apie ką klausi? ").strip().lower()

if "kain" in topic:
    print("Kaina priklauso nuo pasirinkto kurso.")
elif "laik" in topic:
    print("Užsiėmimai vyksta pirmadieniais ir trečiadieniais.")
elif "kontakt" in topic:
    print("Susisiekite el. paštu mokymai@example.lt.")
elif "pagalb" in topic:
    print("Pagalbos komanda pasiekiama darbo dienomis.")
else:
    print("Galiu papasakoti apie kainą, laiką, kontaktus arba pagalbą.")
```

`"kain" in topic` suveikia net jei žodis yra didesnio sakinio dalis (pvz., „kainuoja“), nes `.lower()` panaikina registro skirtumus. **Papildomas iššūkis:** išbandyk įvestį su dviem temomis vienoje žinutėje (pvz., „kaina ir laikas“) ir paaiškink, kodėl atsakoma tik apie vieną.

</details>

## 12. Gilioji laboratorija: sprendimo medis nuo nulio

Ši laboratorija sujungia viską, ko išmokai šioje pamokoje, ir tiesiogiai paruošia pagrindą Asistento 0.2 komandų maršrutizatoriui kitoje pamokoje. Jai skirk apie 90 minučių. Po kiekvieno etapo paleisk programą ir užrašyk, ką tikėjaisi pamatyti.

### 12.1. Tiesa nėra tik `True` ir `False`

```python
for value in ["", "labas", 0, 3, [], ["klausimas"], None]:
    print(repr(value), bool(value))
```

Tuščias tekstas, nulis, tuščias sąrašas ir `None` yra `False`; netušti tekstai ir sąrašai – `True`. Verslo taisyklėje vis tiek rašyk aiškiai: `if quantity == 0` geriau nei neaiškus `if not quantity`, kai tikrini būtent nulį.

### 12.2. Operatoriai turi tvarką

```python
is_ready = age >= 16 and has_ticket or has_parent
```

Ši išraiška skaitoma kaip `(age >= 16 and has_ticket) or has_parent`, nes `and` vykdomas anksčiau už `or`. Skliaustais parodyk ketinimą, o sudėtingą sąlygą išskaidyk į `is_old_enough`, `has_ticket` ir `has_parent`.

### 12.3. Įvesties tikrinimas cikle

```python
while True:
    score_text = input("Įvertinimas 0–10 arba q: ").strip().lower()
    if score_text == "q":
        break
    if not score_text.isdigit():
        print("Įvesk sveiką skaičių.")
        continue
    score = int(score_text)
    if 0 <= score <= 10:
        print(f"Priimta: {score}")
        break
    print("Skaičius turi būti nuo 0 iki 10.")
```

`.isdigit()` čia yra sąmoningas supaprastinimas: jis neatpažįsta `-1` ir `8.5`. Vėliau netinkamus skaičius tvarkysime su `try/except`.

### 12.4. Derinimo iššūkis

```python
age = 15
has_ticket = True
if age >= 18 or has_ticket:
    print("Įleidžiama")
```

Parašyk bandymą, kuris atskleistų problemą. Taisyklėje reikia ir amžiaus, ir bilieto, todėl tikėtinas taisymas yra `and`. Pirma užrašyk gautą ir tikėtiną rezultatą, tik tada taisyk kodą.

### 12.5. Kontrolinis taškas

Laboratorija baigta, jei gali paaiškinti, kada skiriasi `if not message` ir `if message == ""`, kaip skliaustai keičia sąlygą ir kaip neleisti tuščiai įvesčiai pasiekti būsimo DI kvietimo. Šie sprendimai taps Asistento 0.2 komandų maršrutizatoriumi.

## 13. Mini projektas: Asistentas 0.1

### 1. Projekto situacija

Kursų administratorius nori, kad svetainėje veiktų paprastas tekstinis asistentas, atsakantis į dažniausius klausimus apie kursą, kainą ir kontaktus, kol žmogus dar nespėjo parašyti el. laiško.

### 2. Galutinis tikslas

Sukurti `assistant_v01.py`, kuris paima vieną vartotojo žinutę, sprendimų medžiu atpažįsta joje raktažodžius ir atsako viena iš keleto iš anksto paruoštų žinučių.

### 3. Funkciniai reikalavimai

Programa turi:

1. priimti vieną vartotojo žinutę su `input()`;
2. iškart ją sunormalizuoti su `.strip().lower()`;
3. jei žinutė tuščia, atsakyti paprašant klausimo;
4. atpažinti pasisveikinimą (`labas` arba `sveiki`);
5. atpažinti klausimus apie kursą, kainą ir kontaktus;
6. jei nė viena tema neatpažinta, mandagiai pasakyti, apie ką galima klausti;
7. atsakymą parodyti su aiškia f-string žinute, prasidedančia `Asistentas:`.

### 4. Pavyzdinė įvestis

```text
Tu: Kiek kainuoja kursas?
```

### 5. Pavyzdinis rezultatas

```text
Asistentas 0.1. Gali klausti apie kursą, kainą arba kontaktus.
Tu: Kiek kainuoja kursas?
Asistentas: Kainą patikslinkite su mokymų koordinatoriumi.
```

### 6. Projekto kūrimo etapai

1. Sukurk failą `assistant_v01.py` ir parodyk pasisveikinimo antraštę.
2. Priimk vieną žinutę su `input()` ir iškart pritaikyk `.strip().lower()`.
3. Pridėk tuščios žinutės patikrą (`if not message`).
4. Pridėk sveikinimo atpažinimą su `or`.
5. Pridėk temas – kursas, kaina, kontaktai – kiekvieną kaip atskirą `elif`.
6. Pridėk `else` numatytajam atsakymui.
7. Parodyk atsakymą f-string žinute su prefiksu `Asistentas:`.
8. Išbandyk bent 10 skirtingų žinučių ir užsirašyk rezultatus lentelėje (žr. „Galimi patobulinimai“).
9. Kai pagrindas veikia, savarankiškai pridėk dvi naujas temas ir draugišką atsisveikinimą.

### 7. Pseudokodas

```text
PARODYK pasisveikinimo antraštę
GAUK žinutę ir PANORMALIZUOK (strip, lower)
JEI žinutė tuščia TADA atsakymas = prašymas paklausti
KITAIP JEI žinutėje yra sveikinimo žodis TADA atsakymas = sveikinimas
KITAIP JEI žinutėje yra "kurs" TADA atsakymas = info apie kursą
KITAIP JEI žinutėje yra "kain" TADA atsakymas = info apie kainą
KITAIP JEI žinutėje yra "kontakt" TADA atsakymas = kontaktai
KITAIP atsakymas = nežinau, bet galiu padėti su šiomis temomis
PARODYK atsakymą
```

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

```python
print("Asistentas 0.1. Gali klausti apie kursą, kainą arba kontaktus.")
message = input("Tu: ").strip().lower()

if not message:
    answer = "Negavau klausimo. Parašyk bent kelis žodžius."
elif "labas" in message or "sveiki" in message:
    answer = "Sveiki! Kuo galiu padėti?"
elif "kurs" in message:
    answer = "Python kursas trunka 88 akademines valandas."
elif "kain" in message:
    answer = "Kainą patikslinkite su mokymų koordinatoriumi."
elif "kontakt" in message:
    answer = "Parašykite adresu mokymai@example.lt."
else:
    answer = "Dar nesupratau. Galiu papasakoti apie kursą, kainą ir kontaktus."

print(f"Asistentas: {answer}")
```

Eilutė po eilutės: pirmiausia programa parodo antraštę ir gauna vieną žinutę, iškart pritaikydama `.strip().lower()`. Tada `if`/`elif` grandinė nuo konkrečiausio atvejo (tuščia žinutė) iki bendriausio (`else`) tikrina, kuri tema tinka, ir kiekvienai priskiria savo `answer` tekstą. Kadangi sveikinimo patikra parašyta anksčiau nei „kurs“/„kain“/„kontakt“, žinutė, kurioje yra ir „labas“, ir „kaina“ (pvz. „Labas, kiek kainuoja kursas?“), gaus **sveikinimo** atsakymą – tai ta pati tvarkos taisyklė, kurią mokeisi 5 skyriuje. Galiausiai vienu `print()` su f-string parodomas pasirinktas atsakymas.

</details>

### 8. Galimi patobulinimai

- pridėk dvi naujas temas (pvz., „registracija“ ir „tvarkaraštis“) kaip papildomus `elif`;
- pridėk draugišką atsisveikinimą, jei žinutėje yra „viso gero“ ar „ačiū“;
- sudaryk bent 10 testinių žinučių lentelę pagal šabloną žemiau ir užpildyk visas eilutes;
- trečioje pamokoje šis sprendimų medis taps funkcija ir gaus daugiau temų (Asistentas 0.2);
- vėliau pridėsime kartojimą (`while`), kad asistentas priimtų kelias žinutes iš eilės, o ne tik vieną.

Testavimo lentelės šablonas (užpildyk iki 10 eilučių):

| # | Įvestis | Tikėtas atsakymas | Faktinis atsakymas | Pavyko? |
|---|---|---|---|---|
| 1 | `labas` | Sveikinimas | | |
| 2 | `Kiek kainuoja kursas?` | Info apie kainą | | |
| 3 | `` (tuščia) | Prašymas paklausti | | |
| … | | | | |

### 9. `README.md` šablonas

```text
# Asistentas 0.1

Paprastas tekstinis asistentas, atpažįstantis kelias temas iš vienos vartotojo žinutės.

## Funkcijos
- Atpažįsta pasisveikinimą
- Atsako apie kursą, kainą ir kontaktus
- Tvarkingai reaguoja į tuščią ar nesuprastą žinutę

## Paleidimas
python3 assistant_v01.py

## Pavyzdys
Įvesk klausimą apie kursą, kainą ar kontaktus pagal programos klausimą „Tu: “.

## Ką išmokau
Palyginimai, elif grandinės, and/or/not, teksto normalizavimas, tuščios įvesties tikrinimas.

## Tolimesni patobulinimai
Daugiau temų, atsisveikinimas, virtimas funkcija ir kartojimas su while.
```

## 14. Dažniausios klaidos

| Klaida | Kodėl ji atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| Sąlygoje naudojamas `=` vietoj `==` | Supainiojamas priskyrimas su palyginimu | `if age = 18:` | `if age == 18:` | Prisimink: `=` visada priskiria, `==` visada lygina |
| Trūksta dvitaškio | Pamirštama sąlygos antraštės sintaksė | `if age >= 18` | `if age >= 18:` | Po kiekvienos `if`/`elif`/`else` eilutės patikrink dvitaškį |
| Netolygios įtraukos | Python bloką atpažįsta pagal atitraukimą, ne pagal riestinius skliaustus | sumaišyti tarpai ir tabuliacijos | visur naudok po 4 tarpus | Redaktoriuje įjunk tarpų/tabuliacijų rodymą |
| Per plati sąlyga parašyta pirmiausia | Python vykdo tik pirmą tinkamą šaką | `if score >= 5: ... elif score >= 9: ...` | `if score >= 9: ... elif score >= 5: ...` | Griežčiausią (siauriausią) ribą visada rašyk pirmą |
| `Labas` neatpažįstamas kaip `labas` | Palyginimas jautrus raidžių registrui | `if "labas" in message:` be normalizavimo | `if "labas" in message.strip().lower():` | Prieš tikrindamas visada pritaikyk `.strip().lower()` |
| Neaiški `and`/`or` tvarka sudėtingoje sąlygoje | `and` vykdomas anksčiau už `or`, bet be skliaustų tai nematoma | `age >= 18 or has_ticket and has_id` | `age >= 18 or (has_ticket and has_id)` | Sudėtingą sąlygą skaidyk į pavadintus `bool` kintamuosius arba naudok skliaustus |
| Tikrinamas tik `== ""`, praleidžiami kiti „tušti“ atvejai | Manoma, kad tuščias tekstas yra vienintelis „nieko neįvedė“ atvejis | `if question == "":` be `.strip()` | `if not question.strip():` | Prieš tikrindamas tuštumą visada pritaikyk `.strip()` |

## 15. Profesionali praktika

- Sudėtingą sąlygą visada skaidyk į aiškiai pavadintus `bool` kintamuosius (`is_adult`, `has_ticket`), o ne vieną ilgą išraišką.
- Prieš lygindamas vartotojo tekstą, visada pritaikyk `.strip()` ir `.lower()`.
- Griežčiausią / konkrečiausią sąlygą rašyk pirmą `if`/`elif` grandinėje.
- Naudok skliaustus, kai grandinėje yra ir `and`, ir `or`, kad ketinimas būtų aiškus net po mėnesio.
- Kiekvieną naują sąlygų šaką iškart išbandyk bent su vienu atveju, kuris ją turėtų suaktyvinti, ir vienu, kuris neturėtų.
- Rašydamas asistentą ar bet kokį maršrutizatorių, visada palik `else` numatytajam „nesupratau“ atsakymui – niekada nepalik vartotojo be atsakymo.
- Testinių atvejų lentelė (įvestis → tikėtas → faktinis rezultatas) profesionalioje komandoje yra standartinis būdas parodyti, kad sprendimų medis veikia.

## 16. Kodėl tai svarbu mokantis AI?

Net tikrose AI sistemose dalis logikos visada lieka paprastas sprendimų medis: patikrinti, ar įvestis leistina, nuspręsti, kokia tema atitinka vartotojo klausimą, ir pasirinkti, kada atsakyti iš karto, o kada kreiptis į brangesnį AI modelį. `bool` reikšmės čia dažnai žymi, ar tema jau atpažinta, o `float` – modelio pateiktą tikimybę ar „confidence“ balą.

```python
user_message = "atšaukti užsakymą"
intent_known = "atšauk" in user_message or "grąžin" in user_message

if not user_message.strip():
    response = "Parašyk klausimą."
elif intent_known:
    response = "Persiunčiu jus į užsakymų atšaukimo skyrių."
else:
    response = "Perduodu klausimą dirbtinio intelekto modeliui."

print(response)
```

```text
Persiunčiu jus į užsakymų atšaukimo skyrių.
```

Realūs asistentai naudoja lygiai tokį patį principą: kai žinutė atitinka jau žinomą, dažną atvejį, atsakoma iš karto ir pigiai; o kai atvejis neaiškus, klausimas perduodamas galingesniam (ir brangesniam) AI modeliui. Asistentas 0.1, kurį sukūrei šioje pamokoje, yra būtent toks pirmasis, dar visiškai taisyklėmis paremtas sprendimų sluoksnis.

## 17. Pamokos santrauka

- Palyginimo operatoriai (`==`, `!=`, `>`, `<`, `>=`, `<=`) visada grąžina `bool`.
- `if`/`elif`/`else` grandinėje vykdoma tik pirma tinkama šaka – griežčiausią ribą rašyk pirmiausia.
- `and` reikalauja abiejų sąlygų, `or` – bent vienos, `not` apverčia rezultatą.
- Prieš lygindamas vartotojo tekstą, visada pritaikyk `.strip()` ir `.lower()`.
- Tuščia įvestis aptinkama su `if not tekstas:`, be `try`/`except`.
- Sudėtingą sąlygą verta suskaidyti į aiškiai pavadintus `bool` kintamuosius.
- Asistentas 0.1 yra pirmas tavo sprendimų medžiu paremtas pokalbių robotukas – jo logika bus plečiama kitose pamokose.

**Atmintinė:**

```python
message = input("Žinutė: ").strip().lower()

if not message:
    answer = "Klausimas tuščias."
elif "labas" in message:
    answer = "Sveiki!"
elif "kain" in message:
    answer = "Info apie kainą."
else:
    answer = "Nesupratau, bandyk kitaip."

print(f"Asistentas: {answer}")
```

**Sąlygos paverčia programą iš skaičiuoklės į sprendimus priimantį asistentą – ir būtent šis mechanizmas valdo, kada tavo būsimas AI asistentas atsakys pats, o kada paklaus modelio.**

## 18. Savirefleksija

1. Ką dabar gali padaryti, ko negalėjai prieš pamoką?
2. Kurią sąlygą buvo sunkiausia suformuluoti – kodėl?
3. Kokiais bandymais patikrinai, kad tavo sprendimų medis veikia teisinga tvarka?
4. Kaip paaiškintum draugui, kodėl svarbu tikrinti tuščią įvestį prieš kitas sąlygas?
5. Kur galėtum pritaikyti `if`/`elif`/`else` logiką už programavimo ribų, priimdamas kasdienius sprendimus?

## 19. Namų darbas

### Privaloma – kino bilieto rekomendacija

Sukurk programą, kuri pagal amžių, turimą biudžetą ir norimą žanrą pateikia kino bilieto rekomendaciją. Reikalavimai: bent 3 `elif` šakos, viena `and`, viena `or`, tuščios įvesties patikra ir 8 bandymų lentelė (įvestis, tikėtas rezultatas, faktinis rezultatas, ar pavyko).

**Vertinimas (10 taškų):** teisinga `elif` tvarka – 3; `and`/`or` panaudojimas – 2; tuščios įvesties patikra – 2; 8 bandymų lentelė – 2; kodas paleidžiamas be klaidų – 1.

### Pasirenkama – ketvirta rekomendacijos šaka

Prie privalomos programos pridėk ketvirtą `elif` šaką (pvz., specialią rekomendaciją VIP nariams) ir patikrink, ar sąlygų tvarka po pakeitimo liko teisinga.

**Vertinimas (5 taškai):** nauja šaka veikia teisingai – 2; tvarka grandinėje išlieka teisinga – 1; pridėtas bent vienas testas naujai šakai – 1; aiškus kintamųjų pavadinimas – 1.

### Kūrybinis iššūkis – tavo srities maršrutizatorius

Sukurk savo temos raktažodžių atpažinimo asistentą, panašų į Asistentą 0.1, bet kitokia tema (pvz., sporto klubo, restorano ar bibliotekos asistentas). Atpažink bent 4 skirtingas temas ir turėk numatytąjį atsakymą.

**Vertinimas (5 taškai):** reali, prasminga tema – 1; bent 4 temos ir numatytasis atsakymas – 2; įvesties normalizavimas (`strip`/`lower`) – 1; savarankiškas, be kopijavimo, sprendimas – 1.

## 20. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Įžanga: sąlygos vs kintamieji, PIN pavyzdys | 15 min. | Pabrėžti `=` ir `==` skirtumą nuo pirmos minutės |
| Palyginimai ir `bool` | 25 min. | Daug praktikuoti su registro jautrumu (`"AI" == "ai"`) |
| Vizualizacijos ir sąvokų lentelė | 15 min. | Panaudoti diagramas kaip atspirties tašką prieš kodą |
| `elif` grandinės ir tvarka | 30 min. | Rodyti klaidingą tvarką realiu pavyzdžiu, ne tik pasakyti taisyklę |
| `and`, `or`, `not` | 30 min. | Skirti laiko skliaustų svarbai parodyti |
| Įvesties ribos ir tuščios įvesties patikra | 20 min. | Susieti su būsimu `try`/`except` poreikiu |
| Kodo pavyzdžių galerija ir interaktyvios veiklos | 25 min. | Tinka savarankiškam darbui poromis |
| Žinių patikrinimas ir praktinės užduotys (3 lygiai) | 45 min. | Automatiškai tikrinti su keliais testiniais atvejais |
| Gilioji laboratorija: sprendimo medis nuo nulio | 35 min. | Skirta greičiau pažengusiems; gali būti savarankiškas darbas silpnesniems |
| Mini projektas: Asistentas 0.1 | 30 min. | Kodo aiškumą ir `elif` tvarką vertinti rankiniu būdu |

Iliustracija labiausiai padėtų ties sprendimų medžio vizualizacija (A) ir `and`/`or` tiesos lentele (B) – abi vietos, kur mokiniai dažniausiai pasiklysta. Interaktyvų Python redaktorių verta įterpti iškart po PIN pavyzdžio, po `elif` tvarkos pavyzdžio, po `and`/`or` mini užduoties ir prie mini projekto Asistento 0.1. Platformoje verta fiksuoti: kiekvienos mini užduoties bandymų skaičių, dažniausius palyginimo klaidų tipus (`=` vietoj `==`, registro jautrumas, trūkstamas dvitaškis), testo rezultatą, praktinių užduočių (3 lygiai) užbaigimo laiką, ar mokinys atliko gilią laboratoriją, ir mini projekto testinių žinučių lentelės pilnumą.
