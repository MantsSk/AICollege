---
title: Klaidos, derinimas ir testai – sukurk asistentą, kuriuo galima pasitikėti
module: Python praktika
order: 7
---

# Klaidos, derinimas ir testai – sukurk asistentą, kuriuo galima pasitikėti

> **Trukmė:** 6 akademinės valandos. Pamokoje tyčia laužysi programą ir įrodysi, kad ji atsigauna.

## Trumpa anotacija

Iki šiol asistentas veikė tik tada, kai vartotojas elgėsi „teisingai“ – įvedė skaičių, kai jo prašė, ir nepakeitė `knowledge.json` failo. Realiame gyvenime taip nebūna: kažkas įves raidę vietoje skaičiaus, ištrins kablelį JSON faile arba paklaus tuščiu klausimu. Šioje pamokoje išmoksi skaityti Python traceback kaip informaciją, o ne bausmę, tikslingai gaudyti klaidas su `try/except/else/finally`, kurti savo klaidų klases, rašyti automatinius testus su `pytest` ir naudoti žurnalus (angl. *logging*) taip, kad jie padėtų derinti programą, bet neišduotų paslapčių. Rezultatas – Asistentas 0.6: versija, kuri neatsisako veikti vien todėl, kad kažkas ją bandė sulaužyti.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- perskaityti Python traceback nuo paskutinės eilutės ir surasti savo kodo vietą, kurioje kilo klaida;
- praktiškai atskirti sintaksės, vykdymo ir logikos klaidas;
- tikslingai naudoti `try/except/else/finally`, gaudydamas tik tas klaidas, kurias iš tikrųjų gali sutvarkyti;
- kurti savo klaidų klases su `raise` ir paaiškinti, kada verta atskirti domeno klaidą nuo bendros `Exception`;
- rašyti automatinius testus su `pytest`, naudodamas AAA (Arrange–Act–Assert) struktūrą;
- suplanuoti testus tipiniams, ribiniams ir klaidingiems atvejams, įskaitant parametrizuotus testus ir laikinus failus (`tmp_path`);
- naudoti `logging` vietoje atsitiktinių `print()`, neatskleisdamas API rakto, slaptažodžio ar viso vartotojo pokalbio;
- sukurti testuotą ir atsparią Asistento 0.6 versiją, kuri jokiu tipiniu vartotojo veiksmu neužstringa su nepaaiškintu traceback.

## Būtinos ankstesnės žinios

Iš šeštos pamokos turėtum turėti veikiančią Asistento 0.5 versiją: `assistant_core.py` su duomenų apdorojimo funkcijomis, `data/knowledge.json` su bent keliomis temomis ir (jei pasirinkai) `logs/history.json` pokalbio istorijai. Turėtum mokėti įkelti ir išsaugoti JSON su `json.load()` / `json.dump()`, dirbti su keliais per `pathlib.Path` ir paaiškinti, kodėl kodas ir duomenys laikomi atskiruose failuose. Jei šeštos pamokos projektas dar neveikia arba nesi tikras, ar `knowledge.json` struktūra teisinga, grįžk ir pasitikrink prieš tęsdamas – šioje pamokoje sąmoningai laužysime būtent tuos pačius failus, tad jie turi realiai egzistuoti ir veikti.

## 1. Įtraukianti pradžia: kai programa sudūžta priešais klientą

Įsivaizduok: parodei Asistentą 0.5 draugui. Jis paklausė „o kas jei aš parašysiu tuščią žinutę?“ ir paspaudė Enter neįvedęs nieko. Ekrane pasipylė raudonas tekstas su žodžiu `Traceback`, programa užsidarė, o draugas liko įsitikinęs, kad tavo asistentas „sugedo“. Iš tikrųjų nesugedo niekas – tiesiog programa nebuvo paruošta netikėtai įvesčiai.

Šiandien traceback nustosi būti baisus. Jis taps tavo pirmuoju įrankiu, pasakančiu, kur tiksliai ir kodėl kažkas nutiko ne taip.

```python
knowledge = {"kursas": {"answer": "Programa trunka 88 akademines valandas."}}
topic = input("Kokia tema? ")
print(knowledge[topic]["answer"])
```

Įvedus temą, kurios žinių bazėje nėra (pvz. `kaina`), programa nutrūksta su `KeyError`. Tai ne „programa sugedo“ – tai Python sąžiningai praneša: „šio rakto žodyne nėra“.

> **Išbandyk pats:** paleisk šį kodą ir įvesk temą, kurios tikrai nėra `knowledge` žodyne. Prieš skaitydamas tolesnes pamokos dalis, pabandyk savarankiškai atsakyti – kurioje eilutėje, tavo nuomone, klaida kilo, ir ką reikėtų padaryti, kad programa vietoj sudužimo parodytų draugišką žinutę?

## 2. Pagrindinės sąvokos

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| Traceback | Python pranešimas apie tai, kur ir kodėl kilo klaida | Įvykio protokolas su laiku ir vieta | Kaskart, kai programa nutrūksta su išimtimi | Skaitoma nuo viršaus, o ne nuo apačios |
| Sintaksės klaida (`SyntaxError`) | Kodas neatitinka Python kalbos taisyklių | Sakinys be veiksmažodžio | Programa dar nepradėjo veikti | Manoma, kad tai ta pati klaida kaip vykdymo metu |
| Vykdymo klaida (išimtis, pvz. `ValueError`) | Kodas taisyklingas, bet konkreti operacija nepavyko | Teisingai parašytas prašymas, kurio negalima įvykdyti | Vartotojo įvestis, failų operacijos, tinklas | Gaudoma per plačiai (`except Exception`) be priežasties |
| Logikos klaida | Programa vykdosi be klaidos, bet rezultatas neteisingas | Teisingai užrašyta, bet neteisinga formulė | Kai testai ar rankinė patikra parodo netikėtą rezultatą | Manoma, kad be traceback klaidos apskritai nėra |
| `try` / `except` | Bandymo blokas ir jo tvarkymo blokas | Bandymas atidaryti spyną – jei neveikia, žinai, ką daryti | Kai numatai konkretų nepavykimo būdą | Palikta be jokio `except`, arba gaudoma per daug |
| `else` | Vykdoma tik jei `try` bloke klaidos nebuvo | Tęsinys tik jei bandymas pavyko | Kai norima aiškiai atskirti „pavyko“ nuo „bandau tvarkyti klaidą“ | Visas kodas sukišamas į `try`, nors dalis jo nesukelia klaidų |
| `finally` | Vykdoma visada – ir pavykus, ir nepavykus | Šviesos išjungimas išeinant, kad ir kas nutiktų kambaryje | Uždarant išteklius, atlaisvinant resursus | Manoma, kad `finally` reikia kiekvienam `try` |
| Savo klaidos klasė (`class KnowledgeError(Exception)`) | Nauja išimties rūšis, pavadinta pagal domeno problemą | Specializuotas įspėjamasis ženklas, o ne bendras „pavojus“ | Kai reikia atskirti savo programos klaidą nuo Python vidinių | Visoms klaidoms naudojama viena bendra klasė |
| `pytest` ir `assert` | Įrankis ir raktažodis, tikrinantys, ar kodas elgiasi kaip tikimasi | Egzaminas, kurį kodas laiko kaskart pakeitus failą | Prieš įsitikinant, kad pakeitimas nieko nesulaužė | Testas tikrina vidinę realizaciją, ne elgesį |
| AAA (Arrange–Act–Assert) | Trijų dalių testo struktūra: paruošk, atlik, patikrink | Recepto struktūra: paruošk ingredientus, kepk, paragauk | Rašant bet kurį automatinį testą | Dalys sumaišomos, testas tampa sunkiai skaitomas |
| `logging` | Standartinis būdas fiksuoti programos įvykius su lygiais | Laivo žurnalas su data ir įvykio svarba | Derinant programą ir stebint gamybinę versiją | Į žurnalą patenka slaptažodžiai ar API raktai |

## 3. Vizualūs paaiškinimai

### Vizualizacija A – traceback skaitomas nuo apačios į viršų

```text
Traceback (most recent call last):
  File "main.py", line 9, in <module>
    print(get_answer("kaina"))
  File "assistant_core.py", line 4, in get_answer
    return knowledge[topic]["answer"]
           ~~~~~~~~~^^^^^^^
KeyError: 'kaina'
          ▲
          │  1) PRADĖK ČIA – klaidos tipas ir žinutė
          │
  assistant_core.py, eilutė 4
          │  2) TADA – konkreti eilutė, kurioje klaida iškilo
          │
  main.py, eilutė 9
          │  3) GALIAUSIAI – kvietimo vieta tavo faile
```

