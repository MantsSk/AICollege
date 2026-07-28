---
title: Tekstas ir žodynai – tvarkinga asistento žinių bazė
module: Python pagrindai
order: 4
---

# Tekstas ir žodynai – tvarkinga asistento žinių bazė

> **Trukmė:** 8 akademinės valandos. Pamokos rezultatas – raktiniais žodžiais valdoma žinių bazė.

## Trumpa anotacija

Ši pamoka tęsia Asistento kūrimą. Ankstesnėse pamokose jis jau mokėjo kalbėti ciklu ir prisiminti klausimus sąraše, tačiau atsakymus rinkosi iš vis ilgėjančios `if`/`elif` grandinės – kiekvienai naujai temai reikėjo naujos kodo eilutės. Šioje pamokoje išmoksi tvarkyti tekstą teksto metodais (`.strip()`, `.lower()`, `.replace()`, `.split()`, `.join()`, `.find()`, `.startswith()`) ir saugoti prasmingus duomenis žodyne (`dict`). Šias dvi temas sujungsi į žinių bazę – struktūrą, kurioje kiekviena tema turi savo raktažodžius ir atsakymą, o paieška vyksta ciklu per duomenis, o ne per kodo šakas. Rezultatas – Asistentas 0.3, kurio žinias gali papildyti nekeisdamas paieškos logikos.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- išvalyti ir normalizuoti vartotojo įvestą tekstą naudodamas `.strip()`, `.lower()` ir `.replace()`;
- skaidyti tekstą į dalis su `.split()` ir vėl sujungti sąrašą į tekstą su `.join()`;
- naudoti teksto pjūvius (angl. *slicing*) bei `.find()` ir `.startswith()` konkrečiai teksto daliai rasti ar patikrinti;
- sukurti, skaityti ir atnaujinti žodyną (`dict`), saugiai naudojant `.get()` vietoj tiesioginio rakto kreipimosi;
- paaiškinti, kada kreipimasis į žodyną sukelia `KeyError`, ir kaip to išvengti;
- modeliuoti įdėtas struktūras – žodyną, kurio reikšmės yra kiti žodynai su sąrašais – realiai žinių bazei;
- parašyti paieškos ciklą, kuris raktažodžiais suranda tinkamą atsakymą, naudodamas `None` kaip „dar nerasta“ sentinelį;
- sukurti Asistentą 0.3 – dialogą, kuris atsakymus renka iš žinių bazės, o ne iš begalinės `if` grandinės.

## Būtinos ankstesnės žinios

Turėtum jau mokėti dirbti su sąrašais (`list`): pridėti, keisti ir pašalinti elementus, pereiti juos su `for`, kartoti dialogą su `while`, valdyti ciklo eigą su `break` ir `continue`. Turėtum turėti veikiantį Asistentą 0.2 iš trečios pamokos – dialogą, kuris kaupia klausimus sąraše `history` ir atsako pagal `if`/`elif` raktažodžių grandinę. Jei kuri nors iš šių temų neaiški, pasikartok trečią pamoką prieš tęsdamas – ši pamoka pakeis tos `if` grandinės logiką žodynu, o kitos pamokos jau rems šį naują variantą.

## 1. Įtraukianti pradžia: kai `if` grandinė tampa per ilga

Asistentas 0.2 mokėjo atsakyti į tris temas – kursą, kainą ir kontaktus. Įsivaizduok, kad realus produktas turi ne tris, o trisdešimt dažnai užduodamų klausimų temų. `if`/`elif` grandinė atrodytų maždaug taip:

```python
if "kursas" in message:
    answer = "Programa trunka 88 akademines valandas."
elif "kaina" in message:
    answer = "Dėl kainos kreipkis į koordinatorių."
elif "kontaktai" in message:
    answer = "Rašykite mokymai@example.lt."
elif "tvarkarastis" in message:
    answer = "Paskaitos vyksta antradieniais ir ketvirtadieniais."
# ... ir dar mažiausiai 26 panašios sąlygos
```

Kiekvieną kartą, kai reikia pakeisti vieną atsakymą ar pridėti naują temą, tenka redaguoti programos kodą – ne duomenis. Ilgą laiką prižiūrimoje sistemoje tai reiškia daugiau klaidų, sunkiau rasti konkrečią temą ir nepatogu ją testuoti atskirai nuo likusios logikos.

Realios sistemos – DUK puslapiai, palaikymo botai, paieškos varikliai – šią problemą sprendžia atskirdami **žinias** (temos, raktažodžiai, atsakymai) nuo **logikos** (kaip randamas tinkamas atsakymas). Žinios laikomos duomenų struktūroje, o kodas, kuris jas skaito, lieka nepakitęs, net kai temų padaugėja nuo trijų iki trisdešimt trijų.

Šioje pamokoje šitą `if`/`elif` grandinę pakeisi žodynu, kuriame kiekviena tema – atskiras įrašas, o nauja tema atsiranda pridėjus vieną žodyną, o ne dar vieną `elif` sakinį.

> **Išbandyk pats:** suskaičiuok, kiek kodo eilučių prireiktų tokiai `if`/`elif` grandinei su 30 temų, jeigu kiekvienai temai vidutiniškai reikia 3 eilučių. Tada pagalvok, kiek eilučių užimtų 30 panašių įrašų žodyne – ar skirtumas tave nustebino?

## 2. Pagrindinės sąvokos

### Teksto metodai ir pjūviai

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| `.strip()` | Pašalina tarpus (ir kitus tuščius simbolius) teksto kraštuose | Nuvalai suglamžytą etiketės kraštą | Prieš tikrinant ar saugant vartotojo įvestį | Manoma, kad pašalina tarpus ir viduryje teksto |
| `.lower()` | Grąžina tą patį tekstą mažosiomis raidėmis | Perrašai visus žodžius maža raide į sąrašą | Prieš lyginant tekstą, nepaisant registro | Rezultatas nepriskiriamas kintamajam, todėl atrodo, kad „neveikia“ |
| `.replace(a, b)` | Pakeičia visus `a` pasikartojimus į `b` | Korektūra – vieną žodį keiti kitu visame lape | Šalinant skyrybos ženklus ar taisant tekstą | Pakeičiama tik dalis atvejų, nes registras skiriasi |
| `.split()` | Suskaido tekstą į žodžių sąrašą pagal tarpus (ar nurodytą skirtuką) | Sakinį kertate į atskirus žodžius ant kortelių | Norint apdoroti kiekvieną žodį atskirai | Pamirštama, kad rezultatas yra sąrašas, ne tekstas |
| `" ".join(list)` | Sujungia sąrašo elementus į vieną tekstą su nurodytu skirtuku | Kortelės vėl sudedamos į vieną eilutę | Formuojant išvestį iš žodžių sąrašo | Bandoma sujungti elementus, kurie nėra tekstas |
| `.startswith(x)` | Patikrina, ar tekstas prasideda nurodyta dalimi | Tikrini, ar laiškas prasideda kreipiniu | Atpažįstant komandas, pvz. `/help` | Painiojama su `.find()` ar `in`, kai tikrinama bet kur, ne tik pradžioje |
| `.find(x)` | Grąžina pirmo pasikartojimo indeksą arba `-1`, jei nerasta | Ieškai žodžio puslapyje ir pažymi jo vietą | Kai reikia tikslios pozicijos tekste | Pamirštama, kad nerastas atvejis yra `-1`, o ne klaida |
| Pjūvis `tekstas[a:b]` | Ištraukia teksto dalį nuo indekso `a` iki `b` (neįtraukiant) | Kirpi juostelę tarp dviejų žymų | Kai reikia fiksuoto teksto fragmento (kodo, datos dalies) | Manoma, kad indeksas `b` taip pat įtraukiamas |

### Žodyno sąvokos

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| `dict` (žodynas) | Reikšmių rinkinys, kur kiekviena reikšmė pasiekiama pagal raktą | Adresų knygelė: vardas → adresas | Kai duomenis norima rasti pagal prasmingą vardą, ne poziciją | Manoma, kad raktai turi būti surikiuoti kaip sąraše |
| `žodynas[raktas]` | Tiesioginis kreipimasis į reikšmę pagal raktą | Ieškai adreso pagal tikslų vardą knygelėje | Kai esi tikras, kad raktas egzistuoja | Sukelia `KeyError`, jei rakto nėra |
| `.get(raktas, numatytoji)` | Saugus kreipimasis su atsargine reikšme | Klausi bibliotekininko – jei knygos nėra, gauni „nėra“, o ne skandalą | Kai raktas gali neegzistuoti | Pamirštama nurodyti antrą argumentą – tada, jei rakto nėra, grąžinamas `None` |
| `KeyError` | Klaida, kylanti kreipiantis į neegzistuojantį raktą | Ieškai adreso pagal vardą, kurio knygelėje nėra | Signalizuoja programuotojui apie neteisingą prielaidą | Bandoma šalinti pasekmes, o ne priežastį – naudok `.get()` |
| Įdėta struktūra | Žodynas, kurio reikšmės yra kiti žodynai ar sąrašai | Segtuvas su skyriais, kuriuose dar yra lapų sąrašai | Modeliuojant realius duomenis su keliais lygiais | Per daug lygių iš karto – sunku sekti, kuriame lygyje esi |
| `None` | Reikšmė, žyminti „reikšmės nėra“ | Tuščias langelis formoje, o ne nulis ar tuščias tekstas | Kai reikia aiškiai atskirti „nerasta“ nuo „sąmoningai tuščia“ | Painiojama su `False`, `0` ar tuščiu tekstu `""` |

