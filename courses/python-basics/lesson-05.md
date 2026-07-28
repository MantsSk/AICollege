---
title: Funkcijos ir moduliai – išskaidyk asistentą į aiškias dalis
module: Python pagrindai
order: 5
---

# Funkcijos ir moduliai – išskaidyk asistentą į aiškias dalis

> **Trukmė:** 8 akademinės valandos. Tikslas – ne parašyti daugiau eilučių, o sukurti aiškesnę programą.

## Trumpa anotacija

Asistento kodas kol kas gyvena viename ilgame faile, kuriame teksto valymas, temų paieška ir atsakymų formavimas kartojasi kelis kartus skirtingose vietose. Šioje pamokoje tą patį elgesį išskaidysi į aiškiai pavadintas funkcijas ir kelis atskirus `.py` modulius. Išmoksi apibrėžti funkciją su parametrais, argumentais ir `return`, naudoti numatytuosius argumentus bei tipų užuominas, atskirti vietinį kintamąjį nuo globalaus ir tvarkingai importuoti kodą iš kito failo. Šie įgūdžiai – funkcijų rašymas, atsakomybių atskyrimas, modulių kūrimas – yra pagrindas bet kokiai didesnei Python programai, įskaitant automatizavimo scenarijus ir DI įrankius, kuriuose atskiros funkcijos atsako už duomenų paruošimą, užklausos formavimą ir atsakymo apdorojimą.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- apibrėžti funkciją su `def`, parametrais ir aiškiu `return`;
- atskirti parametrą nuo argumento bei `return` nuo `print()`;
- naudoti numatytuosius argumentus ir tipų užuominas (`str`, `int`, `dict`, `tuple`, `| None`);
- paaiškinti, kuo vietinis (local) kintamasis skiriasi nuo globalaus (global);
- sukurti savo modulį ir importuoti iš jo konkrečias funkcijas;
- tinkamai naudoti `if __name__ == "__main__":`;
- parašyti docstring, kuris paaiškina funkcijos sutartį – ką ji priima ir ką grąžina;
- perrašyti Asistento 0.3 ilgą `if` grandinę į mažas, atskirai testuojamas funkcijas (Asistentas 0.4).

## Būtinos ankstesnės žinios

Ketvirtoje pamokoje išmokai valyti ir skaidyti tekstą teksto metodais, naudoti `dict` bei įdėtas struktūras ir su jomis pastatei Asistentą 0.3 – žinių bazę su `keywords`/`answer`, komandomis `/topics` bei `/history` ir pokalbio istoriją kaip žodynų sąrašą. Ši pamoka tą patį elgesį perkelia į funkcijas ir modulius, todėl turėtum turėti veikiantį Asistento 0.3 failą bei mokėti naudoti `for`, `if/elif/else`, `.get()`, sąrašo `.append()` ir žodyno raktų kreipinius. Jei tavo Asistentas 0.3 dar neveikia be klaidų, pasitaisyk jį prieš pradėdamas šią pamoką – ketvirtos pamokos atmintinė padės greitai prisiminti sintaksę.

## 1. Įtraukianti pradžia: kodėl programai reikia funkcijų

Virtuvėje „paruošti arbatą“ slepia kelis žingsnius: užvirinti vandenį, įdėti arbatžolių, palaukti, supilti. Nesakome kiekvieną kartą viso recepto iš naujo – užtenka pavadinimo. Kode veikia tas pats principas: pavadintas veiksmų blokas leidžia jį pakartotinai naudoti nerašant tų pačių eilučių iš naujo.

Pažiūrėk, kaip atrodo Asistento kodas, kai tas pats teksto valymas nukopijuojamas kiekvieną kartą, kai reikia jį pritaikyti:

```python
message_1 = "  Kokia KAINA?! "
cleaned_1 = message_1.strip().lower().replace("!", "").replace("?", "")

message_2 = "  KADA prasideda MOKYMAI??  "
cleaned_2 = message_2.strip().lower().replace("!", "").replace("?", "")

print(cleaned_1)
print(cleaned_2)
```

Jei rytoj nuspręsi valymą papildyti (pvz. pašalinti ir kablelius), teks keisti abi vietas – o realiame projekte tokių vietų gali būti dešimtys. Funkcija leidžia elgesį aprašyti vieną kartą:

```python
def normalize_text(text):
    cleaned = text.strip().lower()
    cleaned = cleaned.replace("!", "")
    cleaned = cleaned.replace("?", "")
    return cleaned

message_1 = normalize_text("  Kokia KAINA?! ")
message_2 = normalize_text("  KADA prasideda MOKYMAI??  ")

print(message_1)
print(message_2)
```

```text
kokia kaina
kada prasideda mokymai
```

`text` yra **parametras** – vardas, kurio funkcija laukia apibrėžime. `"  Kokia KAINA?! "` yra **argumentas** – konkreti reikšmė, perduota kviečiant funkciją. `return` grąžina rezultatą į kvietimo vietą, kur jį galima priskirti kintamajam, panaudoti tolesniame skaičiavime ar perduoti kitai funkcijai. `print()` tik parodo reikšmę ekrane – jis nepakeičia `return` ir nieko negrąžina atgal į kodą.

> **Išbandyk pats:** prieš skaitydamas toliau, savais žodžiais paaiškink, kuo funkcijos *apibrėžimas* (`def normalize_text(text):`) skiriasi nuo jos *iškvietimo* (`normalize_text("Kaina?")`). Kuri eilutė aprašo, o kuri – realiai vykdo veiksmą?

## 2. Pagrindinės sąvokos

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| Funkcija | Pavadintas, pakartotinai kviečiamas veiksmų blokas | Receptas, kurį gali pagaminti kelis kartus | Kai tą patį veiksmą reikia atlikti daugiau nei kartą | Funkcija parašoma, bet niekada nepakviečiama |
| Parametras | Vardas kintamajam, kurio funkcija laukia apibrėžime | Tuščia recepto eilutė „įdėk ___ gramų miltų“ | Aprašant, ko funkcijai reikės | Painiojamas su argumentu |
| Argumentas | Konkreti reikšmė, perduota kviečiant funkciją | Faktiškai įdėti 200 gramų miltų | Kviečiant funkciją su realiais duomenimis | Argumentų tvarka sumaišoma |
| `return` | Grąžina rezultatą į kvietimo vietą | Padavėjas atneša paruoštą patiekalą prie stalo | Kai funkcijos rezultatą reikia naudoti toliau | Pamirštas – funkcija tyliai grąžina `None` |
| `print()` | Parodo reikšmę ekrane, bet nieko negrąžina | Virėjas garsiai pasako, ką pagamino, bet nieko neatiduoda į rankas | Kai norima tik parodyti tarpinę informaciją | Naudojamas vietoj `return`, rezultatas dingsta |
| Numatytasis argumentas | Reikšmė, naudojama, kai kviečiant argumentas nenurodytas | Kavos automatas, kuris be pasirinkimo pilsto vidutinį puodelį | Kai dauguma kvietimų naudoja tą pačią reikšmę | Numatytasis argumentas rašomas prieš privalomą |
| Tipo užuomina | Pastaba, kokio tipo reikšmę funkcija tikisi ar grąžina | Etiketė ant dėžutės „čia – skaičiai“ | Aiškinant kitiems programuotojams ir redaktoriui | Manoma, kad Python patikrins tipą vykdymo metu |
| Sritis (local/global) | Vieta programoje, kur kintamasis egzistuoja ir yra pasiekiamas | Kambario raktas veikia tik tame kambaryje | Nustatant, ar kintamasis matomas už funkcijos ribų | Bandoma naudoti funkcijos vidinį kintamąjį už jos ribų |
| Modulis | Atskiras `.py` failas su funkcijomis, kurį galima importuoti | Atskira įrankių dėžė sandėliuke | Kai kodą reikia dalinti į logines dalis | Failas pavadinamas kaip standartinis modulis, pvz. `json.py` |
| `import` | Komanda, įkelianti kito modulio kodą į dabartinį failą | Atsinešimas įrankio iš kitos dėžės | Naudojant kitame faile parašytas funkcijas | Importuojama visa, kai reikėjo tik vienos funkcijos |
| `if __name__ == "__main__":` | Sąlyga, leidžianti kodą paleisti tik tiesioginio vykdymo metu | Durų kodas, veikiantis tik įėjus pro pagrindinį įėjimą | Atskiriant paleidimo logiką nuo importuojamų funkcijų | Praleista – importavus modulį netyčia paleidžiamas dialogas |
| Docstring | Trumpas aprašymas tarp `"""..."""` po funkcijos apibrėžimo | Naudojimo instrukcija ant įrankio dėžutės | Paaiškinant funkcijos sutartį – ką ji priima ir grąžina | Rašomas komentaras `#`, kurio nemato `help()` |

