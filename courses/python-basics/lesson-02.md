---
title: Vartotojo įvestis: input()
module: 1 · Pati pradžia
order: 2
---

# Vartotojo įvestis: input()

Iki šiol tavo programa turėjo visus duomenis iš anksto – vardą ar skaičių įrašydavai pats į kodą. Tikros programos yra kitokios: jos **paklausia** žmogaus ir dirba su bet kokiu jo atsakymu. Tam skirta funkcija `input()`.

Šioje pamokoje parašysi programą, kuri paklausia vartotojo ir panaudoja jo atsakymą. Taip pat išmoksi svarbiausią su įvestimi susijusią taisyklę: `input()` visada grąžina tekstą.

## Ką išmoksi

Baigęs pamoką gebėsi:

- paklausti vartotojo naudodamas `input()`;
- išsaugoti atsakymą kintamajame ir jį panaudoti;
- paaiškinti, kodėl `input()` visada grąžina tekstą;
- paversti tekstą skaičiumi su `int()` arba `float()`;
- pastebėti ir pataisyti dažną „tekstas vietoj skaičiaus“ klaidą.

## 1. Kaip paklausti vartotojo

Funkcija `input()` sustabdo programą, parodo tavo parašytą klausimą (raginimą) ir laukia, kol vartotojas ką nors įves ir paspaus Enter. Įvestą eilutę ji grąžina kaip reikšmę, kurią gali išsaugoti kintamajame.

```python
vardas = input("Kaip tave vadinti? ")
print("Sveikas,", vardas)
```

Jei vartotojas įves `Aistė`, programa parodys:

```text
Sveikas, Aistė
```

Pagal Python dokumentaciją, `input()` klausimą parodo ekrane **be naujos eilutės**, tada perskaito vieną įvestą eilutę, pašalina paskutinį eilutės perkėlimą ir grąžina likusį tekstą.

> **Laboratorijoje:** kai programa pasieks `input()`, naršyklėje iškils langelis įvesčiai. Įrašyk atsakymą ir paspausk Enter arba „Gerai“. Jei langelį atšauksi, programa nutrūks – tiesiog paleisk ją iš naujo.

## 2. `input()` visada grąžina tekstą

Tai svarbiausia šios pamokos mintis. Net jei vartotojas įves skaitmenis, `input()` grąžins juos kaip **tekstą** (`str`), o ne kaip skaičių.

```python
amzius = input("Kiek tau metų? ")
print(amzius + 1)
```

Įvedus `25`, programa neparodys `26`. Vietoj to Python parodys klaidą:

```text
TypeError: can only concatenate str (not "int") to str
```

Klaida sako paprastą dalyką: `amzius` yra tekstas `"25"`, o `1` yra skaičius. Python nesudeda teksto su skaičiumi, nes nežino, ar nori juos sujungti, ar sudėti aritmetiškai.

> **Dažna klaida:** matyti „skaičių“ ekrane dar nereiškia, kad tai skaičius. `input()` rezultatas visada yra tekstas, kol pats jo nepaversi.

## 3. Tekstą paversk skaičiumi: `int()` ir `float()`

Kad su įvestimi galėtum skaičiuoti, tekstą reikia paversti skaičiumi:

- `int()` paverčia tekstą **sveikuoju** skaičiumi;
- `float()` paverčia tekstą skaičiumi su **trupmenine** dalimi.

```python
amzius = int(input("Kiek tau metų? "))
print("Kitais metais tau bus", amzius + 1)
```

Čia veiksmai vyksta iš vidaus į išorę: pirmiausia `input()` gauna tekstą, tada `int()` jį paverčia skaičiumi, ir tik tada reikšmė priskiriama kintamajam `amzius`. Dabar `amzius + 1` veikia teisingai.

```python
kaina = float(input("Kokia prekės kaina? "))
print("Su 10% nuolaida:", kaina * 0.9)
```