Trumpas bendras pavyzdys, sujungiantis abi lenteles:

```python
raw_input = "  Kokia KURSO kaina?  "
message = raw_input.strip().lower()

prices = {"kursas": 890, "sertifikatas": 45}
print(prices.get("kursas", "nenurodyta"))
```

```text
890
```

`raw_input` išvaloma teksto metodais, o `prices` žodyne kaina ieškoma pagal raktą, ne poziciją.

## 3. Vizualūs paaiškinimai

### Vizualizacija A – teksto valymo konvejeris

```text
"  Noriu sužinoti KURSO kainą!  "
          │ .strip()
          ▼
"Noriu sužinoti KURSO kainą!"
          │ .lower()
          ▼
"noriu sužinoti kurso kainą!"
          │ .replace("!", "")
          ▼
"noriu sužinoti kurso kainą"
          │ .split()
          ▼
["noriu", "sužinoti", "kurso", "kainą"]
```

**Iliustracijos pavadinimas:** „Teksto valymo konvejeris“
**Ką ji turi parodyti:** kad kiekvienas teksto metodas paima ankstesnį rezultatą ir grąžina naują, žingsnis po žingsnio artėjant prie žodžių sąrašo.
**Kokie elementai turi būti matomi:** keturi teksto būsenos blokai vertikalioje sekoje, rodyklės tarp jų su metodo pavadinimu, paskutinis blokas pavaizduotas kaip sąrašas su kabutėmis aplink kiekvieną žodį.
**Siūlomas vaizdo generavimo promptas:** „Vertikali mokomoji proceso diagrama lietuvių kalba: teksto eilutė pereina per keturis etapus – strip, lower, replace, split – kiekvienas etapas atskirame stačiakampyje su rodykle žemyn ir metodo pavadinimu tarp blokų; paskutinis blokas pavaizduotas kaip žodžių sąrašas atskiruose langeliuose; aukštas kontrastas, aiškios etiketės.“

### Vizualizacija B – žodynas kaip pažymėtos dėžutės

```text
course = {
   "title"  : "Python ir DI asistentai"
   "hours"  : 88
   "online" : True
}

  RAKTAS            REIKŠMĖ
┌───────────┐      ┌──────────────────────────┐
│ "title"   │ ───► │ "Python ir DI asistentai" │
├───────────┤      ├──────────────────────────┤
│ "hours"   │ ───► │ 88                       │
├───────────┤      ├──────────────────────────┤
│ "online"  │ ───► │ True                     │
└───────────┘      └──────────────────────────┘
```

**Iliustracijos pavadinimas:** „Raktas veda į reikšmę“
**Ką ji turi parodyti:** kad žodyne kiekvienas raktas yra atskira rodyklė į savo reikšmę, o ne poziciją, kaip sąraše.
**Kokie elementai turi būti matomi:** trys raktų kortelės kairėje, trys reikšmių kortelės dešinėje, rodyklės tarp atitinkamų porų, skirtingos reikšmių spalvos pagal tipą (tekstas, skaičius, loginė reikšmė).
**Siūlomas vaizdo generavimo promptas:** „Minimalistinė edukacinė vektorinė schema lietuviškai: trys raktai title, hours, online kairėje pusėje rodyklėmis susieti su reikšmėmis Python ir DI asistentai, 88, True dešinėje; kiekviena pora kitos spalvos, aiškios etiketės, aukštas kontrastas.“

### Vizualizacija C – įdėta žinių bazės struktūra

```text
knowledge_base
 │
 ├── "kursas" ─────────────┐
 │                         ├── "keywords": ["kursas", "mokymai", "programa"]
 │                         └── "answer":   "Programa trunka 88 akademines valandas."
 │
 └── "kontaktai" ──────────┐
                           ├── "keywords": ["kontaktai", "paštas", "telefonas"]
                           └── "answer":   "Rašykite mokymai@example.lt."
```

**Iliustracijos pavadinimas:** „Žinių bazės medis“
**Ką ji turi parodyti:** kad `knowledge_base` yra žodynas, kurio kiekviena reikšmė – dar vienas žodynas su savo raktais `keywords` (sąrašas) ir `answer` (tekstas).
**Kokie elementai turi būti matomi:** šaknis `knowledge_base`, du šakos mazgai su temų pavadinimais, po du lapus prie kiekvienos šakos (`keywords` sąrašas ir `answer` tekstas), aiškios linijos tarp lygių.
**Siūlomas vaizdo generavimo promptas:** „Hierarchinė medžio diagrama lietuvių kalba: šaknis knowledge_base šakojasi į dvi temas kursas ir kontaktai, kiekviena tema turi du lapus keywords (sąrašas) ir answer (tekstas); naudoti tris hierarchijos lygius skirtingomis spalvomis, aiškios etiketės.“

## 4. Tekstas yra simbolių seka

Python'e tekstas (`str`) yra nekintamas (angl. *immutable*): kiekvienas teksto metodas grąžina naują reikšmę, o ne pakeičia esamą. Tai svarbu suprasti prieš pradedant valyti vartotojo įvestį.

```python
message = "  Noriu sužinoti KURSO kainą!  "
cleaned = message.strip().lower()
print(cleaned)
print(cleaned.split())
```

```text
noriu sužinoti kurso kainą!
['noriu', 'sužinoti', 'kurso', 'kainą!']
```

Eilutė po eilutės:

1. `message` saugo pradinę, „netvarkingą“ vartotojo įvestį – su tarpais kraštuose ir didžiosiomis raidėmis.
2. `.strip()` pašalina tarpus kraštuose, o iškart po to iškviestas `.lower()` paverčia raides mažosiomis. Metodai sujungti grandine (angl. *method chaining*): kiekvienas grąžina naują tekstą, su kuriuo iš karto galima dirbti toliau.
3. `cleaned` saugo galutinį, jau sutvarkytą tekstą – naują reikšmę, kuri nepakeičia `message`.
4. `cleaned.split()` suskaido tekstą pagal tarpus į žodžių sąrašą.

```python
words = cleaned.replace("!", "").split()
print(" | ".join(words))
```

```text
noriu | sužinoti | kurso | kainą
```

`.replace("!", "")` pakeičia šauktuką į tuščią tekstą – tai ir yra būdas simbolį „pašalinti“. `" ".join(words)` atlieka priešingą veiksmą nei `.split()`: sąrašą vėl sujungia į vieną tekstą su nurodytu skirtuku.

> **Dažna klaida:** tekstas yra nekintamas – metodai sukuria naują reikšmę, senosios nepakeičia. Jei parašysi tik `message.lower()`, bet rezultato nepriskirsi kintamajam, `message` liks toks pat, koks buvo prieš tai.