## 3. Vizualūs paaiškinimai

### Vizualizacija A – funkcija kaip juoda dėžė

```text
   Įvestis                 ┌───────────────────────────┐              Išvestis
──────────────────►        │   normalize_text(text)     │        ──────────────────►
"  Kokia KAINA?! "          │                            │        "kokia kaina"
                            └───────────────────────────┘
   parametras: text                                       return reikšmė: str
```

**Iliustracijos pavadinimas:** „Funkcija – juoda dėžė su aiškia įvestimi ir išvestimi“
**Ką ji turi parodyti:** kad funkcija priima reikšmę, ją apdoroja viduje ir grąžina naują reikšmę, nekeisdama to, kas vyksta aplinkui.
**Kokie elementai turi būti matomi:** dėžė su funkcijos vardu viduje, rodyklė „įvestis“ su neapdorotu tekstu, rodyklė „išvestis“ su rezultatu, žymos „parametras“ ir „return“.
**Siūlomas vaizdo generavimo promptas:** „Minimalistinė edukacinė vektorinė schema lietuviškai: dėžė su užrašu normalize_text(text), į ją rodyklė su tekstu 'Kokia KAINA?!', iš jos rodyklė su tekstu 'kokia kaina'; žymos parametras ir return; aukštas kontrastas, plokščias stilius.“

### Vizualizacija B – moduliai importuoja vieni kitus

```text
main.py
 ├── from text_tools import normalize_text ───────► text_tools.py
 ├── from knowledge import KNOWLEDGE_BASE ────────► knowledge.py
 └── from assistant_core import find_answer ──────► assistant_core.py
                                                          │
                                                          └── naudoja knowledge_base,
                                                              bet negrąžina jo iš text_tools.py
```

**Iliustracijos pavadinimas:** „Vienas paleidimo taškas, keturi atsakingi failai“
**Ką ji turi parodyti:** kad `main.py` importuoja funkcijas iš kitų modulių, o ne visa logika sugrūsta į vieną failą.
**Kokie elementai turi būti matomi:** centrinis `main.py` langelis, trys šoniniai moduliai su savo pavadinimais, rodyklės su `import` frazėmis.
**Siūlomas vaizdo generavimo promptas:** „Schema lietuviškai, rodanti main.py centre su trimis rodyklėmis į text_tools.py, knowledge.py ir assistant_core.py; kiekviena rodyklė pažymėta atitinkama import eilute; tvarkingas, techninis stilius.“

## 4. Funkcija: parametras, argumentas ir grąžinama reikšmė

Grįžkime prie `normalize_text` ir perskaitykime ją eilutė po eilutės:

```python
def normalize_text(text):
    cleaned = text.strip().lower()
    cleaned = cleaned.replace("!", "")
    cleaned = cleaned.replace("?", "")
    return cleaned

message = normalize_text("  Kokia KAINA?! ")
print(message)
```

1. `def normalize_text(text):` – apibrėžiama funkcija, vienintelis parametras vadinamas `text`.
2. `cleaned = text.strip().lower()` – iš parametro sukuriamas naujas vietinis kintamasis.
3. Dvi `replace()` eilutės pašalina skyrybos ženklus.
4. `return cleaned` – rezultatas grąžinamas į kvietimo vietą.
5. `normalize_text("  Kokia KAINA?! ")` – kvietimas su konkrečiu argumentu; grąžinta reikšmė priskiriama `message`.

> **Dažna klaida:** jei paskutinė eilutė būtų `print(cleaned)` vietoje `return cleaned`, funkcija ekrane parodytų rezultatą, bet `message = normalize_text(...)` gautų `None` – nes funkcija be aiškaus `return` visada grąžina `None`. `print()` viduje ir `return` iš išorės neatstoja vienas kito.

**Mini užduotis.** Parašyk funkciją `shout_word(word)`, kuri grąžina žodį didžiosiomis raidėmis su šauktuku gale. Patikrink su `"labas"`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
def shout_word(word):
    return word.upper() + "!"

print(shout_word("labas"))
```

```text
LABAS!
```

</details>

## 5. Viena funkcija – viena aiški atsakomybė

```python
def find_topic(message, knowledge_base):
    for topic_name, topic_data in knowledge_base.items():
        for keyword in topic_data["keywords"]:
            if keyword in message:
                return topic_name
    return None


def build_answer(topic_name, knowledge_base):
    if topic_name is None:
        return "Atsakymo žinių bazėje neradau."
    return knowledge_base[topic_name]["answer"]
```

`find_topic` atsakinga tik už paiešką, `build_answer` – tik už atsakymo suformavimą. Kiekviena funkcija turi vieną aiškią atsakomybę, o jos vardas iš karto pasako, ką ji daro, nesigilinant į vidų. Ankstyvas `return topic_name` užbaigia funkciją, vos radus atitikmenį – toliau ieškoti nebereikia.

Palygink su bloga versija, kurioje `return` parašytas per anksti dėl neteisingo įtraukimo:

```python
def find_topic_buggy(message, knowledge_base):
    for topic_name, topic_data in knowledge_base.items():
        first_keyword = topic_data["keywords"][0]
        if first_keyword in message:
            return topic_name
        return None  # ← grąžina po pirmos temos, net jei ji netiko
```

Čia funkcija patikrina tik pirmą temą ir pirmą jos raktažodį – jei nesutampa, iškart grąžina `None`, nors likusios temos net nebuvo patikrintos. Teisingoje versijoje `return None` yra už abiejų ciklų, o ne iškart po pirmo `if`.

> **Dažna klaida:** `return` parašytas neteisingame įtraukimo lygyje patikrina tik dalį duomenų. Prieš baigdamas visada patikrink su keliais skirtingais įrašais, ne tik pirmu žinių bazės elementu.

**Mini užduotis.** Parašyk funkciją `is_known_topic(topic_name, knowledge_base)`, kuri grąžina `True`, jei tema egzistuoja žinių bazėje, ir `False` priešingu atveju.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
def is_known_topic(topic_name, knowledge_base):
    return topic_name in knowledge_base

print(is_known_topic("kursas", {"kursas": {}}))
print(is_known_topic("kaina", {"kursas": {}}))
```

```text
True
False
```

</details>

## 6. Numatytieji argumentai ir tipų užuominos

