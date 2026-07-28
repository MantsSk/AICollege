---
title: Failai, CSV ir JSON – išsaugok asistento žinias bei istoriją
module: Python praktika
order: 6
---

# Failai, CSV ir JSON – išsaugok asistento žinias bei istoriją

> **Trukmė:** 8 akademinės valandos. Sukursi duomenis iš failų įkeliančią Asistento 0.5 versiją.

## Trumpa anotacija

Iki šiol Asistento žinios ir pokalbio istorija gyveno tiesiog Python kode – žodyne ar sąraše, kuris dingdavo uždarius programą. Šioje pamokoje išmoksi patikimai dirbti su failais: naudosi `pathlib`, kad keliai veiktų bet kurioje operacinėje sistemoje, saugiai skaitysi ir rašysi UTF-8 tekstą, įkelsi bei išsaugosi struktūrizuotus duomenis JSON formatu ir apdorosi lentelinius duomenis su CSV. Pakeliui išmoksi, kodėl duomenis verta laikyti atskirai nuo kodo, kaip patikrinti, ar failo turinys tikrai tinkamas, ir kaip elgtis, kai failas sugadintas ar jo trūksta. Pamokos pabaigoje Asistentas pirmą kartą įkels savo žinias ir pokalbio istoriją iš tikrų failų – tai bus Asistentas 0.5.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- naudoti `pathlib.Path`, kad failų keliai veiktų nepriklausomai nuo operacinės sistemos ir darbo katalogo;
- saugiai skaityti ir rašyti UTF-8 tekstinius failus su `with` bloku;
- pasirinkti tinkamą failo režimą (`r`, `w`, `a`, `b`) konkrečiai užduočiai;
- įkelti (`json.load`) ir išsaugoti (`json.dump`) struktūrizuotus duomenis JSON formatu;
- skaityti ir rašyti lentelinius duomenis su `csv.DictReader` ir `csv.DictWriter`;
- paaiškinti, kodėl programos kodą verta laikyti atskirai nuo jos duomenų;
- patikrinti įkeltų duomenų struktūrą prieš ją naudojant (validavimas);
- sukurti Asistentą 0.5, kuris žinių bazę ir pokalbio istoriją įkelia bei saugo failuose.

## Būtinos ankstesnės žinios

Turėtum jau laisvai rašyti funkcijas su parametrais ir `return`, skaidyti kodą į modulius (`main.py`, `assistant_core.py`, `text_tools.py`) ir naudoti `if __name__ == "__main__"`. Penktoje pamokoje sukurtas Asistentas 0.4 jau turi atskirtą `find_answer()` funkciją be `input()`/`print()` viduje bei komandas `/help`, `/history`, `/quit`. Šioje pamokoje ta pati architektūra išlieka – pasikeičia tik tai, iš kur žinių bazė ir istorija atkeliauja: vietoje Python žodyno kode jos gyvens `data/knowledge.json` ir `logs/history.json` failuose. Jei funkcijos, moduliai ar Asistentas 0.4 dar netvirti, prieš tęsdamas pakartok penktos pamokos atmintinę.

## 1. Kodas ir duomenys – kodėl juos verta atskirti

Įsivaizduok: Asistento žinių bazė kol kas yra Python žodynas kintamojo viduje. Kai turinio autorius – nebūtinai programuotojas – nori pridėti naują temą apie kainas, jam reikia atverti `.py` failą, nepažeisti kabučių, kablelių ir įtraukų, tada iš naujo paleisti programą. Viena neteisinga kabutė – ir visa programa nebeveikia.

Jei tas pats turinys gyvena atskirame `knowledge.json` faile, turinio autorius jį redaguoja bet kokiu teksto redaktoriumi, o programos kodas – funkcijos, kurios ieško atsakymo – visai nesikeičia. Kodas apibrėžia, *kaip* elgtis su duomenimis; duomenys – *kokie* konkretūs faktai šiuo metu galioja. Tas pats principas galioja ir pokalbio istorijai: ją saugant faile, Asistentas „prisimena“ ankstesnius pokalbius net iš naujo paleidus programą.

```text
assistant_v05/
├── main.py
├── assistant_core.py
├── data/
│   └── knowledge.json
└── logs/
    └── history.json
```

`data/` katalogas laikys žinių bazę, `logs/` – pokalbių istoriją. Katalogų vardai iš karto pasako failo paskirtį – tai jau savaime dokumentacija, kurios kodo komentarai negali pakeisti.

> **Išbandyk pats:** prieš skaitydamas toliau, pabandyk atspėti, kas nutiktų, jei `knowledge.json` failo turinys būtų sugadintas (pvz., trūktų kablelio). Ar programa turėtų sustoti, ar tyliai tęsti su tuščia žinių baze? Prie šio klausimo grįšime giliojoje laboratorijoje.

## 2. Pagrindinės sąvokos

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| `pathlib.Path` | Objektas, vaizduojantis failo ar katalogo kelią | GPS adresas vietoj laisvos formos aprašymo | Sudarant kelius iki duomenų failų | Kelias „kietai“ įrašomas kaip tekstas su `/` ar `\` |
| Koduotė (UTF-8) | Taisyklė, kaip simboliai paverčiami baitais ir atgal | Bendra abėcėlė, kurią supranta visi skaitytojai | Skaitant ir rašant tekstą su lietuviškomis raidėmis | Koduotė nenurodoma, raidės „ą, č, ę“ virsta nesuprantamais ženklais |
| JSON | Tekstinis formatas struktūrizuotiems duomenims (žodynai, sąrašai) | Užpildyta anketa su aiškiais laukais | Saugant žinių bazę, nustatymus, įrašų sąrašus | Po paskutinio elemento paliktas kablelis |
| CSV | Tekstinis formatas lentelės duomenims, stulpeliai skiriami kableliu | Skaičiuoklės lapas be formatavimo | Saugant vienodos struktūros įrašų sąrašą (išlaidos, atsiliepimai) | Reikšmė su kableliu ardo stulpelius, jei neskaitoma su `csv` moduliu |
| `with` blokas | Sintaksė, garantuojanti, kad failas bus uždarytas | Durys, kurios pačios užsidaro išėjus | Kiekvieną kartą atidarant failą | Failas atidaromas be `with`, uždarymas pamirštamas |
| Failo režimai `r`/`w`/`a`/`b` | Nurodymas, ką su failu leidžiama daryti | Užrašų knygelė: skaityti, perrašyti, papildyti ar naudoti kaip nuotrauką | Renkantis, kaip atidaryti failą | `w` naudojamas norint papildyti, bet jis ištrina seną turinį |
| Validavimas | Patikra, ar įkelti duomenys turi laukiamą struktūrą | Prekių priėmimas pagal sąrašą prieš sudedant į lentyną | Prieš naudojant failo duomenis programoje | Manoma, kad jei JSON įsikėlė be klaidos, struktūra tikrai teisinga |

Trumpas bendras pavyzdys, jungiantis kelis šiuos dalykus:

```python
from pathlib import Path
import json

