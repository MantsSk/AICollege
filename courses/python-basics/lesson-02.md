---
title: Sprendimai su sąlygomis
module: Sąlygos
order: 2
---

# Sprendimai su sąlygomis

Programos tampa naudingos, kai reaguoja į skirtingas situacijas. Tam ir skirtos **sąlygos**.

## if / elif / else

```python
score = 78

if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"

print(grade)  # B
```

Python kalboje įtrauka svarbi: įtrauktas blokas priklauso virš jo esančiai sąlygai.

## Palyginimo operatoriai

| Operatorius | Reikšmė |
|----------|---------|
| `==` | lygu |
| `!=` | nelygu |
| `>` `<` | daugiau / mažiau |
| `>=` `<=` | daugiau arba lygu / mažiau arba lygu |

## Sąlygų jungimas

Naudok `and`, `or`, `not`:

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Sveiki atvykę!")
```

## Tiesa ir netiesa praktikoje

Tušti dalykai laikomi „neteisingais“: `""`, `0`, `[]`, `None`. Visa kita laikoma „teisinga“.

```python
name = ""
if not name:
    print("Įveskite savo vardą")
```

> **Mentoriaus patarimas:** paprašyk DI mentoriaus duoti 3 praktikos užduotis su `if`/`elif`/`else`.

Toliau: kaip veiksmus kartoti naudojant ciklus.
