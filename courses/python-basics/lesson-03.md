---
title: Ciklai ir kartojimas
module: Ciklai
order: 3
---

# Ciklai ir kartojimas

Ciklai leidžia kartoti darbą nekopijuojant kodo.

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

> **Mentoriaus patarimas:** paklausk „Kuo skiriasi `for` ir `while` ciklai? Pateik realų pavyzdį.“

Toliau: logiką sudėsime į pakartotinai naudojamas **funkcijas**.
