---
title: Pirmoji Python programa
module: 1 · Pati pradžia
order: 0
---

# Pirmoji Python programa

Programavimas prasideda ne nuo sudėtingų terminų, o nuo vienos aiškios minties: **tu užrašai komandą, o kompiuteris ją įvykdo**.

Šioje pamokoje parašysi ir paleisi pirmąją Python programą. Taip pat išmoksi perskaityti paprastą klaidos pranešimą ir savarankiškai pataisyti kodą.

## Ką išmoksi

Baigęs pamoką gebėsi:

- paaiškinti, kas yra kodas ir programa;
- paleisti Python failą;
- parodyti tekstą ir skaičius naudojant `print()`;
- suprasti, kodėl tekstui reikalingos kabutės;
- rasti paprastą sintaksės klaidą.

## 1. Kaip veikia programa

Programa yra tiksliai užrašytų komandų seka. Python skaito failą nuo viršaus į apačią ir kiekvieną eilutę vykdo iš eilės.

```text
Tavo kodas → Python → rezultatas
```

Pavyzdžiui, ši programa turi vieną komandą:

```python
print("Labas!")
```

Ją paleidus ekrane pasirodo:

```text
Labas!
```

`print()` yra Python funkcija – paruošta komanda, kuri ekrane parodo tai, ką įrašai tarp skliaustų. Tokį tekstą ar skaičių toliau vadinsime **reikšme**.

## 2. Rašyk kodą tiesiai šioje pamokoje

Šio kurso laboratorijoje Python veikia naršyklėje, todėl prieš pirmą pamoką nieko diegti nereikia. Pasirink viršuje esantį skirtuką **„Laboratorija“** arba slink iki pamokos pabaigoje esančios darbo aplinkos.

Laboratorijoje rasi:

- failą `main.py`, kuriame rašomas kodas;
- mygtuką **„Paleisti“**;
- terminalo išvestį;
- automatinius testus, kurie patikrina sprendimą.

Pirmą kartą paleidžiant kodą Python aplinkos įkėlimas gali užtrukti kelias sekundes. Toliau ji veiks tiesiai tavo naršyklėje, o parašytas kodas bus automatiškai išsaugotas šiame įrenginyje.

> **Išbandyk pats:** laboratorijoje įrašyk `print("Python veikia!")`, paleisk programą ir įsitikink, kad matai tekstą išvesties lange.

## 3. Tekstas ir kabutės

Tekstas Python kalboje rašomas kabutėse:

```python
print("Mokausi Python")
print("Tai mano pirmoji programa")
```

Kabutės parodo, kur tekstas prasideda ir baigiasi. Galima naudoti dvigubas arba viengubas kabutes:

```python
print("Labas")
print('Labas')
```

Svarbu, kad pradžios ir pabaigos kabutės sutaptų.

```python
# Neteisinga: trūksta uždaromųjų kabučių
print("Labas)
```

> **Dažna klaida:** iš teksto redaktoriaus, pokalbio ar tinklalapio nukopijuotos „išmaniosios“ kabutės (`“ ”`) Python netinka – gausi klaidą. Kode visada rašyk tiesias kabutes `" "`.

Eilutė, prasidedanti ženklu `#`, yra komentaras. Python jos nevykdo. Komentarai padeda žmogui suprasti kodą.

## 4. Python gali skaičiuoti

Skaičiams kabučių nereikia:

```python
print(7)
print(4 + 3)
print(10 - 2)
```

Rezultatas:

```text
7
7
8
```

Atkreipk dėmesį į skirtumą:

```python
print(4 + 3)
print("4 + 3")
```

Pirmoje eilutėje Python atlieka skaičiavimą. Antroje eilutėje kabutės nurodo, kad tai yra tekstas, todėl jis parodomas toks, koks parašytas.

**Pasitikrink.** Ką parodys `print("5 + 5")`? Pirmiausia atsakyk mintyse, tik tada atskleisk atsakymą.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

`5 + 5` parašyta kabutėse, todėl Python laiko tai tekstu ir ekrane parodo `5 + 5`. Skaičiavimas atliekamas tik tada, kai skaičiai rašomi be kabučių: `print(5 + 5)` parodytų `10`.

</details>

## 5. Komandų tvarka

Python įprastai vykdo eilutes nuo viršaus į apačią:

```python
print("Programos pradžia")
print(2 + 3)
print("Programos pabaiga")
```

Todėl komandų tvarka yra svarbi. Sukeitus eilutes vietomis, pasikeis ir rezultato tvarka.

> **Išbandyk pats:** sukeisk pirmą ir paskutinę pavyzdžio eilutes. Paleisk programą dar kartą ir palygink rezultatą.

## 6. Klaida nėra nesėkmė

Rašant kodą klaidos yra įprastos. Jos padeda suprasti, kuri programos vieta parašyta netiksliai.

Pabandyk paleisti šį kodą:

```python
print("Labas"
```

Python parodys klaidos pranešimą, nes trūksta uždaromojo skliausto. Ieškodamas problemos:

1. perskaityk paskutinę klaidos pranešimo eilutę;
2. rask nurodytą kodo eilutę;
3. patikrink kabutes ir skliaustus;
4. pataisyk tik vieną dalyką ir paleisk programą dar kartą.

Šiuo atveju taisyklinga eilutė yra:

```python
print("Labas")
```

## 7. Praktinė užduotis

Laboratorijoje parašyk trumpą programą apie save. Ji turi parodyti:

1. tavo vardą;
2. miestą arba šalį;
3. priežastį, kodėl mokaisi Python;
4. skaičiavimo `12 + 8` rezultatą.

Pavyzdinė struktūra:

```python
print("Vardas: Aistė")
print("Miestas: Kaunas")
print("Mokausi Python, nes noriu automatizuoti darbus")
print(12 + 8)
```

Pakeisk pavyzdžio tekstą savo informacija ir paleisk programą. Įsitikink, kad kiekvienas atsakymas rodomas atskiroje eilutėje.

> **Užduoties patikra:** parodyk savo kodą mentoriui ir paklausk „Ar mano programa apie mane parašyta taisyklingai?“

## Svarbiausia iš šios pamokos

- Python programa yra komandų seka.
- `print()` parodo rezultatą ekrane.
- Tekstas rašomas kabutėse, o skaičiai gali būti rašomi be jų.
- Python skaito programą nuo viršaus į apačią.
- Klaidos pranešimas nurodo, kur pradėti ieškoti problemos.

Kitoje pamokoje šias reikšmes išmoksime išsaugoti, pavadinti ir keisti naudodami kintamuosius.
