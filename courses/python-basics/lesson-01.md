---
title: Kintamieji ir duomenų tipai – sukurk interaktyvią kainos skaičiuoklę
module: Python pagrindai
order: 1
---

# Kintamieji ir duomenų tipai – sukurk interaktyvią kainos skaičiuoklę

> **Trukmė:** 6 akademinės valandos (apie 4 val. 30 min.). Bent 3 valandas skirk kodo rašymui, bandymams ir mini projektui.

## Trumpa anotacija

Šioje pamokoje išmoksi programai „prisiminti“ vardą, kainą ar būseną naudojant kintamuosius. Susipažinsi su tekstu, sveikaisiais ir dešimtainiais skaičiais, loginėmis reikšmėmis, vartotojo įvestimi ir tipų keitimu. Šie įgūdžiai naudojami skaičiuoklėse, automatizuotose ataskaitose, duomenų paruošime ir beveik kiekvienoje AI programoje.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- sukurti ir atnaujinti aiškiai pavadintus kintamuosius;
- praktiškai atskirti `str`, `int`, `float` ir `bool` reikšmes;
- su `type()` patikrinti reikšmės tipą;
- priimti vartotojo tekstą su `input()`;
- konvertuoti skaitinį tekstą su `int()` ir `float()`;
- atlikti pagrindinius aritmetinius skaičiavimus;
- su f-string suformuoti aiškią rezultatų žinutę;
- sukurti ir patikrinti interaktyvią kainos skaičiuoklę.

## Būtinos ankstesnės žinios

Turėtum mokėti sukurti ir paleisti `.py` failą, naudoti `print()`, parašyti komentarą ir perskaityti paprasto klaidos pranešimo pabaigą. Jei reikia, pakartok pirmos pamokos atmintinę. Pamoka vis dar pritaikyta visiškam pradedančiajam.

## 0. Privalomas aplinkos patikrinimas

Prieš pradėdamas įsitikink, kad dirbi tame pačiame `python-mokymai` projekte ir aktyvioje virtualioje aplinkoje. Jei pirmą pamoką pradedi nuo šio failo, atlik šiuos veiksmus:

```text
cd python-mokymai
source .venv/bin/activate        # macOS / Linux
```

Windows PowerShell naudok:

```text
cd python-mokymai
.venv\Scripts\Activate.ps1
```

Patikrink:

```text
python --version
python -c "import sys; print(sys.executable)"
```

`sys.executable` kelyje turi būti `.venv`. VS Code atveju per `Ctrl/Cmd + Shift + P` pasirink **Python: Select Interpreter** ir pasirink projekto `.venv`. Jei `python` nerandamas, macOS/Linux pabandyk `python3`, o Windows – `py`; išsamesnis setup ir `setup_check.py` yra [pirmoje pamokoje](lesson-00).

**Kontrolinis taškas:** sukurk `environment_check.py` su `print("Aplinka paruošta")`, paleisk `python environment_check.py` ir tik tada tęsk kintamųjų užduotis.

## 1. Įtraukianti pradžia: kaip programa prisimena informaciją?

Internetinė parduotuvė turi prisiminti prekės pavadinimą, vieneto kainą, kiekį ir ar prekė yra sandėlyje. Jei viską įrašytume tiesiai į kiekvieną `print()` eilutę, pakeitus kainą tektų jos ieškoti visame faile.

Kintamasis suteikia reikšmei vardą. Tai leidžia vienoje vietoje pakeisti duomenį, skaičiuoti ir tą pačią reikšmę panaudoti kelis kartus.

```python
product_name = "Belaidė pelė"
unit_price = 24.90
quantity = 2

print(product_name)
print(unit_price * quantity)
```

```text
Belaidė pelė
49.8
```

> **Išbandyk pats:** nežiūrėdamas į paaiškinimą pasakyk, kuri kodo vieta saugo prekės pavadinimą, kuri – kainą, o kuri – kiekį.

## 2. Pagrindinės sąvokos

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| Kintamasis | Vardas, susietas su reikšme | Etiketė ant dėžutės | Saugant ir pakartotinai naudojant duomenį | Vardas painiojamas su tekstu |
| Priskyrimas `=` | Reikšmės susiejimas su vardu | Daikto įdėjimas į pažymėtą dėžutę | Kuriant ar atnaujinant kintamąjį | `=` palaikomas žodžiu „lygu“ |
| Duomenų tipas | Reikšmės rūšis ir galimi veiksmai | Skirtingos dėžės skysčiui ir dokumentams | Sprendžiant, ar duomenį skaičiuoti, jungti ar tikrinti | Skaičius kabutėse laikomas skaičiumi |
| `input()` | Funkcija, laukianti vartotojo įvesties | Klausimas ir laukimas atsakymo | Interaktyviose programose | Pamirštama, kad rezultatas visada yra tekstas |
| Konvertavimas | Vieno tinkamo tipo keitimas kitu | Užrašyto skaičiaus perrašymas į skaičiuotuvo lauką | Prieš skaičiuojant įvestus skaičius | `int("2.5")` sukelia klaidą |
| f-string | Tekstas, į kurį įstatomos reikšmės | Laiško šablonas su gavėjo vardu | Aiškiai formuojant žinutes | Pamirštama raidė `f` |

Trumpas bendras pavyzdys:

```python
name = input("Koks tavo vardas? ")
age_text = input("Kiek tau metų? ")
age = int(age_text)
print(f"{name}, po metų tau bus {age + 1}.")
```

Jei vartotojas įveda `Ieva` ir `29`:

