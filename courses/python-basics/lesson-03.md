---
title: Ciklai ir kartojimas
module: Ciklai
order: 3
---

# Ciklai ir kartojimas

Ciklai leidžia kartoti darbą nekopijuojant kodo.

**Po šios pamokos galėsi:**

- iteruoti per sąrašus su `for` ir generuoti skaičius su `range()`;
- naudoti `while`, `break` ir `continue`;
- auginti sąrašą cikle ir užrašyti tą patį trumpiau su list comprehension.

## `for` ciklas

Iteruok per rinkinį:

```python
courses = ["Python", "AI Fundamentals", "AI Assistant"]

for course in courses:
    print(f"Mokausi {course}")
```

`range()` generuoja skaičius:

```python
for i in range(3):
    print(i)   # 0, 1, 2
```

## `while` ciklas

Kartok tol, *kol* sąlyga teisinga:

```python
attempts = 0
while attempts < 3:
    print("Bandau...")
    attempts += 1
```

Būk atsargus: jei sąlyga niekada netampa klaidinga, ciklas veiks amžinai.

## Naudingi įrankiai

`break` sustabdo ciklą anksčiau, o `continue` praleidžia iki kito karto:

```python
for n in range(10):
    if n == 5:
        break        # visiškai sustoti
    if n % 2 == 0:
        continue     # praleisti lyginius skaičius
    print(n)         # 1, 3
```

## Sąrašai auga su ciklais

```python
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)  # [1, 4, 9, 16, 25]
```

Trumpesnė versija (*list comprehension*):

```python
squares = [n * n for n in range(1, 6)]
```

## Pasitikrink save

**1. Ką išves `for i in range(3): print(i)`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`0`, `1`, `2` — `range(3)` pradeda nuo nulio ir baigia ties 2 (riba neįtraukiama).

</details>

**2. Kada rinktis `while` vietoj `for`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kai nežinai, kiek kartų reikės kartoti — kartoji, *kol* sąlyga teisinga (pvz., kol vartotojas įves teisingą atsakymą). `for` tinka, kai eini per žinomą rinkinį ar skaičių seką.

</details>

**3. Kuo skiriasi `break` ir `continue`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`break` nutraukia visą ciklą, o `continue` praleidžia tik dabartinį žingsnį ir pereina prie kito.

</details>

## Mini užduotis

Parašyk ciklą, kuris eina per skaičius nuo 1 iki 20 ir išveda tik tuos, kurie dalijasi iš 3. Tada perrašyk tą patį kaip list comprehension.

> **Užduoties patikra:** įklijuok abu variantus mentoriui ir paklausk: „Ar mano list comprehension tikrai atitinka ciklą? Kada comprehension tampa per sudėtingas ir geriau likti prie ciklo?“

> **Mentoriaus patarimas:** paklausk „Kuo skiriasi `for` ir `while` ciklai? Pateik realų pavyzdį.“

Toliau: logiką sudėsime į pakartotinai naudojamas **funkcijas**.
