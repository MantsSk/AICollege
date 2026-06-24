---
title: Kintamieji ir tipai
module: Kintamieji
order: 1
---

# Kintamieji ir tipai

**Kintamasis** yra vardas, rodantis į reikšmę. Jį sukuri su `=` ženklu.

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

## Trumpa užduotis

Sukurk kintamuosius savo vardui ir tikslui, tada išvesk sakinį:

```python
my_name = "..."
my_goal = "išmokti DI"
print(f"Labas, aš esu {my_name} ir noriu {my_goal}.")
```

> **Išbandyk su DI mentoriumi:** paklausk „Kodėl Python nereikia deklaruoti tipų?“ ir pažiūrėk, kaip jis paaiškins.

Kitoje pamokoje priversime programas *priimti sprendimus*.
