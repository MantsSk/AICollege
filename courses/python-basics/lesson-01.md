---
title: Kintamieji ir tipai
module: Kintamieji
order: 1
---

# Kintamieji ir tipai

**Kintamasis** yra vardas, rodantis į reikšmę. Jį sukuri su `=` ženklu.

**Po šios pamokos galėsi:**

- sukurti kintamuosius ir atskirti keturis pagrindinius tipus;
- patikrinti reikšmės tipą su `type()`;
- formatuoti tekstą su f-string.

```python
name = "Aiste"
age = 28
price = 19.99
is_subscribed = True
```

Python *tipą* nustato automatiškai, todėl jo deklaruoti nereikia.

## Pagrindiniai tipai

| Tipas | Pavyzdys | Reikšmė |
|------|---------|---------|
| `str` | `"hello"` | tekstas |
| `int` | `42` | sveikasis skaičius |
| `float` | `3.14` | dešimtainis skaičius |
| `bool` | `True` / `False` | taip/ne reikšmė |

Tipą gali patikrinti su `type()`:

```python
print(type("hello"))   # <class 'str'>
print(type(42))        # <class 'int'>
```

## Darbas su tekstu

Eilutes galima jungti ir formatuoti. **f-string** yra modernus būdas:

```python
name = "Aiste"
lessons = 12
print(f"{name} baigė {lessons} pamokų.")
# Aiste baigė 12 pamokų.
```

## Pasitikrink save

**1. Kokio tipo yra reikšmė `19.99`? O `"19.99"`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`19.99` yra `float` (dešimtainis skaičius), o `"19.99"` — `str` (tekstas), nes yra kabutėse. Su tekstu negalėsi atlikti matematikos, kol nepaversi jo skaičiumi.

</details>

**2. Ką išves `print(f"{name} turi {age} metų")`, jei `name = "Tomas"` ir `age = 30`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`Tomas turi 30 metų` — f-string įstato kintamųjų reikšmes į riestinius skliaustus.

</details>

**3. Kodėl Python nereikia deklaruoti kintamojo tipo?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Python tipą nustato automatiškai pagal priskirtą reikšmę. Tipas priklauso reikšmei, o ne kintamojo vardui — tas pats vardas vėliau gali rodyti į kito tipo reikšmę.

</details>

## Mini užduotis

Sukurk kintamuosius savo vardui ir tikslui, tada išvesk sakinį:

```python
my_name = "..."
my_goal = "išmokti DI"
print(f"Labas, aš esu {my_name} ir noriu {my_goal}.")
```

> **Užduoties patikra:** įklijuok savo kodą mentoriui ir paprašyk: „Patikrink mano kodą ir duok vieną papildomą užduotį su kintamaisiais, kuri būtų truputį sunkesnė.“

> **Mentoriaus patarimas:** paklausk „Kodėl Python nereikia deklaruoti tipų?“ ir pažiūrėk, kaip jis paaiškins.

Kitoje pamokoje priversime programas *priimti sprendimus*.