**Mini užduotis.** Turėdamas `raw = "  PYTHON ir DI!!!  "`, gauk tvarkingą, mažosiomis raidėmis parašytą žodžių sąrašą be šauktukų.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
raw = "  PYTHON ir DI!!!  "
cleaned = raw.strip().lower().replace("!", "")
words = cleaned.split()
print(words)
```

```text
['python', 'ir', 'di']
```

Trys metodai iškviesti vienas po kito: pirma pašalinami kraštiniai tarpai, tada raidės paverčiamos mažosiomis, tada pašalinami šauktukai, ir tik tada tekstas skaidomas į žodžius.

</details>

## 5. Pjūviai ir paieška tekste

Kartais reikia ne viso teksto, o tik jo dalies pagal poziciją. Tam skirti pjūviai (angl. *slicing*):

```python
code = "PYTHON-2026"
print(code[:6])    # PYTHON
print(code[-4:])   # 2026
print(code.find("-"))
```

```text
PYTHON
2026
6
```

Indeksuojant iš pradžios simboliai numeruojami nuo `0`:

```text
indeksas: 0  1  2  3  4  5  6  7  8  9 10
simbolis: P  Y  T  H  O  N  -  2  0  2  6
```

`code[:6]` paima simbolius su indeksais `0`–`5` (šešis simbolius), o pabaigos indeksas `6` pats neįtraukiamas. `code[-4:]` paima paskutinius keturis simbolius skaičiuojant nuo pabaigos.

> **Dažna klaida:** pjūvyje pabaigos indeksas neįtraukiamas. `code[:6]` grąžins 6 simbolius (indeksai `0`–`5`), o ne 7, kaip kartais tikimasi.

`.find()` grąžina rastos dalies pradžios indeksą arba `-1`, jei tokios dalies nėra:

```python
print("-" in code)      # True
print(code.find("@"))   # -1, nes tokio simbolio nėra
```

`find()` neradęs grąžina `-1`, o ne klaidą. Jei tiksli pozicija tekste nesvarbi, o svarbu tik ar dalis yra – skaitomiau naudoti `in`.

**Mini užduotis.** Iš el. pašto `studentas@example.lt` atskirk vardą ir domeną. Patikrink, ar yra `@`, ar tekstas baigiasi `.lt`, ir parodyk inicialus iš vardo bei pavardės.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
email = "studentas@example.lt"
has_at = "@" in email
ends_lt = email.endswith(".lt")

at_position = email.find("@")
username = email[:at_position]
domain = email[at_position + 1:]

print(has_at, ends_lt)
print(username, domain)

full_name = "Jonas Petraitis"
first_name, last_name = full_name.split()
initials = first_name[0] + last_name[0]
print(initials)
```

```text
True True
studentas example.lt
JP
```

`at_position` saugo `@` indeksą, todėl pjūviai `email[:at_position]` ir `email[at_position + 1:]` tiksliai atskiria vardą nuo domeno. `.endswith(".lt")` veikia panašiai kaip `.startswith()`, tik tikrina teksto pabaigą.

</details>

## 6. Žodynas: reikšmė pagal prasmingą raktą

Sąraše reikšmę randame pagal poziciją (indeksą), žodyne – pagal prasmingą raktą.

```python
course = {
    "title": "Python ir DI asistentai",
    "hours": 88,
    "online": True,
}

print(course["title"])
print(course.get("price", "Kaina nenurodyta"))
course["level"] = "pradedantiesiems"
```

```text
Python ir DI asistentai
Kaina nenurodyta
```

`course["title"]` iškart kreipiasi į reikšmę pagal raktą `"title"`. `course.get("price", "Kaina nenurodyta")` saugiai patikrina raktą `"price"`, kurio žodyne nėra, ir grąžina antrą argumentą kaip atsarginę reikšmę. Trečia eilutė – `course["level"] = "pradedantiesiems"` – sukuria naują raktą priskyrimu, lygiai taip pat, kaip atnaujinamas ir jau esantis.

```python
for key, value in course.items():
    print(f"{key}: {value}")
```

```text
title: Python ir DI asistentai
hours: 88
online: True
level: pradedantiesiems
```

`.items()` per kiekvieną ciklo apsisukimą grąžina rakto ir reikšmės porą – patogu, kai reikia parodyti visą žodyno turinį.

> **Dažna klaida:** `course["price"]` sukeltų `KeyError`, nes tokio rakto žodyne nėra:
>
> ```text
> Traceback (most recent call last):
>     ...
> KeyError: 'price'
> ```
>
> `.get()` leidžia pateikti atsarginę reikšmę, ir programa dėl to nenutrūksta.

**Mini užduotis.** Prie `course` žodyno pridėk raktą `"language"` su reikšme `"lietuvių"`, tada su `.get()` saugiai patikrink raktą `"duration"`, kurio žodyne nėra, numatytą reikšmę parašydamas `"nenurodyta"`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
course = {
    "title": "Python ir DI asistentai",
    "hours": 88,
    "online": True,
}

course["language"] = "lietuvių"
print(course.get("duration", "nenurodyta"))
print(course)
```

```text
nenurodyta
{'title': 'Python ir DI asistentai', 'hours': 88, 'online': True, 'language': 'lietuvių'}
```

</details>

## 7. Įdėtos struktūros: žodynas žodyne

Žinių bazei reikia daugiau nei vieno lygio: kiekviena tema turi ne tik atsakymą, bet ir sąrašą raktažodžių, pagal kuriuos ją reikėtų surasti.

```python
knowledge_base = {
    "kursas": {
        "keywords": ["kursas", "mokymai", "programa"],
        "answer": "Programa trunka 88 akademines valandas.",
    },
    "kontaktai": {
        "keywords": ["kontaktai", "paštas", "telefonas"],
        "answer": "Rašykite mokymai@example.lt.",
    },
}
```

Tai žodynas, kurio reikšmės yra kiti žodynai, o juose – sąrašai. Tokią struktūrą lengviausia skaityti iš išorės į vidų: pirma raktas išoriniame žodyne, tada raktas vidiniame, tada, jei reikia, sąrašo indeksas.

```python
print(knowledge_base["kursas"]["answer"])
print(knowledge_base["kontaktai"]["keywords"][0])
```

```text
Programa trunka 88 akademines valandas.
kontaktai
```

Pirmoje eilutėje `knowledge_base["kursas"]` pasirenka temos žodyną, o `["answer"]` iš jo paima atsakymą. Antroje eilutėje `knowledge_base["kontaktai"]["keywords"]` paima raktažodžių sąrašą, o `[0]` – jo pirmą elementą.

> **Dažna klaida:** praleidus vieną žingsnį kelyje (pvz. parašius tik `knowledge_base["kursas"]`) gaunamas visas vidinis žodynas, o ne laukiamas tekstas ar sąrašas. Prieš spausdindamas patikrink, kiek lygių iš tikrųjų turi turėti kreipimasis.

**Mini užduotis.** Prie `knowledge_base` pridėk naują temą `"tvarkarastis"` su bent dviem raktažodžiais ir atsakymu. Parodyk jos pirmą raktažodį ir atsakymą.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
knowledge_base["tvarkarastis"] = {
    "keywords": ["tvarkarastis", "diena"],
    "answer": "Paskaitos vyksta antradieniais ir ketvirtadieniais.",
}

print(knowledge_base["tvarkarastis"]["keywords"][0])
print(knowledge_base["tvarkarastis"]["answer"])
```

```text
tvarkarastis
Paskaitos vyksta antradieniais ir ketvirtadieniais.
```

Nauja tema pridedama lygiai taip pat, kaip nauja reikšmė bet kuriame žodyne – priskyrimu naujam raktui. Paieškos kodo, kuris jau egzistuoja, keisti nereikia.

</details>

## 8. Paieška žinių bazėje

Turint žinių bazę, belieka parašyti paiešką, kuri vartotojo žinutėje suras bent vieną raktažodį ir grąžins atitinkamą atsakymą.

```python
message = input("Klausimas: ").strip().lower()
answer = None

for topic in knowledge_base.values():
    for keyword in topic["keywords"]:
        if keyword in message:
            answer = topic["answer"]
            break
    if answer is not None:
        break

if answer is None:
    answer = "Atsakymo žinių bazėje dar nėra."

print(answer)
```

Žingsnis po žingsnio:

1. Vartotojo įvestis iškart išvaloma su `.strip().lower()` – taip, kaip mokeisi 4 skyriuje.
2. `answer = None` yra sentinelis: ši reikšmė reiškia „atsakymo dar neradome“.
3. Išorinis `for` eina per kiekvieną temą (`topic["keywords"]`, `topic["answer"]`), naudodamas `.values()`, nes čia dar nereikia temos pavadinimo – tik jos turinio.
4. Vidinis `for` eina per kiekvieną tos temos raktažodį.
5. Jei raktažodis randamas žinutėje (`keyword in message`), `answer` gauna temos atsakymą, o `break` išeina iš vidinio ciklo – toliau tos temos raktažodžių tikrinti nebereikia.
6. `if answer is not None: break` nutraukia ir išorinį ciklą, kai atsakymas jau rastas. Be šios eilutės paieška tęstųsi per likusias temas ir galėtų atsakymą perrašyti.
7. Jei nė viena tema neatitiko, `answer` liko `None`, ir `if answer is None:` jį pakeičia numatytuoju pranešimu.

> **Dažna klaida:** be `if answer is not None: break` išoriniame cikle, radus tinkamą atsakymą pirmoje temoje, paieška vis tiek tęsis per likusias temas ir gali **perrašyti** `answer`, jei netikėtai sutaps ir kitas raktažodis.

**Mini užduotis.** Turėdamas

```python
knowledge_base = {
    "kursas": {
        "keywords": ["kursas", "mokymai", "programa"],
        "answer": "Programa trunka 88 akademines valandas.",
    },
    "kontaktai": {
        "keywords": ["kontaktai", "paštas", "telefonas"],
        "answer": "Rašykite mokymai@example.lt.",
    },
}
```