```text
Koks tavo vardas? Ieva
Kiek tau metų? 29
Ieva, po metų tau bus 30.
```

## 3. Vizualūs paaiškinimai

### Vizualizacija A – kintamieji atmintyje

```text
Kintamojo vardas       Reikšmė atmintyje       Tipas
┌──────────────┐        ┌──────────────┐        ┌───────┐
│ product_name │ ─────► │ Belaidė pelė │        │ str   │
├──────────────┤        ├──────────────┤        ├───────┤
│ unit_price   │ ─────► │ 24.90        │        │ float │
├──────────────┤        ├──────────────┤        ├───────┤
│ quantity     │ ─────► │ 2            │        │ int   │
└──────────────┘        └──────────────┘        └───────┘
```

**Iliustracijos pavadinimas:** „Vardai rodo į reikšmes“
**Ką ji turi parodyti:** kintamojo vardas nėra pati reikšmė, o aiški nuoroda į ją.
**Kokie elementai turi būti matomi:** trys vardų kortelės, trys reikšmių kortelės, rodyklės ir tipo žymos.
**Siūlomas vaizdo generavimo promptas:** „Minimalistinė edukacinė vektorinė schema lietuviškai: kintamųjų vardai product_name, unit_price, quantity rodyklėmis susieti su reikšmėmis ir tipais str, float, int; aukštas kontrastas, aiškios etiketės.“

### Vizualizacija B – vartotojo įvesties kelias

```text
Vartotojas įrašo „12“
          │
          ▼
input() grąžina tekstą "12" (str)
          │
          ▼ int()
       skaičius 12 (int)
          │
          ▼ + 3
       rezultatas 15
```

**Iliustracijos pavadinimas:** „Nuo klaviatūros iki skaičiavimo“
**Ką ji turi parodyti:** kodėl prieš matematiką reikia konvertuoti `input()` rezultatą.
**Kokie elementai turi būti matomi:** klaviatūra, `"12"`, `int()`, `12`, skaičiavimas ir rodyklės.
**Siūlomas vaizdo generavimo promptas:** „Vertikali mokomoji proceso diagrama lietuvių kalba, vartotojas įveda 12, input pateikia tekstą su kabutėmis, int konvertuoja į skaičių, atliekama sudėtis; skirtingos spalvos tekstui ir skaičiui.“

### Vizualizacija C – „prieš ir po“

| Fiksuotas kodas | Kodas su kintamuoju |
|---|---|
| `print("Kaina: 9.99")` | `price = 9.99` |
| `print("Su pristatymu: 12.99")` | `print(f"Kaina: {price}")` |
| Kainą reikia keisti keliose vietose | Kainą keičiame vienoje vietoje |

## 4. Kintamasis ir priskyrimas

Kintamasis yra prasmingas vardas, kuriuo vėliau pasiekiame reikšmę. `=` yra priskyrimo operatorius: dešinėje apskaičiuojama reikšmė, kairėje jai suteikiamas vardas.

Kasdienė analogija: užrašai `KAVA` ant dėžutės ir įdedi kavos pupeles. Vėliau ieškai dėžutės pagal etiketę, o ne pagal jos vietą lentynoje.

Sintaksė:

```python
variable_name = value
```

Minimalus pavyzdys:

```python
city = "Vilnius"
print(city)
```

```text
Vilnius
```

Eilutė po eilutės:

1. `city = "Vilnius"` sukuria vardą `city` ir susieja jį su tekstu.
2. `print(city)` paima su `city` susietą reikšmę ir ją parodo.

Atnaujinimas:

```python
task_count = 3
print(task_count)
task_count = 4
print(task_count)
```

```text
3
4
```

Antras priskyrimas pakeičia, kokią dabartinę reikšmę pasiekia vardas `task_count`.

> **Dažna klaida:** `city` be kabučių yra kintamojo vardas, o `"city"` su kabutėmis – tiesiog tekstas.

