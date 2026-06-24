---
title: Funkcijos
module: Funkcijos
order: 4
---

# Funkcijos

**Funkcija** yra pavadintas, pakartotinai naudojamas kodo blokas. Ji priima įvestis ir (pasirinktinai) grąžina rezultatą.

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

> **Mentoriaus patarimas:** įklijuok savo parašytą funkciją ir paklausk DI mentoriaus „Kaip galiu šią funkciją padaryti švaresnę?“

Toliau: realaus pasaulio dalykus modeliuosime su **klasėmis**.