config_path = Path(__file__).resolve().parent / "data" / "settings.json"
settings = json.loads(config_path.read_text(encoding="utf-8"))
print(settings["assistant_name"])
```

```text
Aida
```

## 3. Vizualūs paaiškinimai

### Vizualizacija A – kodas ir duomenys yra atskiri daiktai

```text
Programos kodas                    Programos duomenys
┌──────────────────┐               ┌───────────────────┐
│ main.py           │              │ knowledge.json     │
│ assistant_core.py │  ──skaito──► │ history.json       │
└──────────────────┘               └───────────────────┘
   keičia programuotojas              keičia turinio autorius
```

**Iliustracijos pavadinimas:** „Kodas skaito duomenis, bet jais nėra“
**Ką ji turi parodyti:** kad programos logika ir programos faktai gyvena skirtinguose failuose ir juos keičia skirtingi žmonės.
**Kokie elementai turi būti matomi:** kodo dėžė kairėje, duomenų dėžė dešinėje, rodyklė „skaito“ tarp jų, po kiekviena dėže – kas ją keičia.
**Siūlomas vaizdo generavimo promptas:** „Minimalistinė edukacinė vektorinė schema lietuviškai: kairėje dėžė su užrašais main.py, assistant_core.py, dešinėje dėžė su knowledge.json, history.json, rodyklė tarp jų su užrašu skaito; aukštas kontrastas, aiškios etiketės.“

### Vizualizacija B – JSON kelias nuo disko iki programos ir atgal

```text
knowledge.json (diskas)
        │
        ▼  json.load(file)
Python dict atmintyje: {"kursas": {...}}
        │
        ▼  programa prideda naują temą
Python dict su nauja tema
        │
        ▼  json.dump(data, file, ...)
knowledge.json (diskas, atnaujintas)
```

**Iliustracijos pavadinimas:** „Įkėlimas, pakeitimas, išsaugojimas“
**Ką ji turi parodyti:** kad JSON failas ir Python žodynas yra ta pati informacija dviejose skirtingose formose, o `json.load`/`json.dump` yra tiltas tarp jų.
**Kokie elementai turi būti matomi:** failo ikona viršuje ir apačioje, žodyno kortelė viduryje, rodyklės su užrašais `json.load` ir `json.dump`.
**Siūlomas vaizdo generavimo promptas:** „Vertikali mokomoji proceso diagrama lietuvių kalba: failas knowledge.json viršuje, rodyklė su užrašu json.load žemyn į Python žodyną, tada rodyklė su užrašu json.dump atgal į atnaujintą failą; skirtingos spalvos failui ir žodynui.“

### Vizualizacija C – CSV eilutės tampa žodynų sąrašu

```text
feedback.csv (tekstas)                     csv.DictReader rezultatas
name,rating,comment                        [
Ieva,9,Labai aišku                            {"name": "Ieva",  "rating": "9", ...},
Tomas,7,Norėčiau daugiau praktikos             {"name": "Tomas", "rating": "7", ...}
                                            ]
        │
        └── pirma eilutė tampa žodyno raktais (fieldnames)
```

**Iliustracijos pavadinimas:** „Lentelė virsta žodynų sąrašu“
**Ką ji turi parodyti:** kaip CSV antraštės eilutė nustato kiekvieno žodyno raktus, o kiekviena kita eilutė – po vieną žodyną sąraše.
**Kokie elementai turi būti matomi:** CSV tekstas kairėje, žodynų sąrašas dešinėje, rodyklė nuo antraštės eilutės į raktus.
**Siūlomas vaizdo generavimo promptas:** „Dvi kolonos edukacinė schema lietuvių kalba: kairėje CSV tekstas su antrašte name,rating,comment, dešinėje sąrašas žodynų su tais pačiais raktais; rodyklė, jungianti antraštės eilutę su žodynų raktais.“

## 4. Patikimi keliai su `pathlib`

Kelias iki failo gali atrodyti kaip paprastas tekstas, bet skirtingos operacinės sistemos skirtukus rašo skirtingai (`/` arba `\`), o absoliutus kelias, parašytas ranka, priklauso tik nuo konkretaus kompiuterio. `pathlib.Path` šias problemas išsprendžia už tave.

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
knowledge_path = BASE_DIR / "data" / "knowledge.json"

print(knowledge_path.exists())
```

Eilutė po eilutės:

1. `from pathlib import Path` – įkeliame klasę darbui su keliais.
2. `Path(__file__)` – kelias iki dabar vykdomo failo.
3. `.resolve()` – paverčia kelią absoliučiu ir išsprendžia tokius dalykus kaip `..`.
4. `.parent` – katalogas, kuriame yra failas (ne pats failas).
5. `BASE_DIR / "data" / "knowledge.json"` – operatorius `/` sujungia kelio dalis nepriklausomai nuo operacinės sistemos.
6. `.exists()` – grąžina `True` arba `False`, ar kelias realiai egzistuoja diske.

> **Dažna klaida:** kelias `"/Users/vardas/Desktop/assistant/data/knowledge.json"` veikia tik tavo kompiuteryje. Kito studento aplinkoje ar serveryje tokio katalogo gali visai nebūti – visada skaičiuok kelią nuo `__file__`.

Katalogus, kurių dar nėra, gali sukurti iš karto:

```python
(BASE_DIR / "logs").mkdir(parents=True, exist_ok=True)
```

`parents=True` sukuria visus trūkstamus tarpinius katalogus, o `exist_ok=True` nesukelia klaidos, jei katalogas jau yra. Tai tiksliai tas mechanizmas, kurio prireiks Asistentui 0.5, kad `logs/` katalogas atsirastų automatiškai.

**Mini užduotis.** Sukurk kelią iki `logs/history.json` naudodamas `BASE_DIR`, patikrink, ar failas egzistuoja, ir atskirai patikrink, ar egzistuoja jo tėvinis katalogas `logs/`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
history_path = BASE_DIR / "logs" / "history.json"
print(history_path.exists())
print(history_path.parent.exists())
```

`history_path.parent` grąžina `Path` objektą pačiam katalogui `logs/`, todėl jo egzistavimą galima patikrinti atskirai nuo paties failo.

</details>

## 5. Tekstiniai failai

Paprasčiausias failų tipas – tekstinis. Python leidžia jį nuskaityti ar įrašyti viena eilute arba per `with` bloką, kai reikia daugiau kontrolės.

```python
notes_path = BASE_DIR / "data" / "notes.txt"
notes_path.write_text("Pirma pastaba\nAntra pastaba", encoding="utf-8")
content = notes_path.read_text(encoding="utf-8")
print(content)
```

```text
Pirma pastaba
Antra pastaba
```

`write_text()` sukuria arba perrašo visą failą vienu kvietimu, `\n` viduje sukuria naują eilutę tame pačiame tekste, o `read_text()` grąžina visą turinį kaip vieną `str` reikšmę.

Ilgesniam ar laipsniškam rašymui naudojamas `with` blokas:

```python
with notes_path.open("a", encoding="utf-8") as file:
    file.write("\nTrečia pastaba")