**Mini užduotis.** Sukurk `favorite_tool` su reikšme `"Python"`, parodyk kintamąjį, pakeisk reikšmę į `"Jupyter"` ir parodyk dar kartą.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
favorite_tool = "Python"
print(favorite_tool)
favorite_tool = "Jupyter"
print(favorite_tool)
```

</details>

### Aiškūs vardai

Python kintamųjų vardams įprasta naudoti angliškus žodžius ir `snake_case`: mažąsias raides, o žodžius atskirti pabraukimu.

```python
customer_name = "Jonas"
order_total = 58.40
item_count = 3
```

Venk `x`, `aaa`, `duom` ar `kaina1`, jei vardas nepaaiškina paskirties. Vardas negali prasidėti skaičiumi ir negali turėti tarpo.

## 5. Keturi pagrindiniai duomenų tipai

Duomenų tipas nusako, kokia tai reikšmė ir kokius veiksmus su ja galima atlikti. Kaip virtuvėje skirtingai elgiesi su miltais ir vandeniu, taip Python skirtingai elgiasi su tekstu ir skaičiais.

### 5.1. `str` – tekstas

`str` (angl. *string*) yra simbolių seka tarp kabučių: vardas, el. paštas, miesto pavadinimas ar net skaitmenys, kurių neskaičiuojame.

```python
customer_name = "Rasa"
postal_code = "01100"
print(customer_name)
print(postal_code)
```

```text
Rasa
01100
```

Pašto kodas laikomas tekstu, nes jo nesumuojame, o pradinis nulis svarbus.

> **Mini klausimas:** ar telefono numerį geriau laikyti skaičiumi, ar tekstu?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Tekstu. Telefono numerio nesumuojame, jame gali būti `+`, tarpai ir svarbūs pradiniai nuliai.

</details>

### 5.2. `int` – sveikasis skaičius

`int` saugo sveikąjį skaičių be dešimtainės dalies: kiekį, amžių ar įrašų skaičių.

```python
lesson_count = 12
completed_lessons = 5
remaining_lessons = lesson_count - completed_lessons
print(remaining_lessons)
```

```text
7
```

Pirmos dvi eilutės saugo skaičius, trečia atlieka atimtį ir rezultatą priskiria naujam kintamajam.

### 5.3. `float` – dešimtainis skaičius

`float` saugo skaičių su dešimtaine dalimi. Python kode naudojamas taškas, ne kablelis.

```python
unit_price = 8.50
quantity = 3
total = unit_price * quantity
print(total)
```

```text
25.5
```

`8.50` yra `float`, `3` – `int`, o jų sandauga taip pat yra dešimtainis skaičius.

> **Dažna klaida:** `8,50` Python supranta ne kaip įprastą dešimtainį skaičių. Kode rašyk `8.50`.

### 5.4. `bool` – taip arba ne

`bool` turi tik dvi reikšmes: `True` ir `False`. Jos rašomos be kabučių ir didžiąja pradine raide. Tai panašu į jungiklį: įjungta arba išjungta.

```python
is_paid = True
is_cancelled = False
print(is_paid)
print(is_cancelled)
```

```text
True
False
```

Vėliau loginės reikšmės leis programai pasirinkti veiksmą. Kol kas mokomės jas saugoti ir parodyti.

### 5.5. Tipo patikra su `type()`

`type()` pasako, kokio tipo yra reikšmė. Ji veikia kaip sandėlio etiketės skaitytuvas.

```python
name = "Mantas"
age = 31
price = 12.99
is_active = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_active))
```

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Žodis `class` šiame rezultate kol kas reiškia Python tipo kategoriją; klases išsamiai nagrinėsime vėliau.

> **Išbandyk pats:** patikrink `type("42")` ir `type(42)`. Užrašyk, kodėl atsakymai skiriasi.

## 6. Skaičiavimai su kintamaisiais

Pagrindiniai aritmetiniai operatoriai:

| Operatorius | Veiksmas | Pavyzdys | Rezultatas |
|---|---|---|---:|
| `+` | sudėtis | `8 + 2` | 10 |
| `-` | atimtis | `8 - 2` | 6 |
| `*` | daugyba | `8 * 2` | 16 |
| `/` | dalyba | `8 / 2` | 4.0 |

Kainos skaičiavimas:

```python
hourly_rate = 35.0
hours = 6
project_price = hourly_rate * hours
print(project_price)
```

```text
210.0
```

1. Išsaugome valandos kainą.
2. Išsaugome valandų skaičių.
3. Dauginame ir rezultatą pavadiname `project_price`.
4. Parodome rezultatą.

Operatorių tvarka tokia pati kaip matematikoje: daugyba ir dalyba atliekama prieš sudėtį ir atimtį. Skliaustai leidžia tvarką aiškiai pakeisti.

```python
price = 10
quantity = 3
delivery = 4
total = price * quantity + delivery
print(total)
```

```text
34
```

> **Mini užduotis:** apskaičiuok trijų bilietų po `12.50` kainą ir pridėk `2.0` aptarnavimo mokestį.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
ticket_price = 12.50
ticket_count = 3
service_fee = 2.0
total = ticket_price * ticket_count + service_fee
print(total)
```

```text
39.5
```

</details>

## 7. Vartotojo įvestis su `input()`

`input()` parodo klausimą, sustabdo programą ir laukia, kol vartotojas įrašys atsakymą bei paspaus Enter. Tai panašu į tuščią formos lauką.

Sintaksė:

```python
answer = input("Klausimas: ")
```

Minimalus pavyzdys:

```python
name = input("Koks tavo vardas? ")
print(f"Labas, {name}!")
```

Galima programos eiga:

```text
Koks tavo vardas? Gabija
Labas, Gabija!
```

Pirmoje eilutėje programa parodo klausimą ir vartotojo atsakymą išsaugo `name`. Antroje eilutėje atsakymas įstatomas į žinutę.

> **Svarbu:** `input()` visada grąžina `str`, net jei vartotojas klaviatūra įrašė skaitmenis.

Patikrink:

```python
age = input("Kiek tau metų? ")
print(type(age))
```

Įvedus `25`:

```text
Kiek tau metų? 25
<class 'str'>
```

## 8. Tipų keitimas

Kad galėtume skaičiuoti vartotojo įvestus skaitmenis, tekstą konvertuojame. `int()` tinka sveikam skaičiui, `float()` – dešimtainiam.

Kasdienė analogija: ant lapelio parašytas „25“ žmogui atrodo kaip skaičius, bet skaičiuotuvui jį dar reikia įvesti į skaitinį lauką.

### Tekstas į `int`

```python
age_text = input("Kiek tau metų? ")
age = int(age_text)
next_age = age + 1
print(f"Po metų tau bus {next_age}.")
```

Įvedus `25`:

```text
Kiek tau metų? 25
Po metų tau bus 26.
```

### Tekstas į `float`

```python
price_text = input("Vieneto kaina: ")
price = float(price_text)
total = price * 2
print(f"Dviejų vienetų kaina: {total} Eur")
```

Įvedus `4.75`:

```text
Vieneto kaina: 4.75
Dviejų vienetų kaina: 9.5 Eur
```

> **Dažna klaida:** `int("4.75")` neveikia, nes tekstas vaizduoja dešimtainį, ne sveikąjį skaičių. Naudok `float("4.75")`.