**Iliustracijos pavadinimas:** „Traceback skaitomas iš apačios“
**Ką ji turi parodyti:** kad paskutinė eilutė – klaidos tipas ir žinutė, o kelias į savo klaidą einamas kylant aukštyn per iškvietimų grandinę.
**Kokie elementai turi būti matomi:** traceback tekstas, rodyklė žemyn nuo paskutinės eilutės, trys sunumeruoti žingsniai skaitymo tvarka.
**Siūlomas vaizdo generavimo promptas:** „Vertikali edukacinė schema lietuvių kalba: Python traceback tekstas su rodykle, rodančia skaitymo tvarką nuo paskutinės eilutės (klaidos tipas) į viršų iki kvietimo vietos; trys sunumeruoti žingsniai, aiškus kontrastas.“

### Vizualizacija B – `try/except/else/finally` valdymo srautas

```text
                 ┌─────────────┐
                 │   try:      │
                 │  rizikingas │
                 │   kodas     │
                 └──────┬──────┘
                        │
        klaida? ────────┼──────── klaidos nėra?
           │                            │
           ▼                            ▼
   ┌───────────────┐            ┌───────────────┐
   │  except:      │            │  else:        │
   │  sutvarkyk     │            │  tęsk toliau  │
   │  konkrečią     │            │  su rezultatu │
   │  klaidą        │            └───────┬───────┘
   └───────┬───────┘                     │
           │                             │
           └───────────┬─────────────────┘
                        ▼
                ┌───────────────┐
                │  finally:     │
                │  vykdoma      │
                │  VISADA       │
                └───────────────┘
```

**Iliustracijos pavadinimas:** „Keturi keliai per try bloką“
**Ką ji turi parodyti:** kad `except` ir `else` yra alternatyvūs keliai (vykdomas tik vienas), o `finally` vykdomas nepriklausomai nuo pasirinkto kelio.
**Kokie elementai turi būti matomi:** `try` blokas viršuje, šakojimasis į `except` ir `else`, abu keliai susijungiantys prie `finally`.
**Siūlomas vaizdo generavimo promptas:** „Sprendimų medžio diagrama lietuvių kalba: try blokas viršuje šakojasi į except ir else priklausomai nuo to, ar kilo klaida, abi šakos susijungia į finally bloką apačioje; skirtingos spalvos kiekvienam blokui.“

### Vizualizacija C – raudona → žalia: testo ciklas

```text
1) PARAŠYK testą, kuris apibūdina norimą elgesį
        │
        ▼
2) PALEISK pytest  →  🔴 RAUDONA (testas nepavyksta – kodo dar nėra arba jis klaidingas)
        │
        ▼
3) PARAŠYK/PATAISYK kodą, kad elgesys atitiktų testą
        │
        ▼
4) PALEISK pytest  →  🟢 ŽALIA (testas pavyksta)
        │
        ▼
5) PALEISK VISUS testus – įsitikink, kad nieko kito nesulaužei
```

**Iliustracijos pavadinimas:** „Nuo raudono testo iki žalio“
**Ką ji turi parodyti:** kad testas rašomas prieš arba iškart po klaidos radimo, o „žalia“ būsena pasiekiama tik pataisius kodą, ne testą.
**Kokie elementai turi būti matomi:** penki sunumeruoti žingsniai, raudonos ir žalios spalvos žymos, rodyklės tarp žingsnių.
**Siūlomas vaizdo generavimo promptas:** „Vertikali penkių žingsnių proceso diagrama lietuvių kalba: rašau testą, raudonas nepavykęs testas, taisau kodą, žalias pavykęs testas, paleidžiu visus testus; raudona ir žalia spalvinės žymos prie atitinkamų žingsnių.“

## 4. Traceback: klaida kaip informacija, ne nuosprendis

Traceback yra Python būdas pasakyti: „štai tiksliai kur ir kodėl programa negalėjo tęsti“. Jis visada skaitomas nuo paskutinės eilutės aukštyn: paskutinėje eilutėje – klaidos tipas (pvz. `ValueError`, `KeyError`, `TypeError`) ir žinutė, o virš jos – eilučių grandinė, rodanti, kaip programa iki tos vietos priėjo.

```python
quantity = int("du")
```

```text
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    quantity = int("du")
ValueError: invalid literal for int() with base 10: 'du'
```

Eilutė po eilutės:

1. `ValueError: invalid literal for int() with base 10: 'du'` – klaidos tipas ir žinutė. Skaitome pirmą.
2. `quantity = int("du")` – tiksli eilutė, kurioje klaida kilo.
3. `File "main.py", line 1, in <module>` – failas ir vieta, kur ta eilutė yra.

`int("du")` sukelia `ValueError`, nes tekstas `"du"` neatitinka skaičiaus formato – Python nežino, kaip žodį paversti skaičiumi.

Trys klaidų rūšys, su kuriomis susidursi nuolat:

- **Sintaksės klaida (`SyntaxError`)** – kodas neatitinka Python kalbos taisyklių ir programa apskritai nepradeda veikti, net iki pirmos eilutės. Pavyzdys: pamirštas dvitaškis po `if` arba netinkamai uždaryti skliaustai.
- **Vykdymo klaida (išimtis)** – kodas sintaksiškai teisingas, bet konkreti operacija su konkrečiais duomenimis nepavyksta vykdymo metu, pvz. `int("du")` arba kreipimasis į neegzistuojantį žodyno raktą.
- **Logikos klaida** – programa įvykdoma be jokios klaidos, bet rezultatas neteisingas. Pavyzdžiui, formulė `total = price + quantity` vietoje `price * quantity` niekada nesukels traceback, bet skaičiuos blogai.

```python
def calculate_total(price, quantity):
    return price + quantity  # logikos klaida: turėtų būti daugyba

print(calculate_total(10, 3))
```

```text
13
```

Rezultatas atrodo kaip skaičius ir programa neužstringa, bet `13` yra neteisingas – teisingas atsakymas būtų `30`. Būtent logikos klaidas geriausiai pagauna automatiniai testai, apie kuriuos kalbėsime šios pamokos antroje pusėje.

> **Dažna klaida:** traceback skaitomas nuo pirmos eilutės žemyn, tarsi tai būtų pasakojimas. Iš tikrųjų svarbiausia informacija – paskutinėje eilutėje. Pradėk nuo jos, tada kilk aukštyn ieškodamas savo failo pavadinimo.

**Mini užduotis.** Paleisk šį kodą ir, remdamasis traceback, atsakyk: koks klaidos tipas, kurioje eilutėje ji kilo ir ką reikėtų pakeisti, kad klaidos nebeliktų.

```python
prices = {"kava": 2.50, "arbata": 2.00}
print(prices["sultys"])
```

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

Klaida – `KeyError: 'sultys'`, nes žodyne `prices` tokio rakto nėra. Ji kyla eilutėje `print(prices["sultys"])`. Sprendimas – arba pridėti raktą `"sultys"` į žodyną, arba prieš kreipiantis patikrinti `"sultys" in prices`, arba naudoti `prices.get("sultys", "nėra kainos")`.

```python
prices = {"kava": 2.50, "arbata": 2.00}
print(prices.get("sultys", "Tokios prekės kainos dar neturime."))
```

</details>

## 5. `try` / `except` / `else` / `finally` – tikslingas klaidų gaudymas

`try/except` leidžia numatyti, kuri operacija gali nepavykti, ir aiškiai pasakyti, ką daryti tuo atveju. Svarbiausia taisyklė – gaudyk tik tas klaidas, kurias iš tikrųjų gali sutvarkyti, ir tik ten, kur žinai, kas gali nutikti.

```python
def ask_rating() -> int:
    while True:
        try:
            rating = int(input("Įvertinimas 1–10: "))
            if not 1 <= rating <= 10:
                raise ValueError("įvertinimas už ribų")
        except ValueError:
            print("Įvesk sveiką skaičių nuo 1 iki 10.")
        else:
            return rating
```

Eilutė po eilutės:

1. `while True:` – kartojame, kol negausime tinkamos reikšmės; funkcija pati nusprendžia, kada baigti, per `return`.
2. `rating = int(input(...))` – bandome konvertuoti vartotojo įvestį. Jei tekstas ne skaičius, `int()` iškart sukels `ValueError`, ir tolesnės `try` bloko eilutės nebebus vykdomos.
3. `if not 1 <= rating <= 10: raise ValueError(...)` – net jei konvertavimas pavyko, patys tikslingai sukeliame klaidą, kai skaičius už ribų. Tai leidžia tą pačią `except` šaką panaudoti abiem netinkamos įvesties atvejams.
4. `except ValueError:` – gaudome tik šią konkrečią klaidą, parodome suprantamą žinutę ir ciklas kartojasi.
5. `else: return rating` – vykdoma tik tada, jei `try` blokas baigėsi be klaidos. Grąžiname tinkamą reikšmę ir funkcija baigiasi.

`else` čia naudingas, nes aiškiai atskiria „sėkmės“ kodą nuo pačios rizikingos operacijos – jei `return rating` būtų paskutinė `try` bloko eilutė, būtų sunkiau iš karto pamatyti, kuri dalis gali sukelti klaidą, o kuri – ne.