```

`with` bloką galima suprasti kaip pasižadėjimą: „atidaryk failą, leisk man su juo dirbti, o baigus – pats uždaryk, net jei kelyje įvyks klaida“. Failo režimai: `r` – skaityti, `w` – perrašyti nuo nulio, `a` – pridėti į pabaigą, `b` – dvejetainiams duomenims (pvz., paveikslėliams).

> **Dažna klaida:** atidarius failą be `with` ir pamiršus `file.close()`, failas gali likti neuždarytas – dalis duomenų neįrašoma į diską arba failas lieka užrakintas kitoms programoms.

**Mini užduotis.** Parašyk kodą, kuris paprašo vartotojo pastabos su `input()`, ją prideda į `notes.txt`, o tada perskaito ir parodo visą failą.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
new_note = input("Įrašyk pastabą: ")

with notes_path.open("a", encoding="utf-8") as file:
    file.write(f"\n{new_note}")

print(notes_path.read_text(encoding="utf-8"))
```

</details>

## 6. JSON: Python struktūros faile

JSON (angl. *JavaScript Object Notation*) yra tekstinis formatas, kuris beveik tiesiogiai atitinka Python žodynus ir sąrašus: `{}` tampa `dict`, `[]` – `list`, tekstas kabutėse – `str`, skaičiai – `int`/`float`, o `true`/`false`/`null` – `True`/`False`/`None`.

`knowledge.json`:

```json
{
  "kursas": {
    "keywords": ["kursas", "mokymai", "programa"],
    "answer": "Programa trunka 88 akademines valandas.",
    "source": "Kurso programa"
  }
}
```

Įkėlimas:

```python
import json

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
```

1. `path.open("r", encoding="utf-8")` atidaro failą skaitymui kaip tekstą su UTF-8.
2. `json.load(file)` perskaito visą failo turinį ir jį paverčia Python struktūra – šiuo atveju žodynu.
3. `with` blokas užtikrina, kad failas bus uždarytas iškart po skaitymo.

Išsaugojimas:

```python
def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
```

1. `path.parent.mkdir(parents=True, exist_ok=True)` sukuria trūkstamus katalogus (pvz., `data/`), kad rašymas nesulūžtų.
2. `path.open("w", ...)` atidaro (ar sukuria) failą rašymui – senas turinys bus perrašytas.
3. `json.dump(data, file, ensure_ascii=False, indent=2)` Python struktūrą paverčia JSON tekstu ir jį įrašo. `ensure_ascii=False` išsaugo lietuviškas raides skaitomas, o `indent=2` suformatuoja failą, kad jį būtų patogu skaityti žmogui.

JSON palaiko objektus, masyvus, tekstą, skaičius, `true`, `false`, `null`; jis nepalaiko Python `set` ar funkcijų.

> **Dažna klaida:** `w` režimas visada perrašo visą failą nuo nulio – jei prieš tai neįkėlei esamo turinio į atmintį, jis bus prarastas.

**Mini užduotis.** Įkelk `knowledge.json` su `load_json()`, pridėk naują temą `"testavimas"` su bent vienu raktažodžiu ir atsakymu, tada išsaugok pakeitimus su `save_json()`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
data = load_json(knowledge_path)
data["testavimas"] = {
    "keywords": ["testas", "testavimas"],
    "answer": "Testavimas patikrina, ar kodas veikia taip, kaip tikimasi.",
    "source": "Kurso programa",
}
save_json(knowledge_path, data)
```

</details>

## 7. CSV: lentelės duomenims

CSV (angl. *Comma-Separated Values*) yra paprasčiausias būdas saugoti lentelę tekstiniu failu: pirma eilutė – stulpelių vardai, kiekviena kita eilutė – vienas įrašas.

`feedback.csv`:

```text
name,rating,comment
Ieva,9,Labai aišku
Tomas,7,Norėčiau daugiau praktikos
```

```python
import csv

with (BASE_DIR / "data" / "feedback.csv").open(
    "r", encoding="utf-8", newline=""
) as file:
    reader = csv.DictReader(file)
    rows = list(reader)

for row in rows:
    print(row["name"], int(row["rating"]))
```

1. `newline=""` rekomenduojamas CSV failams, kad Windows sistemoje eilutės nebūtų dvigubinamos.
2. `csv.DictReader(file)` kiekvieną eilutę paverčia žodynu, kurio raktai – pirmos eilutės stulpelių vardai.
3. `list(reader)` visus žodynus surenka į sąrašą, kad juos galėtume naudoti ir po failo uždarymo.
4. `int(row["rating"])` – CSV reikšmės visada perskaitomos kaip tekstas, reitingą reikia konvertuoti patiems.

Rašymas:

```python
with (BASE_DIR / "data" / "feedback.csv").open(
    "a", encoding="utf-8", newline=""
) as file:
    writer = csv.DictWriter(file, fieldnames=["name", "rating", "comment"])
    writer.writerow({"name": "Asta", "rating": 10, "comment": "Puiku"})
```

1. `"a"` režimas prideda naują eilutę failo gale, nekeisdamas senų įrašų.
2. `csv.DictWriter(file, fieldnames=[...])` nurodo stulpelių tvarką.
3. `writer.writerow({...})` žodyną paverčia viena CSV eilute ta pačia tvarka, kaip `fieldnames`.

> **Dažna klaida:** jei `writer.writerow()` žodyne trūksta rakto, kuris yra `fieldnames` sąraše, gausi `ValueError`; jei žodyne yra papildomas raktas, kurio nėra `fieldnames`, taip pat gausi klaidą (nebent naudoji `extrasaction="ignore"`).

**Mini užduotis.** Perskaityk `feedback.csv`, apskaičiuok vidutinį reitingą (`rating`) ir parodyk jį suapvalintą iki vieno skaitmens po kablelio.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
with (BASE_DIR / "data" / "feedback.csv").open(
    "r", encoding="utf-8", newline=""
) as file:
    reader = csv.DictReader(file)
    ratings = [int(row["rating"]) for row in reader]

average_rating = sum(ratings) / len(ratings)
print(f"Vidutinis reitingas: {round(average_rating, 1)}")
```

</details>

## 8. Duomenų validavimas

`json.load()` patikrina tik tai, ar tekstas yra teisingas JSON – ne tai, ar struktūra atitinka tavo programos lūkesčius. Failas gali būti sintaksiškai teisingas, bet turėti eilutę be `answer` arba `keywords` kaip tekstą vietoje sąrašo.

```python
def validate_knowledge(data: dict) -> list[str]:
    errors = []
    for topic_name, topic in data.items():
        if not isinstance(topic.get("keywords"), list):
            errors.append(f"{topic_name}: keywords turi būti sąrašas")
        if not topic.get("answer"):
            errors.append(f"{topic_name}: trūksta answer")
    return errors
```

1. `errors = []` – kaupiame visas rastas problemas, o ne sustojame ties pirma.
2. `isinstance(topic.get("keywords"), list)` patikrina tipą, ne tik tai, ar reikšmė apskritai egzistuoja.
3. `topic.get("answer")` tikrina, ar reikšmė ne tuščia (tuščias tekstas `""` loginiame kontekste taip pat laikomas „klaidingu“).
4. Grąžinamas klaidų tekstų sąrašas – tuščias sąrašas reiškia, kad viskas gerai.