Patogus trumpesnis variantas:

```python
quantity = int(input("Kiekis: "))
```

Vykdymas vyksta iš vidaus į išorę: pirma `input()`, tada `int()`, tada priskyrimas. Pradžioje ilgesnis variantas su `quantity_text` gali būti lengviau tikrinamas.

**Mini užduotis.** Paprašyk vartotojo įvesti mokymosi dienų skaičių, konvertuok į `int`, padaugink iš 30 minučių ir parodyk bendrą minučių skaičių.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
days_text = input("Kiek dienų mokysies? ")
days = int(days_text)
minutes = days * 30
print(f"Iš viso mokysies {minutes} min.")
```

</details>

## 9. f-string – aiški rezultatų žinutė

f-string yra teksto šablonas su raide `f` prieš kabutes. Kintamųjų vardai rašomi tarp `{` ir `}`, o Python į jų vietą įstato reikšmes.

```python
product = "Užrašinė"
quantity = 3
total = 14.7
print(f"Prekė: {product}, kiekis: {quantity}, suma: {total} Eur")
```

```text
Prekė: Užrašinė, kiekis: 3, suma: 14.7 Eur
```

Be raidės `f` riestiniai skliaustai lieka paprastu tekstu:

```python
name = "Lina"
print("Labas, {name}!")
```

```text
Labas, {name}!
```

Pataisymas:

```python
name = "Lina"
print(f"Labas, {name}!")
```

> **Patarimas:** f-string leidžia išvengti neaiškaus teksto ir skaičių jungimo. Pradedančiajam tai saugiausias rezultatų formatavimo būdas.

## 10. Įvairūs kodo pavyzdžiai

### Minimalus pavyzdys

**Problema:** vieną reikšmę panaudoti du kartus.

```python
language = "Python"
print(language)
print(f"Mokausi {language}.")
```

```text
Python
Mokausi Python.
```

**Paaiškinimas:** pakeitus `language` reikšmę, pasikeis abi išvesties vietos. **Patobulinimas:** pridėk `learning_goal`.

### Kasdienis pavyzdys – kelionės laikas

```python
distance_km = 120
average_speed = 80
travel_hours = distance_km / average_speed
print(f"Kelionė truks apie {travel_hours} val.")
```

```text
Kelionė truks apie 1.5 val.
```

**Patobulinimas:** priimk atstumą ir greitį su `input()`.

### Kasdienis pavyzdys – bendros išlaidos

```python
food = 32.50
transport = 8.20
entertainment = 15.0
total = food + transport + entertainment
print(f"Dienos išlaidos: {total} Eur")
```

```text
Dienos išlaidos: 55.7 Eur
```

**Patobulinimas:** pridėk ketvirtą išlaidų kategoriją.

### Darbo pavyzdys – sąskaitos suma

```python
service_name = "Duomenų ataskaita"
hourly_rate = 40.0
hours = 6
total = hourly_rate * hours

print(f"Paslauga: {service_name}")
print(f"Valandos: {hours}")
print(f"Mokėtina suma: {total} Eur")
```

```text
Paslauga: Duomenų ataskaita
Valandos: 6
Mokėtina suma: 240.0 Eur
```

**Patobulinimas:** valandų skaičių priimk iš vartotojo.

### Automatizavimo pavyzdys – laiko sutaupymas

```python
minutes_per_task = 12
tasks_per_week = 25
saved_minutes = minutes_per_task * tasks_per_week
saved_hours = saved_minutes / 60

print(f"Automatizacija sutaupo {saved_minutes} min. per savaitę.")
print(f"Tai yra {saved_hours} val.")
```

```text
Automatizacija sutaupo 300 min. per savaitę.
Tai yra 5.0 val.
```

**Patobulinimas:** abu pradinius skaičius priimk su `input()` ir `int()`.

### Duomenų ir AI pavyzdys – duomenų rinkinio suvestinė

```python
training_rows = 800
test_rows = 200
total_rows = training_rows + test_rows
dataset_name = "Klientų žinučių temos"
is_ready = True