`finally` vykdomas visada, nesvarbu, ar klaida kilo, ar ne – naudingas uždarant išteklius (failą, tinklo ryšį, laikiną užraktą), kurie turi būti sutvarkyti bet kuriuo atveju:

```python
file = open("data/notes.txt", "a", encoding="utf-8")
try:
    file.write("Nauja pastaba\n")
finally:
    file.close()
```

Failams paprastai patogiau ir saugiau naudoti `with`, nes jis pats pasirūpina uždarymu net kilus klaidai – `finally` daugiausia prireikia tada, kai valdai išteklių, kuris neturi savo `with` sintaksės.

> **Dažna klaida:** plikas `except:` (be klaidos tipo) sugauna absoliučiai viską – ir tavo numatytą `ValueError`, ir netikėtą programavimo klaidą, pvz. rašybos klaidą kintamojo varde. Tokiu atveju programa „veikia“ toliau, bet tyliai slepia rimtą problemą, kurią būtų daug lengviau pastebėti su nepagautu traceback.

```python
try:
    rating = int(input("Įvertinimas: "))
except:  # pavojinga: sugaus ir ValueError, ir bet kokią kitą klaidą
    print("Kažkas negerai")
```

Pataisymas – gaudyk konkrečią klaidą:

```python
try:
    rating = int(input("Įvertinimas: "))
except ValueError:
    print("Įvesk skaičių.")
```

**Mini užduotis.** Parašyk funkciją `ask_price()`, kuri kartoja klausimą „Kaina: “, kol vartotojas įveda teigiamą dešimtainį skaičių. Naudok `try/except/else`, o klaidą, kai skaičius neigiamas, sukelk pats su `raise ValueError`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
def ask_price() -> float:
    while True:
        try:
            price = float(input("Kaina: "))
            if price <= 0:
                raise ValueError("kaina turi būti teigiama")
        except ValueError:
            print("Įvesk teigiamą skaičių, pvz. 12.5.")
        else:
            return price
```

Struktūra ta pati kaip `ask_rating()`: konvertavimas ir taisyklės patikra abi gali sukelti `ValueError`, o `else` grąžina rezultatą tik tada, kai abi sąlygos tenkinamos.

</details>

## 6. Savo klaidų klasės su `raise`

Kartais standartinės Python klaidos (`ValueError`, `KeyError`, `TypeError`) nepasako, kas konkrečiai tavo programos kontekste nutiko. Kai kviečiantis kodas turi atskirti domeno problemą (pvz. „žinių bazėje trūksta atsakymo“) nuo, tarkime, disko gedimo ar tinklo klaidos, naudinga sukurti savo klaidos klasę.

```python
class KnowledgeError(Exception):
    """Žinių bazės struktūra netinkama."""


def require_answer(topic_name: str, topic: dict) -> None:
    if not topic.get("answer"):
        raise KnowledgeError(f"Temai '{topic_name}' trūksta atsakymo")
```

`KnowledgeError` paveldi iš `Exception` – tai reiškia, kad ji elgiasi kaip bet kuri kita Python klaida (ją galima sugauti su `except`, ji turi žinutę), bet jos pavadinimas iš karto pasako, apie kokią problemą kalbama. Kviečiantis kodas gali ją apdoroti atskirai nuo, pavyzdžiui, `FileNotFoundError`:

```python
try:
    require_answer("kursas", {"keywords": ["kursas"]})
except KnowledgeError as error:
    print(f"Žinių bazės klaida: {error}")
```

```text
Žinių bazės klaida: Temai 'kursas' trūksta atsakymo
```

Didesniame projekte klaidas dažnai organizuoji į hierarchiją: bendrą klaidą failo problemoms (failas nerastas, sugadintas JSON) ir atskirą – žinių struktūros problemoms (trūksta lauko, netinkamas tipas). Taip kviečiantis kodas gali nuspręsti, ar klaida atkuriama (pvz. siūlyti atsarginę kopiją), ar ne:

```python
class KnowledgeFileError(Exception):
    """Nepavyko rasti, perskaityti ar išanalizuoti žinių failą."""


class MissingAnswerError(KnowledgeError):
    """Konkreti KnowledgeError atmaina – temai trūksta atsakymo lauko."""
```

`MissingAnswerError` paveldi iš `KnowledgeError`, todėl bendras `except KnowledgeError` sugaus ir ją, bet prireikus galima tvarkyti tiksliau.

> **Dažna klaida:** viena bendra klaidos klasė naudojama absoliučiai viskam. Tada kviečiantis kodas negali atskirti, ar reikia siūlyti atkurti failą iš atsarginės kopijos, ar tiesiog paprašyti vartotojo pataisyti temą – jam telieka viena neaiški žinutė visiems atvejams.

**Mini užduotis.** Sukurk klaidos klasę `InvalidRatingError(Exception)` ir funkciją `require_valid_rating(rating: int) -> None`, kuri sukelia šią klaidą, jei `rating` nėra tarp 1 ir 10.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
class InvalidRatingError(Exception):
    """Įvertinimas už leidžiamų ribų."""


def require_valid_rating(rating: int) -> None:
    if not 1 <= rating <= 10:
        raise InvalidRatingError(f"Įvertinimas {rating} turi būti nuo 1 iki 10")
```

</details>

## 7. Grynos funkcijos ir pirmieji testai su `pytest`

Grynoji funkcija (be `input()`, `print()` ar failų operacijų) yra lengviausiai testuojama, nes jos rezultatas priklauso tik nuo įvesties – nereikia imituoti klaviatūros ar ekrano.

`assistant_core.py`:

```python
def normalize_text(text: str) -> str:
    return " ".join(text.strip().lower().split())


def is_exit_command(text: str) -> bool:
    return normalize_text(text) in {"baigti", "/quit", "exit"}
```

`test_assistant_core.py`:

```python
from assistant_core import is_exit_command, normalize_text


def test_normalize_text_removes_extra_spaces():
    assert normalize_text("  Labas   Rytas ") == "labas rytas"


def test_exit_command_accepts_quit():
    assert is_exit_command(" /QUIT ") is True


def test_regular_message_is_not_exit():
    assert is_exit_command("Kokia kaina?") is False
```

Terminale:

```bash
python -m pip install pytest
python -m pytest -q
```

```text
...                                                                      [100%]
3 passed in 0.04s
```

Kiekvienas taškas atitinka po vieną pavykusį testą. Testo pavadinimas aprašo elgesį, kurį jis tikrina (`test_exit_command_accepts_quit`), o ne implementacijos detalę (pvz. `test_line_5`) – taip skaitydamas testų sąrašą iš karto matai, kokį elgesį programa garantuoja.

> **Dažna klaida:** testas rašomas taip, kad tikrina, kaip funkcija *implementuota* (pvz. „ar viduje iškviestas `.strip()`“), o ne ką ji *daro* iš kviečiančio kodo perspektyvos. Jei vėliau pakeisi implementaciją, bet elgesys liks tas pats, toks testas be reikalo sulūš.

**Mini užduotis.** Parašyk funkciją `count_words(text: str) -> int`, grąžinančią žodžių skaičių, ir bent du testus jai: vieną tipiniam sakiniui, kitą – tuščiam tekstui.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
def count_words(text: str) -> int:
    return len(text.split())
```

```python
def test_count_words_counts_regular_sentence():
    assert count_words("Kokia šiandien kaina?") == 3


def test_count_words_empty_text_is_zero():
    assert count_words("") == 0
```

</details>

## 8. AAA struktūra ir ribiniai atvejai

Testą patogu mąstyti trimis dalimis: **Arrange** – paruošk pradinius duomenis, **Act** – atlik veiksmą, kurį tikrini, **Assert** – patikrink rezultatą. Ši struktūra padeda net ir sudėtingesnį testą skaityti iš karto, nesigilinant į kiekvieną eilutę.

```python
def test_unknown_topic_returns_fallback():
    # Arrange – paruošiame žinių bazę ir žinutę
    knowledge = {"kursas": {"keywords": ["kursas"], "answer": "88 val."}}
    message = "Koks šiandien oras?"

    # Act – atliekame veiksmą, kurį testuojame
    answer, topic = find_answer(message, knowledge)

    # Assert – patikriname, ar rezultatas toks, kokio tikimės
    assert answer == "Atsakymo dar nežinau."
    assert topic is None
```

Komentarai `# Arrange`, `# Act`, `# Assert` kode nebūtini – svarbu, kad struktūra būtų aiški ir be jų, tiesiog atskiriant blokus tuščia eilute.

Kiekvienai funkcijai verta iš anksto suplanuoti, kokias atvejų klases testuosi:

| Atvejo tipas | Ką jis parodo | Pavyzdys `normalize_text` funkcijai |
|---|---|---|
| Tipinis | Įprastas, kasdienis naudojimas | `"Kokia kaina?"` → `"kokia kaina?"` |
| Ribinis | Kraštinės reikšmės: tuščia, vienas simbolis, labai ilgas tekstas | `""` → `""`, tekstas iš 5000 simbolių |
| Klaidingas | Netinkamas tipas ar netikėta struktūra | `None` vietoje teksto – ar funkcija tai tvarko, ar sukelia klaidą? |
| Su lietuviškomis raidėmis | Ar veikia ne tik su ASCII simboliais | `"Ąžuolas Šalia Ežero"` → `"ąžuolas šalia ežero"` |

> **Dažna klaida:** testuojamas tik tas atvejis, kurį jau žinai, kad veikia. Tokie testai patvirtina, kad kodas veikia taip, kaip jį parašei – bet nieko nepasako apie ribinius ar klaidingus atvejus, kuriuose realūs vartotojai dažniausiai ir suranda problemas.

**Mini užduotis.** Parašyk testą `test_normalize_text_handles_lithuanian_letters`, kuris AAA struktūra patikrina, kad `normalize_text("ĄŽUOLAS")` grąžina `"ąžuolas"`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
def test_normalize_text_handles_lithuanian_letters():
    # Arrange
    raw_text = "ĄŽUOLAS"

    # Act
    result = normalize_text(raw_text)

    # Assert
    assert result == "ąžuolas"
```

</details>

## 9. Žurnalai (`logging`) vietoje atsitiktinių `print`

`print()` puikiai tinka mokymuisi, bet realioje programoje reikia žinoti, KADA ir KIEK SVARBUS buvo įvykis – tam skirtas `logging` su lygiais (`INFO`, `WARNING`, `ERROR`) ir laiko žyma.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logging.info("Žinių bazė įkelta")
logging.warning("Tema nerasta")
```

```text
2026-07-20 10:15:03,120 INFO Žinių bazė įkelta
2026-07-20 10:15:07,442 WARNING Tema nerasta
```

Svarbiausia taisyklė: **niekada nerašyk į žurnalą API rakto, slaptažodžio, viso asmeninio pokalbio turinio ar kitų jautrių duomenų.** Vartotojui rodyk suprantamą, trumpą žinutę; kūrėjui žurnale palik pakankamai techninės informacijos problemai atsekti – bet be konkretaus turinio, kuris gali būti asmeninis ar slaptas.

```python
# Blogai – visas klausimas ir raktas patenka į žurnalą
logging.info(f"Klausimas: {user_question}, raktas: {api_key}")

# Geriau – tik įvykis ir techninė informacija, be turinio ir be paslapčių
logging.info("Gautas klausimas, ilgis %d simbolių", len(user_question))
logging.error("Nepavyko prisijungti prie API, būsenos kodas: %s", status_code)
```

> **Dažna klaida:** derinimo metu greitam patikrinimui parašomas `logging.info(f"Duomenys: {api_key}")`, pamirštama jį pašalinti, ir raktas lieka žurnalo faile, kuris gali patekti į versijų valdymo sistemą ar būti persiųstas kolegai.

**Mini užduotis.** Žemiau pateiktas žurnalo įrašas nutekina jautrią informaciją. Perrašyk jį taip, kad liktų naudingas derinimui, bet neatskleistų slaptažodžio.

```python
logging.info(f"Prisijungimo bandymas: vartotojas={username}, slaptazodis={password}")
```

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
logging.info("Prisijungimo bandymas: vartotojas=%s", username)
```

Slaptažodžio žurnale apskritai nereikia – pakanka žinoti, kuris vartotojas bandė prisijungti. Jei reikia užfiksuoti nesėkmę, pakanka `logging.warning("Nepavykęs prisijungimas: vartotojas=%s", username)` be jokios slaptos reikšmės.

</details>

## 10. Įvairūs kodo pavyzdžiai

### Minimalus pavyzdys

**Problema:** apsaugoti dalybą nuo nulio.

```python
def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

```text
5.0
None
```

**Paaiškinimas:** funkcija grąžina `None`, o ne sukelia klaidą kviečiančiam kodui. **Patobulinimas:** pridėk žurnalo įrašą, kai dalyba iš nulio.

### Kasdienis pavyzdys – amžiaus patikra

```python
def parse_age(text: str) -> int:
    age = int(text)
    if age < 0 or age > 130:
        raise ValueError(f"Neįtikėtinas amžius: {age}")
    return age

try:
    print(parse_age("27"))
    print(parse_age("-5"))
except ValueError as error:
    print(f"Netinkama įvestis: {error}")
```

```text
27
Netinkama įvestis: Neįtikėtinas amžius: -5
```

**Patobulinimas:** parašyk tris testus – tipiniam, ribiniam (`0` ir `130`) ir klaidingam amžiui.

### Darbo pavyzdys – konfigūracijos patikra

```python
class ConfigError(Exception):
    """Konfigūracijos failui trūksta būtino lauko."""


def require_fields(config: dict, fields: list[str]) -> None:
    missing = [field for field in fields if field not in config]
    if missing:
        raise ConfigError(f"Trūksta laukų: {', '.join(missing)}")

config = {"model": "gpt", "timeout": 10}
require_fields(config, ["model", "timeout", "api_key"])
```

```text
ConfigError: Trūksta laukų: api_key
```

**Patobulinimas:** prieš `raise` pridėk `logging.error(...)` su trūkstamų laukų sąrašu, bet be pačių reikšmių.

### Duomenų ir AI pavyzdys – modelio atsakymo patikra

```python
class ModelResponseError(Exception):
    """AI modelio atsakymo struktūra netinkama."""


def extract_confidence(response: dict) -> float:
    if "confidence" not in response:
        raise ModelResponseError("Atsakyme trūksta 'confidence' lauko")
    confidence = response["confidence"]
    if not isinstance(confidence, (int, float)):
        raise ModelResponseError("'confidence' turi būti skaičius")
    return float(confidence)

print(extract_confidence({"confidence": 0.87}))
```

```text
0.87
```

**Patobulinimas:** parašyk testus trims atvejams – lauko trūksta, laukas netinkamo tipo, laukas tinkamas.

### Klaidingas pavyzdys – pataisyk

```python
def load_setting(name):
    try:
        return settings[name]
    except:
        return None
```

Šis kodas gaudo absoliučiai viską – jei `settings` dar neapibrėžtas kintamasis, `NameError` bus paslėptas taip pat tyliai, kaip ir laukiamas `KeyError`. Klaidą pastebėsi tik tada, kai `load_setting()` visada tyliai grąžins `None`, o priežastis liks nežinoma.

Pataisymas:

```python
def load_setting(name: str, settings: dict):
    try:
        return settings[name]
    except KeyError:
        return None
```

## 11. Interaktyvios veiklos

### 1. Nuspėk rezultatą

```python
try:
    value = int("7")
except ValueError:
    print("A")
else:
    print("B")
finally:
    print("C")
```

A. Tik `B`
B. `B`, tada `C`
C. `A`, tada `C`
D. Tik `A`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** `int("7")` pavyksta be klaidos, todėl `except` nevykdomas. `else` vykdomas, nes klaidos nebuvo (parodo `B`), o `finally` vykdomas visada (parodo `C`).

</details>

### 2. Užpildyk trūkstamą kodą

```python
try:
    quantity = int(input("Kiekis: "))
____ ValueError:
    print("Įvesk sveiką skaičių.")
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
except ValueError:
```

Reikia gaudyti būtent tą klaidą, kurią sukelia netinkamas `int()` argumentas.

</details>

### 3. Surask klaidą

```python
def get_topic_answer(knowledge, topic_name):
    try:
        return knowledge[topic_name]["answer"]
    except:
        print("Klaida")
```

Nustatyk problemą, paaiškink ir pataisyk.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Plikas `except:` sugauna bet kokią klaidą, ne tik tikėtiną `KeyError`. Jei `knowledge` netikėtai būtų `None`, gautum tą pačią neinformatyvią žinutę „Klaida“ vietoje aiškaus traceback, padedančio surasti tikrąją priežastį.

```python
def get_topic_answer(knowledge: dict, topic_name: str) -> str | None:
    try:
        return knowledge[topic_name]["answer"]
    except KeyError:
        print(f"Temos '{topic_name}' žinių bazėje nėra.")
        return None
```

</details>

### 4. Sudėliok teisingą tvarką