> **Dažna klaida:** `validate_knowledge()` grąžina klaidų sąrašą, bet niekas jo nepatikrina su `if errors: ...` – tada klaidos tyliai ignoruojamos ir programa tęsia darbą su blogais duomenimis.

**Mini užduotis.** Iškviesk `validate_knowledge()` su duomenimis, kuriuose vienai temai trūksta `answer`, ir parodyk žmogui suprantamą pranešimą, jei sąrašas netuščias.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
errors = validate_knowledge(data)
if errors:
    print("Žinių bazėje rastos problemos:")
    for error in errors:
        print(f"- {error}")
else:
    print("Žinių bazė tvarkinga.")
```

</details>

## 9. Įvairūs kodo pavyzdžiai

### Minimalus pavyzdys

**Problema:** išsaugoti ir vėl perskaityti vieną eilutę teksto.

```python
log_path = Path("last_run.txt")
log_path.write_text("Programa paleista sėkmingai", encoding="utf-8")
print(log_path.read_text(encoding="utf-8"))
```

```text
Programa paleista sėkmingai
```

**Patobulinimas:** prie teksto pridėk paleidimo laiką su `datetime.now()`.

### Kasdienis pavyzdys – asmeninis dienoraštis

```python
diary_path = Path("diary.txt")
entry = input("Šiandienos įrašas: ")

with diary_path.open("a", encoding="utf-8") as file:
    file.write(f"{entry}\n")

print("Įrašas išsaugotas.")
```

**Patobulinimas:** prie kiekvieno įrašo pridėk datą iš `datetime.date.today()`.

### Kasdienis pavyzdys – kontaktų knygelė CSV

```python
import csv
from pathlib import Path

contacts_path = Path("contacts.csv")

with contacts_path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "phone"])
    writer.writeheader()
    writer.writerow({"name": "Rūta", "phone": "+37060000000"})
    writer.writerow({"name": "Dovydas", "phone": "+37061111111"})

with contacts_path.open("r", encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file):
        print(f"{row['name']}: {row['phone']}")
```

```text
Rūta: +37060000000
Dovydas: +37061111111
```

**Patobulinimas:** prieš rašydamas patikrink, ar kontaktas su tuo pačiu vardu jau egzistuoja.

### Darbo pavyzdys – konfigūracijos failas

```python
import json
from pathlib import Path

config_path = Path("config.json")
config = {
    "assistant_name": "Aida",
    "max_history_entries": 100,
    "language": "lt",
}

config_path.write_text(
    json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8"
)

loaded_config = json.loads(config_path.read_text(encoding="utf-8"))
print(loaded_config["assistant_name"])
```

```text
Aida
```

**Patobulinimas:** jei konfigūracijos failo nėra, sukurk jį su numatytosiomis reikšmėmis.

### Automatizavimo pavyzdys – išlaidų suvestinė iš CSV

```python
import csv
from pathlib import Path

totals_by_category: dict[str, float] = {}

with Path("expenses.csv").open("r", encoding="utf-8", newline="") as file:
    for row in csv.DictReader(file):
        category = row["category"]
        amount = float(row["amount"])
        totals_by_category[category] = totals_by_category.get(category, 0.0) + amount

for category, total in totals_by_category.items():
    print(f"{category}: {total:.2f} Eur")
```

**Patobulinimas:** pridėk bendrą visų kategorijų sumą po ciklo.

### Duomenų ir AI pavyzdys – prompt šablonų saugykla

```python
import json
from pathlib import Path

prompts_path = Path("prompts.json")
prompts = {
    "system": "Tu esi draugiškas kurso asistentas, atsakantis lietuviškai.",
    "no_answer": "Atsiprašau, šiuo klausimu žinių dar neturiu.",
}

prompts_path.write_text(
    json.dumps(prompts, ensure_ascii=False, indent=2), encoding="utf-8"
)

loaded_prompts = json.loads(prompts_path.read_text(encoding="utf-8"))
print(loaded_prompts["system"])
```

```text
Tu esi draugiškas kurso asistentas, atsakantis lietuviškai.
```

**Patobulinimas:** vėliau šis failas taps tikru sisteminiu promptu, siunčiamu AI modeliui per API.

### Klaidingas pavyzdys – pataisyk

```python
history_path = Path("history.json")

with history_path.open("w", encoding="utf-8") as file:
    file.write("Naujas pokalbis įrašytas")
```

Kiekvieną kartą paleidus programą `"w"` režimas ištrina visą ankstesnę istoriją – po kelių paleidimų liktų tik paskutinis įrašas.

Pataisymas – pirma įkeliame esamą istoriją, tada ją papildome:

```python
import json
from pathlib import Path

history_path = Path("history.json")
history = (
    json.loads(history_path.read_text(encoding="utf-8"))
    if history_path.exists()
    else []
)
history.append({"note": "Naujas pokalbis įrašytas"})
history_path.write_text(
    json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8"
)
```

## 10. Interaktyvios veiklos

### 1. Nuspėk rezultatą

```python
path = Path("data.json")
path.write_text('{"a": 1}', encoding="utf-8")
data = json.loads(path.read_text(encoding="utf-8"))
data["b"] = 2
print(data)
```

A. `{"a": 1}`
B. `{'a': 1, 'b': 2}`
C. Klaida
D. `{"a": 1, "b": 2}`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Python žodyną spausdina su vienguboms kabutėms, o `data["b"] = 2` prideda naują raktą prieš spausdinimą.

</details>

### 2. Užpildyk trūkstamą kodą

```python
with path.open("____", encoding="utf-8") as file:
    content = file.read()
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
with path.open("r", encoding="utf-8") as file:
    content = file.read()
```

Kadangi failą tik skaitome, o ne keičiame, tinka režimas `"r"`.

</details>

### 3. Surask klaidą

```python
with open("notes.txt", encoding="utf8") as file
    content = file.read()
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Po `as file` trūksta dvitaškio. Pataisytas variantas:

```python
with open("notes.txt", encoding="utf-8") as file:
    content = file.read()
```

</details>

### 4. Sudėliok teisingą tvarką

```text
naudoti duomenis programoje
patikrinti validate_knowledge(data)
įkelti duomenis su load_json(path)
patikrinti, ar path.exists()
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```text
patikrinti, ar path.exists()
įkelti duomenis su load_json(path)
patikrinti validate_knowledge(data)
naudoti duomenis programoje
```

Duomenis reikia patikrinti prieš juos naudojant – kiekvienas žingsnis apsaugo nuo klaidos, kurią kitaip pastebėtum tik vėliau.

</details>

### 5. Pasirink tinkamą sprendimą

Nori pridėti naują atsiliepimą į `feedback.csv`, nepanaikindamas senų įrašų. Kurį režimą naudosi?

A. `"r"`
B. `"w"`
C. `"a"`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**C.** `"a"` prideda naują eilutę failo gale, o `"w"` visą turinį perrašytų nuo nulio.

</details>

### 6. Parašyk pats

Parašyk programą, kuri paklaus vartotojo vardo ir mėgstamos knygos, tada šį įrašą pridės (append) į `contacts.csv` failą kaip naują eilutę su stulpeliais `name` ir `favorite_book`.

### 7. Patobulink kodą

```python
def load(p):
    f = open(p, "r", encoding="utf-8")
    d = json.load(f)
    return d