print(f"Rinkinys: {dataset_name}")
print(f"Visi įrašai: {total_rows}")
print(f"Parengtas AI mokymui: {is_ready}")
```

```text
Rinkinys: Klientų žinučių temos
Visi įrašai: 1000
Parengtas AI mokymui: True
```

**Patobulinimas:** pridėk `validation_rows` ir įtrauk jį į bendrą sumą.

### Klaidingas pavyzdys – pataisyk

```python
price = input("Kaina: ")
quantity = 3
total = price * quantity
print(f"Suma: {total}")
```

Įvedus `5`, programa parodys ne `15`, o `555`, nes tekstą padauginus iš 3 jis pakartojamas.

Pataisymas:

```python
price_text = input("Kaina: ")
price = float(price_text)
quantity = 3
total = price * quantity
print(f"Suma: {total} Eur")
```

## 11. Interaktyvios veiklos

### 1. Nuspėk rezultatą

```python
items = 4
items = items + 2
print(items)
```

A. `4`
B. `6`
C. `items + 2`
D. Klaida

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Dešinėje paimama sena reikšmė `4`, pridedama `2`, tada vardui `items` priskiriama `6`.

</details>

### 2. Užpildyk trūkstamą kodą

```python
price_text = input("Kaina: ")
price = ____(price_text)
print(price * 2)
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
price = float(price_text)
```

Kainoje gali būti dešimtainė dalis, todėl tinka `float()`.

</details>

### 3. Surask klaidą

```python
user name = "Tomas"
print(user name)
```

Nustatyk klaidą, paaiškink ir pataisyk.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Kintamojo varde negali būti tarpo. Naudok pabraukimą.

```python
user_name = "Tomas"
print(user_name)
```

</details>

### 4. Sudėliok teisinga tvarka

```text
total = price * quantity
price = 6.5
print(f"Suma: {total} Eur")
quantity = 2
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
price = 6.5
quantity = 2
total = price * quantity
print(f"Suma: {total} Eur")
```

Kintamieji turi gauti reikšmes prieš juos naudojant skaičiavime.

</details>

### 5. Pasirink tinkamą sprendimą

Vartotojas įveda sveiką bilietų skaičių. Kuris variantas tinka skaičiavimui?

A. `count = input("Kiekis: ")`
B. `count = int(input("Kiekis: "))`
C. `count = "input"`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** `input()` rezultatą reikia konvertuoti į sveikąjį skaičių su `int()`.

</details>

### 6. Parašyk pats

Paprašyk vartotojo įvesti vardą ir per savaitę mokymuisi skiriamas valandas. Parodyk sakinį, kuriame yra vardas ir per 4 savaites susidarantis valandų skaičius.

### 7. Patobulink kodą

```python
a = 12.5
b = 4
c = a * b
print(c)
```

Pakeisk kintamųjų vardus taip, kad būtų aišku: `a` yra bilieto kaina, `b` – bilietų kiekis, `c` – visa suma. Rezultatą pateik aiškia f-string žinute.

## 12. Žinių patikrinimas prieš platformos testą

Pirmiausia atsakyk neužleisdamas atsakymų.

1. Kuo skiriasi `42` ir `"42"`?
2. Kokio tipo reikšmę visada grąžina `input()`?
3. Kada rinktumeisi `int()`, o kada `float()`?
4. Ką reiškia `=` eilutėje `total = price * quantity`?
5. Ką parodys `type(True)`?
6. Kodėl profesionaliau rašyti `customer_name`, o ne `x`?
7. Kas nutiks pamiršus `f` prieš `"Labas, {name}"`?
8. Kokia bus `10 / 2` reikšmė?
9. Kuris tipas tiktų pašto kodui ir kodėl?
10. Rask problemą: `age = input("Amžius: "); print(age + 1)`.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymus ir paaiškinimus</summary>

1. `42` yra `int`, o `"42"` – `str`; tik pirmasis iškart tinka matematikai.
2. `str`.
3. `int()` sveikam skaičiui, `float()` skaičiui su dešimtaine dalimi.
4. Apskaičiuota dešinės pusės reikšmė priskiriama vardui `total`.
5. `<class 'bool'>`.
6. Prasmingas vardas paaiškina duomens paskirtį ir sumažina klaidų tikimybę.
7. Bus parodyti pažodiniai ženklai `{name}`, o ne kintamojo reikšmė.
8. `5.0`, nes `/` grąžina dešimtainį rezultatą.
9. `str`, nes pašto kodo nesumuojame ir jame gali būti svarbių pradinių nulių.
10. `age` yra tekstas. Reikia `age = int(input("Amžius: "))`.

</details>

## 13. Praktinės užduotys

### 1 lygis – pagrindai

#### Užduotis 1. Mokinio profilis

**Sąlyga:** sukurk keturis kintamuosius: vardą (`str`), amžių (`int`), savaitės mokymosi valandas (`float`) ir ar kursas pradėtas (`bool`). Parodyk kiekvieną reikšmę bei tipą.
**Pradiniai duomenys:** `Ema`, `27`, `4.5`, `True`.
**Laukiamas rezultatas:** keturios reikšmės ir keturi tipai.
**Užuomina:** tipą tikrina `type()`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
student_name = "Ema"
student_age = 27
weekly_hours = 4.5
course_started = True

print(student_name)
print(type(student_name))
print(student_age)
print(type(student_age))
print(weekly_hours)
print(type(weekly_hours))
print(course_started)
print(type(course_started))
```

Kiekviena reikšmė turi jos paskirtį nusakantį vardą. **Papildomas iššūkis:** su f-string pateik viską keturiomis aiškiomis eilutėmis.

</details>

#### Užduotis 2. Stačiakampio plotas

**Sąlyga:** su `length = 8.5` ir `width = 4` apskaičiuok plotą.
**Laukiamas rezultatas:** `Stačiakampio plotas: 34.0`.
**Užuomina:** plotas yra ilgis padaugintas iš pločio.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
length = 8.5
width = 4
area = length * width
print(f"Stačiakampio plotas: {area}")
```

**Papildomas iššūkis:** abu matmenis priimk su `input()` ir `float()`.

</details>

#### Užduotis 3. Asmeninis pasisveikinimas

**Sąlyga:** paklausk vardo ir miesto, tada pateik vieną pasisveikinimo sakinį.
**Pavyzdinė įvestis:** `Nojus`, `Klaipėda`.
**Laukiamas rezultatas:** `Labas, Nojau iš Klaipėdos!` arba gramatiškai paprastesnis sakinys su nepakeistomis įvestimis.
**Užuomina:** naudok du `input()` ir vieną f-string.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
name = input("Tavo vardas: ")
city = input("Tavo miestas: ")
print(f"Labas, {name}! Tavo miestas – {city}.")
```

Programa nekeičia įvestų žodžių galūnių. **Papildomas iššūkis:** paklausk ir mokymosi tikslo.

</details>

### 2 lygis – pritaikymas

#### Užduotis 4. Savaitės atlygio skaičiuoklė