```python
def format_reply(answer: str, source: str | None = None) -> str:
    if source:
        return f"{answer}\nŠaltinis: {source}"
    return answer
```

Tipų užuominos (`answer: str`, `-> str`) Python nepriverčia laikytis tipo vykdymo metu – jos nurodo *ketinimą* ir padeda skaitytojui bei redaktoriui, kuris gali iš anksto pastebėti neatitikimą. Numatytieji argumentai visada rašomi po privalomų:

```python
print(format_reply("Pamoka prasideda 9:00."))
print(format_reply("Kursas trunka 88 val.", "Kurso programa"))
```

```text
Pamoka prasideda 9:00.
Kursas trunka 88 val.
Šaltinis: Kurso programa
```

> **Dažna klaida:** `def format_reply(source: str | None = None, answer: str):` sukelia `SyntaxError` – numatytasis argumentas negali eiti prieš privalomą. Rašyk visus privalomus parametrus pirmiau, o numatytuosius – gale.

Yra ir subtilesnis spąstas – **kintamas numatytasis argumentas**:

```python
def add_entry(entry, history=[]):
    history.append(entry)
    return history

print(add_entry("pirmas"))
print(add_entry("antras"))
```

```text
['pirmas']
['pirmas', 'antras']
```

Nors tikimasi, kad kiekvienas kvietimas be `history` argumento sukurtų naują tuščią sąrašą, Python sukuria numatytąjį `[]` tik vieną kartą – funkcijos apibrėžimo metu – ir jis dalinamas tarp *visų* kvietimų. Saugus sprendimas:

```python
def add_entry(entry, history=None):
    if history is None:
        history = []
    history.append(entry)
    return history
```

> **Dažna klaida:** numatytuoju argumentu naudojamas kintamas objektas (`[]`, `{}`). Vietoje jo naudok `None` ir sąrašą arba žodyną sukurk funkcijos viduje.

## 7. Sritis: kur kintamasis matomas

```python
assistant_name = "Aida"

def greet(user_name):
    greeting = f"Labas, {user_name}! Aš {assistant_name}."
    return greeting
```

`greeting` yra **vietinis (local)** kintamasis – jis sukuriamas funkcijos viduje ir už jos ribų neegzistuoja. `assistant_name` yra **globalus** – jis apibrėžtas modulio lygyje ir funkcijos viduje tik *skaitomas*, ne keičiamas. Funkcijoms geriau perduoti reikšmes per parametrus bei grąžinti rezultatą su `return`, o ne tyliai keisti globalią būseną:

Blogiau:

```python
history = []

def save_message(message):
    history.append(message)
```

Aiškiau:

```python
def save_message(history, message):
    history.append(message)
    return history
```

Antrame variante iš funkcijos parašo iš karto matosi, nuo ko ji priklauso ir ką paveikia – to nereikia spėti skaitant visą failą.

Jei funkcijos viduje kintamajam priskiri reikšmę tuo pačiu vardu, kaip globalus kintamasis, bet nenaudoji `global`, Python tą vardą visoje funkcijoje laikys vietiniu – net eilutėse *prieš* priskyrimą:

```python
counter = 0

def increment():
    counter = counter + 1  # UnboundLocalError
    return counter

increment()
```

```text
UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
```

Python, pamatęs `counter = ...` funkcijos viduje, nusprendžia, kad `counter` yra vietinis kintamasis nuo pat funkcijos pradžios – todėl dešinėje pusėje esantis `counter` dar neturi reikšmės. Aiškesnis sprendimas – neliesti globalaus kintamojo, o perduoti ir grąžinti reikšmę:

```python
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
print(counter)
```

> **Dažna klaida:** bandymas pakeisti globalų kintamąjį iš funkcijos vidaus be aiškaus parametro ir `return`. Beveik visada geriau perduoti reikšmę parametru ir grąžinti naują – tai nuspėjama ir lengvai testuojama.

**Mini užduotis.** Turi kodą `total = 0; def add(value): total = total + value`. Perrašyk jį taip, kad `add` priimtų `total` kaip parametrą ir grąžintų naują sumą.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
def add(total, value):
    return total + value

total = 0
total = add(total, 5)
total = add(total, 3)
print(total)
```

```text
8
```

</details>

## 8. Moduliai, importai ir dokumentavimas

Standartinė biblioteka įdiegiama kartu su Python – jos funkcijas gauni vien importuodamas:

```python
from datetime import datetime
from pathlib import Path

now = datetime.now()
project_dir = Path(__file__).parent
print(now.strftime("%Y-%m-%d %H:%M"))
print(project_dir)
```

Savo projektą taip pat gali padalyti į kelis failus:

```text
assistant_project/
├── main.py
├── text_tools.py
└── knowledge.py
```

`text_tools.py`:

```python
def normalize_text(text: str) -> str:
    return " ".join(text.strip().lower().split())
```

`main.py`:

```python
from text_tools import normalize_text

def main():
    message = input("Tu: ")
    print(normalize_text(message))

if __name__ == "__main__":
    main()
```

Paskutinė sąlyga paleidžia `main()` tik tada, kai failas vykdomas tiesiogiai (`python main.py`). Importuojant `main.py` iš kito failo – pavyzdžiui, testų – ši sąlyga `False`, todėl dialogas savaime neprasidės ir funkcijas galima saugiai išbandyti be `input()`.

Kai modulis auga, verta paaiškinti kiekvienos funkcijos sutartį – ką ji priima ir ką grąžina – trumpu docstring:

```python
def calculate_discount(total: float, percent: float) -> float:
    """Grąžina sumą po procentinės nuolaidos."""
    return total * (1 - percent / 100)
```

Docstring skiriasi nuo paprasto komentaro `#` tuo, kad jį gali pamatyti bet kas, iškvietęs `help(calculate_discount)`, ir kad jis rodomas redaktoriaus paaiškinimuose kviečiant funkciją. Komentaras `#` reikalingas sprendimo *priežasčiai* paaiškinti, o ne akivaizdžiai eilutei perpasakoti.

> **Dažna klaida:** savo failą pavadinus taip pat, kaip standartinį modulį (pvz. `json.py` arba `random.py`), `import json` gali įkelti tavo failą vietoje standartinės bibliotekos – tai sukelia sunkiai suprantamas klaidas. Prieš pavadindamas naują failą, patikrink, ar toks vardas jau nenaudojamas Python bibliotekoje.

## 9. Įvairūs kodo pavyzdžiai

### Minimalus pavyzdys

**Problema:** apskaičiuoti kvadratą kelis kartus, nekartojant formulės.

```python
def square(number):
    return number ** 2

print(square(4))
print(square(9))
```

```text
16
81
```

**Paaiškinimas:** viena funkcija pakeičia kelis pasikartojančius skaičiavimus. **Patobulinimas:** pridėk tipų užuominas `number: float` ir `-> float`.

### Kasdienis pavyzdys – kelionės laiko funkcija

```python
def travel_time(distance_km: float, average_speed: float) -> float:
    return distance_km / average_speed

print(travel_time(120, 80))
```

```text
1.5
```

**Patobulinimas:** pridėk numatytąjį `average_speed=80`, kad dažniausią atvejį būtų galima iškviesti su vienu argumentu.

### Darbo pavyzdys – projekto pasiūlymo suma

```python
def calculate_quote(hours: float, hourly_rate: float, extra_costs: float = 0.0) -> float:
    """Grąžina bendrą projekto kainą kartu su papildomomis išlaidomis."""
    return hours * hourly_rate + extra_costs

print(calculate_quote(12.5, 40))
print(calculate_quote(5, 35, extra_costs=15))
```