```

Perrašyk naudodamas `with` bloką, aiškius vardus ir tipų užuominas, panašiai kaip `load_json()`.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
```

`with` blokas garantuoja uždarymą net įvykus klaidai, o vardai `path` ir `file` paaiškina paskirtį geriau nei `p` ir `f`.

</details>

## 11. Žinių patikrinimas prieš platformos testą

Pirmiausia atsakyk neužleisdamas atsakymų.

1. Kuo skiriasi `.read_text()` ir `.open("r", encoding="utf-8")` naudojant `for eilutė in file`?
2. Ką grąžins `json.load(file)`, jei failo turinys yra `["a", "b", "c"]`?
3. Kodėl CSV failus verta atidaryti su `newline=""`?
4. Koks skirtumas tarp `validate_knowledge()`, kuri grąžina klaidų sąrašą, ir `require_topic()`, kuri meta `ValueError`?
5. Kodėl `atomic_save()` pirma rašo į laikiną `.tmp` failą, o ne tiesiai į galutinį?
6. Kas atsitiks, jei `csv.DictWriter().writerow()` gaus žodyną be vieno iš `fieldnames` raktų?
7. Kodėl `BASE_DIR = Path(__file__).resolve().parent` yra patikimiau nei absoliutus kelias, parašytas ranka?
8. Kada rinktumeisi TXT, kada CSV, o kada JSON savo duomenims saugoti?
9. Kodėl svarbu iškviesti `mkdir(parents=True, exist_ok=True)` prieš rašant į `logs/history.json`?
10. Kas nutinka, jei failas atidaromas be `with` bloko ir jo neuždarome rankiniu būdu?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymus ir paaiškinimus</summary>

1. `.read_text()` grąžina visą failo turinį kaip vieną `str`, o `.open()` su ciklu leidžia apdoroti failą eilutė po eilutės, nelaikant visko atmintyje iš karto.
2. Python sąrašą (`list`), kuriame yra trys tekstinės reikšmės.
3. Kad Windows sistemoje CSV modulis pats tvarkytų eilučių pabaigas ir tarp įrašų neatsirastų tuščių eilučių.
4. `validate_knowledge()` surenka visas rastas problemas ir leidžia programai pačiai nuspręsti, ką daryti; `require_topic()` iškart sustabdo vykdymą, kai tik randama pirma klaida.
5. Kad, jei programa sugestų rašymo metu, senas failas liktų nepaliestas – pakeičiama tik tada, kai naujas turinys jau visiškai parašytas.
6. Bus iškelta klaida, nes `DictWriter` tikisi reikšmės kiekvienam `fieldnames` sąraše nurodytam raktui.
7. Jis apskaičiuojamas nuo vykdomo failo vietos, todėl veikia nepriklausomai nuo to, iš kurio katalogo programa paleista, ir nepriklauso nuo konkretaus kompiuterio.
8. TXT – laisvai formos tekstui; CSV – vienodos struktūros lentelėms; JSON – įdėtoms, hierarchinėms struktūroms su žodynais ir sąrašais.
9. Nes katalogo `logs/` gali dar nebūti – be `mkdir()` bandymas rašyti į jį baigtųsi klaida.
10. Failas gali likti neuždarytas: dalis duomenų gali neatsidurti diske arba failas liks užrakintas kitoms programoms.

</details>

## 12. Praktinės užduotys

### 1 lygis – užrašinė

#### Užduotis 1. Asmeninė užrašinė faile

**Sąlyga:** sukurk programą, kuri leidžia vartotojui įvesti pastabas ir jas pridėti (append) į `notes.txt` failą. Komanda `/show` turi parodyti visą failo turinį, o `/quit` – baigti darbą.

**Pavyzdinė įvestis:**

```text
Įrašyk pastabą arba komandą: Nepamiršti nupirkti pieno
Įrašyk pastabą arba komandą: /show
Įrašyk pastabą arba komandą: /quit
```

**Laukiamas rezultatas:**

```text
=== Užrašai ===
Nepamiršti nupirkti pieno
```

**Užuomina:** naudok `while True` ciklą ir tikrink, ar įvestis prasideda nuo `/`, prieš spręsdamas, ar tai komanda, ar pastaba.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
from pathlib import Path

notes_path = Path(__file__).resolve().parent / "notes.txt"

while True:
    entry = input("Įrašyk pastabą arba komandą: ")

    if entry == "/quit":
        break

    if entry == "/show":
        if notes_path.exists():
            print("=== Užrašai ===")
            print(notes_path.read_text(encoding="utf-8"))
        else:
            print("Užrašų dar nėra.")
        continue

    with notes_path.open("a", encoding="utf-8") as file:
        file.write(f"{entry}\n")
```

**Papildomas iššūkis:** pridėk komandą `/clear`, kuri ištrina visas pastabas (`notes_path.write_text("", encoding="utf-8")`).

</details>

### 2 lygis – išlaidų CSV

#### Užduotis 2. Išlaidų sekimas CSV faile

**Sąlyga:** sukurk programą, kuri leidžia įvesti išlaidos datą, kategoriją, sumą ir komentarą, prideda įrašą į `expenses.csv`, o komanda `/summary` parodo bendrą sumą bei sumas pagal kategorijas.

**Pavyzdinė įvestis:**

```text
Data, kategorija, suma, komentaras arba /summary, /quit: 2026-07-18,maistas,12.50,Pietūs
Data, kategorija, suma, komentaras arba /summary, /quit: 2026-07-18,transportas,3.00,Autobusas
Data, kategorija, suma, komentaras arba /summary, /quit: /summary
```

**Laukiamas rezultatas:**

```text
Bendra suma: 15.50 Eur
  maistas: 12.50 Eur
  transportas: 3.00 Eur
```

**Užuomina:** stulpelių vardus (`fieldnames`) sukurk vieną kartą kaip sąrašą ir naudok jį tiek rašymui, tiek skaitymui.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
import csv
from pathlib import Path

expenses_path = Path(__file__).resolve().parent / "expenses.csv"
fieldnames = ["date", "category", "amount", "comment"]

if not expenses_path.exists():
    with expenses_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

while True:
    entry = input("Data, kategorija, suma, komentaras arba /summary, /quit: ")

    if entry == "/quit":
        break

    if entry == "/summary":
        with expenses_path.open("r", encoding="utf-8", newline="") as file:
            rows = list(csv.DictReader(file))

        totals_by_category: dict[str, float] = {}
        grand_total = 0.0
        for row in rows:
            amount = float(row["amount"])
            grand_total += amount
            category = row["category"]
            totals_by_category[category] = totals_by_category.get(category, 0.0) + amount

        print(f"Bendra suma: {grand_total:.2f} Eur")
        for category, total in totals_by_category.items():
            print(f"  {category}: {total:.2f} Eur")
        continue

    date, category, amount, comment = entry.split(",", maxsplit=3)
    with expenses_path.open("a", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(
            {
                "date": date.strip(),
                "category": category.strip(),
                "amount": amount.strip(),
                "comment": comment.strip(),
            }
        )
```

