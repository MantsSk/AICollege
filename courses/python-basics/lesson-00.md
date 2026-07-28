---
title: Pirmoji Python programa – nuo tuščio failo iki veikiančio rezultato
module: Python pagrindai
order: 0
---

# Pirmoji Python programa – nuo tuščio failo iki veikiančio rezultato

> **Trukmė:** 4 akademinės valandos (apie 3 val. kontaktinio arba savarankiško darbo). Bent pusę laiko skirk rašymui ir bandymams.

## Trumpa anotacija

Šioje pamokoje pasiruoši Python darbo aplinką, sukursi pirmą `.py` failą ir išmoksi išvesti informaciją su `print()`. Taip pat saugiai suklysi ir perskaitysi pirmą klaidos pranešimą. Šie įgūdžiai būtini visoms vėlesnėms automatizavimo, duomenų ir AI programoms.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- patikrinti įdiegtą Python 3 versiją;
- sukurti, išsaugoti ir terminale paleisti `.py` failą;
- su `print()` išvesti tekstą ir skaičių;
- paaiškinti, kuo skiriasi programa, komanda ir rezultatas;
- parašyti prasmingą vienos eilutės komentarą;
- pagal klaidos pranešimą rasti failą, eilutę ir tikėtiną problemą;
- savarankiškai sukurti mažą informacinę konsolės programą.

## Būtinos ankstesnės žinios

Ankstesnių programavimo žinių nereikia. Pakanka mokėti sukurti aplanką, įrašyti tekstą ir atidaryti programą kompiuteryje. Pamoka tinka visiškam pradedančiajam.

## 1. Įtraukianti pradžia: kaip kompiuteriui perduoti aiškią užduotį?

Įsivaizduok, kad kiekvieną rytą darbuotojams reikia parodyti tris priminimus: patikrinti el. paštą, atnaujinti užduočių lentą ir peržiūrėti pardavimų skaičius. Galima tekstą kaskart rašyti ranka, bet galima sukurti failą, kurį kompiuteris įvykdys visada vienodai.

Programa – tai kompiuteriui suprantama, nustatyta tvarka vykdomų komandų seka. Šiandien tavo seka bus trumpa, tačiau jos veikimo principas toks pats kaip didelės duomenų ar AI sistemos.

```text
Tavo kodas (.py failas) → Python vykdyklė → rezultatas ekrane
```

> **Išbandyk pats:** prieš skaitydamas toliau užrašyk vieną sakinį: kokią pasikartojančią žinutę norėtum patikėti programai?

## 2. Pagrindinės sąvokos

| Sąvoka | Paprastai | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| Python | Programavimo kalba ir programa, vykdanti Python kodą | Vertėjas tarp tavo instrukcijų ir kompiuterio | Vykdant `.py` failus | Painiojamas Python ir kodo redaktorius |
| Kodas | Tiksliai užrašytos instrukcijos | Receptas | Kuriant bet kokią programą | Komandos rašomos apytiksliai, ne tikslia sintakse |
| Sintaksė | Taisyklės, kaip užrašyti kodą | Gramatika kalboje | Rašant kiekvieną komandą | Trūksta kabutės ar skliausto |
| `print()` | Funkcija, parodanti reikšmę ekrane | Garsiakalbis | Rezultatams ir patikrai | Parašoma `Print` arba pamirštamos kabutės |
| Komentaras | Pastaba žmogui, kurios Python nevykdo | Paraštės pastaba recepte | Aiškinant sprendimo priežastį | Komentaras tik pakartoja kodą |
| Klaidos pranešimas | Python paaiškinimas, kodėl vykdymas sustojo | Navigacijos pranešimas apie neteisingą posūkį | Ieškant ir taisant gedimą | Skaitomas tik pirmas sakinys |

Minimalus visų šių idėjų pavyzdys:

```python
# Parodome pasisveikinimą
print("Labas, Python!")
```

```text
Labas, Python!
```

Pirma eilutė yra komentaras. Antroje eilutėje `print` paprašo Python parodyti tekstą, o kabutės pažymi teksto pradžią ir pabaigą.

## 3. Vizualūs paaiškinimai

### Vizualizacija A – programos kelias

```text
┌────────────────┐     ┌────────────────┐     ┌─────────────────┐
│  hello.py      │     │    Python 3    │     │ Terminalo langas│
│ print("Labas") │ ──► │ skaito ir vykdo│ ──► │ Labas           │
└────────────────┘     └────────────────┘     └─────────────────┘
       Įvestis                 Procesas                Išvestis
```