```text
500.0
190.0
```

**Patobulinimas:** grąžink `tuple` `(darbo_kaina, bendra_suma)`, kad kvietimo vieta matytų abu skaičius atskirai.

### Automatizavimo pavyzdys – ta pati funkcija kelioms užduotims

```python
def minutes_saved(minutes_per_task: float, tasks_per_week: int) -> float:
    return minutes_per_task * tasks_per_week

email_savings = minutes_saved(12, 25)
report_savings = minutes_saved(30, 4)
print(f"El. laiškai: {email_savings} min., ataskaitos: {report_savings} min.")
```

```text
El. laiškai: 300 min., ataskaitos: 120 min.
```

**Patobulinimas:** parašyk funkciją `total_minutes(*savings)`, kuri sudėtų bet kokį kiekį atskirų sutaupytų minučių reikšmių.

### Duomenų ir AI pavyzdys – klasifikavimo rezultato formatavimas

```python
def format_ai_result(message: str, predicted_topic: str, confidence: float) -> str:
    """Suformuoja žmogui skaitomą DI klasifikavimo rezultato eilutę."""
    return f"'{message}' → tema: {predicted_topic} (pasitikėjimas {confidence:.0%})"

print(format_ai_result("Noriu pakeisti adresą", "pristatymas", 0.92))
```

```text
'Noriu pakeisti adresą' → tema: pristatymas (pasitikėjimas 92%)
```

**Patobulinimas:** pridėk parametrą `threshold: float = 0.5`, žemiau kurio tema pažymima kaip nepatikima.

### Klaidingas pavyzdys – pataisyk

```python
def calculate_total(price, quantity):
    price * quantity

result = calculate_total(10, 3)
print(f"Suma: {result}")
```

```text
Suma: None
```

Funkcija apskaičiuoja sandaugą, bet niekur jos negrąžina – rezultatas dingsta, o `result` tampa `None`.

Pataisymas:

```python
def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(10, 3)
print(f"Suma: {result}")
```

```text
Suma: 30
```

## 10. Interaktyvios veiklos

### 1. Nuspėk rezultatą

```python
def add_bonus(total, bonus=5):
    return total + bonus

print(add_bonus(10))
```

A. `10`
B. `15`
C. Klaida, nes trūksta antro argumento
D. `None`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** `bonus` nenurodytas, todėl naudojama numatytoji reikšmė `5`, ir funkcija grąžina `10 + 5 = 15`.

</details>

### 2. Užpildyk trūkstamą kodą

```python
def shout(text):
    ____ text.upper()

print(shout("labas"))
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
return text.upper()
```

Be `return` funkcija grąžintų `None`, o `print(shout("labas"))` parodytų `None` vietoje `"LABAS"`.

</details>

### 3. Surask klaidą

```python
def calculate_total(price, quantity)
    return price * quantity
```

Nustatyk klaidą, paaiškink ir pataisyk.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Po parametrų sąrašo trūksta dvitaškio – tai `SyntaxError`.

```python
def calculate_total(price, quantity):
    return price * quantity
```

</details>

### 4. Sudėliok teisinga tvarka

```text
if __name__ == "__main__":
from text_tools import normalize_text
    main()
def main():
    print(normalize_text(input("Tu: ")))
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
from text_tools import normalize_text

def main():
    print(normalize_text(input("Tu: ")))

if __name__ == "__main__":
    main()
```

Pirma importuojama funkcija, tada apibrėžiama `main()`, o `if __name__ == "__main__":` su kvietimu `main()` visada rašomas paskiausiai.

</details>

### 5. Pasirink tinkamą sprendimą

Reikia funkcijos, kuri apskaičiuotų kainą su nuolaida, bet leistų neprivalomai nurodyti valiutą. Kuris variantas tinkamas ir teisingas sintaksiškai?

A. `def calculate_price(total, percent, currency):`
B. `def calculate_price(total, percent, currency="Eur"):`
C. `def calculate_price(total, currency="Eur", percent):`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Numatytasis argumentas `currency="Eur"` eina po privalomų `total` ir `percent`. Variantas **C** sukeltų `SyntaxError`, nes numatytasis argumentas negali eiti prieš privalomą.

</details>

### 6. Parašyk pats

Parašyk funkciją `is_valid_hours(hours)`, kuri grąžina `True`, jei valandų skaičius yra teigiamas skaičius, ir `False` priešingu atveju. Iškviesk ją su keliomis skirtingomis reikšmėmis, įskaitant `0` ir neigiamą skaičių.

### 7. Patobulink kodą

```python
message_1 = "  Ačiū už PASLAUGĄ!!  "
result_1 = message_1.strip().lower().replace("!", "")
print(result_1)

message_2 = "  Kada KITA pamoka???  "
result_2 = message_2.strip().lower().replace("?", "")
print(result_2)
```

Pakeisk kodą taip, kad abi žinutės būtų valomos ta pačia funkcija, o ne pasikartojančiu kodu.

<details class="selfcheck" markdown="1"><summary>Rodyti vieną galimą sprendimą</summary>

```python
def normalize_text(text):
    return text.strip().lower().replace("!", "").replace("?", "")

print(normalize_text("  Ačiū už PASLAUGĄ!!  "))
print(normalize_text("  Kada KITA pamoka???  "))
```

</details>

## 11. Žinių patikrinimas prieš platformos testą

Pirmiausia atsakyk neužleisdamas atsakymų.

1. Kur funkcijos apibrėžime turi būti rašomi numatytieji (default) argumentai – prieš privalomus parametrus ar po jų?
2. Ar tipo užuomina `def get_price(amount: float) -> float:` privers Python atmesti sveikąjį skaičių kaip argumentą?
3. Kas atsitiks, jei funkcijos viduje kintamajam priskirsi reikšmę tuo pačiu vardu kaip globalus kintamasis, bet nenaudosi `global`?
4. Kaip importuoti tik vieną konkrečią funkciją iš modulio `text_tools.py`, o ne visą modulį?
5. Kodėl du moduliai neturėtų importuoti vienas kito (apskritiminis importas)?
6. Kokia rizika slypi funkcijoje `def add_entry(entry, history=[]):`, kai ji kviečiama kelis kartus?
7. Kuo docstring naudingesnis už paprastą komentarą `#` prieš funkciją?
8. Kodėl funkcija `find_answer(message, knowledge_base)` neturėtų viduje kviesti `input()` ar `print()`?
9. Kas nutinka, kai parametrų sąraše prieš kitus parametrus parašai vien žvaigždutę `*`, pvz. `def make_summary(title, *, limit=80):`?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymus ir paaiškinimus</summary>

1. Po privalomų parametrų; priešingu atveju kiltų `SyntaxError`.
2. Ne – tipo užuomina yra tik dokumentacija ir pagalba redaktoriui, Python vykdymo metu tipo nepatikrina.
3. Python tą kintamąjį visoje funkcijoje laikys vietiniu, todėl bandymas jį perskaityti prieš priskyrimą sukels `UnboundLocalError`.
4. `from text_tools import normalize_text`.
5. Nes kiekvienas modulis bando įkelti kitą, kol tas dar nebaigtas įkelti – gaunama klaida arba nepilnas importas; bendrą dalį reikia iškelti į trečią modulį.
6. Numatytasis sąrašas sukuriamas tik vieną kartą, funkcijos apibrėžimo metu, ir dalinamas tarp visų kvietimų – įrašai kaupsis tarp tarpusavyje nesusijusių kvietimų.
7. Docstring pasiekiamas per `help()` ir rodomas redaktoriaus paaiškinimuose; jis aprašo sutartį, o ne tik paaiškina vieną eilutę.
8. Kad funkciją būtų galima testuoti be klaviatūros ir ekrano bei naudoti kitokioje sąsajoje (pvz. žiniatinklio serveryje) nekeičiant pačios logikos.
9. Visi po jos einantys parametrai tampa tik vardu (keyword-only) perduodami argumentai – jų nebegalima nurodyti pagal poziciją.