**Sąlyga:** vartotojas įveda dirbtų valandų skaičių ir valandos atlygį. Pasirink tinkamus tipus, apskaičiuok bei parodyk bendrą sumą.
**Pavyzdinė įvestis:** `32.5` valandos ir `18.0` Eur.
**Laukiamas rezultatas:** `Savaitės suma: 585.0 Eur`.
**Užuomina:** abu dydžiai gali turėti dešimtainę dalį.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
hours_text = input("Dirbtos valandos: ")
rate_text = input("Valandos atlygis: ")
hours = float(hours_text)
hourly_rate = float(rate_text)
weekly_pay = hours * hourly_rate
print(f"Savaitės suma: {weekly_pay} Eur")
```

`float()` pasirinktas dėl galimų valandos dalių ir centų. **Papildomas iššūkis:** apskaičiuok keturių savaičių sumą.

</details>

#### Užduotis 5. Renginio biudžetas

**Sąlyga:** priimk dalyvių skaičių, maisto kainą vienam dalyviui ir fiksuotą salės kainą. Parodyk bendrą biudžetą.
**Pavyzdinė įvestis:** `20`, `14.5`, `180`.
**Laukiamas rezultatas:** `Bendras biudžetas: 470.0 Eur`.
**Užuomina:** dalyvių skaičiui tinka `int`, kainoms – `float`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
people = int(input("Dalyvių skaičius: "))
food_per_person = float(input("Maisto kaina vienam: "))
venue_price = float(input("Salės kaina: "))
total_budget = people * food_per_person + venue_price
print(f"Bendras biudžetas: {total_budget} Eur")
```

Pirmiausia skaičiuojama viso maisto kaina, tada pridedama salė. **Papildomas iššūkis:** pridėk dekoracijų kainą.

</details>

### 3 lygis – iššūkis

#### Užduotis 6. Automatizavimo naudos skaičiuoklė

**Sąlyga:** vartotojas įveda vienai rankinei užduočiai skiriamas minutes, užduočių skaičių per savaitę, darbuotojo valandos kainą ir savaičių skaičių. Apskaičiuok bendras sutaupytas minutes, valandas ir piniginę vertę.
**Pavyzdinė įvestis:** `10`, `30`, `25.0`, `4`.
**Laukiamas rezultatas:** `1200` min., `20.0` val. ir `500.0 Eur`.
**Užuomina:** minutes paversk valandomis dalydamas iš `60`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
minutes_per_task = float(input("Minutės vienai užduočiai: "))
tasks_per_week = int(input("Užduotys per savaitę: "))
hourly_cost = float(input("Darbo valandos kaina: "))
week_count = int(input("Savaičių skaičius: "))

saved_minutes = minutes_per_task * tasks_per_week * week_count
saved_hours = saved_minutes / 60
saved_value = saved_hours * hourly_cost

print(f"Sutaupyta minučių: {saved_minutes}")
print(f"Sutaupyta valandų: {saved_hours}")
print(f"Sutaupyta vertė: {saved_value} Eur")
```

Kiekvienas tarpinis rezultatas turi aiškų vardą, todėl formulę lengva tikrinti. **Papildomas iššūkis:** pridėk vienkartinę automatizacijos sukūrimo kainą ir atimk ją iš sutaupytos vertės.

</details>

## 14. Mini projektas – interaktyvi paslaugos kainos skaičiuoklė

### 1. Projekto situacija

Laisvai samdomas specialistas nori greitai apskaičiuoti preliminarią projekto kainą pagal kliento vardą, paslaugą, planuojamas valandas, valandos kainą ir papildomas išlaidas.

### 2. Galutinis tikslas

Sukurti `quote_calculator.py`, kuris priima duomenis, apskaičiuoja darbų kainą ir parodo tvarkingą pasiūlymo suvestinę.

### 3. Funkciniai reikalavimai

Programa turi:

1. priimti kliento vardą ir paslaugos pavadinimą kaip tekstą;
2. priimti planuojamas valandas ir valandos kainą kaip dešimtainius skaičius;
3. priimti papildomas išlaidas kaip dešimtainį skaičių;
4. apskaičiuoti darbų kainą `valandos * valandos kaina`;
5. apskaičiuoti bendrą sumą pridėjus papildomas išlaidas;
6. aiškiai parodyti visus svarbiausius duomenis su f-string;
7. naudoti prasmingus angliškus kintamųjų vardus ir bent vieną komentarą.

### 4. Pavyzdinė įvestis

```text
Kliento vardas: UAB Pavyzdys
Paslauga: Pardavimų ataskaitos automatizavimas
Planuojamos valandos: 12.5
Valandos kaina: 40
Papildomos išlaidos: 25
```

### 5. Pavyzdinis rezultatas

```text
=== PASIŪLYMO SUVESTINĖ ===
Klientas: UAB Pavyzdys
Paslauga: Pardavimų ataskaitos automatizavimas
Planuojamos valandos: 12.5
Darbų kaina: 500.0 Eur
Papildomos išlaidos: 25.0 Eur
Bendra suma: 525.0 Eur
```

### 6. Projekto kūrimo etapai

1. Sukurk failą ir parodyk antraštę.
2. Priimk du tekstinius laukus, parodyk juos ir patikrink.
3. Priimk valandas; konvertuok su `float()` ir parodyk tipą tik kūrimo patikrai.
4. Priimk dvi kainas ir apskaičiuok darbų kainą.
5. Apskaičiuok bendrą sumą.
6. Suformuok galutinę suvestinę.
7. Pašalink laikiną `type()` patikrą, paleisk su pavyzdiniais duomenimis.
8. Paleisk dar kartą su savo sugalvotais duomenimis.

### 7. Pseudokodas

```text
PARODYK programos pavadinimą
PAKLAUSK kliento vardo
PAKLAUSK paslaugos
PAKLAUSK valandų ir PAKEISK į float
PAKLAUSK valandos kainos ir PAKEISK į float
PAKLAUSK papildomų išlaidų ir PAKEISK į float
APSKAIČIUOK darbų kainą
APSKAIČIUOK bendrą sumą
PARODYK pasiūlymo suvestinę
```

> **Užuomina:** jei gauni `ValueError`, patikrink, ar kainą įvedei su tašku (`12.5`), o ne kableliu (`12,5`).

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

```python
print("PASLAUGOS KAINOS SKAIČIUOKLĖ")