**Iliustracijos pavadinimas:** „Nuo kodo iki rezultato“
**Ką ji turi parodyti:** tris nuoseklius programos vykdymo etapus.
**Kokie elementai turi būti matomi:** `.py` failas, Python simbolis, terminalas, krypties rodyklės.
**Siūlomas vaizdo generavimo promptas:** „Švari edukacinė vektorinė infografika lietuvių kalba, trys horizontalios kortelės: Python kodo failas, Python vykdyklė, terminalo rezultatas; aiškios rodyklės, aukštas kontrastas, be dekoratyvaus triukšmo.“

### Vizualizacija B – klaidos pranešimo skaitymas

```text
  File "hello.py", line 2      ← KUR? failas ir eilutė
    printt("Labas")            ← KURI komanda?
NameError: name 'printt'...     ← KAS nutiko? Pradėk skaityti čia
```

**Iliustracijos pavadinimas:** „Klaida yra žemėlapis“
**Ką ji turi parodyti:** skaitymo kryptį nuo paskutinės eilutės į viršų.
**Kokie elementai turi būti matomi:** trys spalvomis pažymėtos zonos „kas“, „kur“, „kuri komanda“.
**Siūlomas vaizdo generavimo promptas:** „Mokomoji terminalo klaidos anotacija, Python NameError, trys spalvinės žymos KAS, KUR, KURI KOMANDA, rodyklė nuo apačios į viršų, lietuviški užrašai.“

## 4. Darbo aplinka ir pirmas failas

### 4.1. Patikrink Python

Python vykdyklė – kompiuteryje veikianti programa, kuri perskaito tavo kodą. Ji panaši į virtuvės šefą: failas yra receptas, o vykdyklė pagal jį atlieka veiksmus.

Atidaryk „Terminal“ (`macOS` / `Linux`) arba „PowerShell“ (`Windows`) ir įrašyk vieną komandą:

```text
python3 --version
```

„Windows“ sistemoje gali reikėti:

```text
python --version
```

Tikėtinas rezultatas (tikslus numeris gali skirtis):

```text
Python 3.13.5
```

Jeigu matai Python 3.10 ar naujesnę versiją, gali tęsti. Jei komanda nerasta, įdiek Python 3 iš oficialaus `python.org`; „Windows“ diegimo lange pažymėk „Add Python to PATH“ ir atidaryk naują terminalą.

> **Dažna klaida:** terminalo komanda nėra Python kodo eilutė. `python3 --version` rašoma terminale, ne `.py` faile.

### 4.1.1. Susikurk tvarkingą mokymosi aplinką

Šio žingsnio nepraleisk. Vėliau diegsime `requests`, `pytest`, `python-dotenv` ir OpenAI SDK. Jei kiekvienai pamokai naudosime skirtingą vietą ar Python versiją, klaidos atrodys kaip programavimo problemos, nors iš tikrųjų bus aplinkos problema.

#### A. Įsidiek kodo redaktorių

Pradedančiajam rekomenduoju **Visual Studio Code**. Gali naudoti ir PyCharm Community, Thonny ar kitą redaktorių, tačiau visose ekrano nuotraukose ir komandose remsimės VS Code.

**Diegimo tvarka nuo tuščio kompiuterio:**