</details>

## 12. Praktinės užduotys

### A lygis – skaičiuoklių biblioteka

**Sąlyga:** parašyk keturias funkcijas: `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)`. Dalijant iš nulio `divide` turi grąžinti `None`, o ne sukelti klaidą. Sukurk atskirą `main.py`, kuris šias funkcijas importuoja iš `calculator.py` ir jas išbando.
**Pavyzdinė įvestis:** `add(6, 3)`, `divide(10, 0)`, `divide(9, 3)`.
**Laukiamas rezultatas:** `9`, `None`, `3.0`.
**Užuomina:** dalybos funkcijoje pirmiausia patikrink, ar antrasis argumentas lygus nuliui, ir tik tada dalyk.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

`calculator.py`:

```python
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b
```

`main.py`:

```python
from calculator import add, subtract, multiply, divide

print(add(6, 3))
print(subtract(10, 4))
print(multiply(2.5, 4))
print(divide(10, 0))
print(divide(9, 3))
```

```text
9
6
10.0
None
3.0
```

**Papildomas iššūkis:** pridėk funkciją `power(base, exponent=2)`, kuri be antro argumento skaičiuoja kvadratą.

</details>

### B lygis – teksto įrankiai

**Sąlyga:** sukurk `normalize_text(text)`, `count_words(text)`, `shorten_text(text, limit=50)`, `contains_any(text, keywords)`. Kiekvienai funkcijai pateik po 4 bandymus: įprastą, ribinį, tuščią ir netikėtą atvejį.
**Pavyzdinė įvestis:** `normalize_text("  Labas PASAULI!  ")`.
**Laukiamas rezultatas:** `"labas pasauli!"`.
**Užuomina:** `shorten_text` turi tikrinti, ar tekstas jau trumpesnis už `limit`, prieš jį trumpindama.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
def normalize_text(text: str) -> str:
    return " ".join(text.strip().lower().split())

def count_words(text: str) -> int:
    normalized = normalize_text(text)
    if not normalized:
        return 0
    return len(normalized.split())

def shorten_text(text: str, limit: int = 50) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."

def contains_any(text: str, keywords: list[str]) -> bool:
    normalized = normalize_text(text)
    return any(keyword in normalized for keyword in keywords)


print(normalize_text("  Labas PASAULI!  "))
print(normalize_text(""))
print(count_words("Python yra   smagus"))
print(count_words(""))
print(shorten_text("Trumpas tekstas"))
print(shorten_text("Tai yra ilgas sakinys, kurį reikės sutrumpinti", limit=10))
print(contains_any("Kokia kaina?", ["kaina", "kontaktai"]))
print(contains_any("Sveiki visi", ["kaina", "kontaktai"]))
```

```text
labas pasauli!

3
0
Trumpas tekstas
Tai yra il...
True
False
```

**Papildomas iššūkis:** parašyk `highlight_keyword(text, keyword)`, kuri rastą raktažodį apgaubia žvaigždutėmis, pvz. `*kaina*`.

</details>

### C lygis – asistento architektūra

**Sąlyga:** išskirk funkcijas `get_command`, `find_topic`, `build_answer`, `save_turn`, `show_history`, `main`. Nė viena funkcija, išskyrus `main`, neturi tiesiogiai kviesti `input()` ar `print()`.
**Pavyzdinė įvestis (dialogas):**

```text
Tu: /help
Tu: Kokia kaina?
Tu: /quit
```

**Laukiamas rezultatas:**

```text
Komandos: /help, /history, /quit.
Asistentas: Kaina priklauso nuo pasirinkto paketo.
Iki!
```

**Užuomina:** `get_command` turi grąžinti komandos vardą be `/`, jei žinutė prasideda `/`, kitaip – `None`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
HELP_TEXT = "Komandos: /help, /history, /quit."

def get_command(raw_message: str) -> str | None:
    cleaned = raw_message.strip().lower()
    if cleaned.startswith("/"):
        return cleaned[1:]
    return None

def find_topic(message: str, knowledge_base: dict) -> str | None:
    for topic_name, topic_data in knowledge_base.items():
        if any(keyword in message for keyword in topic_data["keywords"]):
            return topic_name
    return None

def build_answer(topic_name: str | None, knowledge_base: dict) -> str:
    if topic_name is None:
        return "Atsakymo žinių bazėje neradau."
    return knowledge_base[topic_name]["answer"]

def save_turn(history: list, question: str, answer: str) -> list:
    history.append({"question": question, "answer": answer})
    return history

def show_history(history: list) -> str:
    if not history:
        return "Istorija dar tuščia."
    lines = [f"{i}. {t['question']} → {t['answer']}" for i, t in enumerate(history, start=1)]
    return "\n".join(lines)

def main() -> None:
    knowledge_base = {
        "kaina": {"keywords": ["kaina"], "answer": "Kaina priklauso nuo pasirinkto paketo."},
    }
    history = []
    raw_message = input("Tu: ")
    if get_command(raw_message) == "help":
        print(HELP_TEXT)
    else:
        topic_name = find_topic(raw_message.strip().lower(), knowledge_base)
        answer = build_answer(topic_name, knowledge_base)
        print(f"Asistentas: {answer}")
        save_turn(history, raw_message, answer)

if __name__ == "__main__":
    main()
```

Ši struktūra – atskiros, testuojamos funkcijos ir plonas `main()` orkestratorius – yra tiesioginis pagrindas Asistento 0.4 mini projektui.

</details>

## 13. Mini projektas: Asistentas 0.4

### 1. Projekto situacija

Asistento 0.3 kodas veikė, bet visa logika buvo sugrūsta į vieną ilgą `while` ciklą su pasikartojančiu teksto valymu ir įterptomis `if` sąlygomis. Norint pridėti naują funkciją ar ją išbandyti, tekdavo skaityti visą failą nuo pradžios iki galo.

### 2. Galutinis tikslas

Perrašyti Asistentą taip, kad jo logika būtų padalyta į keturis modulius su aiškiomis atsakomybėmis, o `main.py` liktų tik plonas paleidimo taškas.

### 3. Funkciniai reikalavimai

Rekomenduojama struktūra:

```text
assistant_v04/
├── main.py
├── assistant_core.py
├── knowledge.py
└── text_tools.py
```

`assistant_core.py` šerdis:

```python
def find_answer(message: str, knowledge_base: dict) -> tuple[str, str | None]:
    for topic_name, topic in knowledge_base.items():
        if any(keyword in message for keyword in topic["keywords"]):
            return topic["answer"], topic_name
    return "Atsakymo dar nežinau.", None
```

`any(...)` grąžina `True`, jei bent viena vidinė sąlyga teisinga. Jei ši trumpa forma dar neaiški, naudok įprastą vidinį `for` – skaitomumas svarbiau už trumpumą.

**Baigimo kriterijai:**

- programa paleidžiama tik iš `main.py`;
- dialogas turi `/help`, `/history`, `/quit`;
- teksto valymas vyksta vienoje funkcijoje;
- atsakymo paieška neturi `input()` ar `print()`;
- bent 5 funkcijos turi tipų užuominas ir docstring;
- pakeitus žinių bazę nereikia keisti paieškos funkcijos.

