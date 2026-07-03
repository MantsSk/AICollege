---
title: Klasės ir objektai
module: Klasės
order: 5
---

# Klasės ir objektai

**Klasė** yra planas. **Objektas** yra dalykas, sukurtas pagal tą planą. Klasės sujungia *duomenis* ir *elgesį*.

**Po šios pamokos galėsi:**

- apibrėžti klasę su `__init__`, atributais ir metodais;
- sukurti objektus ir kviesti jų metodus;
- atpažinti klases DI bibliotekų kode.

```python
class Student:
    def __init__(self, name, plan="free"):
        self.name = name
        self.plan = plan
        self.completed_lessons = 0

    def complete_lesson(self):
        self.completed_lessons += 1

    def is_subscribed(self):
        return self.plan == "paid"
```

## Objektų kūrimas

```python
aiste = Student("Aiste", plan="paid")
aiste.complete_lesson()
aiste.complete_lesson()

print(aiste.completed_lessons)  # 2
print(aiste.is_subscribed())    # True
```

## Pagrindinės dalys

- `__init__` yra **konstruktorius** — jis paleidžiamas kuriant objektą.
- `self` reiškia *šį konkretų objektą*.
- **Atributai** (`self.name`) saugo duomenis.
- **Metodai** (`complete_lesson`) yra objektui priklausančios funkcijos.

## Kodėl klasės svarbios DI darbuose

Dauguma DI bibliotekų paremtos klasėmis. Kai rašai:

```python
client = OpenAI()
response = client.chat.completions.create(...)
```

...tu sukuri objektą (`client`) ir kvieti jo metodus. Supratus klases, kiekvienas DI SDK tampa pažįstamas.

## Pasitikrink save

**1. Kuo skiriasi klasė nuo objekto?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Klasė yra planas (aprašymas), o objektas — pagal tą planą sukurtas konkretus egzempliorius. Iš vienos `Student` klasės gali sukurti daug skirtingų studentų.

</details>

**2. Ką reiškia `self` metodo viduje?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Tą konkretų objektą, kuriam iškviestas metodas. `aiste.complete_lesson()` viduje `self` yra `aiste`, todėl keičiasi būtent jos `completed_lessons`.

</details>

**3. Ką išves `print(aiste.completed_lessons)` po dviejų `complete_lesson()` kvietimų?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`2` — kiekvienas kvietimas padidina atributą vienetu, o būsena saugoma pačiame objekte.

</details>

## Mini užduotis

Sukurk klasę `Course` su atributais `title` ir `lessons_done` bei metodais `complete()` (padidina skaitiklį) ir `progress_text()` (grąžina, pvz., „Python pagrindai: 3 pamokos baigtos“). Sukurk du kursus ir parodyk jų progresą.

> **Užduoties patikra:** įklijuok savo klasę mentoriui ir paprašyk: „Peržiūrėk mano klasę: ar atributai ir metodai logiškai paskirstyti? Ką pridėtum, kad ji būtų naudinga realioje programoje?“

> **Mentoriaus patarimas:** paprašyk DI mentoriaus sumodeliuoti `BankAccount` klasę su įnešimo ir išėmimo metodais, tada paaiškinti kiekvieną eilutę.

Sveikinimai — dabar turi Python pagrindą, kurio reikia tolimesniems kursams: **Junior AI programuotojo projektai** ir **Sukurk savo DI asistentą**.