nuspėk, koks bus atsakymas, kai `message = "kada prasideda kursas ir kur kontaktai"` po `.strip().lower()` normalizavimo. Tada paleisk aukščiau pateiktą paieškos kodą ir patikrink save.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Atsakymas bus apie temą `"kursas"`: `"Programa trunka 88 akademines valandas."` Nors žinutėje yra ir žodis „kontaktai“, žodynai Python 3.7+ išlaiko įrašymo tvarką, todėl išorinis ciklas pirmiausia patikrina temą `"kursas"` (ji aprašyta pirmoji) ir, radęs atitikmenį, iškart nutraukia paiešką su `break`. Tema `"kontaktai"`, nors irgi atitiktų, net nebus patikrinta. Tai paaiškina, kodėl temų tvarka žodyne veikia kaip numanomas prioritetas – ši mintis toliau plėtojama C lygio užduotyje ir 14.4 skyriaus `rank_topics` funkcijoje.

</details>

## 9. Įvairūs kodo pavyzdžiai

### Minimalus pavyzdys

**Problema:** išvalyti vieną žodį ir jo pirmą raidę parodyti didžiąja.

```python
word = "  python  "
clean_word = word.strip()
print(clean_word.capitalize())
```

```text
Python
```

**Paaiškinimas:** `.capitalize()` didžiąja raide parašo tik pirmą simbolį, likusius paverčia mažosiomis. **Patobulinimas:** pritaikyk viso sakinio pirmai raidei, o ne tik vienam žodžiui.

### Kasdienis pavyzdys – prekės kodo skaitymas

```python
product_code = "SKU-00214-LT"
category = product_code[:3]
number = product_code[4:9]
country = product_code[-2:]
print(f"Kategorija: {category}, numeris: {number}, šalis: {country}")
```

```text
Kategorija: SKU, numeris: 00214, šalis: LT
```

**Patobulinimas:** prieš pjaustydamas patikrink kodo ilgį su `len()`, kad išvengtum netikėtų rezultatų su trumpesniais kodais.

### Darbo pavyzdys – kliento užklausos nukreipimas

```python
department_map = {
    "sąskaita": "Finansų skyrius",
    "prisijungimas": "IT skyrius",
    "pristatymas": "Logistikos skyrius",
}

request = "Turiu problemą su sąskaita"
cleaned_request = request.lower()

department = "Bendras skyrius"
for keyword, team in department_map.items():
    if keyword in cleaned_request:
        department = team
        break

print(f"Užklausa nukreipta į: {department}")
```

```text
Užklausa nukreipta į: Finansų skyrius
```

**Patobulinimas:** pridėk dar tris skyrius ir patikrink, kas atsitinka, kai žinutėje yra du raktažodžiai vienu metu.

### Automatizavimo pavyzdys – el. pašto adresų sąrašo valymas

```python
raw_emails = ["  Ieva@example.lt ", "TOMAS@example.LT", " ona@example.lt"]
clean_emails = [email.strip().lower() for email in raw_emails]
print(clean_emails)
```

```text
['ieva@example.lt', 'tomas@example.lt', 'ona@example.lt']
```

**Patobulinimas:** pašalink galimus dublikatus paversdamas rezultatą `set()` tipu.

### Duomenų ir AI pavyzdys – žodžių dažnio žodynas

```python
message = "python yra galingas python moko duomenų mokslo"
words = message.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
```

```text
{'python': 2, 'yra': 1, 'galingas': 1, 'moko': 1, 'duomenų': 1, 'mokslo': 1}
```

**Paaiškinimas:** `word_counts.get(word, 0)` grąžina esamą skaičių arba `0`, jei žodis dar nematytas – tai bazinis žingsnis prieš tekstų dažnio analizę ar „bag of words“ modelius, su kuriais susidursi vėliau. **Patobulinimas:** dažniausią žodį parodyk naudodamas `max(word_counts, key=word_counts.get)`.

### Klaidingas pavyzdys – pataisyk

```python
settings = {"language": "lt", "theme": "dark"}
print(settings["notifications"])
```

Šis kodas sukels `KeyError: 'notifications'`, nes tokio rakto žodyne nėra.

Pataisymas:

```python
settings = {"language": "lt", "theme": "dark"}
print(settings.get("notifications", "nenustatyta"))
```

```text
nenustatyta
```

## 10. Interaktyvios veiklos

### 1. Nuspėk rezultatą

```python
text = "  Labas  "
result = text.strip()
print(text)
print(result)
```

A. `Labas` ir `Labas`
B. `  Labas  ` ir `Labas`
C. `Labas` ir `  Labas  `
D. Klaida

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Tekstas nekintamas: `.strip()` grąžina naują reikšmę, kuri priskiriama `result`, o `text` lieka toks, koks buvo.

</details>

### 2. Užpildyk trūkstamą kodą

```python
prices = {"kava": 2.5, "arbata": 2.0}
value = prices.____("sultys", "nėra kainoraštyje")
print(value)
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
value = prices.get("sultys", "nėra kainoraštyje")
```

Rakto `"sultys"` žodyne nėra, todėl `.get()` grąžina antrą argumentą kaip atsarginę reikšmę, o ne sukelia klaidą.

</details>

### 3. Surask klaidą

```python
data = {"name": "Ona"}
print(data["age"])
```

Nustatyk klaidą, paaiškink ir pataisyk.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Kodas sukelia `KeyError: 'age'`, nes tokio rakto žodyne nėra.

```python
data = {"name": "Ona"}
print(data.get("age", "amžius nenurodytas"))
```

</details>

### 4. Sudėliok teisinga tvarka

```text
print(answer)
answer = knowledge_base.get(topic, "Nežinoma tema")
topic = input("Tema: ").strip().lower()
knowledge_base = {"kursas": "88 val.", "kaina": "Klauskite koordinatoriaus"}
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
knowledge_base = {"kursas": "88 val.", "kaina": "Klauskite koordinatoriaus"}
topic = input("Tema: ").strip().lower()
answer = knowledge_base.get(topic, "Nežinoma tema")
print(answer)
```

Pirmiausia turi egzistuoti žodynas, tada surenkama ir išvaloma vartotojo įvestis, tik po to iš žodyno saugiai paimamas atsakymas ir parodomas.

</details>

### 5. Pasirink tinkamą sprendimą

Nori saugiai perskaityti temos šaltinį, kuris kai kuriose temose gali būti nenurodytas.

A. `topic["source"]`
B. `topic.get("source", "šaltinis nenurodytas")`
C. `topic["source"] = None`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** `.get()` su aiškia atsargine reikšme leidžia saugiai skaityti raktą, kuris ne visose temose privalo egzistuoti, ir nesukelia `KeyError`.

</details>

### 6. Parašyk pats

Sukurk žodyną su penkiais Lietuvos miestais ir jų gyventojų skaičiumi (sveikasis skaičius). Paprašyk vartotojo įvesti miesto pavadinimą ir su `.get()` parodyk gyventojų skaičių arba aiškų pranešimą, kad miesto sąraše nėra.

### 7. Patobulink kodą

```python
d = {"a": "kursas", "b": "kaina"}
x = input("ivesk: ")
y = d.get(x, "nera")
print(y)
```