### 4. Pavyzdinė sąveika

```text
Sveikas! Aš – mokymosi asistentas. Įrašyk /help, jei reikia pagalbos.
Tu: /help
Komandos: /help, /history, /quit. Kitu atveju užduok klausimą.
Tu: Kokia kaina?
Asistentas: Kaina priklauso nuo pasirinkto paketo, žr. kainoraštį. (tema: kaina)
Tu: /history
1. Tu: Kokia kaina?
   Asistentas: Kaina priklauso nuo pasirinkto paketo, žr. kainoraštį.
Tu: /quit
Iki!
```

### 5. Pavyzdinis rezultatas

Programa paleista be `input()` pakeitimų grąžina tuos pačius atsakymų tekstus kaip Asistentas 0.3, tačiau kiekvieną žingsnį – komandos atpažinimą, paiešką, atsakymo formavimą, istorijos saugojimą – atlieka atskira, savarankiškai testuojama funkcija.

### 6. Projekto kūrimo etapai

1. Sukurk keturis tuščius failus pagal rekomenduojamą struktūrą.
2. Į `knowledge.py` perkelk žinių bazės žodyną iš Asistento 0.3.
3. Į `text_tools.py` perkelk teksto valymo funkciją.
4. Į `assistant_core.py` parašyk `find_answer`, `format_reply`, `get_command`, `save_turn`, `show_history`.
5. `main.py` importuok visas reikalingas funkcijas ir sudėk `while` ciklą, kuris tik kviečia funkcijas.
6. Pridėk `if __name__ == "__main__":` apsaugą.
7. Paleisk 10 žinučių testų lentelę iš Asistento 0.3 ir palygink atsakymus.
8. Patikrink, ar visi Baigimo kriterijai įvykdyti.

### 7. Pseudokodas

```text
ĮKELK žinių bazę iš knowledge.py
PALEISK begalinį ciklą:
    GAUK vartotojo žinutę
    JEI žinutė yra komanda:
        ATLIK komandą (/help, /history, /quit)
    KITAIP:
        IŠVALYK žinutę
        SURASK atsakymą ir temą (find_answer)
        SUFORMUOK atsakymo eilutę (format_reply)
        PARODYK atsakymą
        IŠSAUGOK pokalbio įrašą (save_turn)
```

> **Užuomina:** jei paleidus `main.py` gauni `ModuleNotFoundError`, patikrink, ar visi keturi failai yra tame pačiame aplanke ir ar paleidi komandą iš to paties aplanko.

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

`knowledge.py`:

```python
"""Asistento žinių bazė – tik duomenys, jokios logikos."""

KNOWLEDGE_BASE = {
    "kursas": {
        "keywords": ["kursas", "mokymai", "programa"],
        "answer": "Programa trunka 88 akademines valandas.",
    },
    "kontaktai": {
        "keywords": ["kontaktai", "paštas", "telefonas"],
        "answer": "Rašykite mokymai@example.lt.",
    },
    "kaina": {
        "keywords": ["kaina", "kainuoja", "moketi"],
        "answer": "Kaina priklauso nuo pasirinkto paketo, žr. kainoraštį.",
    },
}
```

`text_tools.py`:

```python
"""Teksto valymo pagalbinės funkcijos."""

def normalize_text(text: str) -> str:
    """Grąžina sutvarkytą tekstą: be kraštinių tarpų, mažosiomis raidėmis."""
    return " ".join(text.strip().lower().split())


if __name__ == "__main__":
    print(normalize_text("  Kokia KAINA?! "))
```

`assistant_core.py`:

```python
"""Asistento sprendimų logika – jokio input() ar print() čia nėra."""

def find_answer(message: str, knowledge_base: dict) -> tuple[str, str | None]:
    for topic_name, topic in knowledge_base.items():
        if any(keyword in message for keyword in topic["keywords"]):
            return topic["answer"], topic_name
    return "Atsakymo dar nežinau.", None


def format_reply(answer: str, topic_name: str | None = None) -> str:
    """Suformuoja atsakymo eilutę, papildomai nurodydama rastą temą."""
    if topic_name:
        return f"{answer} (tema: {topic_name})"
    return answer


def get_command(raw_message: str) -> str | None:
    """Grąžina komandos vardą (be '/'), jei žinutė yra komanda, kitaip None."""
    cleaned = raw_message.strip().lower()
    if cleaned.startswith("/"):
        return cleaned[1:]
    return None


def save_turn(history: list, question: str, answer: str, topic_name: str | None) -> list:
    """Prideda vieną pokalbio įrašą į istorijos sąrašą ir jį grąžina."""
    history.append({"question": question, "answer": answer, "topic": topic_name})
    return history


def show_history(history: list) -> str:
    """Suformuoja visos pokalbio istorijos tekstinę santrauką."""
    if not history:
        return "Istorija dar tuščia."
    lines = []
    for index, turn in enumerate(history, start=1):
        lines.append(f"{index}. Tu: {turn['question']}")
        lines.append(f"   Asistentas: {turn['answer']}")
    return "\n".join(lines)
```

`main.py`:

```python
"""Asistentas 0.4 – paleidimo taškas, jungiantis visus modulius."""

from assistant_core import find_answer, format_reply, get_command, save_turn, show_history
from knowledge import KNOWLEDGE_BASE
from text_tools import normalize_text

HELP_TEXT = "Komandos: /help, /history, /quit. Kitu atveju užduok klausimą."


def main() -> None:
    history = []
    print("Sveikas! Aš – mokymosi asistentas. Įrašyk /help, jei reikia pagalbos.")

    while True:
        raw_message = input("Tu: ")
        command = get_command(raw_message)

        if command == "quit":
            print("Iki!")
            break
        if command == "help":
            print(HELP_TEXT)
            continue
        if command == "history":
            print(show_history(history))
            continue

        cleaned_message = normalize_text(raw_message)
        answer, topic_name = find_answer(cleaned_message, KNOWLEDGE_BASE)
        reply = format_reply(answer, topic_name)
        print(f"Asistentas: {reply}")
        save_turn(history, raw_message, answer, topic_name)


if __name__ == "__main__":
    main()
```

Penkios funkcijos (`find_answer`, `format_reply`, `get_command`, `save_turn`, `show_history`) turi tipų užuominas ir docstring, `find_answer` neturi jokio `input()` ar `print()`, o žinių bazės pakeitimai `knowledge.py` faile nereikalauja liesti `assistant_core.py`.

</details>

### 8. Galimi patobulinimai

- pridėk komandą `/topics`, kuri parodo visų žinomų temų sąrašą;
- `format_reply` papildyk parametru, kuris valdo, ar rodyti temą;
- `find_answer` papildyk paprastu reitingavimu, jei sutampa keli raktažodžiai;
- perkelk `HELP_TEXT` bei kitas pastovias eilutes į atskirą `messages.py` modulį;
- parašyk atskirą testų failą, kuris iškviečia kiekvieną `assistant_core.py` funkciją be `input()`.

### 9. `README.md` šablonas

```text
# Asistentas 0.4

Modulinė mokymosi asistento versija: kodas išskaidytas į main.py,
assistant_core.py, knowledge.py ir text_tools.py.

## Moduliai
- main.py – paleidimo taškas ir dialogo ciklas
- assistant_core.py – paieškos ir atsakymo logika (be input()/print())
- knowledge.py – žinių bazės duomenys
- text_tools.py – teksto valymo funkcijos

## Komandos
/help, /history, /quit

## Paleidimas
python3 main.py

## Ką išmokau
Funkcijos, parametrai, return, numatytieji argumentai, tipų užuominos,
sritis (local/global), moduliai, importai, docstring.

## Tolimesni patobulinimai
/topics komanda, atsakymų reitingavimas, atskiras testų failas.
```