client_name = input("Kliento vardas: ")
service_name = input("Paslauga: ")
planned_hours = float(input("Planuojamos valandos: "))
hourly_rate = float(input("Valandos kaina: "))
extra_costs = float(input("Papildomos išlaidos: "))

# Atskiri tarpiniai rezultatai leidžia lengvai patikrinti formulę
work_cost = planned_hours * hourly_rate
total_price = work_cost + extra_costs

print("=== PASIŪLYMO SUVESTINĖ ===")
print(f"Klientas: {client_name}")
print(f"Paslauga: {service_name}")
print(f"Planuojamos valandos: {planned_hours}")
print(f"Darbų kaina: {work_cost} Eur")
print(f"Papildomos išlaidos: {extra_costs} Eur")
print(f"Bendra suma: {total_price} Eur")
```

`input()` surenka tekstą. Tris skaitinius laukus `float()` paverčia skaičiais. `work_cost` ir `total_price` saugo atskirus tarpinius rezultatus, todėl kodą lengva skaityti ir tikrinti. f-string sujungia aiškias etiketes su reikšmėmis.

</details>

### 8. Galimi patobulinimai

- trečioje pamokoje patikrink, ar įvesti skaičiai nėra neigiami;
- pridėk nuolaidos procentą;
- pridėk mokesčius;
- rezultatą suapvalink iki dviejų skaitmenų po kablelio, kai išmoksi formatavimą;
- vėliau išsaugok pasiūlymą faile.

### 9. `README.md` šablonas

```text
# Paslaugos kainos skaičiuoklė

Interaktyvi Python programa preliminariai projekto kainai apskaičiuoti.

## Funkcijos
- Priima kliento ir paslaugos duomenis
- Apskaičiuoja darbų kainą
- Prideda papildomas išlaidas
- Parodo pasiūlymo suvestinę

## Paleidimas
python3 quote_calculator.py

## Pavyzdys
Įvesk valandas, valandos kainą ir papildomas išlaidas pagal programos klausimus.

## Ką išmokau
Kintamieji, str, float, input(), tipų keitimas, aritmetika ir f-string.

## Tolimesni patobulinimai
Įvesties tikrinimas, nuolaida ir rezultato išsaugojimas.
```

## 15. Dažniausios klaidos

| Klaida | Kodėl ji atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| Skaičiuojama su `input()` tekstu | Pamirštama, kad `input()` grąžina `str` | `age = input(...); age + 1` | `age = int(input(...)); age + 1` | Prieš skaičiuodamas pasirink `int()` ar `float()` |
| Skaičius įrašytas kabutėse | Vizualiai atrodo kaip skaičius | `price = "10.5"` | `price = 10.5` | Su `type()` patikrink abejotiną reikšmę |
| Dešimtainis skaičius su kableliu | Taikoma lietuviška rašyba | `price = 10,5` | `price = 10.5` | Python kode naudok tašką |
| `int()` taikomas dešimtainiam tekstui | Pasirinktas netinkamas konverteris | `int("4.5")` | `float("4.5")` | Įvertink, ar galimos skaičiaus dalys |
| Pamiršta `f` raidė | f-string palaikomas paprastu tekstu | `"Suma: {total}"` | `f"Suma: {total}"` | Prieš kabutes patikrink `f` |
| Kintamojo varde yra tarpas | Vardas rašomas kaip sakinys | `user name = "Ona"` | `user_name = "Ona"` | Naudok `snake_case` |
| Kintamasis naudojamas per anksti | Vykdymo tvarka ignoruojama | `print(total); total = 5` | `total = 5; print(total)` | Pirma priskirk, tada naudok |

## 16. Profesionali praktika

- Rinkis pavadinimus pagal reikšmės paskirtį: `hourly_rate`, ne `number1`.
- Naudok `snake_case` ir vieną kalbą pavadinimuose; profesiniame Python kode dažniausia anglų kalba.
- Aplink `=` ir operatorius palik po vieną tarpą: `total = price * quantity`.
- Sudėtingesnę formulę skaidyk į prasmingus tarpinius rezultatus.
- Testuok bent su įprasta, nuline ir dešimtaine reikšme. Šioje pamokoje netinkamą tekstą dar taiso pats vartotojas; vėliau išmoksi jį apdoroti kode.
- Komentaras turi paaiškinti verslo taisyklę ar neakivaizdžią priežastį, o ne perpasakoti `total = price * quantity`.
- Realiame projekte kintamieji laiko formų duomenis, API atsakymus, skaičiavimų rezultatus ir programos būsenas.

## 17. Kodėl tai svarbu mokantis AI?

AI programose kintamieji saugo failų pavadinimus, duomenų rinkinių dydžius, modelio nustatymus ir gautus rezultatus. Duomenų tipai ypač svarbūs: modelis negali skaičiuoti su skaičiais, kurie netyčia liko tekstu. `bool` dažnai žymi, ar duomenys jau patikrinti, o `float` – tikimybę arba modelio įvertį.

Paprasta AI klasifikatoriaus rezultato imitacija be išorinių bibliotekų:

```python
message = "Noriu pakeisti pristatymo adresą"
predicted_topic = "pristatymas"
confidence = 0.92
is_reviewed = False