**Papildomas iššūkis:** pridėk komandą `/month 2026-07`, kuri suvestinę parodo tik nurodyto mėnesio įrašams.

</details>

### 3 lygis – JSON žinių redaktorius

#### Užduotis 3. Žinių bazės redaktorius su atsargine kopija

**Sąlyga:** komandos turi leisti pridėti temą, papildyti raktažodį, pakeisti atsakymą ir išsaugoti `knowledge.json`. Prieš perrašydamas failą, programa turi sukurti `.backup.json` kopiją.

**Pavyzdinė įvestis:**

```text
Komanda (/add-topic, /add-keyword, /edit-answer, /save, /quit): /add-topic
Naujos temos vardas: kaina
Komanda (/add-topic, /add-keyword, /edit-answer, /save, /quit): /save
```

**Laukiamas rezultatas:**

```text
Žinių bazė išsaugota, atsarginė kopija atnaujinta.
```

**Užuomina:** kopijuok seną failą į atsarginį prieš rašydamas naują, naudodamas `shutil.copy()`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
import json
import shutil
from pathlib import Path

knowledge_path = Path(__file__).resolve().parent / "data" / "knowledge.json"
backup_path = knowledge_path.parent / f"{knowledge_path.stem}.backup.json"


def load_knowledge() -> dict:
    return json.loads(knowledge_path.read_text(encoding="utf-8"))


def save_knowledge(data: dict) -> None:
    if knowledge_path.exists():
        shutil.copy(knowledge_path, backup_path)
    knowledge_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )


knowledge = load_knowledge()

while True:
    command = input("Komanda (/add-topic, /add-keyword, /edit-answer, /save, /quit): ")

    if command == "/quit":
        break

    if command == "/add-topic":
        topic_name = input("Naujos temos vardas: ")
        knowledge[topic_name] = {"keywords": [], "answer": "", "source": ""}

    elif command == "/add-keyword":
        topic_name = input("Kurios temos: ")
        keyword = input("Naujas raktažodis: ")
        knowledge[topic_name]["keywords"].append(keyword)

    elif command == "/edit-answer":
        topic_name = input("Kurios temos: ")
        answer = input("Naujas atsakymas: ")
        knowledge[topic_name]["answer"] = answer

    elif command == "/save":
        save_knowledge(knowledge)
        print("Žinių bazė išsaugota, atsarginė kopija atnaujinta.")
```

**Papildomas iššūkis:** pridėk komandą `/undo`, kuri atkuria `knowledge.json` iš `.backup.json` per `shutil.copy(backup_path, knowledge_path)`.

</details>

## 13. Mini projektas: Asistentas 0.5

### 1. Projekto situacija

Asistentas jau turi tvarkingą funkcijų ir modulių architektūrą (0.4 versija), tačiau kiekvieną kartą paleidus programą jo žinios ir atmintis dingsta – viskas gyvena tik kintamuosiuose. Nori, kad Asistentas atsimintų pokalbius tarp paleidimų, o žinių bazę galėtum redaguoti nekeisdamas kodo.

### 2. Galutinis tikslas

Sukurti Asistentą 0.5, kuris žinių bazę įkelia iš `data/knowledge.json`, o pokalbio istoriją – gavęs vartotojo sutikimą – saugo `logs/history.json`.

### 3. Funkciniai reikalavimai

Programa turi:

- programa pasileidžia iš bet kurio terminalo katalogo;
- neegzistuojant žinių failui parodoma aiški instrukcija;
- netinkama žinių struktūra neleidžia tyliai tęsti;
- istorijos katalogas sukuriamas automatiškai;
- `/reload` iš naujo įkelia redaguotą žinių bazę;
- slaptažodžiai ir būsimi API raktai į istoriją neįrašomi.

### 4. Pavyzdinė įvestis

```text
Tu: Kiek trunka kursas?
Aida: Programa trunka 88 akademines valandas.
Tu: /reload
Aida: Žinių bazė įkelta iš naujo.
Tu: /quit
```

### 5. Pavyzdinis rezultatas

Po pokalbio (jei vartotojas sutiko saugoti istoriją), `logs/history.json` turi tokį įrašą:

```python
{
    "timestamp": "2026-07-17T10:30:00",
    "question": "Kiek trunka kursas?",
    "answer": "Programa trunka 88 akademines valandas.",
    "topic": "kursas"
}
```

### 6. Projekto kūrimo etapai

1. Sukurk `data/` ir `logs/` katalogus, perkelk žinių bazę į `data/knowledge.json`.
2. Parašyk `load_json()`/`save_json()`, naudodamas `BASE_DIR = Path(__file__).resolve().parent`.
3. Paleidus programą, patikrink, ar `knowledge.json` egzistuoja; jei ne – parodyk aiškią instrukciją ir sustabdyk programą.
4. Iškviesk `validate_knowledge()` ir sustabdyk paleidimą, jei grąžintas sąrašas netuščias.
5. Paklausk vartotojo sutikimo saugoti istoriją; jei sutinka, sukurk `logs/` katalogą su `mkdir(parents=True, exist_ok=True)`.
6. Kiekvieną klausimą ir atsakymą įrašyk į istoriją su nustatyta struktūra (`timestamp`, `question`, `answer`, `topic`).
7. Pridėk `/reload` komandą, kuri iš naujo iškviečia `load_json()` ir `validate_knowledge()`.
8. Patikrink, kad jautrūs duomenys (slaptažodžiai, API raktai) niekada nepatenka į įrašomą istoriją.

### 7. Pseudokodas

```text
PATIKRINK, ar knowledge.json egzistuoja; jei ne – PARODYK instrukciją ir SUSTOK
ĮKELK knowledge.json
VALIDUOK žinių bazę; jei yra klaidų – PARODYK jas ir SUSTOK
PAKLAUSK, ar vartotojas sutinka saugoti istoriją
KARTOK:
    PERSKAITYK vartotojo žinutę
    JEI žinutė yra komanda – ĮVYKDYK komandą (/help, /history, /reload, /quit)
    KITAIP – RASK temą, SUFORMUOK atsakymą, PARODYK jį
        JEI sutikta saugoti istoriją – PRIDĖK įrašą į history.json
KOL vartotojas neišeina
```

### 8. Galimi patobulinimai

- kai istorija auga, senus įrašus perkelti į archyvą;
- pridėti `/export` komandą, kuri istoriją išsaugo kaip CSV;
- prieš rašant `knowledge.json` daryti automatinę atsarginę kopiją (žr. giliąją laboratoriją);
- leisti kelias žinių bazės kalbas skirtinguose failuose.

### 9. `README.md` šablonas

```text
# Asistentas 0.5

Python asistentas, kuris žinias ir pokalbio istoriją saugo failuose.

## Funkcijos
- Įkelia žinių bazę iš data/knowledge.json
- Validuoja žinių bazės struktūrą prieš paleidimą
- Saugo pokalbio istoriją logs/history.json (su vartotojo sutikimu)
- Komanda /reload iš naujo įkelia redaguotą žinių bazę

## Paleidimas
python3 main.py

