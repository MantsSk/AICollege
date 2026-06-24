---
title: Klasės ir objektai
module: Klasės
order: 5
---

# Klasės ir objektai

**Klasė** yra planas. **Objektas** yra dalykas, sukurtas pagal tą planą. Klasės sujungia *duomenis* ir *elgesį*.

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

> **Mentoriaus patarimas:** paprašyk DI mentoriaus sumodeliuoti `BankAccount` klasę su įnešimo ir išėmimo metodais, tada paaiškinti kiekvieną eilutę.

Sveikinimai — dabar turi Python pagrindą, kurio reikia **DI pagrindų** kursui.
