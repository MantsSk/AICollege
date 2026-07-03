---
title: Funkcijos
module: Funkcijos
order: 4
---

# Funkcijos

**Funkcija** yra pavadintas, pakartotinai naudojamas kodo blokas. Ji priima įvestis ir (pasirinktinai) grąžina rezultatą.

**Po šios pamokos galėsi:**

- apibrėžti funkciją su parametrais ir numatytosiomis reikšmėmis;
- suprasti, ką ir kada grąžina `return`;
- kviesti funkcijas su vardiniais argumentais.

```python
def greet(name):
    return f"Labas, {name}!"

message = greet("Aiste")
print(message)   # Labas, Aiste!
```

## Parametrai ir numatytosios reikšmės

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25  (exponent numatyta reikšmė yra 2)
print(power(2, 10))  # 1024
```

## Reikšmių grąžinimas

Funkcija be aiškaus `return` grąžina `None`.

```python
def add(a, b):
    return a + b

total = add(3, 4)   # 7
```

## Kodėl funkcijos svarbios

Jos leidžia:

- **Vengti kartojimo** — parašyk logiką vieną kartą, naudok visur.
- **Pavadinti idėjas** — `calculate_tax()` skaitosi geriau nei 5 matematikos eilutės.
- **Testuoti mažas dalis** atskirai.

## Vardiniai argumentai

Aiškumui argumentus gali perduoti pagal vardą:

```python
def create_user(email, plan="free"):
    return {"email": email, "plan": plan}

create_user(email="a@b.com", plan="paid")
```

## Pasitikrink save

**1. Ką grąžina funkcija be `return`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`None`. Funkcija gali kažką išvesti su `print`, bet jei nėra `return`, jos rezultato negalėsi priskirti kintamajam ar naudoti toliau.

</details>

**2. Ką išves `print(power(3))`, jei `def power(base, exponent=2)`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`9` — nenurodžius antro argumento, naudojama numatytoji reikšmė `exponent=2`, taigi `3 ** 2`.

</details>

**3. Kodėl verta logiką dėti į funkcijas, o ne rašyti iš eilės?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kad išvengtum kartojimo, galėtum pavadinti idėją suprantamu vardu ir testuoti mažas dalis atskirai.

</details>

## Mini užduotis

Parašyk funkciją `bmi(weight_kg, height_m)`, kuri grąžina kūno masės indeksą, ir funkciją `bmi_text(value)`, kuri pagal reikšmę grąžina tekstą („mažas“, „normalus“, „didelis“). Sujunk jas viename `print`.

> **Užduoties patikra:** įklijuok savo funkcijas mentoriui ir paprašyk: „Kaip galiu šias funkcijas padaryti švaresnes? Ar gerai parinkti vardai ir parametrai?“

> **Mentoriaus patarimas:** įklijuok savo parašytą funkciją ir paklausk DI mentoriaus „Kaip galiu šią funkciją padaryti švaresnę?“

Toliau: realaus pasaulio dalykus modeliuosime su **klasėmis**.