Pakeisk kintamųjų ir raktų vardus taip, kad kodas būtų aiškus, ir pateik informatyvesnę išvestį.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
topic_labels = {"kursas": "Kursas ir programa", "kaina": "Kaina ir apmokėjimas"}
user_key = input("Įvesk temą: ").strip().lower()
label = topic_labels.get(user_key, "Tokios temos nėra")
print(f"Tema: {label}")
```

`d`, `x`, `y` pakeisti prasmingais vardais (`topic_labels`, `user_key`, `label`), o rezultatas parodomas su aiškia f-string žinute vietoj vienos neaiškios eilutės.

</details>

## 11. Žinių patikrinimas prieš platformos testą

Pirmiausia atsakyk neužleisdamas atsakymų.

1. Kodėl `message.strip()` pati savaime nepakeičia kintamojo `message`?
2. Kas atsitiks paleidus `contacts["telefonas"]`, jei tokio rakto žodyne nėra?
3. Kuo situacija skiriasi naudojant `contacts.get("telefonas")`, palyginti su `contacts["telefonas"]`?
4. Ką reiškia rezultatas `-1`, gautas iš `.find()`?
5. Kiek kreipimosi lygių turi `knowledge_base["kursas"]["keywords"][0]` ir ką kiekvienas iš jų atlieka?
6. Kodėl paieškos cikle atsakymo kintamasis pradžioje priskiriamas `None`, o ne tuščiam tekstui `""`?
7. Kas nutiktų, jei paieškos cikle praleistum `if answer is not None: break` sakinį po vidinio ciklo?
8. Kuo `.split()` rezultatas skiriasi nuo `" ".join(...)` rezultato?
9. Kodėl raktažodis `"ai"` gali klaidingai suveikti žinutėje `"pakalbėkim apie kainas"`?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymus ir paaiškinimus</summary>

1. Nes tekstas Python'e yra nekintamas (angl. *immutable*) – metodas grąžina naują reikšmę, o ne pakeičia seną; norint pakeitimą išsaugoti, jį reikia priskirti tam pačiam ar naujam kintamajam.
2. Programa sukels `KeyError: 'telefonas'` ir nutrūks, jei klaida nesutvarkyta.
3. `contacts.get("telefonas")` klaidos nesukels – jei rakto nėra, grąžins `None` (arba nurodytą atsarginę reikšmę), o `contacts["telefonas"]` sukeltų `KeyError`.
4. Kad nurodytos teksto dalies žinutėje nėra – paieška nepavyko.
5. Trys lygiai: pirmas raktas (`"kursas"`) pasirenka temą pačiame `knowledge_base` žodyne, antras raktas (`"keywords"`) paima tos temos raktažodžių sąrašą, o indeksas `[0]` iš to sąrašo paima pirmą elementą.
6. `None` aiškiai reiškia „atsakymo dar nėra“, o tuščias tekstas galėtų būti supainiotas su sąmoningai tuščiu, bet jau rastu atsakymu.
7. Radus atitikmenį, paieška vis tiek tęstųsi per likusias temas ir galėtų netyčia perrašyti jau rastą teisingą atsakymą.
8. `.split()` tekstą paverčia žodžių sąrašu, o `" ".join(...)` sąrašą sujungia atgal į vieną tekstą su nurodytu skirtuku – tai priešingos krypties operacijos.
9. Nes raktažodžio paieška su `in` tikrina simbolių seką bet kurioje teksto vietoje – seka „ai“ yra ir žodyje „kainas“, todėl toks trumpas raktažodis gali klaidingai suveikti nesusijusiame kontekste.

</details>

## 12. Praktinės užduotys

### A lygis – kontaktų knygelė

**Sąlyga:** sukurk žodyną su trimis žmonėmis ir jų el. paštais (raktas – vardas, reikšmė – el. paštas). Leisk vartotojui įvesti vardą; naudok `.get()` ir aiškų atsakymą, kai žmogaus nėra.
**Pavyzdinė įvestis:** `Rūta`
**Laukiamas rezultatas:** `El. paštas: ruta@example.lt`, o įvedus nežinomą vardą – `Tokio kontakto nėra.`
**Užuomina:** vardą prieš paiešką suvienodink su `.strip().capitalize()`, o patį atsakymą gauk su `.get()` ir `None` kaip sentineliu.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
contacts = {
    "Rūta": "ruta@example.lt",
    "Tomas": "tomas@example.lt",
    "Ieva": "ieva@example.lt",
}

name = input("Kieno el. paštą ieškai? ").strip().capitalize()
email = contacts.get(name)

if email is None:
    print("Tokio kontakto nėra.")
else:
    print(f"El. paštas: {email}")
```

`.strip().capitalize()` suvienodina vardo formą, kad `"rūta"`, `"Rūta "` ir `"RŪTA"` būtų palyginti vienodai. `contacts.get(name)` be antro argumento grąžina `None`, jei vardo nėra – tai tas pats `None` sentinelis, kurį naudojai 8 skyriaus paieškoje. **Papildomas iššūkis:** pridėk dar du kontaktus ir leisk vartotojui pridėti naują kontaktą, jei jo dar nėra knygelėje.

</details>

### B lygis – teksto statistika

**Sąlyga:** suskaidyk pastraipą į žodžius, pašalink `.`, `,`, `!`, `?`, suskaičiuok kiekvieno žodžio pasikartojimus žodyne ir parodyk dažniausią.
**Pavyzdinė įvestis:** `"Python yra galingas. Python moko, Python įkvepia!"`
**Laukiamas rezultatas:** žodžių dažnio žodynas ir eilutė `Dažniausias žodis: python (3 kartus)`.
**Užuomina:** prieš skaičiuojant visą tekstą paverski mažosiomis raidėmis, o skyrybos ženklus pašalink pakartotinai naudodamas `.replace()` per keturis ženklus.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
paragraph = "Python yra galingas. Python moko, Python įkvepia!"

cleaned = paragraph.lower()
for punctuation_mark in [".", ",", "!", "?"]:
    cleaned = cleaned.replace(punctuation_mark, "")

words = cleaned.split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

most_common_word = None
most_common_count = 0
for word, count in word_counts.items():
    if count > most_common_count:
        most_common_word = word
        most_common_count = count

print(word_counts)
print(f"Dažniausias žodis: {most_common_word} ({most_common_count} kartus)")
```

```text
{'python': 3, 'yra': 1, 'galingas': 1, 'moko': 1, 'įkvepia': 1}
Dažniausias žodis: python (3 kartus)
```

Ciklas per `punctuation_mark` sąrašą iš eilės pašalina kiekvieną skyrybos ženklą. `word_counts.get(word, 0) + 1` yra klasikinis skaičiavimo žodyne šablonas. Antras ciklas rankiniu būdu suranda didžiausią reikšmę – tai tas pats kaupiklio principas, kurį mokeisi trečioje pamokoje, tik dabar taikomas žodynui. **Papildomas iššūkis:** vietoj rankinės paieškos panaudok `max(word_counts, key=word_counts.get)` ir palygink rezultatą.

</details>

### C lygis – DUK paieška

**Sąlyga:** sukurk bent 8 temų žinių bazę. Kiekviena tema turi turėti `keywords`, `answer` ir `source`. Atsakyme parodyk šaltinį. Jei tinka kelios temos, rink pirmą – tik aiškiai aprašyta prioritetų tvarka.
**Pavyzdinė įvestis:** `"kada prasideda kursas ir kokia kaina?"`
**Laukiamas rezultatas:** atsakymas apie temą, kuri žodyne aprašyta pirmiau (šiuo atveju – „kursas“), kartu su šaltiniu.
**Užuomina:** naudok tą pačią dviejų ciklų paieškos schemą kaip 8 skyriuje, tik prie `answer` papildomai prijunk `topic.get("source", "šaltinis nenurodytas")`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
faq = {
    "kursas": {
        "keywords": ["kursas", "mokymai", "programa"],
        "answer": "Programa trunka 88 akademines valandas.",
        "source": "Mokymo planas",
    },
    "kaina": {
        "keywords": ["kaina", "kainuoja", "mokėti"],
        "answer": "Pilnas kursas kainuoja 890 Eur.",
        "source": "Kainoraštis",
    },
    "kontaktai": {
        "keywords": ["kontaktai", "paštas", "telefonas"],
        "answer": "Rašykite mokymai@example.lt.",
        "source": "Kontaktų puslapis",
    },
    "tvarkarastis": {
        "keywords": ["tvarkaraštis", "diena", "laikas"],
        "answer": "Paskaitos vyksta antradieniais ir ketvirtadieniais.",
        "source": "Tvarkaraštis",
    },
    "pazymejimas": {
        "keywords": ["pažymėjimas", "sertifikatas", "diplomas"],
        "answer": "Baigus kursą gausi pažymėjimą.",
        "source": "Kurso taisyklės",
    },
    "reikalavimai": {
        "keywords": ["reikalavimai", "pradedantiesiems", "patirtis"],
        "answer": "Kursas tinka pradedantiesiems be patirties.",
        "source": "Kurso aprašymas",
    },
    "uzduotys": {
        "keywords": ["užduotys", "namų darbai", "praktika"],
        "answer": "Kiekvienai pamokai skiriama savarankiška užduotis.",
        "source": "Mokymo planas",
    },
    "grazinimas": {
        "keywords": ["grąžinimas", "atsisakymas", "pinigai"],
        "answer": "Pinigus grąžiname per 14 dienų nuo užsakymo.",
        "source": "Pirkimo taisyklės",
    },
}

message = input("Klausimas: ").strip().lower()
answer = None

# Temos tikrinamos ta tvarka, kuria jos aprašytos žodyne –
# tai ir yra prioritetų tvarka: pirmoji atitikusi tema laimi.
for topic in faq.values():
    for keyword in topic["keywords"]:
        if keyword in message:
            source = topic.get("source", "šaltinis nenurodytas")
            answer = f"{topic['answer']} (šaltinis: {source})"
            break
    if answer is not None:
        break

if answer is None:
    answer = "Atsakymo žinių bazėje dar nėra."

print(answer)
```