## Duomenų failai
- data/knowledge.json – temos, raktažodžiai, atsakymai ir šaltiniai.
- logs/history.json – pokalbio įrašai su timestamp, question, answer ir topic laukais (kuriami tik gavus sutikimą).
- Slaptažodžiai ir API raktai šiuose failuose nesaugomi.

## Ką išmokau
pathlib, JSON, CSV, validavimas, kodo ir duomenų atskyrimas.

## Tolimesni patobulinimai
Klaidų apdorojimas, automatiniai testai, atsarginės kopijos.
```

## 14. Gilioji laboratorija: failas gali būti sugadintas

Failai realiame pasaulyje ne visada būna tvarkingi. Ši dalis parodo, kaip programai elgtis, kai JSON sugadintas, trūksta lauko ar CSV komentare yra kablelis – lygiai tas pats klausimas, kurį iškėlėme pačioje pamokos pradžioje.

### JSON schemos patikra

Vien `json.load()` patikrina sintaksę, bet ne tavo programos sutartį. Išbandyk gerą JSON, JSON be `answer` ir JSON, kuriame `keywords` yra tekstas vietoje sąrašo.

```python
def require_topic(name: str, topic: dict) -> None:
    if not isinstance(topic.get("keywords"), list):
        raise ValueError(f"{name}: keywords turi būti sąrašas")
    if not all(isinstance(item, str) and item.strip() for item in topic["keywords"]):
        raise ValueError(f"{name}: raktažodžiai turi būti netušti tekstai")
    if not isinstance(topic.get("answer"), str) or not topic["answer"].strip():
        raise ValueError(f"{name}: trūksta answer")
```

Skirtingai nei `validate_knowledge()`, kuri surenka visas klaidas į sąrašą ir leidžia programai spręsti toliau, `require_topic()` iškart sustabdo vykdymą per `raise ValueError`. Abu stiliai teisingi – pasirinkimas priklauso nuo to, ar nori pilną klaidų sąrašą, ar nedelsiamą sustojimą.

### Saugus perrašymas

Jei programa sugenda tarp failo atidarymo ir `json.dump`, failas gali likti tuščias. Mokymosi projekte naudok laikiną failą:

```python
import json
import os
from pathlib import Path

def atomic_save(path: Path, data: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, path)
```

Pirma parašoma visa nauja versija, tik tada pakeičiamas senas failas. Prieš išsaugodamas svarbią žinių bazę papildomai sukurk atsarginę kopiją.

### CSV realybė ir atkūrimas

CSV komentare gali turėti kablelius, kabutes, tuščią eilutę ar kitą skirtuką. Nenaudok `line.split(",")`; naudok `csv.DictReader` ir patikrink, ar yra visi laukų vardai. Išbandyk komentarą `Norėčiau daugiau, praktikos` ir įsitikink, kad jis lieka viename lauke.

Sukurk `load_knowledge_or_empty(path)`: jei failas neegzistuoja, grąžink tuščią bazę su instrukcija; jei JSON sugadintas, parodyk, kad reikia atkurti atsarginę kopiją; jei struktūra netinkama, sustabdyk paleidimą ir nurodyk temą. Niekada tyliai nepakeisk sugadintos žinių bazės tuščia – turinys gali būti prarastas.

### Kontrolinis taškas

Aplinkai paruošk penkis failus su skirtingomis klaidomis. Užrašyk klaidos tipą, vartotojui rodomą žinutę, ar programa gali tęsti ir ar reikia žmogaus įsikišimo. Šis sprendimas vėliau saugos asistento konfigūraciją prieš DI API kvietimą.

## 15. Dažniausios klaidos

| Klaida | Kodėl ji atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| `FileNotFoundError` | Kelias neteisingas arba failo dar nėra | `load_json(Path("knowledge.json"))` iš netinkamo katalogo | Patikrinti `path.exists()` prieš skaitant, kelią skaičiuoti nuo `BASE_DIR` | Visada tikrink `exists()` ir rodyk aiškią instrukciją, ne tik „kažkas negerai“ |
| Sugadintas JSON | Trūksta kablelio ar liko kablelis po paskutinio elemento | `{"a": 1,}` | `{"a": 1}` | Redaguoti JSON per redaktorių su sintaksės patikra, po pakeitimų iš karto bandyti `json.load()` |
| Koduotės klaida (mojibake) | Failas skaitomas ar rašomas be UTF-8 | `path.read_text()` be `encoding` | `path.read_text(encoding="utf-8")` | Visur nurodyti `encoding="utf-8"` skaitant ir rašant |
| Atsitiktinis `"w"` perrašymas | Manoma, kad `"w"` prideda, o ne perrašo | `path.open("w", ...)` norint pridėti įrašą | `path.open("a", ...)` arba įkelti, papildyti ir išsaugoti visą struktūrą | Prieš renkantis režimą paklausti savęs: ar noriu prarasti seną turinį? |
| Paslaptys faile | API raktas ar slaptažodis įrašomas tiesiai į duomenų failą | `{"api_key": "sk-..."}` viešame `knowledge.json` | Slaptus duomenis laikyti aplinkos kintamuosiuose, ne repozitorijos faile | Prieš commit'inant peržiūrėti, kas yra duomenų failuose |
| CSV reikšmė su kableliu | Failas skaitomas ranka su `split(",")` | `"Ieva,9,Labai, aišku".split(",")` | `csv.DictReader(file)` | Visada naudoti `csv` modulį, ne rankinį skaidymą |
| Trūkstamas `newline=""` rašant CSV | Windows sistemoje tarp eilučių atsiranda tuščios eilutės | `open("data.csv", "w", encoding="utf-8")` | `open("data.csv", "w", encoding="utf-8", newline="")` | CSV failams visada nurodyti `newline=""` |
| Failas nenurodytas su `with` | Uždarymas paliekamas atsitiktinumui | `file = open(path); file.read()` | `with path.open("r", encoding="utf-8") as file: file.read()` | `with` naudoti kiekvieną kartą atidarant failą |

## 16. Profesionali praktika

- Kelius visada skaičiuok nuo `Path(__file__).resolve().parent`, ne nuo darbo katalogo.
- Skaitant ir rašant tekstą visada nurodyk `encoding="utf-8"`.
- Prieš naudodamas failo duomenis, patikrink jų struktūrą – nesitikėk, kad viskas visada bus tvarkinga.
- Svarbius failus prieš perrašant kopijuok arba naudok atominį įrašymą (`atomic_save`).
- Niekada nelaikyk slaptažodžių ar API raktų duomenų failuose – jiems skirti aplinkos kintamieji.
- CSV failams naudok `csv` modulį, o ne rankinį `split(",")`.
- JSON failus formatuok su `indent=2` ir `ensure_ascii=False`, kad juos būtų patogu skaityti ir redaguoti žmogui.

## 17. Kodėl tai svarbu mokantis AI?

Realios AI sistemos beveik visada atskiria kodą nuo duomenų taip pat, kaip šiandien darai su Asistentu: sisteminiai promptai dažnai laikomi atskiruose tekstiniuose ar JSON failuose, kad juos būtų galima keisti nekeičiant programos; embeddingų (vektorinių teksto atvaizdų) rezultatai kešuojami JSON ar panašiuose failuose, kad jų nereikėtų kaskart skaičiuoti iš naujo; pokalbių žurnalai saugomi failuose vėlesnei analizei ir modelio tobulinimui.

```python
embedding_cache_path = Path("embedding_cache.json")
embedding_cache = {
    "Kiek trunka kursas?": [0.12, 0.98, 0.44],
}

