---
title: Sprendimai su sąlygomis
module: Sąlygos
order: 2
---

# Sprendimai su sąlygomis

Programos tampa naudingos, kai reaguoja į skirtingas situacijas. Tam ir skirtos **sąlygos**.

**Po šios pamokos galėsi:**

- rašyti `if` / `elif` / `else` šakas;
- jungti sąlygas su `and`, `or`, `not`;
- suprasti, kodėl `""`, `0` ir `[]` laikomi „netiesa“.

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

## Pasitikrink save

**1. Kokį pažymį gaus `score = 90` pavyzdyje viršuje?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`A` — sąlyga `score >= 90` teisinga, todėl `elif` ir `else` šakos net netikrinamos. Python vykdo tik pirmą teisingą šaką.

</details>

**2. Kuo skiriasi `=` ir `==`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`=` priskiria reikšmę kintamajam, o `==` palygina dvi reikšmes ir grąžina `True` arba `False`. Jų supainiojimas — viena dažniausių pradedančiųjų klaidų.

</details>

**3. Ką išves `if not "": print("tuščia")`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

`tuščia` — tuščias tekstas `""` laikomas netiesa, todėl `not ""` yra `True`.

</details>

## Mini užduotis

Parašyk programą, kuri pagal valandą (0–23) išveda pasisveikinimą: „Labas rytas“, „Laba diena“ arba „Labas vakaras“.

> **Užduoties patikra:** įklijuok savo sprendimą mentoriui ir paprašyk: „Patikrink mano kodą: ar ribinės reikšmės (0, 12, 18, 23) veikia teisingai? Jei ne, neduok atsakymo — duok užuominą.“

> **Mentoriaus patarimas:** paprašyk DI mentoriaus duoti 3 praktikos užduotis su `if`/`elif`/`else`.

Toliau: kaip veiksmus kartoti naudojant ciklus.