```text
2. paleisk pytest ir pamatyk žalią rezultatą
1. parašyk testą, kuris apibūdina norimą elgesį
3. paleisk visus testus, ne tik naują
0. pataisyk kodą, kad testas pavyktų
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

1. Parašyk testą, kuris apibūdina norimą elgesį.
2. Pataisyk kodą, kad testas pavyktų.
3. Paleisk `pytest` ir pamatyk žalią rezultatą.
4. Paleisk visus testus, ne tik naują.

Testas turi nepavykti pirma (arba dėl klaidos, arba dėl kodo trūkumo) – tada matai, kad jis iš tikrųjų ką nors tikrina.

</details>

### 5. Pasirink tinkamą sprendimą

Funkcija turi konvertuoti vartotojo įvestą tekstą į sveiką skaičių ir aiškiai reaguoti, jei tai nepavyksta. Kuris variantas geriausias?

A. `except:` be klaidos tipo
B. `except Exception:` visoms galimoms klaidoms
C. `except ValueError:` konkrečiai šiai klaidai

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**C.** `int()` netinkamam tekstui visada sukelia būtent `ValueError` – gaudant tik ją, kitos, nenumatytos klaidos (pvz. programavimo klaida kitoje kodo vietoje) liks matomos, o ne paslėptos.

</details>

### 6. Parašyk pats

Parašyk funkciją `require_non_empty(text: str) -> None`, kuri sukelia savo klaidos klasę `EmptyInputError`, jei `text.strip()` yra tuščias. Parašyk jai bent du testus: vieną, kuris patikrina, kad tuščias tekstas sukelia klaidą, ir kitą, kuris patikrina, kad tekstas su turiniu klaidos nesukelia.

### 7. Patobulink kodą

```python
def load_history(path):
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        print(e)
        return None
```

Šis kodas gaudo bet kokią klaidą su ta pačia bendra žinute. Perrašyk taip, kad atskirai tvarkytum `FileNotFoundError` (parodyk draugišką žinutę, kad failo dar nėra) ir kitas galimas klaidas (pvz. leidimų problemą) – ir pridėk vieną testą su laikinu neegzistuojančiu keliu.

## 12. Žinių patikrinimas prieš platformos testą

Pirmiausia atsakyk neužleisdamas atsakymų.

1. Kuo `SyntaxError` iš esmės skiriasi nuo vykdymo klaidos, pvz. `ValueError`?
2. Kada verta naudoti `finally`, o ne vien `except`?
3. Kodėl `require_answer()` kelia savo `KnowledgeError`, o ne tiesiog grąžina `None`?
4. Ką grąžins `normalize_text("  Kokia   KAINA?  ")`, jei `normalize_text` apibrėžta kaip pamokoje?
5. Kam skirtas dekoratorius `@pytest.mark.parametrize`?
6. Kam testuose naudojamas `tmp_path`?
7. Kodėl testuose AI klientui geriau naudoti netikrą (angl. *fake*) objektą su `SimpleNamespace`, o ne tikrą tinklo užklausą?
8. Ką `caplog` leidžia patikrinti automatiniame teste?
9. Kokia komanda paleidžia visus `pytest` testus tyliuoju (glaustu) režimu?
10. Kodėl vartotojui rodoma klaidos žinutė turi skirtis nuo to, kas įrašoma į žurnalą?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymus ir paaiškinimus</summary>

1. `SyntaxError` reiškia, kad kodas neatitinka Python kalbos taisyklių ir programa apskritai nepradeda vykdytis; vykdymo klaida (pvz. `ValueError`) kyla jau veikiančioje programoje, konkrečiai operacijai su konkrečiais duomenimis nepavykus.
2. Kai reikia garantuotai atlikti veiksmą (pvz. uždaryti resursą) nepriklausomai nuo to, ar `try` bloke kilo klaida, ar ne.
3. Savo klaida leidžia kviečiančiam kodui tiksliai atskirti „žinių bazėje trūksta atsakymo“ nuo kitų problemų ir tinkamai sureaguoti; `None` neatskleistų priežasties.
4. `"kokia kaina?"` – `strip()` pašalina kraštinius tarpus, `lower()` pažemina raides, o `split()`/`" ".join()` sutraukia kelis tarpus tarp žodžių į vieną.
5. Jis leidžia vieną testo funkciją paleisti su keliais skirtingais duomenų rinkiniais, parodydamas, kad ta pati taisyklė galioja visai atvejų šeimai, be kodo pasikartojimo.
6. `tmp_path` sukuria laikiną, testui skirtą katalogą diske, kad testas galėtų rašyti ir skaityti failus nepaliesdamas tikrų projekto duomenų.
7. Kad testas būtų greitas, nepriklausomas nuo interneto ryšio ir nekainuotų realių pinigų už kiekvieną paleidimą.
8. `caplog` leidžia patikrinti, kokie žurnalo įrašai buvo sukurti vykdant testuojamą kodą – pavyzdžiui, ar žurnale nėra API rakto ar viso vartotojo klausimo.
9. `python -m pytest -q`.
10. Nes vartotojui reikia suprantamos, veiksmingos žinutės be techninių detalių, o žurnalui – pakankamai technine kalbos informacijos problemai atsekti, bet be jautrių duomenų.

</details>

## 13. Praktinės užduotys

### A lygis – atspari skaičiuoklė

**Sąlyga:** parašyk funkciją `safe_divide(a: float, b: float) -> float`, kuri sukelia savo klaidą `DivisionByZeroInputError`, jei `b == 0`. Tada parašyk vartotojo įvesties ciklą, kuris kartoja klausimą, kol gaus du tinkamus skaičius, atskirai tvarkydamas netinkamą tekstą (`ValueError` iš `float()`) ir dalybą iš nulio. Parašyk bent 6 testus pačiai `safe_divide` funkcijai.
**Pavyzdinė įvestis:** vartotojas iš pradžių įveda `abc`, tada `10` ir `0`, galiausiai `10` ir `2`.
**Laukiamas rezultatas:** po netinkamų bandymų programa parodo aiškias žinutes ir galiausiai `Rezultatas: 5.0`.
**Užuomina:** dalybos iš nulio klaidą sukelk pačioje `safe_divide` funkcijoje su `raise`, o ne tikrindamas `b == 0` kiekvieną kartą kviečiančiame kode.

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

`calculator.py`:

```python
class DivisionByZeroInputError(Exception):
    """Vartotojas bandė dalyti iš nulio."""


def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroInputError("Negalima dalyti iš nulio")
    return a / b


def ask_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Įvesk skaičių, pvz. 10 arba 2.5.")


def run_calculator() -> None:
    first = ask_number("Pirmas skaičius: ")
    while True:
        second = ask_number("Antras skaičius: ")
        try:
            result = safe_divide(first, second)
        except DivisionByZeroInputError as error:
            print(f"Klaida: {error}")
        else:
            print(f"Rezultatas: {result}")
            break


if __name__ == "__main__":
    run_calculator()
```

`test_calculator.py`:

```python
import pytest

from calculator import DivisionByZeroInputError, safe_divide


def test_safe_divide_typical_case():
    assert safe_divide(10, 2) == 5.0


def test_safe_divide_with_negative_numbers():
    assert safe_divide(-10, 2) == -5.0


def test_safe_divide_with_float_result():
    assert safe_divide(7, 2) == 3.5


def test_safe_divide_by_one_returns_same_number():
    assert safe_divide(9, 1) == 9.0


def test_safe_divide_zero_by_number_is_zero():
    assert safe_divide(0, 5) == 0.0


def test_safe_divide_by_zero_raises_custom_error():
    with pytest.raises(DivisionByZeroInputError):
        safe_divide(10, 0)