Komentaras kode aiškiai dokumentuoja, kad temų tvarka žodyne = prioritetų tvarka – tai svarbu, kai kelios temos gali atitikti tą pačią žinutę. **Papildomas iššūkis:** panaudok 14.4 skyriaus `rank_topics` idėją ir parodyk visas atitikusias temas, surikiuotas pagal atitikčių skaičių, o ne tik pirmą rastą.

</details>

## 13. Mini projektas: Asistentas 0.3

### 1. Projekto situacija

Asistentas 0.2 (trečia pamoka) atsakinėjo per `if`/`elif` grandinę su keliomis temomis ir kaupė klausimus paprastame sąraše. Realaus produkto DUK gali turėti dešimtis temų, o kiekvienam atsakymo pakeitimui tektų redaguoti kodą. Reikia atskirti „žinias“ (temos, raktažodžiai, atsakymai) nuo „programos logikos“ (kaip randamas atsakymas).

### 2. Galutinis tikslas

Sukurti Asistentą 0.3 – dialogą, kuris atsakymus renka iš `knowledge_base` žodyno, saugo pilną pokalbio istoriją kartu su surastos temos pavadinimu ir leidžia bet kada peržiūrėti temų sąrašą bei istoriją komandomis.

### 3. Funkciniai reikalavimai

Programa turi:

1. `knowledge_base` laikyti kaip žodyną, kurio kiekviena reikšmė – žodynas su `keywords` (sąrašas) ir `answer` (tekstas), pagal 7 skyriaus struktūrą;
2. dialogą vesti `while True` cikle, kol vartotojas parašo „baigti“;
3. neleisti tuščiai įvesčiai eiti toliau (`continue`);
4. komanda `/topics` – parodyti visų žinomų temų pavadinimus;
5. komanda `/history` – parodyti sunumeruotą pokalbio istoriją;
6. paiešką atlikti 8 skyriuje aprašyta dviejų `for` ciklų schema su `answer = None` sentineliu;
7. kiekvieną pokalbio įrašą saugoti kaip žodyną `{"question": ..., "answer": ..., "matched_topic": ...}`;
8. nežinomą klausimą įrašyti į atskirą sąrašą `unanswered`;
9. jei atsakymas nerastas, `matched_topic` turi likti `None`.

### 4. Pavyzdinė sąveika

```text
Asistentas 0.3. Parašyk „baigti“, kai norėsi išeiti.
Komandos: /topics – temų sąrašas, /history – pokalbio istorija.
Tu: Kokia kurso kaina?
Asistentas: Dėl kainos kreipkis į koordinatorių. (šaltinis: Kainoraštis)
Tu: /topics
- kursas
- kaina
- kontaktai
Tu: kas yra grybai
Asistentas: Atsakymo žinių bazėje dar nėra.
Tu: /history
1. Tu: Kokia kurso kaina?
   Asistentas: Dėl kainos kreipkis į koordinatorių. (šaltinis: Kainoraštis)
2. Tu: kas yra grybai
   Asistentas: Atsakymo žinių bazėje dar nėra.
Tu: baigti
Asistentas: Iki! Atsakiau į 2 klausimus.
```

### 5. Pavyzdinis rezultatas

Užbaigus pokalbį, programa papildomai parodo neatsakytus klausimus:

```text
Neatsakyti klausimai: 1
1. kas yra grybai
```

### 6. Projekto kūrimo etapai

1. Nukopijuok Asistento 0.2 karkasą (`while` ciklas, `input()`, „baigti“ ir tuščios įvesties patikros).
2. Pridėk `knowledge_base` žodyną su bent trimis temomis.
3. Pakeisk `if`/`elif` grandinę dviejų ciklų paieška su `answer = None`.
4. Pridėk kintamąjį `matched_topic`, kuris atnaujinamas kartu su `answer`.
5. Sukurk `history` sąrašą ir po kiekvieno atsakymo pridėk žodyną su trimis raktais: `question`, `answer`, `matched_topic`.
6. Sukurk `unanswered` sąrašą ir į jį rašyk klausimus, kai `answer is None`.
7. Prieš paieškos bloką pridėk `/topics` ir `/history` komandas.
8. Baigiant dialogą, parodyk atsakytų klausimų skaičių, o po ciklo – neatsakytų klausimų sąrašą.
9. Rankiniu būdu išbandyk bent 10 skirtingų klausimų, įskaitant tokius, kurie atitinka kelias temas.

### 7. Pseudokodas

```text
SUKURK knowledge_base su temomis (keywords, answer, source)
SUKURK tuščią history sąrašą
SUKURK tuščią unanswered sąrašą

KARTOK:
    PAKLAUSK klausimo
    IŠVALYK klausimą (strip, lower)

    JEI klausimas yra "baigti": PARODYK atsakytų klausimų skaičių IR NUTRAUK
    JEI klausimas tuščias: PARAŠYK priminimą IR PEREIK PRIE KITO ŽINGSNIO
    JEI klausimas yra "/topics": PARODYK visas temas IR PEREIK PRIE KITO ŽINGSNIO
    JEI klausimas yra "/history": PARODYK istoriją IR PEREIK PRIE KITO ŽINGSNIO

    answer = None
    matched_topic = None
    KIEKVIENAI temai knowledge_base:
        KIEKVIENAM raktažodžiui temoje:
            JEI raktažodis yra klausime:
                answer = temos atsakymas
                matched_topic = temos pavadinimas
                NUTRAUK vidinį ciklą
        JEI answer jau rastas: NUTRAUK išorinį ciklą

    JEI answer vis dar None:
        answer = "Atsakymo žinių bazėje dar nėra."
        PRIDĖK klausimą prie unanswered
    KITAIP:
        PRIDĖK šaltinį prie answer, jei jis žinomas

    PRIDĖK {question, answer, matched_topic} PRIE history
    PARODYK atsakymą

PARODYK neatsakytų klausimų sąrašą
```

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

```python
knowledge_base = {
    "kursas": {
        "keywords": ["kursas", "mokymai", "programa"],
        "answer": "Programa trunka 88 akademines valandas.",
        "source": "Mokymo planas",
    },
    "kaina": {
        "keywords": ["kaina", "kainuoja", "mokėti"],
        "answer": "Dėl kainos kreipkis į koordinatorių.",
        "source": "Kainoraštis",
    },
    "kontaktai": {
        "keywords": ["kontaktai", "paštas", "telefonas"],
        "answer": "Rašykite mokymai@example.lt.",
        "source": "Kontaktų puslapis",
    },
}

history = []
unanswered = []

print("Asistentas 0.3. Parašyk „baigti“, kai norėsi išeiti.")
print("Komandos: /topics – temų sąrašas, /history – pokalbio istorija.")

while True:
    original_message = input("Tu: ").strip()
    message = original_message.lower()

    if message == "baigti":
        print(f"Asistentas: Iki! Atsakiau į {len(history)} klausimus.")
        break

    if not message:
        print("Asistentas: Parašyk klausimą.")
        continue

    if message == "/topics":
        for topic_name in knowledge_base:
            print(f"- {topic_name}")
        continue

    if message == "/history":
        for number, item in enumerate(history, start=1):
            print(f"{number}. Tu: {item['question']}")
            print(f"   Asistentas: {item['answer']}")
        continue

    answer = None
    matched_topic = None

    for topic_name, topic in knowledge_base.items():
        for keyword in topic["keywords"]:
            if keyword in message:
                answer = topic["answer"]
                matched_topic = topic_name
                break
        if answer is not None:
            break

    if answer is None:
        answer = "Atsakymo žinių bazėje dar nėra."
        unanswered.append(original_message)
    else:
        source = knowledge_base[matched_topic].get("source")
        if source:
            answer = f"{answer} (šaltinis: {source})"

    history.append({
        "question": original_message,
        "answer": answer,
        "matched_topic": matched_topic,
    })

    print(f"Asistentas: {answer}")

if unanswered:
    print(f"Neatsakyti klausimai: {len(unanswered)}")
    for number, question in enumerate(unanswered, start=1):
        print(f"{number}. {question}")
```

Svarbiausios eilutės: `answer = None` ir `matched_topic = None` yra sentineliai prieš paiešką. Dviejų ciklų schema tiksliai tokia pati, kokią mokeisi 8 skyriuje – tik papildomai prisimena, **kurios** temos atsakymas rastas (`matched_topic`), kad tai būtų galima įrašyti į istoriją ir pridėti šaltinį. `history.append({...})` visada prideda tris raktus, net kai `matched_topic` lieka `None` – taip istorijos įrašai lieka vienodos struktūros nepriklausomai nuo to, ar atsakymas rastas.

</details>

### 8. Galimi patobulinimai