## 14. Gilioji laboratorija: funkcijos kaip sutartys

Asistento 0.4 funkcijos kol kas priima paprastus argumentus pagal poziciją. Realiame projekte dažnai reikia griežtesnės sutarties – kad argumentai būtų aiškiai pavadinti, o funkcija nepriimtų bet ko. Ši laboratorija pagilina tris temas: vardinius argumentus, `*args`/`**kwargs` ir modulio testavimą – bei baigiasi kontroliniu refaktoringo tašku, kuris tiesiogiai sujungia šią pamoką su Asistento 0.3 kodu.

### Poziciniai ir vardiniai argumentai

```python
def make_summary(title: str, *, limit: int = 80, include_source: bool = True) -> str:
    text = title[:limit]
    return f"{text} (šaltinis pridėtas: {include_source})"

print(make_summary("Python kursas", include_source=False))
```

Žvaigždutė reiškia, kad `limit` ir `include_source` perduodami vardu. Tai apsaugo nuo argumentų sumaišymo. Kiekvienai funkcijai užrašyk normalų, ribinį ir blogos įvesties atvejį.

### `*args` ir `**kwargs` tik tada, kai tikrai reikia

```python
def join_keywords(*keywords: str, separator: str = ", ") -> str:
    return separator.join(keyword.strip().lower() for keyword in keywords)

print(join_keywords("Python", " API ", "Testai"))
```

`*args` patogu kintamam raktažodžių skaičiui, tačiau žinių bazės įrašui dažnai aiškesnis `list[str]` parametras. Profesionali funkcija turi aiškią sutartį, o ne priima viską.

### Modulio importo laboratorija

Sukurk `text_tools.py` ir `test_text_tools.py`. Į modulį įdėk tik funkcijas, o demonstracinį `print()` – po `if __name__ == "__main__"`. Importuok modulį iš testo ir įrodyk, kad importas nesukelia dialogo. Jei gauni `ModuleNotFoundError`, patikrink, iš kur paleidi komandą ir ar failai yra tame pačiame projekte.

```python
# test_text_tools.py
from text_tools import normalize_text

def test_normalize_removes_extra_spaces():
    assert normalize_text("  Labas   PASAULI  ") == "labas pasauli"

def test_normalize_handles_empty_string():
    assert normalize_text("") == ""

test_normalize_removes_extra_spaces()
test_normalize_handles_empty_string()
print("Visi testai praėjo.")
```

### Refaktoringo kontrolinis taškas

Nukopijuok Asistento 0.3 ilgą `if` grandinę, išskirk funkcijas nekeičiant elgesio ir paleisk tą pačią 10 žinučių testų lentelę. Baigta, jei rezultatų tekstai nesikeitė, o `main()` liko tik įvesties, funkcijų kvietimo ir išvesties orkestratorius.

## 15. Dažnos klaidos

| Klaida | Kodėl ji atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| Funkcija nieko negrąžina | Trūksta `return`, todėl rezultatas – `None` | `def add(a, b): a + b` | `def add(a, b): return a + b` | Po kiekvienos naujos funkcijos patikrink, ar reikia `return` |
| Ankstyvas `return` cikle | `return` parašytas per anksti, patikrinamas tik pirmas elementas | `return` po pirmos iteracijos be tinkamos sąlygos | `return` perkeltas už ciklo arba į teisingą įtraukimo lygį | Išbandyk su keliais skirtingais įrašais, ne tik pirmu |
| Modulio vardas sutampa su standartiniu | Failas pavadintas kaip biblioteka, pvz. `json.py` | `json.py` savo projekte | `my_json_tools.py` | Prieš pavadindamas patikrink, ar toks modulis jau egzistuoja standartinėje bibliotekoje |
| Apskritiminiai importai | Du moduliai importuoja vienas kitą | `a.py` importuoja `b.py`, o `b.py` – `a.py` | Bendrą dalį iškelk į trečią modulį | Prieš rašydamas `import`, nubraižyk modulių priklausomybių schemą |
| Visa programa vienoje funkcijoje | `main()` atlieka viską – įvestį, logiką, išvestį | 80 eilučių viename `main()` | Logika iškelta į atskiras funkcijas, `main()` tik orkestruoja | Kiekvienai naujai atsakomybei kurk atskirą funkciją |
| Kintamas numatytasis argumentas | Numatytoji reikšmė sukuriama tik kartą ir dalinama tarp kvietimų | `def add(entry, history=[]):` | `def add(entry, history=None): history = history or []` | Kintamiems tipams numatytuoju argumentu naudok `None` |
| `UnboundLocalError` | Funkcijoje priskiriama globaliam vardui be `global` | `def increment(): counter = counter + 1` | Perduok `counter` parametru ir grąžink naują reikšmę | Verčiau naudok parametrus ir `return`, nei `global` |
| Pamirštas `if __name__` apsauga | Importuojant modulį testams automatiškai paleidžiamas dialogas | `main()` kviečiamas modulio lygyje | `main()` kviečiamas tik po `if __name__ == "__main__":` | Demonstracinį paleidimo kodą visada dėk už šios sąlygos |

## 16. Profesionali praktika

- Funkcijų vardai – veiksmažodžiai arba veiksmažodinės frazės: `find_topic`, `save_turn`, ne `data1`.
- Viena funkcija – viena atsakomybė; jei sakinys su „ir“ apibūdina jos veikimą, tikriausiai reikia dviejų funkcijų.
- Docstring rašyk funkcijoms, kurių sutartis nėra akivaizdi iš vardo ir parametrų.
- Tipų užuominos naudingiausios viešoms funkcijų sutartims – ypač toms, kurias importuos kitas modulis.
- Venk keisti globalią būseną iš funkcijos vidaus; verčiau priimk parametrus ir grąžink rezultatą.
- `main()` laikyk plonu – jis turi tik kviesti kitas funkcijas, ne pats atlikti visą logiką.
- Rašyk grynas (be šalutinio poveikio) funkcijas visur, kur tai įmanoma – jas lengviausia testuoti.
- Organizuok failus pagal atsakomybę: duomenys, logika ir paleidimas – atskiruose moduliuose.

## 17. Kodėl tai svarbu mokantis AI?

DI programose kodas greitai išauga: reikia nuskaityti duomenis, paruošti juos modeliui, suformuoti užklausą, iškviesti API ir apdoroti atsakymą. Jei visa tai liktų viename faile, kiekvieną pakeitimą – pvz. naują duomenų šaltinį ar kitą modelį – tektų ieškoti per šimtus eilučių. Funkcijos ir moduliai leidžia kiekvieną žingsnį apibrėžti atskirai ir testuoti jį be tikro API kvietimo.

```python
def load_config() -> dict:
    """Grąžina programos nustatymus (imituota, be tikro failo)."""
    return {"model": "demo-model", "max_tokens": 200}


def build_prompt(message: str, context: str) -> str:
    """Sujungia vartotojo žinutę su kontekstu į vieną užklausą."""
    return f"Kontekstas: {context}\nKlausimas: {message}"


def call_model(prompt: str) -> str:
    """Vietoje tikro API kvietimo – imituotas atsakymas mokymuisi."""
    return f"[imituotas atsakymas į: {prompt[:30]}...]"


def format_ai_reply(raw_response: str) -> str:
    """Paruošia modelio atsakymą rodymui vartotojui."""
    return raw_response.strip()


config = load_config()
prompt = build_prompt("Kiek trunka kursas?", "Kurso programa: 88 val.")
raw_response = call_model(prompt)
print(format_ai_reply(raw_response))
```