```

`pytest.raises(...)` patikrina, kad blokas viduje iš tikrųjų sukelia nurodytą klaidą – jei klaida nekyla, testas nepavyksta. **Papildomas iššūkis:** pridėk testą, kuris patikrina konkretų klaidos pranešimo tekstą su `pytest.raises(...) as exc_info` ir `str(exc_info.value)`.

</details>

### B lygis – JSON įkėlimo diagnostika

**Sąlyga:** parašyk funkciją `load_knowledge_or_raise(path: Path) -> dict`, kuri atskirai atpažįsta tris problemas: neegzistuojantį failą, sintaksiškai sugadintą JSON ir netinkamą žinių struktūrą (trūksta `answer` lauko). Kiekvienam atvejui sukelk savo klaidą su aiškiu, skirtingu pranešimu. Parašyk testus su `tmp_path` – po vieną kiekvienam atvejui.
**Pavyzdinė įvestis:** kelias į failą, kurio nėra; failas su tekstu `{"kursas": {"answer": }` (sugadintas JSON); failas su `{"kursas": {"keywords": ["a"]}}` (trūksta `answer`).
**Laukiamas rezultatas:** trys skirtingos, aiškios klaidos – `KnowledgeFileError` failo problemoms, `KnowledgeError` struktūros problemai.
**Užuomina:** JSON sintaksės klaidą Python praneša per `json.JSONDecodeError` – tai irgi reikia sugauti ir paversti savo, vartotojui suprantama klaida.

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

`knowledge_loader.py`:

```python
import json
from pathlib import Path


class KnowledgeFileError(Exception):
    """Nepavyko rasti, perskaityti ar išanalizuoti žinių failą."""


class KnowledgeError(Exception):
    """Žinių bazės struktūra netinkama."""


def load_knowledge_or_raise(path: Path) -> dict:
    if not path.exists():
        raise KnowledgeFileError(f"Žinių failas nerastas: {path}")

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise KnowledgeFileError(f"Žinių failas sugadintas: {error}") from error

    for topic_name, topic in data.items():
        if not topic.get("answer"):
            raise KnowledgeError(f"Temai '{topic_name}' trūksta atsakymo")

    return data
```

`test_knowledge_loader.py`:

```python
import pytest

from knowledge_loader import KnowledgeError, KnowledgeFileError, load_knowledge_or_raise


def test_missing_file_raises_file_error(tmp_path):
    missing_path = tmp_path / "knowledge.json"

    with pytest.raises(KnowledgeFileError):
        load_knowledge_or_raise(missing_path)


def test_broken_json_raises_file_error(tmp_path):
    path = tmp_path / "knowledge.json"
    path.write_text('{"kursas": {"answer": }', encoding="utf-8")

    with pytest.raises(KnowledgeFileError):
        load_knowledge_or_raise(path)


def test_missing_answer_field_raises_knowledge_error(tmp_path):
    path = tmp_path / "knowledge.json"
    path.write_text('{"kursas": {"keywords": ["a"]}}', encoding="utf-8")

    with pytest.raises(KnowledgeError):
        load_knowledge_or_raise(path)


def test_valid_file_loads_successfully(tmp_path):
    path = tmp_path / "knowledge.json"
    path.write_text('{"kursas": {"answer": "88 val."}}', encoding="utf-8")

    knowledge = load_knowledge_or_raise(path)

    assert knowledge["kursas"]["answer"] == "88 val."
```

`from error` išlaiko originalią `json.JSONDecodeError` kaip priežastį (`__cause__`), todėl traceback vis tiek parodys, kas iš tikrųjų nutiko, net kelią klaidą apvyniojus savo klase. **Papildomas iššūkis:** pridėk `KnowledgeFileError`, kai `keywords` yra tekstas, o ne sąrašas.

</details>

### C lygis – regresijos testas

**Sąlyga:** ankstesnėje asistento versijoje (5-oje pamokoje) `is_exit_command` funkcijos idėja buvo tikrinti tik lygiai sutampantį tekstą. Rask panašią klaidą – parašyk `is_exit_command`, kuri KLAIDINGAI netinka su papildomu tarpu gale (`"baigti "` neturėtų būti laikoma išėjimo komanda pagal blogą versiją, bet turėtų pagal reikalavimus). Pirmiausia parašyk testą, kuris tai atskleidžia (jis turi nepavykti su blogu kodu), tada pataisyk kodą naudodamas jau žinomą `normalize_text()`, ir įsitikink, kad testas tampa žalias.
**Laukiamas rezultatas:** trumpas „buvo – tikėjausi – pataisiau“ aprašymas ir testas, kuris iš pradžių raudonas, o po pataisymo – žalias.
**Užuomina:** klaida atsiranda todėl, kad palyginimas atliekamas su neapdorotu tekstu, o ne su `normalize_text()` rezultatu.

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

**Buvo** (klaidinga versija, neapdoroja teksto prieš palyginimą):

```python
def is_exit_command(text: str) -> bool:
    return text in {"baigti", "/quit", "exit"}
```

**Testas, kuris atskleidžia klaidą** (parašomas PIRMA, prieš taisant kodą):

```python
def test_exit_command_ignores_extra_spaces_and_case():
    assert is_exit_command(" Baigti ") is True
```

Su „buvo“ versija testas nepavyksta:

```text
FAILED test_assistant_core.py::test_exit_command_ignores_extra_spaces_and_case
AssertionError: assert False is True
```

**Tikėjausi:** kad `" Baigti "` (su tarpais ir didžiąja raide) bus atpažinta kaip išėjimo komanda, nes vartotojai retai rašo lygiai `"baigti"` be jokių tarpų.

**Pataisiau** – naudojant jau turimą `normalize_text()`:

```python
def normalize_text(text: str) -> str:
    return " ".join(text.strip().lower().split())


def is_exit_command(text: str) -> bool:
    return normalize_text(text) in {"baigti", "/quit", "exit"}
```

Po pataisymo tas pats testas tampa žalias:

```text
.                                                                        [100%]
1 passed in 0.01s
```

**Papildomas iššūkis:** paleisk visą testų rinkinį (ne tik naują testą) ir įsitikink, kad pataisymas nesulaužė jokio kito, anksčiau žalio testo.

</details>

## 14. Mini projektas: Asistentas 0.6

### 1. Projekto situacija

Asistentas 0.5 jau moka skaityti ir rašyti duomenis failuose, bet vis dar pasitiki, kad viskas bus tvarkinga: kad `knowledge.json` egzistuos, kad jo sintaksė bus teisinga, kad kiekviena tema turės `answer` lauką, o vartotojas niekada neįves nei tuščio, nei itin ilgo klausimo. Draugas ar kolega, bandydamas programą, greitai atrastų bent vieną šių prielaidų pažeidimą – ir gautų nepaaiškintą traceback vietoje suprantamos žinutės.

### 2. Galutinis tikslas

Sukurti Asistentą 0.6 – testuotą ir atsparią versiją, kuri turi automatinių testų rinkinį, aiškią klaidų hierarchiją ir žurnalus, o vartotojui klaidos atveju visada parodo suprantamą žinutę, ne techninį traceback.

### 3. Funkciniai reikalavimai

Projektas turi turėti:

1. `tests/test_text_tools.py` ir `tests/test_assistant_core.py` su automatiniais testais;
2. bent 12 automatinių testų iš viso;
3. aiškią klaidų hierarchiją failui ir žinių struktūrai (pvz. atskiras klases failo problemoms ir struktūros problemoms);
4. vartotojui draugišką klaidos pranešimą – be techninio traceback teksto;
5. `logging`, kuris nefiksuoja žinučių turinio ar paslapčių (API rakto, slaptažodžių, viso vartotojo klausimo pažodžiui);
6. `requirements.txt` su `pytest`;
7. README su komandomis programos paleidimui ir testų paleidimui.

### 4. Pavyzdinė įvestis

Terminalo sesija, kurioje sąmoningai bandoma sulaužyti programą:

```text
$ mv data/knowledge.json data/knowledge_renamed.json
$ python main.py
Tu:
```

### 5. Pavyzdinis rezultatas

Vietoje traceback – suprantama žinutė ir programa toliau veikianti (arba tvarkingai užsibaigianti su aiškiu paaiškinimu):

```text
Nepavyko rasti žinių failo: data/knowledge.json
Patikrink, ar failas yra tinkamoje vietoje, ir paleisk programą iš naujo.
```

O testų paleidimas rodo, kad projektas atitinka reikalavimus:

```bash
python -m pytest -q
```

```text
............                                                             [100%]
12 passed in 0.21s
```

### 6. Projekto kūrimo etapai

1. Sukurk `tests/` katalogą ir tuščius `test_text_tools.py`, `test_assistant_core.py` failus.
2. Parašyk testus esamoms `text_tools.py` funkcijoms (`normalize_text`, `count_words`, `contains_any`, `shorten_text`) – bent po 2 testus kiekvienai.
3. Parašyk testus `assistant_core.py` funkcijoms (`find_answer`, `is_exit_command`) tipiniam, ribiniam ir klaidingam atvejui.
4. Sukurk klaidų hierarchiją: klasę failo problemoms (pvz. `KnowledgeFileError`) ir klasę struktūros problemoms (pvz. `KnowledgeError`), naudodamas jau žinomą `require_answer()` pavyzdį kaip pagrindą.
5. Apgaubk žinių įkėlimą ir pagrindinį pokalbio ciklą `try/except`, kad kiekviena savo klaida virstų draugiška žinute vartotojui, o techninė informacija liktų žurnale.
6. Sukonfigūruok `logging` ir patikrink, kad žurnale nėra API rakto, slaptažodžio ar viso klausimo teksto.
7. Parašyk `requirements.txt` su `pytest` ir README su dviem skyriais – „Paleidimas“ (`python main.py`) ir „Testai“ (`python -m pip install -r requirements.txt`, `python -m pytest -q`).
8. Paleisk visą testų rinkinį ir įsitikink, kad yra bent 12 pavykusių testų.
9. Atlik „Paruoštumo kriterijaus“ patikrą (žr. 9 punktą žemiau) ir pataisyk viską, kas dar sukelia nepaaiškintą traceback.

### 7. Pseudokodas

```text
BANDYK įkelti žinių bazę iš data/knowledge.json
    JEI failo nėra → PARODYK draugišką žinutę, UŽFIKSUOK žurnale, SUSTABDYK tvarkingai
    JEI JSON sugadintas → PARODYK draugišką žinutę, UŽFIKSUOK žurnale, SUSTABDYK tvarkingai
    JEI struktūra netinkama → PARODYK draugišką žinutę, UŽFIKSUOK žurnale, SUSTABDYK tvarkingai

KOL vartotojas nenurodė išeiti:
    GAUK klausimą
    BANDYK rasti atsakymą žinių bazėje
        JEI klausimas tuščias → PAPRAŠYK įvesti klausimą iš naujo
        JEI klausimas nerastas → PARODYK "atsakymo dar nežinau"
    PARODYK atsakymą
    UŽFIKSUOK žurnale įvykį (be paties klausimo turinio)
```

### 8. Galimi patobulinimai

- pridėk `--verbose` parametrą, įjungiantį detalesnį žurnalavimo lygį derinimui;
- automatiškai siūlyk atkurti žinių bazę iš atsarginės kopijos, kai failas sugadintas;
- pridėk testą, tikrinantį, kad programa neužstringa gavusi itin ilgą (pvz. 10 000 simbolių) klausimą;
- kitoje pamokoje šią pačią klaidų valdymo logiką pritaikysi tikroms HTTP užklausoms.

### 9. Paruoštumo kriterijus

Projektas laikomas baigtu tik tada, kai visi šie bandymai sulaužyti asistentą baigiasi suprantama žinute, o **ne** nepaaiškintu traceback:

- pervadinai `knowledge.json` į kitą failą arba perkėlei jį į kitą aplanką;
- tyčia sugadinai JSON sintaksę (pvz. pridėjai papildomą kablelį arba ištrynei uždarantį skliaustą);
- ištrynei privalomą `answer` lauką iš vienos temos;
- įvedei visiškai tuščią klausimą (vien Enter);
- įvedei labai ilgą klausimą (kelis tūkstančius simbolių).

Šis testuotas ir atsparus pagrindas – Asistentas 0.6 – yra tai, ant ko aštuntoje pamokoje statysi tikras HTTP užklausas, o devintoje – tikrus AI modelio kvietimus. Jei šis pagrindas trapus, kiekviena vėlesnė pamoka tą trapumą tik padidins.

## 15. Gilioji laboratorija: testai be tinklo

### Parametrizuoti testai

Kai ta pati taisyklė turi galioti keliems skirtingiems duomenims, vietoje kelių beveik identiškų testo funkcijų naudok `@pytest.mark.parametrize` – jis paleidžia tą pačią testo funkciją su kiekvienu duomenų rinkiniu atskirai, todėl ataskaitoje matai, kuris konkretus atvejis nepavyko.

```python
import pytest

@pytest.mark.parametrize("raw, expected", [
    ("  LABAS  ", "labas"),
    ("Kokia   kaina?", "kokia kaina?"),
    ("", ""),
])
def test_normalize_text(raw, expected):
    assert normalize_text(raw) == expected
```

Pridėk lietuviškas raides, kelis tarpus ir naujos eilutės simbolį. Parametrizacija parodo, kad viena taisyklė galioja atvejų šeimai, o ne vien vienam pavyzdžiui – jei norėsi patikrinti dar vieną atvejį, tereikės pridėti dar vieną eilutę sąraše, ne naują funkciją.

### Laikini failai ir netikras API klientas

`tmp_path` yra `pytest` sukurta funkcija (angl. *fixture*), kuri kiekvienam testui automatiškai paruošia tuščią, laikiną katalogą diske. Tai leidžia kurti failą testui nepaliečiant tikros `knowledge.json`:

```python
def test_load_knowledge(tmp_path):
    path = tmp_path / "knowledge.json"
    path.write_text('{"kursas": {"keywords": ["python"], "answer": "88"}}', encoding="utf-8")
    assert load_knowledge(path)["kursas"]["answer"] == "88"
```

Katalogas ir jo turinys po testo automatiškai sunaikinami – projekto tikri duomenys niekada nerizikuojami.

Antra svarbi taisyklė: **nesiųsk mokamos užklausos vien tam, kad patikrintum `ask_model()`.** Sukurk netikrą (angl. *fake*) objektą, kurio `responses.create()` grąžina `SimpleNamespace(output_text="Testas")` – jis apsimeta tikru API klientu, bet neprisijungia prie interneto:

```python
from types import SimpleNamespace

def fake_client(reply_text: str):
    create = lambda **kwargs: SimpleNamespace(output_text=reply_text)
    return SimpleNamespace(responses=SimpleNamespace(create=create))

def test_ask_model_returns_reply_text():
    client = fake_client("Testinis atsakymas")
    assert ask_model(client, model="test-model", question="Ar veikia?") == "Testinis atsakymas"
```

Atskirai sukurk fake atsakymą su `function_call` lauku ir patikrink įrankio ciklą – įsitikinsi, kad asistentas atpažįsta funkcijos kvietimą, ir vėl be jokios realios, mokamos užklausos.

### Žurnalų ir regresijos kontrolinis taškas

`caplog` yra `pytest` fixture, leidžianti teste patikrinti, kas buvo įrašyta į žurnalą vykdant testuojamą kodą – be jos tektų tikrinti žurnalą rankiniu būdu.

```python
def test_logging_does_not_leak_secrets(caplog):
    with caplog.at_level(logging.INFO):
        handle_question("Koks mano slaptažodis yra 12345?", api_key="sk-tikras-raktas")

    log_text = caplog.text
    assert "sk-tikras-raktas" not in log_text
    assert "Koks mano slaptažodis yra 12345?" not in log_text
```

Patikrink, kad žurnalas turi būsenos kodą ar įvykio pavadinimą, bet neturi `OPENAI_API_KEY`, viso vartotojo klausimo ir slaptažodžio.

Tada tyčia sugadink `normalize_text` (pvz. laikinai pašalink `.strip()`), pamatyk vieną aiškų nepavykusį testą, pataisyk kodą atgal ir paleisk visą rinkinį. Baigta, kai 15 testų apima funkcijas, failus, klaidas ir netikrą tinklą.

## 16. Dažniausios klaidos

| Klaida | Kodėl ji atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| Plikas `except:` paslepia klaidas | Norima „bet kokia kaina“ išvengti traceback | `except:` | `except ValueError:` | Visada nurodyk konkretų klaidos tipą |
| Gaudoma per plati klaida | `except Exception` naudojamas ten, kur pakaktų konkrečios | `except Exception:` viskam | `except (ValueError, KeyError):` | Gaudyk tik tas klaidas, kurias tikrai numatai |
| `else`/`finally` nenaudojami pagal paskirtį | Visas kodas sukišamas į `try` | Visos eilutės, įskaitant sėkmės atvejį, `try` viduje | Sėkmės kodas – `else`, valymas – `finally` | Prieš rašydamas nuspręsk, kuri dalis iš tikrųjų gali sukelti klaidą |
| Testuojama implementacija, ne elgesys | Testas priklauso nuo to, KAIP funkcija parašyta viduje | Tikrinama, ar iškviestas konkretus vidinis metodas | Tikrinamas tik grąžinamas rezultatas | Klausk „ką ši funkcija turi daryti kviečiančiam kodui“ |
| Testuojamas tik jau žinomas geras atvejis | Patogu, bet nieko naujo nepatikrina | Vienas testas su „normaliu“ sakiniu | Testai tipiniam, ribiniam ir klaidingam atvejui | Iš anksto suplanuok atvejų lentelę |
| Paslaptys patenka į žurnalą | Derinimo metu paliktas pilnas `print`/`log` su duomenimis | `logging.info(f"raktas: {api_key}")` | `logging.info("API užklausa išsiųsta")` | Prieš commit'inant peržiūrėk, ką tiksliai loginame |
| Testai priklauso vieni nuo kitų tvarkos | Vienas testas palieka bendrą būseną, kurią naudoja kitas | Bendras sąrašas keičiamas tarp testų | Kiekvienas testas pats susikuria savo duomenis | Kiekvienas testas turi veikti paleistas atskirai, bet kokia tvarka |

## 17. Profesionali praktika

- Gaudyk konkrečią klaidą arti tos vietos, kur žinai, kaip ją sutvarkyti – ne bendrą klaidą kažkur toli nuo problemos šaltinio.
- Kurk savo klaidų klases, kai kviečiančiam kodui svarbu atskirti domeno problemą nuo kitų – bet nekurk naujos klasės kiekvienai smulkmenai.
- Testo pavadinimas turi būti sakinys apie elgesį: `test_exit_command_accepts_quit`, ne `test_1`.
- Kiekvienai naujai funkcijai iš karto suplanuok bent tipinį, ribinį ir klaidingą atvejį – tai pigiau nei ieškoti klaidos vėliau gamyboje.
- Prieš pataisydamas rastą klaidą, pirma parašyk testą, kuris ją atskleidžia – tada žinosi, kad pataisei būtent tą problemą, o ne kažką kitą.
- Žurnale lik technikas: būsenos kodai, klaidų tipai, laikai – ne turinys, kuris gali būti asmeninis ar slaptas.
- Prieš laikant projektą „baigtu“, sąmoningai pabandyk jį sulaužyti – trūkstamu failu, tuščia įvestimi, sugadintais duomenimis.

## 18. Kodėl tai svarbu mokantis AI?

Kitoje pamokoje pradėsi siųsti tikras HTTP užklausas išoriniams serveriams, o po jos – tikrus AI modelio kvietimus. Abi šios operacijos yra iš prigimties nepatikimos: tinklas gali laikinai dingti, serveris gali grąžinti klaidą, o AI paslauga gali būti laikinai perkrauta arba grąžinti netikėtos struktūros atsakymą. Skirtingai nei šioje pamokoje nagrinėti failai ar vartotojo įvestis, šių klaidų dažnai negalima „ištaisyti“ patariant vartotojui įvesti kitaip – reikia numatyti pakartotinius bandymus, laiko limitus ir aiškias atsarginio elgesio strategijas.

Be to, kiekvienas AI modelio kvietimas kainuoja pinigus arba turi griežtą naudojimo limitą. Jei testuosi siųsdamas tikrą užklausą kiekvieną kartą paleidęs `pytest`, greitai išnaudosi limitą arba apmokėsi už bandymus, kurie tiesiog tikrina, ar tavo kodas teisingai apdoroja atsakymą. Būtent todėl šioje pamokoje išmokai kurti netikrą (angl. *fake*) klientą su `SimpleNamespace` – ta pati technika devintoje pamokoje leis patikrinti visą pokalbio logiką, funkcijų kvietimo ciklą ir klaidų valdymą, nė karto nesumokėjus už tikrą API užklausą.

Galiausiai, žurnalai be paslapčių tampa dar svarbesni, kai atsiranda tikras API raktas – jo nutekėjimas į žurnalo failą ar versijų valdymo sistemą gali kainuoti realius pinigus arba prieigą prie paskyros. Įgūdis, kurį šiandien įtvirtinai su `knowledge.json` ir slaptažodžiais, tiesiogiai apsaugos tave, kai žurnaluose atsiras `OPENAI_API_KEY`.

## 19. Pamokos santrauka

- Traceback skaitomas nuo paskutinės eilutės – ten klaidos tipas ir žinutė.
- Sintaksės, vykdymo ir logikos klaidos yra trys skirtingos problemos su skirtingais požymiais.
- `try/except` gaudo tik numatytas klaidas; plikas `except:` slepia ir programavimo klaidas.
- `else` vykdomas tik po sėkmingo `try`, `finally` – visada.
- Savo klaidos klasė (pvz. `KnowledgeError`) leidžia kviečiančiam kodui atskirti domeno problemą nuo kitų.
- `pytest` ir `assert` automatiškai patikrina, ar kodas elgiasi taip, kaip tikimasi.
- AAA (Arrange–Act–Assert) struktūra padaro testą aiškų ir lengvai skaitomą.
- Testuok tipinį, ribinį ir klaidingą atvejį – ne vien tą, kurį jau žinai veikiant.
- `logging` pakeičia atsitiktinius `print()`, bet niekada neturi atskleisti paslapčių ar viso turinio.

**Atmintinė:**

```python
import logging

class KnowledgeError(Exception):
    """Žinių bazės struktūra netinkama."""

def safe_action():
    try:
        risky_step()
    except ValueError as error:
        logging.warning("Netinkama įvestis: %s", error)
    else:
        logging.info("Veiksmas pavyko")
    finally:
        logging.info("Veiksmas baigtas")

def test_safe_action_handles_bad_input():
    # Arrange – Act – Assert
    assert safe_action() is None
```

Vienu sakiniu: **programa, kuri numato, kur gali suklysti, ir turi testus, įrodančius, kad ji atsigauna, yra programa, kuria galima pasitikėti.**

## 20. Savirefleksija

1. Kurią klaidą šioje pamokoje pirmą kartą perskaičiau iki galo, o ne tiesiog paleidau kodą iš naujo?
2. Kur mano ankstesniame asistente slėpėsi plikas `except:` ar kita per plati klaida?
3. Kuris testo atvejis (tipinis, ribinis ar klaidingas) man buvo sunkiausiai sugalvojamas ir kodėl?
4. Ar galėčiau kitam žmogui per minutę paaiškinti, kodėl `try/except` nėra tas pats, kas klaidos ignoravimas?
5. Ką konkrečiai savo asistento kode dabar žinau nesulūšiant, ko prieš pamoką nežinojau?

## 21. Namų darbas

### Privaloma – Asistento 0.6 užbaigimas

Užbaik Asistentą 0.6 taip, kad pasiektum bent 15 prasmingų automatinių testų, apimančių funkcijas, failų klaidas, klaidų klases ir bent vieną netikrą (fake) tinklo klientą. Sukurk klaidų scenarijų lentelę (klaidos tipas → vartotojui rodoma žinutė → ar programa gali tęsti). Paprašyk porininko (klasės draugo, šeimos nario ar kolegos) pabandyti „sulaužyti“ tavo asistentą bet kokiu būdu per 5 minutes ir užrašyk, ką jam pavyko rasti.

**Vertinimas (10 taškų):** bent 15 prasmingų testų – 4; klaidų hierarchija ir draugiškos žinutės – 2; žurnalai be paslapčių – 2; klaidų scenarijų lentelė – 1; porininko bandymo išvados užrašytos – 1.

### Pasirenkama – regresijos medžioklė

Rask dar vieną ankstesnės asistento versijos klaidą (kitokią nei praktinėje C lygio užduotyje), parašyk ją atskleidžiantį testą, pataisyk kodą ir įrodyk, kad testas tapo žalias. Trumpai aprašyk „buvo – tikėjausi – pataisiau“.

**Vertinimas (5 taškai):** rasta reali klaida – 2; testas iš pradžių raudonas – 1; kodas pataisytas ir testas žalias – 1; aiškus aprašymas – 1.

### Kūrybinis iššūkis – klaidų atsparumo auditas

Pasirink bet kurią savo ankstesnę (ar draugo) Python programą iš šio kurso ir atlik jai „klaidų auditą“: sąrašą galimų vartotojo klaidų, po vieną testą kiekvienai, ir bent vieną savo klaidos klasę ten, kur ji pagerintų aiškumą.

**Vertinimas (5 taškai):** rastas bent vienas realus pažeidžiamumas – 2; parašytas testą jį atskleidžiantis – 1; pridėta savo klaidos klasė su pagrindimu – 1; trumpa išvada, ko išmokai – 1.

## 22. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Traceback ir klaidų tipai | 30 min. | Kartu paleisti tris skirtingus klaidingus kodo fragmentus ir garsiai perskaityti traceback |
| `try/except/else/finally` | 40 min. | Vizualizuoti valdymo srautą lentoje prieš rodant kodą |
| Savo klaidų klasės | 30 min. | Diskusija: kada verta kurti naują klasę, o kada užtenka standartinės |
| `pytest` ir grynos funkcijos | 40 min. | Kartu paleisti pirmą testų rinkinį ir aptarti `-q` išvestį |
| AAA ir ribiniai atvejai | 30 min. | Kiekvienai naujai funkcijai iš karto sudaryti atvejų lentelę |
| Žurnalai be paslapčių | 25 min. | Parodyti realų (fiktyvų) žurnalo failą su nutekėjusiu raktu kaip perspėjimą |
| Kodo pavyzdžiai ir interaktyvios veiklos | 35 min. | Aktyviai kviesti mokinius atspėti rezultatą prieš paleidžiant kodą |
| Žinių patikrinimas | 20 min. | Fiksuoti, kurie klausimai sukėlė daugiausiai abejonių |
| Praktinės užduotys (A/B/C) | 60 min. | Leisti dirbti poromis; B ir C lygiai sunkesni – skirti daugiau laiko |
| Mini projektas ir gilioji laboratorija | 50 min. | Paruoštumo kriterijų tikrinti gyvai su visa grupe, kiekvienam bandant sulaužyti kito asistentą |

Animacija labiausiai padėtų ties traceback skaitymo tvarka (vizualizacija A) ir `try/except/else/finally` valdymo srautu (vizualizacija B) – šios dvi temos mokiniams dažniausiai kelia daugiausiai painiavos. Interaktyvų Python redaktorių verta įterpti po kiekvieno naujo klaidų tipo pavyzdžio, prieš kiekvieną mini užduotį ir viso mini projekto metu. Platformoje verta fiksuoti: pirmą savarankiškai perskaitytą traceback, pirmą parašytą testą, pytest paleidimų skaičių iki visų testų žalios būsenos, ar žurnale rasta paslaptis (automatinė patikra pagal raktinius žodžius), praktinių A/B/C užduočių užbaigimą, mini projekto Paruoštumo kriterijaus patikrinimų rezultatus ir savirefleksijos pasirinkimus.