print(f"Žinutė: {message}")
print(f"Numatyta tema: {predicted_topic}")
print(f"Modelio užtikrintumas: {confidence}")
print(f"Patikrino žmogus: {is_reviewed}")
```

```text
Žinutė: Noriu pakeisti pristatymo adresą
Numatyta tema: pristatymas
Modelio užtikrintumas: 0.92
Patikrino žmogus: False
```

Čia nėra tikro modelio – tik jo galimų rezultatų duomenų struktūra. Vėlesniuose moduliuose tas pačias reikšmių rūšis gausi iš AI bibliotekų.

## 18. Pamokos santrauka

- Kintamasis yra prasmingas vardas, susietas su reikšme.
- `=` priskiria dešinėje gautą reikšmę vardui kairėje.
- `str` saugo tekstą, `int` – sveikąjį skaičių, `float` – dešimtainį, `bool` – `True` arba `False`.
- `type()` padeda patikrinti reikšmės tipą.
- `input()` visada pateikia tekstą.
- `int()` ir `float()` tinkamą tekstą paverčia skaičiumi.
- Aritmetiniai operatoriai leidžia skaičiuoti su skaitiniais kintamaisiais.
- f-string įstato reikšmes į aiškią žinutę.

**Atmintinė:**

```python
name = input("Vardas: ")
quantity = int(input("Kiekis: "))
price = float(input("Kaina: "))
total = quantity * price
is_ready = True

print(f"{name}, suma: {total} Eur")
print(type(total))
print(is_ready)
```

Vienu sakiniu: **tinkamai pavadinti ir tinkamo tipo kintamieji paverčia fiksuotą kodą programa, kuri priima, apdoroja ir aiškiai pateikia duomenis.**

## 19. Savirefleksija

1. Ką dabar galiu padaryti, ko negalėjau prieš pamoką?
2. Kuri dalis buvo sunkiausia: tipų pasirinkimas, konvertavimas ar formulė?
3. Kokią klaidą dabar mokėčiau atpažinti?
4. Kur galėčiau šias žinias pritaikyti realiame gyvenime ar darbe?
5. Ar galėčiau kitam žmogui paaiškinti, kodėl `input()` rezultatą kartais reikia konvertuoti?

## 20. Namų darbas

### Privaloma – kelionės biudžeto skaičiuoklė

Priimk keliautojo vardą, dienų skaičių, nakvynės kainą už dieną, maisto kainą už dieną ir transporto kainą. Apskaičiuok nakvynės, maisto ir bendrą kainą; pateik aiškią suvestinę.

**Vertinimas (10 taškų):** tinkami tipai ir konvertavimas – 2; teisingos formulės – 3; prasmingi vardai – 2; aiški f-string išvestis – 2; kodas paleidžiamas – 1.

### Pasirenkama – mėnesio mokymosi statistika

Priimk mokymosi dienų skaičių ir vidutines minutes per dieną. Parodyk visas minutes ir valandas per mėnesį.

**Vertinimas (5 taškai):** įvestis – 1; konvertavimas – 1; abu skaičiavimai – 2; aiški išvestis – 1.

### Kūrybinis iššūkis – tavo srities skaičiuoklė

Sukurk skaičiuoklę darbui ar pomėgiui: recepto porcijoms, medžiagoms, renginio kainai, sporto laikui ar kitai realiai situacijai. Naudok bent keturis kintamuosius, dviejų rūšių skaitinius tipus, tris įvestis ir du tarpinius rezultatus.

**Vertinimas (5 taškai):** reali nauda – 1; reikalavimų įgyvendinimas – 2; pavadinimų ir išvesties aiškumas – 1; savarankiškas sprendimas – 1.

## 21. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Kintamieji ir vardai | 35 min. | Tikrinti skirtumą tarp `name` ir `"name"` |
| Keturi tipai ir `type()` | 45 min. | Daugiausia painiavos tarp skaitinio teksto ir skaičiaus |
| Aritmetika | 35 min. | Naudoti realias kainas, laiką ir kiekius |
| `input()` bei konvertavimas | 55 min. | Vizualizuoti teksto kelią į skaičių; čia mokiniai stringa dažniausiai |
| f-string ir pavyzdžiai | 35 min. | Automatiškai tikrinti išvesties šabloną |
| Interaktyvios veiklos ir testas | 45 min. | Fiksuoti klaidų kategorijas, ne tik balą |
| Trijų lygių praktika | 70 min. | Formules tikrinti automatiškai su keliomis įvestimis |
| Mini projektas | 75 min. | Kodo aiškumą ir vardus vertinti rankiniu būdu |

Animacija labiausiai padėtų ties `input() → str → float/int → skaičiavimas` procesu. Interaktyvų Python redaktorių verta įterpti po kiekvieno tipo, tipų konvertavimo bloke, klaidingame `price * quantity` pavyzdyje ir mini projekte. Platformoje verta fiksuoti atliktas mini užduotis, pirmą sėkmingą konvertavimą, `TypeError` / `ValueError` dažnį, testo rezultatą, bandymų skaičių, mini projekto užbaigimą ir savirefleksijos pasirinkimą.