```text
[imituotas atsakymas į: Kontekstas: Kurso programa: 8...]
```

Čia nėra tikro DI modelio – tik jo galimo iškvietimo struktūra. Kiekviena funkcija atsako už vieną žingsnį: nustatymus, užklausos formavimą, „iškvietimą“ ir atsakymo paruošimą. Vėlesnėse pamokose `call_model` taps tikru API kvietimu, tačiau likusios funkcijos ir jų sutartys išliks tos pačios – tai ir yra funkcijų bei modulių nauda.

## 18. Pamokos santrauka

- Funkcija – pavadintas, pakartotinai kviečiamas veiksmų blokas su parametrais ir `return`.
- Parametras yra vardas apibrėžime, argumentas – konkreti reikšmė kvietime.
- `return` grąžina rezultatą kvietimo vietai; `print()` tik parodo ekrane.
- Numatytieji argumentai eina po privalomų; kintamų tipų numatytuoju argumentu naudok `None`.
- Tipo užuomina padeda skaitytojui, bet nepriverčia Python tikrinti tipo vykdymo metu.
- Vietinis kintamasis egzistuoja tik funkcijos viduje; globalios būsenos keitimą geriau pakeisti parametrais ir `return`.
- Modulis – atskiras `.py` failas, kurio funkcijas gali importuoti kitas failas su `import`.
- `if __name__ == "__main__":` leidžia importuoti modulį netaikant jo paleidimo logikos.
- Docstring aprašo funkcijos sutartį – ką ji priima ir ką grąžina.

**Atmintinė:**

```python
def find_answer(message: str, knowledge_base: dict) -> tuple[str, str | None]:
    """Suranda atsakymą pagal raktažodžius, negrąžina jokios rodymo logikos."""
    for topic_name, topic in knowledge_base.items():
        if any(keyword in message for keyword in topic["keywords"]):
            return topic["answer"], topic_name
    return "Atsakymo dar nežinau.", None


def main() -> None:
    message = input("Tu: ")
    answer, topic_name = find_answer(message.lower(), {})
    print(answer)


if __name__ == "__main__":
    main()
```

Vienu sakiniu: **aiškiai pavadintos funkcijos su tvarkinga sutartimi ir savo moduliu paverčia augantį kodą programa, kurią lengva skaityti, testuoti ir plėsti.**

## 19. Savirefleksija

1. Kurią Asistento 0.3 kodo dalį buvo lengviausia perkelti į atskirą funkciją, o kurią – sunkiausia?
2. Ar galėčiau paaiškinti kolegai, kodėl `find_answer` neturi kviesti `input()` ar `print()`?
3. Kur mano kode iki šiol kito kintamasis, kuris turėjo likti tik vietinis?
4. Kuris naujas terminas (parametras, sritis, modulis, docstring) man vis dar mažiausiai aiškus?
5. Kaip funkcijos ir moduliai palengvins man dirbti su didesniu projektu ateityje?

## 20. Namų darbas

### Privaloma – užbaik Asistentą 0.4

Užbaik Asistentą 0.4 pagal visus šeši Baigimo kriterijus (žr. mini projekto skyrių). Kiekvienai grynajai funkcijai (be šalutinio poveikio, pvz. `find_answer`, `format_reply`, `get_command`) parašyk po tris numatomo rezultato pavyzdžius – po vieną komentarą su įvestimi ir laukiamu rezultatu prieš kiekvieną kvietimą.

**Vertinimas (10 taškų):** visi keturi failai ir tinkama struktūra – 3; visi Baigimo kriterijai įvykdyti – 3; tipų užuominos ir docstring bent 5 funkcijoms – 2; po tris pavyzdžius kiekvienai grynajai funkcijai – 2.

### Pasirenkama – `/topics` komanda

Pridėk komandą `/topics`, kuri importuota iš `assistant_core.py` funkcija grąžina visų žinių bazės temų sąrašą tekstu, o `main.py` jį tik parodo.

**Vertinimas (5 taškai):** nauja funkcija be `input()`/`print()` – 2; teisingas rezultatas – 2; tvarkingas importas – 1.

### Kūrybinis iššūkis – tavo srities biblioteka

Sukurk savo modulį (pvz. `recipe_tools.py`, `budget_tools.py` ar `training_tools.py`) su bent keturiomis funkcijomis, iš kurių bent viena turi numatytąjį argumentą, o bent viena – tipo užuomina `-> tuple`. Parašyk atskirą `main.py`, kuris jas importuoja ir išbando.

**Vertinimas (5 taškai):** reali, nuosekli tema – 1; bent keturios funkcijos su aiškiomis atsakomybėmis – 2; numatytasis argumentas ir `tuple` grąžinimas – 1; tvarkingas `main.py` su importais – 1.

## 21. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Įžanga, pagrindinės sąvokos ir vizualizacijos | 35 min. | Akcentuoti skirtumą tarp funkcijos apibrėžimo ir iškvietimo |
| Funkcijos apibrėžimas: parametrai ir `return` | 40 min. | Dažniausia klaida – `print()` vietoje `return` |
| Viena atsakomybė, pavadinimai, ankstyvas `return` | 35 min. | Parodyti klaidingą `find_topic_buggy` pavyzdį gyvai |
| Numatytieji argumentai ir tipų užuominos | 30 min. | Būtinai parodyti kintamo numatytojo argumento spąstą |
| Sritis: local vs global | 30 min. | `UnboundLocalError` demonstruoti realiu paleidimu, ne tik teorija |
| Moduliai, importai, `if __name__`, docstring | 45 min. | Kiekvienam mokiniui – atskiras aplankas su keliais failais |
| Kodo pavyzdžių galerija ir interaktyvios veiklos | 45 min. | Aktyvumas 4 (sudėliojimas) dažnai užtrunka ilgiausiai |
| Žinių patikrinimas prieš testą | 20 min. | Fiksuoti, kurie klausimai renka daugiausiai klaidingų atsakymų |
| Praktinės užduotys trimis lygiais | 60 min. | B lygio 4 funkcijas tikrinti automatiniais bandymais |
| Mini projektas: Asistentas 0.4 | 80 min. | Būtina patikrinti, ar `find_answer` neturi `input()`/`print()` |
| Gilioji laboratorija ir refaktoringo kontrolinis taškas | 60 min. | Palyginti Asistento 0.3 ir 0.4 atsakymus tose pačiose 10 žinučių |

Animacija labiausiai padėtų ties vizualizacija B (kvietimo vieta → funkcijos vidus → `return` atgal) ir vizualizacija C (moduliai importuoja vieni kitus). Interaktyvų Python redaktorių verta įterpti po kiekvienos core temos (4–8 skyriai), prie kintamo numatytojo argumento spąsto, prie `UnboundLocalError` pavyzdžio ir prie mini projekto. Platformoje verta fiksuoti atliktas mini užduotis, pirmą sėkmingai perrašytą funkciją be `return` klaidos, `Praktinių užduočių` lygių baigtumą, testo rezultatą, mini projekto Baigimo kriterijų atžymėjimą ir savirefleksijos pasirinkimus – tai padės pastebėti, ar mokiniai realiai perkėlė Asistento 0.3 logiką į funkcijas, ar tik nukopijavo sprendimą.
