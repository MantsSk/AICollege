---
title: Pasiruošimas: Python, pirmas failas ir pirmoji klaida
module: Pasiruošimas
order: 0
---

# Pasiruošimas: Python, pirmas failas ir pirmoji klaida

Prieš mokantis kintamųjų reikia vieno dalyko, kurį daugelis kursų praleidžia: veikiančios aplinkos ir drąsos perskaityti klaidos pranešimą. Ši pamoka — apie tai. Ji nuobodesnė už kitas, bet be jos užstrigsi jau pirmą vakarą.

**Po šios pamokos galėsi:**

- pasitikrinti, ar kompiuteryje veikia Python;
- sukurti ir paleisti savo pirmą `.py` failą;
- perskaityti klaidos pranešimą ir suprasti, nuo ko pradėti jį taisyti.

## 1. Ar Python jau įdiegtas?

Atsidaryk terminalą (macOS: programa „Terminal“; Windows: „PowerShell“) ir įvesk:

```bash
python3 --version
```

Jei matai `Python 3.10` ar naujesnę versiją — viskas gerai. Jei komanda nerasta, atsisiųsk Python iš [python.org/downloads](https://www.python.org/downloads/) ir diegdamas „Windows“ sistemoje būtinai pažymėk **Add Python to PATH** — tai dažniausia pradedančiųjų kliūtis.

## 2. Pirmas failas

Sukurk aplanką kursui ir jame failą `hello.py` su vienintele eilute:

```python
print("Veikia!")
```

Paleisk jį terminale:

```bash
python3 hello.py
```

Jei ekrane pasirodė `Veikia!` — tu ką tik parašei ir paleidai programą. Rimtai, tai visa programavimo esmė: failas, komanda, rezultatas.

## 3. Pirmoji klaida (specialiai)

Dabar sugadink programą. Pakeisk `print` į `printt` ir paleisk dar kartą:

```text
Traceback (most recent call last):
  File "hello.py", line 1, in <module>
    printt("Veikia!")
NameError: name 'printt' is not defined. Did you mean: 'print'?
```

Išmok skaityti šį pranešimą iš apačios į viršų:

- **paskutinė eilutė** sako, *kas* nutiko (`NameError` — nežinomas vardas) ir dažnai net pasiūlo pataisymą;
- **eilutės viršuje** rodo, *kur* tai nutiko (failas ir eilutės numeris).

Klaidos pranešimas nėra bausmė — tai instrukcija. Programuotojai jų mato dešimtis per dieną.

## Pasitikrink save

**1. Ką daryti, jei `python3 --version` sako „command not found“?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Įdiegti Python iš python.org, o „Windows“ sistemoje diegimo metu pažymėti „Add Python to PATH“. Po diegimo atidaryti naują terminalo langą ir bandyti dar kartą.

</details>

**2. Iš kurios pusės skaityti ilgą klaidos pranešimą?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Nuo apačios: paskutinė eilutė pasako klaidos tipą ir priežastį, o aukščiau esančios eilutės — failą ir eilutę, kurioje ji įvyko.

</details>

**3. Kuo skiriasi failo paleidimas nuo jo parašymo?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Failas — tik tekstas. Programa jis tampa, kai terminale paleidi `python3 failo_vardas.py` ir Python įvykdo jame esančias komandas.

</details>

## Mini užduotis

Sukurk failą `apie_mane.py`, kuris išveda tris eilutes: tavo vardą, kodėl mokaisi programuoti ir vieną dalyką, kurį nori sukurti. Tada specialiai padaryk jame klaidą, paleisk ir perskaityk pranešimą.

> **Užduoties patikra:** nukopijuok gautą klaidos pranešimą mentoriui ir paklausk: „Paaiškink šį klaidos pranešimą eilutė po eilutės: kas, kur ir kodėl įvyko?“

> **Mentoriaus patarimas:** paklausk „Kokias 3 klaidas pradedantieji daro dažniausiai per pirmą Python savaitę ir kaip jas atpažinti?“

Toliau: kintamieji ir tipai — pirmieji tikri programavimo blokai.