- pridėk komandą `/clear`, kuri išvalo `history`, nesustabdydama programos;
- leisk kelioms temoms atitikti vienu metu ir parodyk visas, o ne tik pirmą (žr. 14.4 skyriaus `rank_topics` funkciją);
- saugok, kiek kartų kiekviena tema buvo panaudota, ir parodyk populiariausią;
- prieš rodydamas atsakymą, patikrink, ar `original_message` nėra per ilgas ar neturi draudžiamų simbolių;
- eksportuok `history` į tekstinį failą pamokos pabaigoje (failų darbą išmoksi vėlesnėse pamokose).

### 9. `README.md` šablonas

```text
# Asistentas 0.3

Dialogo asistentas, kuris atsakymus randa raktažodžiais valdomoje žinių bazėje.

## Funkcijos
- knowledge_base žodynas su temomis, raktažodžiais ir atsakymais
- Komanda /topics – parodo visas temas
- Komanda /history – parodo pokalbio istoriją
- Neatsakyti klausimai kaupiami atskirai

## Paleidimas
python3 asistentas_03.py

## Pavyzdys
Užduok klausimą su vienu iš žinomų raktažodžių (kursas, kaina, kontaktai)
arba parašyk /topics, kad pamatytum visas temas.

## Ką išmokau
Teksto metodai, žodynai, įdėtos struktūros, saugi paieška su .get() ir None.

## Tolimesni patobulinimai
Kelių temų reitingavimas, populiariausios temos statistika, istorijos eksportas.
```

## 14. Gilioji laboratorija: nuo teksto iki patikimos temos

Šis skyrius skirtas gilesniam paieškos patikimumo supratimui – jis parodo, kaip paprastą raktažodžių paiešką padaryti tikslesnę ir kaip ją derinti, kai kažkas veikia netaip, kaip tikėtasi.

### 14.1. Formatuok taip, kad žmogus matytų prasmę

```python
topic = "Python"
hours = 88
price = 19.9
print(f"{topic}: {hours:03d} val., kaina {price:.2f} Eur")
```

Rezultatas: `Python: 088 val., kaina 19.90 Eur`. `:03d` prideda nulius iki trijų skaitmenų, `:.2f` palieka dvi dešimtaines vietas. Tai svarbu ataskaitoms ir asistento atsakymams, kurie neturi atrodyti kaip neapdoroti duomenys – tas pats formatavimas praverstų ir rodant `matched_topic` statistiką Asistento 0.3 patobulinimuose.

### 14.2. Unicode ir lietuvių kalba

```python
message = "Žinių bazė – Python ir DI"
print(message.upper())
print(len(message))
```

`len()` skaičiuoja Unicode simbolius, todėl lietuviškų raidžių nereikia šalinti vien dėl to, kad jos kitokios nei anglų abėcėlėje. Įvestį normalizuok vienoje vietoje ir tą funkciją testuok – tai ypač svarbu, nes tavo žinių bazės raktažodžiai ir vartotojų žinutės beveik visada turės lietuviškų raidžių.

### 14.3. Kodėl vien `in` gali suklaidinti

```python
print("api" in "kapitalas")
```

Tai `True`, nors tema apie API neminima. Paprastam raktažodžių filtrui suskaidyk žinutę į žodžius:

```python
import re
words = set(re.findall(r"[\wąčęėįšųūž]+", message.lower()))
```

Tai dar nėra lietuvių kalbos morfologija, bet sumažina klaidingus dalinius sutapimus. Į žinių bazę įrašyk formas, kurias realiai naudos tavo auditorija – šis pavojus (per trumpas ar per platus raktažodis) yra ir „Dažniausios klaidos“ lentelėje žemiau.

### 14.4. Temų reitingavimas

```python
def rank_topics(message: str, knowledge_base: dict) -> list[tuple[int, str]]:
    words = set(message.lower().split())
    ranked = []
    for name, topic in knowledge_base.items():
        score = sum(keyword in words for keyword in topic["keywords"])
        if score:
            ranked.append((score, name))
    return sorted(ranked, reverse=True)
```

Išbandyk `"kursas kaina"` su dviem temomis ir užrašyk, ką darytum lygiųjų atveju. Vėliau ši paieškos sutartis taps pirmuoju sluoksniu prieš kreipiantis į DI – ji leidžia grąžinti ne tik pirmą, bet visas atitikusias temas, surikiuotas pagal atitikčių skaičių.

### 14.5. Derinimo laboratorija

Parašyk tris testus su `"Kontaktai"`, `" kontaktai "` ir `"Kokie jūsų kontaktai?"`. Tada iškelk valymą į vieną funkciją ir vienoje vietoje dokumentuok, ką reiškia „atitikmuo“. Kontrolinis taškas pasiektas, kai gali pridėti naują temą, nepakeisdamas paieškos ciklo.

## 15. Duomenų sauga ir profesionali praktika

Nelaikyk API raktų, slaptažodžių ar asmens kodų žinių bazėje. Vartotojo tekstą laikyk nepatikimu: jo nevykdyk kaip Python kodo, nedėk tiesiai į sistemos komandą. Aiškūs raktai (`answer`, `source`) yra geriau už miglotus (`a`, `x`).

Papildomai:

- prieš įrašydamas naują temą į `knowledge_base`, peržiūrėk, ar atsakyme neatsiduria vidiniai duomenys (darbuotojų vardai, vidinės nuorodos), kurių viešai rodyti nereikėtų;
- jei žinių bazę augsi iš failo ar duomenų bazės, prieš naudojant paieškoje patikrink, ar kiekviena tema turi `keywords` ir `answer`;
- istorijoje (`history`) niekada nesaugok slaptažodžių ar mokėjimo duomenų, net jei vartotojas juos netyčia parašo klausime.

## 16. Dažniausios klaidos

| Klaida | Kodėl ji atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| `KeyError` | Kreiptasi į neegzistuojantį raktą | `contacts["telefonas"]` | `contacts.get("telefonas", "nenurodyta")` | Naudok `.get()` arba prieš tai patikrink `in` |
| `AttributeError` | Teksto metodas iškviestas ne teksto reikšmei | `age.strip()`, kai `age` yra `int` | `str(age).strip()` arba teksto metodo skaičiui nekviesti | Prieš kviesdamas metodą patikrink tipą su `type()` |
| Pakeitimas „neveikia“ | Metodo rezultatas nepriskirtas kintamajam | `message.lower()` be priskyrimo | `message = message.lower()` | Visada priskirk teksto metodo rezultatą kintamajam |
| Paieška per plati | Trumpas raktažodis atsitiktinai atitinka kitą žodį | `"ai" in "kainas"` | Ilgesnis, tikslesnis raktažodis, pvz. `"dirbtinis intelektas"` | Rinkis pakankamai ilgus, unikalius raktažodžius |
| Cikle gaunamas tik paskutinis atsakymas | `answer` perrašomas kiekviename žingsnyje, nes trūksta `break` sąlygos | Praleistas `if answer is not None: break` | Pridėta ši sąlyga iškart po vidinio ciklo | Radus atitikmenį, iškart nutrauk abu ciklus |
| Rakto pavadinimo klaida (typo) | Vidinis raktas parašytas su rašybos klaida | `topic["keywrods"]` | `topic["keywords"]` | Naudok vienodus, patikrintus raktų vardus visoje žinių bazėje |
| Painiojama `None` su tuščiu tekstu | Sentinelis tikrinamas netinkamai | `if answer == "":` | `if answer is None:` | Sentinelį visada lygink su `is None`, o ne su `""` |
| Užmirštas `.lower()` prieš palyginimą | Įvestis nenormalizuota, todėl `"Kursas"` ≠ `"kursas"` | `if "kursas" in message:`, kai `message` su didžiosiomis raidėmis | `message = original.lower()` prieš paiešką | Visada normalizuok įvestį prieš lygindamas ar ieškodamas |

## 17. Profesionali praktika

- Duomenis, kurie gali keistis (temos, atsakymai, raktažodžiai), laikyk atskirai nuo paieškos logikos – naujai temai pridėti neturėtum keisti ciklo kodo.
- Žodyno raktų vardus rašyk vienodai visoje žinių bazėje (`keywords`, `answer`, `source`), o ne kaskart kitaip.
- Prieš naudodamas žodyno reikšmę, apsvarstyk, ar ji tikrai visada bus – jei ne, naudok `.get()` su aiškia atsargine reikšme.
- Teksto palyginimams visada normalizuok abi puses vienodai (`.strip().lower()`), kitaip lygini nesuderinamus variantus.
- Rašyk trumpus rankinius testus su keliais skirtingais įvesties variantais (tikslus atitikimas, dalinis, jokio atitikimo), kaip 14.5 skyriuje.
- Sudėtingesnę paieškos ar formatavimo logiką iškelk į atskirą, aiškiai pavadintą funkciją (kaip `rank_topics` 14.4 skyriuje) – tai palengvins kitos pamokos refaktoringą.
- Dokumentuok, ką reiškia „atitikmuo“ tavo žinių bazėje – ar pakanka vieno raktažodžio, ar reikia kelių.