1. Atsidaryk oficialų [Python diegimo puslapį](https://www.python.org/downloads/) ir įsidiek naujausią palaikomą Python 3 versiją.
   - Windows diegimo lange pažymėk **Add Python to PATH**.
   - macOS atidaryk atsisiųstą `.pkg` diegiklį ir užbaik vedlį.
   - Linux naudok savo distribucijos paketų tvarkyklę arba oficialias Python instrukcijas.
2. Atsidaryk oficialų [VS Code diegimo puslapį](https://code.visualstudio.com/download) ir pasirink savo operacinę sistemą.
   - Windows pasirink **User Installer**, paleisk `.exe` ir palik pažymėtą galimybę pridėti `code` į PATH.
   - macOS atidaryk `.dmg` ir nutempk VS Code į **Applications**.
   - Ubuntu/Debian gali naudoti `.deb` paketą arba oficialią saugyklą.
3. Paleisk VS Code ir kairėje atidaryk **Extensions** (`Ctrl/Cmd + Shift + X`). Paieškoje rask **Python** leidėjo **Microsoft** plėtinį ir paspausk **Install**.

Svarbu: VS Code, Python plėtinys ir Python interpretatorius yra trys skirtingi dalykai. VS Code yra vieta rašyti kodą, plėtinys suteikia paleidimo ir derinimo funkcijas, o interpretatorius faktiškai vykdo `.py` failą. Vien įdiegti VS Code neužtenka. Šią trijų dalių schemą patvirtina [oficialus VS Code Python vadovas](https://code.visualstudio.com/docs/python/python-tutorial).

Plėtinys suteikia sintaksės spalvinimą, paleidimo mygtuką, klaidų žymes ir testų paleidimą.

#### B. Susikurk vieną projekto aplanką

Terminale vykdyk:

```text
mkdir python-mokymai
cd python-mokymai
```

Windows PowerShell sistemoje šios komandos taip pat veikia. Patikrink, kuriame aplanke esi:

```text
pwd
```

Windows alternatyva:

```text
Get-Location
```

Atidaryk būtent šį aplanką VS Code meniu **File → Open Folder**. Kiekvienos kitos pamokos failai turi būti šiame projekte, o ne atsitiktiniame aplanke „Downloads“.

#### C. Sukurk virtualią aplinką

Virtuali aplinka – atskira projekto Python biblioteka. Ji neleidžia vieno kurso priklausomybėms susimaišyti su kitais projektais.

macOS ir Linux:

```text
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```text
py -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```text
py -m venv .venv
.venv\Scripts\activate.bat
```

Aktyvioje aplinkoje terminalo pradžioje turėtum matyti `(.venv)`. Patikrink:

```text
python --version
python -c "import sys; print(sys.executable)"
```

Antra komanda turi rodyti kelią į tavo projekto `.venv` aplanką. Jei matai sisteminį Python, aktyvuok aplinką dar kartą.

> **Windows saugumo pranešimas:** jei PowerShell neleidžia aktyvuoti scenarijaus, gali naudoti Command Prompt variantą. Jei turi administratoriaus teisę ir nori taisyti PowerShell, vadovaukis oficialia dokumentacija, o ne atsitiktine komanda iš forumo.

#### D. Pasirink tą patį interpretatorių VS Code

Paspausk `Ctrl/Cmd + Shift + P`, pasirink **Python: Select Interpreter** ir pasirink kelią, kuriame yra `.venv` (`.venv/bin/python` arba `.venv\\Scripts\\python.exe`). Atidaryk naują VS Code terminalą ir dar kartą paleisk:

```text
python -c "import sys; print(sys.executable)"
```

Jei VS Code paleidimo mygtukas naudoja kitą kelią nei terminalas, pirmiausia sutvarkyk interpretatorių. Vienoje pamokoje naudok vieną aktyvią aplinką.

#### E. Įsitikink, kad aplinka paruošta

Sukurk failą `setup_check.py`:

```python
import sys

print("Python veikia")
print(f"Versija: {sys.version.split()[0]}")
print(f"Vykdyklė: {sys.executable}")
```

Paleisk:

```text
python setup_check.py
```

Tikėtinas rezultatas (kelias ir smulkus versijos numeris skirsis):

```text
Python veikia
Versija: 3.13.5
Vykdyklė: /.../python-mokymai/.venv/bin/python
```

Prieš tęsdami pažymėk tris kontrolinius punktus:

- `python --version` parodo Python 3;
- `sys.executable` rodo projekto `.venv`;
- `setup_check.py` paleidžiamas be klaidos.

#### F. Jei kažkas neveikia

| Simptomas | Ką patikrinti |
|---|---|
| `python: command not found` | pabandyk `python3` macOS/Linux arba `py` Windows; patikrink Python diegimą |
| VS Code raudonai pabraukia `import` | pasirink `.venv` per **Python: Select Interpreter** |
| `No module named ...` | aktyvuok `.venv` ir diek paketą su `python -m pip`, ne atsitiktiniu `pip` |
| Failas paleidžiamas dukart spustelėjus ir iškart dingsta | paleisk jį iš terminalo, kad matytum rezultatą ir klaidą |
| `Permission denied` aktyvuojant PowerShell | naudok Command Prompt variantą arba sutvarkyk PowerShell pagal oficialią dokumentaciją |
| Kodas rodo seną rezultatą | išsaugok failą (`Ctrl/Cmd + S`) prieš paleidimą |

**Savarankiškas patikrinimas.** Tyčia pasirink neteisingą interpretatorių VS Code ir palygink klaidą su teisingu `.venv` interpretatoriumi. Tada grąžink teisingą pasirinkimą. Taip išmoksi atskirti kodo klaidą nuo aplinkos klaidos.

### 4.2. Sukurk ir paleisk failą

Sukurk aplanką `python-mokymai`, jame – failą `hello.py`. Kodo redaktoriuje įrašyk:

```python
print("Labas, Python!")
```

Eilutės paaiškinimas:

- `print` yra Python suteiktas funkcijos vardas;
- `(` ir `)` apgaubia tai, ką perduodame funkcijai;
- kabutės žymi tekstą;
- `Labas, Python!` yra išvedamas turinys.

Terminale pereik į failo aplanką ir paleisk:

```text
python3 hello.py
```

„Windows“ sistemoje naudok `python hello.py`, jei taip tikrinai versiją.

```text
Labas, Python!
```

> **Išbandyk pats:** pakeisk pasisveikinimą į savo vardą, išsaugok failą ir paleisk dar kartą. Kas pasikeitė? Kodėl prieš paleidžiant svarbu išsaugoti failą?

## 5. `print()` – programos balsas

### 5.1. Tekstas

Tekstas Python kalboje rašomas tarp tiesių viengubų arba dvigubų kabučių. Kabutės veikia kaip dėžutės sienelės: jos parodo, kur tekstas prasideda ir baigiasi.

Sintaksė:

```python
print("tekstas")
```

Minimalus pavyzdys:

```python
print("Mokausi Python")
```

```text
Mokausi Python
```

Praktikoje `print()` patogu naudoti rodant ataskaitą, perspėjimą ar tarpinį programos rezultatą.

> **Dažna klaida:** „išmaniosios“ kabutės `“ ”`, nukopijuotos iš teksto redaktoriaus, Python netinka. Rašyk tiesias kabutes `" "`.

**Mini užduotis.** Parašyk komandą, kuri išveda `Mano pirmoji programa veikia!`. Pirmiausia pabandyk pats.

<details class="selfcheck" markdown="1">
<summary>Rodyti galimą atsakymą</summary>

```python
print("Mano pirmoji programa veikia!")
```

</details>

### 5.2. Kelios eilutės ir vykdymo tvarka

Python failą įprastai vykdo iš viršaus į apačią – kaip skaitai pirkinių sąrašą. Kiekvienas `print()` sukuria naują rezultato eilutę.

```python
print("1. Atidaryti užduočių sąrašą")
print("2. Patikrinti svarbius laiškus")
print("3. Pradėti svarbiausią darbą")
```

```text
1. Atidaryti užduočių sąrašą
2. Patikrinti svarbius laiškus
3. Pradėti svarbiausią darbą
```

Python pirmiausia įvykdo 1, tada 2, paskui 3 eilutę. Tai programos veikimo seka.

**Mini klausimas.** Jei sukeisi pirmą ir trečią kodo eilutes, ar Python vis tiek išves numerius didėjimo tvarka?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Ne. Python laikysis failo eilučių tvarkos, net jei pačiame tekste įrašyti kitokie numeriai.

</details>

### 5.3. Skaičiai

Skaičiui kabučių nereikia. `print(7)` parodo skaičių, o `print("7")` – skaitmenį kaip tekstą. Ekrane jie atrodo vienodai, bet vėliau su skaičiais galėsime skaičiuoti.

```python
print(7)
print(2 + 3)
```

```text
7
5
```

Antroje eilutėje Python pirmiausia apskaičiuoja `2 + 3`, tada `print()` parodo rezultatą.

> **Išbandyk pats:** išvesk šios dienos datą trimis atskiromis skaičių eilutėmis: metus, mėnesį ir dieną.

## 6. Komentarai – pastabos būsimam sau

Komentaras prasideda `#`. Python ignoruoja viską nuo `#` iki eilutės pabaigos. Tai panašu į recepto pastabą „nedidinti kaitros“ – ji skirta žmogui, ne puodui.

```python
# Šią antraštę matys ataskaitos skaitytojas
print("Savaitės ataskaita")
```

```text
Savaitės ataskaita
```

Pirma eilutė rezultato nesukuria. Komentaras paaiškina, kodėl rodome antraštę.

Prastas komentaras:

```python
# Išspausdina Savaitės ataskaita
print("Savaitės ataskaita")
```

Geresnis komentaras:

```python
# Antraštė atskiria naują automatinės ataskaitos dalį
print("Savaitės ataskaita")
```

> **Patarimas:** komentuok priežastį arba kontekstą. Nekartok to, ką aiškiai sako pati kodo eilutė.

**Mini užduotis.** Prie savo pasisveikinimo pridėk komentarą, paaiškinantį, kam ši programa skirta.

## 7. Klaidos – normali programavimo dalis

Sintaksės klaida reiškia, kad kodas neatitinka Python rašybos taisyklių. Tai tarsi sakinys be uždaromųjų kabučių – skaitytojas nežino, kur jis baigiasi.

Klaidingas kodas:

```python
print("Labas)
```

Tikėtino pranešimo pabaiga:

```text
SyntaxError: unterminated string literal
```

Taisymas:

```python
print("Labas")
```

Kita dažna klaida – neteisingas vardas:

```python
printt("Labas")
```

```text
NameError: name 'printt' is not defined. Did you mean: 'print'?
```

Skaitymo seka:

1. Perskaityk paskutinę eilutę – kas nutiko?
2. Surask failo pavadinimą ir eilutės numerį – kur nutiko?
3. Palygink tą eilutę su veikiančiu pavyzdžiu.
4. Pakeisk vieną dalyką, išsaugok ir paleisk iš naujo.

> **Svarbu:** klaidos pranešimas nėra tavo gebėjimų įvertinimas. Tai diagnostinė informacija apie konkretų bandymą.

## 8. Įvairūs kodo pavyzdžiai

### Kasdienis pavyzdys – ryto planas

**Problema:** telefone nenori kaskart rinkti tos pačios trijų žingsnių atmintinės.

```python
print("RYTO PLANAS")
print("1. Stiklinė vandens")
print("2. Dienos prioritetas")
print("3. 25 minutės susikaupimo")
```

```text
RYTO PLANAS
1. Stiklinė vandens
2. Dienos prioritetas
3. 25 minutės susikaupimo
```

**Paaiškinimas:** komandos įvykdomos iš viršaus į apačią. **Patobulinimas:** kitoje pamokoje dalį teksto laikysime kintamuosiuose.

### Kasdienis pavyzdys – recepto žingsniai

```python
print("Avižinė košė")
print("1. Užvirinti vandenį")
print("2. Suberti avižas")
print("3. Virti 5 minutes")
```

```text
Avižinė košė
1. Užvirinti vandenį
2. Suberti avižas
3. Virti 5 minutes
```

**Patobulinimas:** papildyk dviem savo žingsniais.

### Darbo pavyzdys – ataskaitos antraštė

```python
# Vienoda antraštė padeda atpažinti automatinę ataskaitą
print("PARDAVIMŲ ATASKAITA")
print("Laikotarpis: ši savaitė")
print("Būsena: parengta")
```

```text
PARDAVIMŲ ATASKAITA
Laikotarpis: ši savaitė
Būsena: parengta
```

**Patobulinimas:** pridėk eilutę su atsakingu skyriumi.

### Automatizavimo pavyzdys – vykdymo žurnalas

Automatizavimo programa dažnai praneša, kurį etapą baigė. Kol kas tik imituojame procesą.

```python
print("[1/3] Duomenų failas rastas")
print("[2/3] Ataskaita parengta")
print("[3/3] Darbas baigtas")
```

```text
[1/3] Duomenų failas rastas
[2/3] Ataskaita parengta
[3/3] Darbas baigtas
```

**Patobulinimas:** pridėk pradžios žinutę prieš pirmą etapą.

### Duomenų ir AI pavyzdys – duomenų kortelė

```python
print("DUOMENŲ RINKINYS")
print("Įrašų skaičius: 250")
print("Paskirtis: mokyti teksto klasifikatorių")
print("Paruošta AI analizei: taip")
```

```text
DUOMENŲ RINKINYS
Įrašų skaičius: 250
Paskirtis: mokyti teksto klasifikatorių
Paruošta AI analizei: taip
```

**Patobulinimas:** pridėk duomenų šaltinio eilutę.

## 9. Interaktyvios veiklos

### 1. Nuspėk rezultatą

Ką išves ši programa?

```python
print("A")
print("B")
```

A. `AB` vienoje eilutėje
B. `A`, tada `B` naujoje eilutėje
C. Tik `B`
D. Klaida

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Kiekvienas `print()` įprastai baigia savo išvestį nauja eilute.

</details>

### 2. Užpildyk trūkstamą kodą

```python
____("Programa veikia")
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
print("Programa veikia")
```

</details>

### 3. Surask klaidą

Nustatyk klaidą, paaiškink ją ir pataisyk:

```python
Print("Sveiki!")
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Python skiria didžiąsias ir mažąsias raides. Funkcijos vardas yra `print`, ne `Print`.

```python
print("Sveiki!")
```

</details>

### 4. Sudėliok teisinga tvarka

Sudėliok eilutes taip, kad būtų rodoma antraštė, pradžia ir pabaiga:

```text
print("Pabaiga")
print("DIENOS DARBAS")
print("Pradžia")
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
print("DIENOS DARBAS")
print("Pradžia")
print("Pabaiga")
```

</details>

### 5. Pasirink tinkamą sprendimą

Reikia ekrane parodyti skaičiavimo rezultatą 10. Kuris kodas tinkamas?

A. `print("5 + 5")`
B. `print(5 + 5)`
C. `Print(10)`

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Python apskaičiuoja `5 + 5` ir parodo `10`. A variantas parodytų pažodinį tekstą `5 + 5`.

</details>

### 6. Parašyk pats

Be paruošto kodo sukurk trijų eilučių programą, kuri parodo tavo mokymosi tikslą, numatomą savaitės laiką ir norimą projektą.

### 7. Patobulink kodą

Šis kodas veikia, bet jo pranešimai neaiškūs:

```python
print("Pradžia")
print("Gerai")
print("Pabaiga")
```

Pakeisk tekstus taip, kad vartotojas suprastų, koks procesas pradėtas, kas pavyko ir kas baigta. Pridėk vieną komentarą, paaiškinantį kontekstą.

## 10. Praktinės užduotys

### 1 lygis – pagrindai

#### Užduotis 1. Vizitinė kortelė

**Sąlyga:** trimis `print()` komandomis parodyk vardą, miestą ir mokymosi tikslą.
**Pradiniai duomenys:** `Austėja`, `Kaunas`, `išmokti automatizuoti ataskaitas`.
**Laukiamas rezultatas:** trys aiškiai pavadintos eilutės.
**Užuomina:** visas tekstas turi būti kabutėse.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
print("Vardas: Austėja")
print("Miestas: Kaunas")
print("Tikslas: išmokti automatizuoti ataskaitas")
```

Kiekviena komanda parodo vieną kortelės lauką. **Papildomas iššūkis:** pridėk ketvirtą eilutę su mėgstama veikla.

</details>

#### Užduotis 2. Skaičiavimo patikra

**Sąlyga:** parodyk tekstą `Dienų skaičius:` ir atskiroje eilutėje apskaičiuok `5 + 2`.
**Laukiamas rezultatas:** antraštė ir skaičius `7`.
**Užuomina:** skaičiavimo nedėk į kabutes.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
print("Dienų skaičius:")
print(5 + 2)
```

Python apskaičiuoja išraišką prieš perduodamas rezultatą `print()`. **Papildomas iššūkis:** vietoje sudėties išbandyk `7 * 4`.

</details>

#### Užduotis 3. Tikslingas komentaras

**Sąlyga:** virš ataskaitos antraštės parašyk komentarą, paaiškinantį, kam ataskaita skirta.
**Pradiniai duomenys:** ataskaita skirta pirmadienio komandos susitikimui.
**Laukiamas rezultatas:** ekrane rodoma tik antraštė.
**Užuomina:** komentaras prasideda `#`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
# Ši antraštė naudojama pirmadienio komandos susitikime
print("SAVAITĖS ATASKAITA")
```

Komentaro terminale nematysi. **Papildomas iššūkis:** pridėk dvi aiškias ataskaitos eilutes.

</details>

### 2 lygis – pritaikymas

#### Užduotis 4. Siuntos būsenos seka

**Sąlyga:** pats pasirink tinkamą `print()` komandų skaičių ir parodyk siuntos kelią: užsakymas gautas, supakuotas, perduotas kurjeriui, pristatytas.
**Laukiamas rezultatas:** keturios būsenos teisinga tvarka.
**Užuomina:** pagalvok, kuri būsena turi būti pirma.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
print("1/4 Užsakymas gautas")
print("2/4 Užsakymas supakuotas")
print("3/4 Siunta perduota kurjeriui")
print("4/4 Siunta pristatyta")
```

Eilučių tvarka perteikia proceso eigą. **Papildomas iššūkis:** pridėk proceso antraštę ir komentarą.

</details>

#### Užduotis 5. Klaidos detektyvas

**Sąlyga:** pataisyk visas klaidas neperrašydamas norimų tekstų.

```python
print("Pradžia)
Print("Duomenys parengti")
print("Pabaiga"
```

**Laukiamas rezultatas:** trys teksto eilutės be klaidos.
**Užuomina:** tikrink kabučių poras, funkcijos raidžių dydį ir skliaustų poras.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
print("Pradžia")
print("Duomenys parengti")
print("Pabaiga")
```

Pirmoje eilutėje trūko kabutės, antroje buvo netinkama didžioji raidė, trečioje – uždaromasis skliaustas. **Papildomas iššūkis:** specialiai sukurk vieną kitą klaidą ir paaiškink jos pranešimą.

</details>

### 3 lygis – iššūkis

#### Užduotis 6. AI duomenų ruošimo žurnalas

**Sąlyga:** sukurk programą, kuri parodo antraštę ir penkių etapų seką: failas rastas, duomenys nuskaityti, tušti įrašai patikrinti, tekstai parengti, procesas baigtas. Naudok bent vieną prasmingą komentarą ir vieną paprastą skaičiavimą, rodantį visų įrašų skaičių `120 + 30`.
**Laukiamas rezultatas:** aiškus, iš viršaus į apačią skaitomas žurnalas ir skaičius `150`.
**Užuomina:** skaičiavimo nedėk į kabutes.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
# Žurnalas padeda stebėti AI duomenų paruošimo etapus
print("AI DUOMENŲ RUOŠIMAS")
print("1/5 Failas rastas")
print("2/5 Duomenys nuskaityti")
print("Įrašų skaičius:")
print(120 + 30)
print("3/5 Tušti įrašai patikrinti")
print("4/5 Tekstai parengti")
print("5/5 Procesas baigtas")
```

Programa naudoja tik šioje pamokoje išmoktus elementus. **Papildomas iššūkis:** pridėk aiškią žinutę, kiek įrašų atmesta, naudodamas skaičiavimą `150 - 4`.

</details>

## 11. Mini projektas – konsolės dienos starto skydelis

### Situacija ir tikslas

Komandos narys ryte nori vienu failo paleidimu pamatyti dienos pradžios informaciją. Sukurk tvarkingą konsolės skydelį, tinkamą pirmajam tavo GitHub darbui.

### Funkciniai reikalavimai

Programa turi:

1. parodyti skydelio antraštę;
2. parodyti datą kaip tekstą;
3. parodyti tris dienos prioritetus;
4. parodyti darbo etapų skaičių, apskaičiuotą `2 + 2`;
5. baigtis motyvuojančia žinute;
6. turėti bent vieną komentarą, paaiškinantį sprendimo priežastį.

### Pavyzdinė išvestis

```text
=== DIENOS STARTAS ===
Data: 2026-07-16
1. Patikrinti kalendorių
2. Parengti ataskaitą
3. Mokytis Python
Darbo etapai:
4
Sėkmingos dienos!
```

### Kūrimo etapai

1. Sukurk `day_start.py`.
2. Išvesk antraštę ir paleisk failą.
3. Pridėk datą bei prioritetus; vėl paleisk.
4. Pridėk skaičiavimą ir pabaigos žinutę.
5. Specialiai sugadink vieną kabutę, perskaityk klaidą ir pataisyk.
6. Sukurk `README.md` pagal šabloną.

### Pseudokodas

```text
PARODYK antraštę
PARODYK datą
PARODYK tris prioritetus teisinga tvarka
PARODYK darbo etapų antraštę
APSKAIČIUOK ir PARODYK 2 + 2
PARODYK pabaigos žinutę
```

> **Užuomina:** kurk po vieną dalį ir po kiekvienos dalies paleisk programą. Taip klaidos paieškos sritis bus maža.

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

```python
# Pastovi seka padeda kiekvieną rytą pradėti vienodai
print("=== DIENOS STARTAS ===")
print("Data: 2026-07-16")
print("1. Patikrinti kalendorių")
print("2. Parengti ataskaitą")
print("3. Mokytis Python")
print("Darbo etapai:")
print(2 + 2)
print("Sėkmingos dienos!")
```

Kiekviena eilutė atlieka vieną aiškų veiksmą. Data kol kas įrašyta tiesiog tekste; kitoje pamokoje informaciją laikysime kintamuosiuose, todėl ją keisti bus patogiau.

</details>

### Galimi patobulinimai

- pritaikyk prioritetus savo darbui;
- pridėk mokymosi laiko eilutę;
- sukurk vakaro skydelio variantą;
- antroje pamokoje pakeisk fiksuotą tekstą kintamaisiais ir vartotojo įvestimi.

### `README.md` šablonas

```text
# Dienos starto skydelis

Maža Python programa, parodanti mano dienos prioritetus.

## Kaip paleisti
python3 day_start.py

## Ką išmokau
- Paleisti Python failą
- Naudoti print()
- Skaityti paprastą klaidos pranešimą

## Tolimesnė idėja
Leisti vartotojui įvesti savo vardą ir prioritetą.
```

## 12. Dažniausios klaidos

| Klaida | Kodėl atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| Neuždarytos kabutės | Kabutės rašomos ne pora | `print("Labas)` | `print("Labas")` | Po teksto patikrink antrą kabutę |
| Trūksta skliausto | Pamirštama funkcijos pabaiga | `print("Labas"` | `print("Labas")` | Mintyse poruok `(` su `)` |
| Netinkamas raidžių dydis | Python skiria didžiąsias raides | `Print("Labas")` | `print("Labas")` | Funkciją rašyk mažosiomis |
| Tekstas be kabučių | Python tekstą palaiko vardu | `print(Labas)` | `print("Labas")` | Tekstą visada apgaubk kabutėmis |
| Naudojamos lenktos kabutės | Tekstas nukopijuotas iš dokumento | `print(“Labas”)` | `print("Labas")` | Kodą rink kodo redaktoriuje |
| Paleidžiamas neišsaugotas failas | Redaktoriaus pakeitimai dar ne diske | Pakeistas tekstas, senas rezultatas | Išsaugoti ir paleisti | Įprask spausti Save prieš Run |

## 13. Profesionali praktika

- Viena kodo eilutė turėtų atlikti vieną aiškų veiksmą.
- Tekstus formatuok nuosekliai: vienodo stiliaus antraštės ir būsenos lengviau skaitomos.
- Venk komentarų `# spausdiname tekstą`; rašyk kontekstą, kurio kodas nepasako.
- Pirmą testą atlik paleisdamas programą ir palygindamas faktinę išvestį su laukiamu rezultatu.
- Po mažo pakeitimo vėl paleisk kodą. Maži žingsniai leidžia greitai rasti klaidą.
- Realiame projekte `print()` dažnai padeda laikinai patikrinti duomenis arba parodyti konsolės programos būseną.

## 14. Kodėl tai svarbu mokantis AI?

AI biblioteka taip pat vykdoma Python programoje. Prieš mokydamas modelį turėsi paleisti failus, stebėti tarpinius rezultatus ir skaityti klaidas. Duomenų ruošimo programos dažnai parodo, kiek įrašų nuskaityta ar kuriame etape procesas sustojo.

```python
print("AI duomenų patikra")
print("Rasta įrašų:")
print(40 + 10)
print("Duomenys parengti: taip")
```

```text
AI duomenų patikra
Rasta įrašų:
50
Duomenys parengti: taip
```

Kol kas tai tik aiški ataskaita. Vėliau skaičiai bus gaunami iš tikrų failų, bet vykdymo ir rezultato stebėjimo principas liks tas pats.

## 15. Pamokos santrauka

- `.py` faile laikomos Python instrukcijos.
- Python vykdo kodą iš viršaus į apačią.
- `print()` parodo tekstą, skaičių arba skaičiavimo rezultatą.
- Tekstas rašomas tarp tiesių kabučių; skaičiui kabučių nereikia.
- `#` pradeda žmogui skirtą komentarą.
- Klaidos pranešimą verta skaityti nuo paskutinės eilutės.
- Dažnas paleidimas mažais žingsniais padeda greitai taisyti klaidas.

**Atmintinė:**

```python
# Prasmingas komentaras
print("Tekstas")
print(2 + 3)
```

Vienu sakiniu: **Python programa yra tiksliai užrašytų komandų seka, kurią gali paleisti, stebėti ir taisyti.**

## 16. Savirefleksija

Atsakyk sau raštu:

1. Ką dabar galiu padaryti, ko negalėjau prieš pamoką?
2. Kuri dalis man buvo sunkiausia?
3. Kokią klaidą dabar mokėčiau atpažinti?
4. Kur galėčiau šias žinias pritaikyti realiame gyvenime?
5. Ar galėčiau kitam žmogui paaiškinti kelią nuo `.py` failo iki rezultato?

## 17. Namų darbas

### Privaloma – mano darbo dienos atmintinė

Sukurk `workday.py`, kuris parodo antraštę, penkis tavo dienos veiksmus, vieną apskaičiuotą skaičių ir baigiamąją žinutę. Naudok bent vieną prasmingą komentarą.

**Vertinimas (10 taškų):** failas paleidžiamas be klaidų – 3; yra visi reikalauti elementai – 3; aiški seka ir tekstai – 2; prasmingas komentaras – 1; savarankiškas papildymas – 1.

### Pasirenkama – klaidų katalogas

Sukurk tris skirtingas klaidas, nukopijuok jų paskutines pranešimų eilutes ir prie kiekvienos užrašyk pataisymą.

**Vertinimas (5 taškai):** trys skirtingos klaidos – 2; tiksliai nustatyta vieta – 1; veikiantys pataisymai – 2.

### Kūrybinis iššūkis – tekstinis plakatas

Vien `print()` komandomis sukurk terminale atvaizduojamą renginio, produkto ar mokymosi plakato maketą.

**Vertinimas (5 taškai):** skaitomumas – 2; kūrybiškumas – 2; kodas be klaidų – 1.

## 18. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Įžanga, aplinkos patikra | 25 min. | Dažniausia kliūtis – PATH ir skirtingos `python` / `python3` komandos |
| `print()` demonstracija | 30 min. | Po kiekvieno pakeitimo mokinys turi paleisti failą |
| Komentarai ir klaidos | 30 min. | Normalizuoti klaidas; rodyti skaitymą nuo apačios |
| Interaktyvios veiklos | 35 min. | Automatiškai tikrinti pasirinkimus ir trumpas spragas |
| Trijų lygių praktika | 55 min. | Kodo išvestį galima tikrinti automatiškai |
| Mini projektas | 70 min. | Struktūrą vertinti automatiškai, aiškumą – rankiniu būdu |
| Testas ir refleksija | 25 min. | Fiksuoti bandymų skaičių ir klaidų tipus |

Rekomenduojama įterpti animaciją ties schema „failas → Python → terminalas“ ir spalvinę klaidos anotaciją. Interaktyvus Python redaktorius naudingiausias prie `print()` veiklų, klaidų taisymo ir mini projekto. Platformoje verta fiksuoti pirmą sėkmingą paleidimą, atliktas veiklas, testo rezultatą, pakartotinių bandymų skaičių ir projekto pateikimą.