Svarbu: `int()` ir `float()` veikia tik su tekstu, kuris **atrodo** kaip skaičius. `int("25")` grąžina `25`, bet `int("25 metai")` ar `int("dvidešimt")` sukelia klaidą:

```text
ValueError: invalid literal for int() with base 10: '25 metai'
```

**Pasitikrink.** Kokio tipo reikšmę grąžina `input()` – skaičių ar tekstą? Pirmiausia atsakyk pats.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Visada **tekstą** (`str`), net jei įvedei vien skaitmenis. Kad su įvestimi galėtum skaičiuoti, ją reikia paversti skaičiumi su `int()` arba `float()`.

</details>

## 4. Maža interaktyvi programa

Sujungę tai, ką jau moki, gauname programą, kuri klausia, skaičiuoja ir parodo rezultatą:

```python
a = int(input("Pirmas skaičius: "))
b = int(input("Antras skaičius: "))
print("Suma:", a + b)
```

Įvedus `2` ir `3`, programa parodys:

```text
Suma: 5
```

Atkreipk dėmesį į skirtumą: jei praleistum `int()` ir sudėtum du tekstus, `"2" + "3"` duotų ne `5`, o `"23"` – tekstai tiesiog sujungiami vienas prie kito. Klaidos nebūtų, bet rezultatas būtų neteisingas. Todėl `int()` čia būtinas.

## 5. Dažnos klaidos

### Pamiršta konversija į skaičių

```python
kiekis = input("Kiek vienetų? ")
print(kiekis * 2)
```

`kiekis` yra tekstas, todėl `kiekis * 2` ne padvigubins skaičiaus, o pakartos tekstą du kartus (`"5"` taps `"55"`). Pirmiausia paversk įvestį skaičiumi: `kiekis = int(input("Kiek vienetų? "))`.

### `int()` su netinkamu tekstu

```python
amzius = int(input("Kiek tau metų? "))
```

Jei vartotojas įves `maždaug 25`, `int()` parodys klaidą, nes tai nėra vien skaičius. Šiame kurse laikysimės susitarimo, kad vartotojas įveda tvarkingą skaičių; kaip saugiai tikrinti įvestį, mokysimės vėliau.

### Neišsaugotas atsakymas

```python
input("Koks tavo vardas? ")
print("Sveikas!")
```

Programa paklausia, bet atsakymo niekur neišsaugo, todėl vėliau jo panaudoti nebegali. Priskirk `input()` rezultatą kintamajam: `vardas = input("Koks tavo vardas? ")`.

## 6. Praktinė užduotis

Laboratorijoje parašyk programą, kuri:

1. paklausia vartotojo dviejų skaičių;
2. paverčia įvestį skaičiais su `int()`;
3. parodo jų sumą su aiškiu užrašu.

Pradžia gali atrodyti taip:

```python
a = int(input("Pirmas skaičius: "))
b = int(input("Antras skaičius: "))
print("Suma:", a + b)
```

Paleisk programą, įvesk du skaičius ir įsitikink, kad suma teisinga.

> **Užduoties patikra:** parodyk savo kodą mentoriui ir paklausk „Ar teisingai paverčiau vartotojo įvestį skaičiumi?“

## Svarbiausia iš šios pamokos

- `input()` paklausia vartotojo ir grąžina jo įvestą tekstą (`str`).
- `input()` rezultatas visada tekstas – net jei įvesti vien skaitmenys.
- `int()` paverčia tekstą sveikuoju skaičiumi, `float()` – skaičiumi su trupmenine dalimi.
- Netinkamas tekstas `int()` ar `float()` viduje sukelia klaidą (`ValueError`).
- Įvestį būtina išsaugoti kintamajame, kad galėtum ja pasinaudoti vėliau.

Kitoje pamokoje programa išmoks pati priimti sprendimus: pagal vartotojo atsakymą pasirinks, ką daryti toliau (`if`, `elif`, `else`).