embedding_cache_path.write_text(
    json.dumps(embedding_cache, ensure_ascii=False, indent=2), encoding="utf-8"
)

cached = json.loads(embedding_cache_path.read_text(encoding="utf-8"))
print(cached["Kiek trunka kursas?"])
```

```text
[0.12, 0.98, 0.44]
```

Čia nėra tikro AI modelio – tik jo rezultatų kešavimo šablonas: tiksliai tas pats `write_text`/`read_text`/JSON derinys, kurį jau mokaisi šioje pamokoje, tik vietoje atsakymo teksto saugomi skaičiai. Vėlesniuose moduliuose tokie failai saugos tikrus AI API atsakymus ir konfigūraciją, o API raktai visada liks aplinkos kintamuosiuose, ne duomenų failuose.

## 18. Pamokos santrauka

- Kodą ir duomenis verta laikyti atskirai – tai leidžia keisti turinį nekeičiant programos logikos.
- `pathlib.Path` ir `Path(__file__).resolve().parent` užtikrina, kad keliai veiktų bet kurioje aplinkoje.
- Tekstinius failus skaitome ir rašome su `read_text()`/`write_text()` arba `with ... open()`, visada nurodydami `encoding="utf-8"`.
- JSON idealiai tinka įdėtoms struktūroms: `json.load()` įkelia, `json.dump()` išsaugo.
- CSV tinka vienodos formos lentelėms: `csv.DictReader` skaito, `csv.DictWriter` rašo.
- Failo režimai `r`/`w`/`a`/`b` lemia, ką su failu galima daryti – `"w"` visada perrašo nuo nulio.
- Prieš naudojant įkeltus duomenis juos reikia validuoti, nes teisingas JSON dar nereiškia teisingos struktūros.
- Asistentas 0.5 žinias ir istoriją įkelia bei saugo failuose, o ne Python kode.

**Atmintinė:**

```python
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
knowledge_path = BASE_DIR / "data" / "knowledge.json"

data = json.loads(knowledge_path.read_text(encoding="utf-8"))
errors = validate_knowledge(data)

if errors:
    print("Žinių bazėje rastos problemos:", errors)
else:
    knowledge_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
```

Vienu sakiniu: **kai duomenys gyvena atskiruose, patikimai pasiekiamuose ir patikrintuose failuose, programa tampa lankstesnė, o jos turinį gali keisti net tas, kas nemoka programuoti.**

## 19. Savirefleksija

1. Ką dabar galiu padaryti su failais, ko negalėjau prieš pamoką?
2. Kuri dalis buvo sunkiausia: keliai su `pathlib`, JSON struktūra, CSV ar validavimas?
3. Kokią klaidą su failais dabar mokėčiau atpažinti ir pataisyti?
4. Kur galėčiau šias žinias pritaikyti realiame projekte ar darbe?
5. Ar galėčiau kitam žmogui paaiškinti, kodėl duomenis verta laikyti atskirai nuo kodo?

## 20. Namų darbas

### Privaloma – Asistentas 0.5

Paruošk Asistentą 0.5 su bent 12 temų `data/knowledge.json` faile, veikiančia validavimo funkcija, aiškiu sutikimo klausimu prieš rašant į `logs/history.json` ir README dalimi „Duomenų failai“.

**Vertinimas (10 taškų):** žinių bazė su bent 12 temų – 2; validavimas veikia ir sustabdo paleidimą su netinkama struktūra – 2; istorijos rašymas priklauso nuo sutikimo – 2; `/reload` veikia teisingai – 2; README su „Duomenų failai“ dalimi – 2.

### Pasirenkama – atsiliepimų CSV suvestinė

Parašyk funkciją, kuri įkelia `feedback.csv`, apskaičiuoja vidutinį reitingą ir parodo, kiek atsiliepimų turi komentarą, o kiek – ne.

**Vertinimas (5 taškai):** teisingas failo įkėlimas – 1; teisinga vidurkio formulė – 2; komentarų skaičiavimas – 1; aiški išvestis – 1.

### Kūrybinis iššūkis – tavo srities duomenų failas

Sukurk JSON arba CSV failą savo pasirinktai sričiai (receptai, treniruotės, knygų sąrašas ar kita), parašyk funkcijas jam įkelti, validuoti ir papildyti, o rezultatus rodyk su f-string.

**Vertinimas (5 taškai):** reali struktūra ir bent 5 įrašai – 1; įkėlimo ir išsaugojimo funkcijos – 2; validavimas – 1; aiški išvestis – 1.

## 21. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Įžanga: kodas vs duomenys, sąvokos, vizualizacijos | 45 min. | Aptarti, kodėl turinio autorius negali saugiai redaguoti Python kodo |
| `pathlib` ir patikimi keliai | 35 min. | Parodyti, kas nutinka su absoliučiu keliu kito studento kompiuteryje |
| Tekstinių failų skaitymas ir rašymas | 40 min. | Akcentuoti `r`/`w`/`a` skirtumą praktiškai, ne tik teoriškai |
| JSON: `load`/`dump` ir struktūros | 55 min. | Daug laiko skirti `ensure_ascii=False` ir įdėtų struktūrų skaitymui |
| CSV: `DictReader`/`DictWriter` | 55 min. | Parodyti realų atvejį su kableliu komentare |
| Validavimas ir dažnos klaidos | 40 min. | Fiksuoti, kiek mokinių pamiršta patikrinti `errors` sąrašą |
| Kodo pavyzdžiai ir interaktyvios veiklos | 45 min. | Interaktyvų redaktorių įterpti po kiekvieno pavyzdžio tipo |
| Žinių patikrinimas ir praktinės užduotys | 65 min. | Trijų lygių užduotis tikrinti automatiškai su keliais bandymų failais |
| Mini projektas: Asistentas 0.5 | 75 min. | Kodo aiškumą, sutikimo logiką ir README vertinti rankiniu būdu |
| Gilioji laboratorija (jei liko laiko) | 25 min. | Kontrolinį tašką su penkiais sugadintais failais galima palikti savarankiškam darbui |

Animacija labiausiai padėtų ties JSON įkėlimo–pakeitimo–išsaugojimo ciklu bei CSV eilutės virtimu žodynu. Platformoje verta fiksuoti atliktas mini užduotis, pirmą sėkmingą JSON įkėlimą, `FileNotFoundError`/`json.JSONDecodeError` dažnį, testo rezultatą, mini projekto užbaigimą (ar sukurti visi reikalaujami failai ir katalogai) bei savirefleksijos pasirinkimą. Ši pamoka yra pamatas septintajai pamokai, kurioje ta pati failų įkėlimo logika bus apgaubta klaidų apdorojimu ir automatiniais testais – todėl funkcijų vardai ir failų struktūra čia neturėtų keistis be reikalo.