## 18. Kodėl tai svarbu mokantis AI?

Beveik kiekvienas AI įrankis pirmiausia išvalo tekstą: pašalina tarpus, suvienodina raidžių dydį, suskaido į žodžius ar dalis (tokenus). Tai tas pats `.strip().lower().split()` konvejeris, kurį naudojai šioje pamokoje – tik pramoninio dydžio sistemose jis vadinamas teksto normalizavimu (angl. *text normalization*) ir tekstų skaidymu (angl. *tokenization*).

Žinių bazė, kurią sukūrei žodynu, yra paprasčiausias „gavimu paremto atsakymo“ (angl. *retrieval*) pavyzdys: prieš kreipiantis į didelį kalbos modelį, sistema pirmiausia patikrina, ar atsakymas jau žinomas patikimame šaltinyje. Tikrose AI asistento architektūrose (pvz. RAG – *retrieval-augmented generation*) ši idėja išauga iki paieškos tarp tūkstančių dokumentų, tačiau principas tas pats: raktažodžiai ar reikšmės nukreipia į teisingą atsakymą greičiau ir patikimiau, nei modelis „atspėtų“ kiekvieną kartą iš naujo.

`None` sentinelis irgi turi savo atitikmenį AI kode: modeliai dažnai grąžina „nežinau“ tipo atsakymą arba žemą pasitikėjimo balą (angl. *confidence*), kai duomenų nepakanka – tai ta pati logika, kai tavo asistentas sąžiningai prisipažįsta, kad atsakymo žinių bazėje dar nėra, o ne bando sugalvoti ką nors klaidingo.

```python
faq_lookup_result = {
    "matched_topic": "kaina",
    "confidence": "high",
    "source": "Kainoraštis",
}
print(f"Rasta tema: {faq_lookup_result['matched_topic']}")
print(f"Šaltinis: {faq_lookup_result['source']}")
```

```text
Rasta tema: kaina
Šaltinis: Kainoraštis
```

Čia nėra tikro modelio – tik jo galimų rezultatų duomenų struktūra. Vėlesniuose moduliuose tas pačias reikšmių rūšis gausi iš AI bibliotekų.

## 19. Pamokos santrauka

- Tekstas Python'e yra nekintamas: metodai grąžina naują reikšmę, kurią reikia priskirti.
- `.strip()`, `.lower()`, `.replace()`, `.split()` ir `.join()` sudaro tipinį teksto valymo ir skaidymo konvejerį.
- Pjūviai (`[a:b]`) ištraukia teksto dalį, o `.find()` ir `in` padeda ją surasti.
- `dict` sieja prasmingą raktą su reikšme; `.get()` saugiai grąžina atsarginę reikšmę vietoj `KeyError`.
- Įdėtos struktūros (žodynas žodyne su sąrašais) leidžia modeliuoti realią žinių bazę.
- Paieškos ciklas su `None` sentineliu aiškiai atskiria „dar nerasta“ nuo bet kokios kitos reikšmės.
- Asistentas 0.3 atsakymus renka iš duomenų, o ne iš vis ilgėjančios `if` grandinės.

**Atmintinė:**

```python
message = input("Klausimas: ").strip().lower()

knowledge_base = {
    "tema": {"keywords": ["raktas"], "answer": "Atsakymas."},
}

answer = None
for topic in knowledge_base.values():
    for keyword in topic["keywords"]:
        if keyword in message:
            answer = topic["answer"]
            break
    if answer is not None:
        break

print(answer if answer else "Atsakymo žinių bazėje dar nėra.")
```

**Tvarkingas tekstas ir prasmingai pavadinti žodyno raktai paverčia žinias duomenimis, kuriuos gali augti be baimės sulaužyti programos logiką.**

## 20. Savirefleksija

1. Ką dabar galiu padaryti su tekstu ir žodynais, ko negalėjau prieš pamoką?
2. Kuri dalis buvo sunkiausia: teksto metodų grandinė, saugus žodyno skaitymas ar paieškos ciklas su `None`?
3. Ar galėčiau kitam žmogui paaiškinti, kodėl `if answer is not None: break` būtinas išoriniame paieškos cikle?
4. Kur savo kasdienybėje ar darbe galėčiau pritaikyti raktažodžiais valdomą žinių bazę?
5. Ką pakeisčiau savo Asistento 0.3 žinių bazėje, jei ji augtų iki 50 temų?

## 21. Namų darbas

### Privaloma – Asistento 0.3 žinių bazės plėtra

Paruošk Asistentą 0.3 su bent 10 temų, 3 raktažodžiais kiekvienai, šaltiniais ir 20 bandymų lentele. Pažymėk klaidingus atitikmenis ir patobulink raktažodžius. Bandymų lentelė turėtų turėti stulpelius: Nr., Klausimas, Laukiama tema, Gauta tema, Ar teisinga?

**Vertinimas (10 taškų):** `knowledge_base` struktūra ir bent 10 temų – 3; paieškos logika (`None` sentinelis, teisingas `break`) – 3; 20 bandymų lentelė su pažymėtais klaidingais atitikimais – 2; raktažodžių patobulinimas po analizės – 2.

### Pasirenkama – komandos ir statistika

Jei dar neįgyvendinai savarankiškai, pridėk komandas `/topics` ir `/history`, o taip pat `unanswered` sąrašo rodymą baigiant pokalbį.

**Vertinimas (5 taškai):** `/topics` veikia – 1; `/history` veikia – 2; `unanswered` sekimas ir rodymas – 2.

### Kūrybinis iššūkis – savo srities žinių bazė

Sukurk žinių bazę savo pasirinktai sričiai (pomėgis, mokykla, darbas, klubas) su bent 8 temomis, kiekvienai temai – bent 3 skirtingi raktažodžiai (įskaitant sinonimus ar šnekamosios kalbos variantus), ir parodyk bent vieną atvejį, kai du raktažodžiai sutampa; paaiškink, kodėl pasirinkai būtent tokią temų prioriteto tvarką.

**Vertinimas (5 taškai):** originalumas ir reali nauda – 2; raktažodžių įvairovė – 1; prioriteto paaiškinimas – 1; kodas paleidžiamas be klaidų – 1.

## 22. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Teksto metodų įvadas ir valymas | 50 min. | Pabrėžti nekintamumą – dažniausia painiava, kad `.lower()` be priskyrimo „neveikia“ |
| Pjūviai, paieška tekste ir dažnos klaidos | 40 min. | Vizualizuoti indeksus, ypač neigiamus ir pjūvio pabaigos taisyklę |
| Žodynai: kūrimas, skaitymas, `.get()`, `KeyError` | 55 min. | Parodyti `KeyError` gyvai, tada iškart pataisyti su `.get()` |
| Įdėtos struktūros ir žinių bazės modeliavimas | 45 min. | Naudoti medžio diagramą, kad kreipimosi lygiai netaptų mįsle |
| Paieškos algoritmas su `None` sentineliu | 40 min. | Rankiniu būdu „sekti“ cikle kintamųjų reikšmes lentoje |
| Kodo pavyzdžių galerija ir interaktyvios veiklos | 40 min. | Skatinti mokinius patiems nuspėti rezultatą prieš paleidžiant kodą |
| Žinių patikrinimas ir praktinės užduotys (A/B/C) | 70 min. | A/B/C lygius vertinti kaip vieną progresiją, ne atskirai |
| Mini projektas: Asistentas 0.3 | 80 min. | `history` struktūrą tikrinti rankiniu būdu – tai pagrindas 5 pamokos refaktoringui |
| Gilioji laboratorija (formatavimas, Unicode, `in`, `rank_topics`, derinimas) | 60 min. | Skirti stipresniems mokiniams arba namų darbo pratęsimui, jei laiko trūksta |

Vizualizacijos labiausiai padėtų ties teksto valymo konvejeriu ir žinių bazės medžio struktūra – šias dvi temas mokiniai painioja dažniausiai. Interaktyvų Python redaktorių verta įterpti po teksto metodų grandinės, po pirmo `KeyError` pavyzdžio, prieš paieškos ciklą ir mini projekte. Platformoje verta fiksuoti: pirmą sėkmingą `.get()` naudojimą, `KeyError`/`AttributeError` dažnį, testo rezultatą, praktinių užduočių (A/B/C) užbaigimą, mini projekto bandymų lentelės pilnumą ir savirefleksijos pasirinkimą.
