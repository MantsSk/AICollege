---
title: HTTP ir API – kaip Python kalbasi su kitomis sistemomis
module: API ir integracijos
order: 8
---

# HTTP ir API – kaip Python kalbasi su kitomis sistemomis

> **Trukmė:** 8 akademinės valandos. Šioje pamokoje dar nekuriame DI atsakymo – pirmiausia išmokstame patikimai bendrauti su bet kuria API.

## Trumpa anotacija

Iki šiol Asistentas gyveno tik tavo kompiuteryje: skaitė failus, atsakinėjo pagal vietinę žinių bazę ir buvo testuojamas be jokio tinklo. Ši pamoka atveria langą į išorę – išmoksi, kaip Python programa siunčia HTTP užklausą kitai sistemai internetu ir kaip patikimai priima jos atsakymą. Susipažinsi su biblioteka `requests`, `GET` ir `POST` metodais, JSON turiniu, būsenos kodais, laiko limitais, tinklo klaidomis, `.env` paslaptimis ir atsakymo validavimu. Pamoka nekuria naujos sunumeruotos Asistento versijos – vietoj to paruoši atskirą, pakartotinai naudojamą modulį `api_client.py`, kurį 9 pamoka prijungs prie tikros OpenAI Responses API. Tai tiltas tarp Python pagrindų ir tikros DI integracijos: viskas, ką čia išmoksi apie patikimą HTTP klientą, veiks nepakitę, kai už jo atsidurs realus DI modelis.

## Mokymosi rezultatai

Baigęs šią pamoką mokinys gebės…

- paaiškinti, kas vyksta HTTP užklausos ir atsakymo kelionėje tarp Python programos ir API serverio;
- atskirti `GET` ir `POST` metodų paskirtį bei žinoti, kada naudoti `params`, o kada JSON kūną (`json=`);
- perskaityti ir paaiškinti 2xx, 3xx, 4xx ir 5xx būsenos kodų grupes bei reaguoti į konkrečius kodus;
- kiekvienai užklausai nustatyti `timeout` ir paaiškinti, kodėl jo nebuvimas pavojingas;
- tvarkyti tinklo klaidas su `try/except` ir `requests` išimtimis, paversdamas jas aiškiomis vartotojui skirtomis žinutėmis;
- saugiai laikyti API raktą `.env` faile ir jį pašalinti iš versijų kontrolės su `.gitignore`;
- validuoti API atsakymo JSON turinį prieš jį naudojant tolimesniame kode;
- sukurti pakartotinai naudojamą modulį `api_client.py` su funkcija `send_question`, kurią vėliau, nekeičiant jos sutarties, naudos tikras DI asistentas.

## Būtinos ankstesnės žinios

Iš 7 pamokos turėtum mokėti skaityti `traceback` iki galo, naudoti `try/except/else/finally`, kurti savo klaidų klases su `raise` ir rašyti `pytest` testus grynoms funkcijoms, taip pat naudoti `logging` vietoje atsitiktinių `print()`. Šioje pamokoje lygiai tie patys įgūdžiai pritaikomi naujoje srityje – tinkle. Skirtumas tik toks: anksčiau klaidą galėjai sukelti pats (blogas failas, netinkamas JSON), o dabar klaidą gali sukelti ir visiškai nuo tavęs nepriklausanti sistema – lėtas internetas, laikinai neveikiantis serveris ar netikėtai pasikeitusi atsakymo struktūra. Jei jautiesi nesaugiai dėl `try/except` ar testavimo su netikrais (angl. *fake*) objektais, verta trumpai grįžti prie 7 pamokos prieš tęsiant.

## 1. API kaip aptarnavimo langelis

Įsivaizduok aptarnavimo langelį įstaigoje. Klientas neįeina į vidų ir nesiknisa po serverio dokumentus – jis užpildo tiksliai apibrėžtą formą: nurodo, ko nori (metodas), kokius duomenis pateikia (turinys), o langelio darbuotojas grąžina atsakymą pagal aiškią tvarką: arba išduoda pažymą (sėkmė), arba paaiškina, kodėl negali (klaida), arba paprašo užpildyti dar kartą (netinkama forma). Klientas niekada nemato, kas vyksta langelio viduje – jam svarbi tik forma ir atsakymas.

API (angl. *Application Programming Interface*) veikia lygiai taip pat. Tavo Python programa yra klientas, kitos sistemos serveris – aptarnaujantis darbuotojas. Jūs abu sutariate dėl griežtos „formos“: adreso, metodo, laukų, autentifikavimo ir galimų atsakymų. Ši sutartis vadinama API kontraktu, ir jos nesilaikant serveris tavo užklausos tiesiog nesupras arba grąžins klaidą.

```text
Python programa → HTTP užklausa → API serveris
Python programa ← HTTP atsakymas ← API serveris
```

Kiekvienoje užklausoje ir atsakyme kartojasi tos pačios dalys:

- **URL** – kur siunčiame (langelio adresas);
- **metodas** – ką norime daryti (`GET` – gauti, `POST` – sukurti/nusiųsti, `PUT/PATCH` – atnaujinti, `DELETE` – pašalinti);
- **headers** – metaduomenys, pvz. autorizacijos raktas ar programos identifikacija;
- **params** – URL užklausos parametrai (dažniausiai su `GET`);
- **JSON body** – struktūruotas siunčiamas turinys (dažniausiai su `POST`);
- **status code** – trumpas rezultato kategorijos kodas;
- **response body** – grąžinti duomenys, kuriuos programa toliau apdoroja.

Svarbiausia šios pamokos mintis: **API yra sutartis, o ne pokalbis**. Serveris nemėgins atspėti tavo ketinimo – jis tikrinsis tik pagal sutartus laukus. Todėl kiekvieną kartą, kai kuri užklausą, klausk savęs: ar žinau tikslų adresą, metodą ir laukiamą laukų formą?

> **Išbandyk pats:** įsivaizduok, kad eini į paštą siųsti registruoto laiško. Kokia informacija atitinka URL, kokia – metodą, kokia – headers, o kokia – JSON body? Užrašyk keturis atitikmenis prieš skaitydamas toliau.

## 2. Pagrindinės sąvokos

| Sąvoka | Paprastas apibrėžimas | Kasdienė analogija | Kada naudojama | Dažna klaida |
|---|---|---|---|---|
| URL | Tikslus adresas, kur siunčiama užklausa | Įstaigos langelio numeris | Kiekvienoje užklausoje | Praleista `https://` ar rašybos klaida adrese |
| HTTP metodas | Veiksmo tipas: `GET`, `POST`, `PUT/PATCH`, `DELETE` | Skirtingi formų tipai (užklausa, prašymas, pataisymas, panaikinimas) | Renkantis, ar gauname, ar siunčiame duomenis | `POST` naudojamas ten, kur pakaktų `GET` |
| Headers (antraštės) | Papildomi užklausos metaduomenys | Voko antraštė su siuntėjo duomenimis | Autorizacijai, programos identifikacijai | Manoma, kad headers yra tas pats kas turinys |
| Params (URL parametrai) | Papildomi raktažodžiai prie adreso | Formos laukeliai virš linijos | Filtruojant ar nurodant `GET` užklausos detales | Parametrai įterpiami rankiniu būdu į tekstą, ne per `params=` |
| JSON body | Struktūruotas siunčiamas turinys | Užpildytas vidinis formos lapas | Siunčiant duomenis su `POST`/`PUT` | Painiojama `json=` ir `data=` |
| Status code | Trijų skaitmenų rezultato kodas | Antspaudas ant grąžintos pažymos | Sprendžiant, ar užklausa pavyko | Manoma, kad sėkmingas kodas garantuoja teisingą turinį |
| Timeout | Maksimalus laukimo laikas atsakymui | Laiko limitas eilėje prie langelio | Kiekvienoje tinklo užklausoje | Timeout nenurodomas visai |
| Session (sesija) | Pakartotinai naudojamas ryšys su tuo pačiu serveriu | Nuolatinis kliento kortelė tame pačiame skyriuje | Kai siunčiama daug užklausų tam pačiam serveriui | Kiekvienai užklausai kuriamas naujas ryšys be reikalo |

Trumpas bendras pavyzdys, kuriame dalyvauja beveik visos sąvokos:

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    params={"topic": "python"},
    headers={"User-Agent": "kurso-demo/1.0"},
    timeout=10,
)
print(response.status_code)
print(response.json()["args"])
```

```text
200
{'topic': 'python'}
```

## 3. Vizualūs paaiškinimai

### Vizualizacija A – užklausos ir atsakymo kelionė

```text
   TAVO PYTHON PROGRAMA                         API SERVERIS
   ┌─────────────────────┐                     ┌─────────────────┐
   │ requests.get(url,    │  ── HTTP užklausa ─►│ Priima metodą,  │
   │ params, headers,     │     (metodas, URL,   │ headers, params │
   │ timeout=10)           │      headers, params)│ Apdoroja        │
   └─────────────────────┘                     └─────────────────┘
             ▲                                          │
             │        ◄── HTTP atsakymas ────────────────┘
             │        (status code + JSON body)
   ┌─────────────────────┐
   │ response.status_code │
   │ response.json()      │
   └─────────────────────┘
```

**Iliustracijos pavadinimas:** „Užklausos ir atsakymo apskritas ratas“
**Ką ji turi parodyti:** kad HTTP bendravimas visada turi dvi kryptis – išsiunčiama užklausa su savo dalimis, gaunamas atsakymas su savo dalimis, ir tarp jų praeina laikas, kurį riboja `timeout`.
**Kokie elementai turi būti matomi:** Python programos dėžutė, API serverio dėžutė, rodyklė „į priekį“ su užklausos dalimis, rodyklė „atgal“ su atsakymo dalimis.
**Siūlomas vaizdo generavimo promptas:** „Minimalistinė edukacinė vektorinė schema lietuviškai: kairėje Python programa, dešinėje API serveris, viršutinė rodyklė žymi HTTP užklausą su metodu ir parametrais, apatinė rodyklė – HTTP atsakymą su status code ir JSON; aiškios etiketės, aukštas kontrastas.“

### Vizualizacija B – būsenos kodų kategorijos

```text
        HTTP STATUS CODE
              │
    ┌─────────┼─────────┬─────────┐
    ▼         ▼         ▼         ▼
  2xx       3xx       4xx       5xx
 Pavyko   Nukreipta  Kliento   Serverio
          (retry     klaida    klaida
           su naujo   (patikrink (bandyk
           adresu)    savo       vėliau /
                      užklausą)  praneškite)
  200 OK    301, 302   400, 401   500, 502
  201                  403, 404   503, 504
                       429
```

**Iliustracijos pavadinimas:** „Keturios būsenos kodų šeimos“
**Ką ji turi parodyti:** kad pirmas skaitmuo iškart pasako, kuriai bendrai kategorijai priklauso atsakymas, dar neskaitant konkretaus kodo.
**Kokie elementai turi būti matomi:** vienas šaltinis „HTTP status code“, keturios šakos su etiketėmis 2xx/3xx/4xx/5xx, kiekvienai šakai trumpas paaiškinimas ir po du pavyzdinius kodus.
**Siūlomas vaizdo generavimo promptas:** „Vertikali šakojimosi diagrama lietuvių kalba: viršuje HTTP status code, keturios šakos 2xx žalia, 3xx mėlyna, 4xx geltona, 5xx raudona, kiekviena su trumpu paaiškinimu ir pavyzdiniais kodais.“

### Vizualizacija C – pakartojimas su eksponentiniu laukimu

```text
Bandymas 1  ──► GET  ──► 503 (serveris laikinai perkrautas)
                              │
                        lauk 1 s (2^0)
                              ▼
Bandymas 2  ──► GET  ──► 503
                              │
                        lauk 2 s (2^1)
                              ▼
Bandymas 3  ──► GET  ──► 200 OK ──► grąžinamas atsakymas
```

**Iliustracijos pavadinimas:** „Eksponentinio laukimo laiko juosta“
**Ką ji turi parodyti:** kad kiekvienas nesėkmingas bandymas didina laukimo laiką prieš kitą bandymą, o ne kartoja iškart be pauzės.
**Kokie elementai turi būti matomi:** trys bandymai su rodyklėmis į dešinę, kiekvienam bandymui gautas status code, tarp bandymų laukimo intervalo etiketė su didėjančia trukme.
**Siūlomas vaizdo generavimo promptas:** „Horizontali laiko juostos diagrama lietuvių kalba: trys GET bandymai su status code virš kiekvieno, tarp jų didėjančio ilgio laukimo segmentai pažymėti 1 s ir 2 s, paskutinis bandymas paryškintas žaliai kaip sėkmingas.“

## 4. Pirma GET užklausa

`GET` naudojamas, kai norime **gauti** duomenis, nieko serveryje nekeisdami. Kaip klausimas bibliotekininkui „ar turite šią knygą?“ – užklausa nieko nesukuria ir nesugadina, todėl ją galima saugiai kartoti.

Įdiek biblioteką virtualioje aplinkoje:

```bash
python -m pip install requests
```

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    params={"topic": "python", "level": "beginner"},
    timeout=10,
)

print(response.status_code)
data = response.json()
print(data["args"])
```

```text
200
{'topic': 'python', 'level': 'beginner'}
```

Eilutė po eilutės:

1. `requests.get(...)` sukuria ir iškart išsiunčia `GET` užklausą nurodytu adresu.
2. `params={...}` biblioteka pati priklijuoja prie URL kaip `?topic=python&level=beginner` – tau nereikia rankomis rašyti klaustuko ir `&`.
3. `timeout=10` sako: jei per 10 sekundžių atsakymo negaunu, sukelk klaidą, o ne lauk amžinai.
4. `response.status_code` yra sveikasis skaičius – trijų skaitmenų HTTP kodas.
5. `response.json()` paverčia atsakymo tekstą (JSON) į įprastus Python žodynus ir sąrašus, su kuriais jau moki dirbti.

> **Dažna klaida:** `timeout` praleidžiamas, nes „juk internetas paprastai veikia“. Kai serveris laikinai neatsako, programa be `timeout` gali kaboti neribotą laiką – vartotojas net nesupras, ar programa dar dirba, ar užstrigo.

**Mini užduotis.** Nusiųsk `GET` užklausą į `https://httpbin.org/get` su parametru `course="python-basics"` ir parodyk tik gautą `status_code`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    params={"course": "python-basics"},
    timeout=10,
)
print(response.status_code)
```

</details>

## 5. Būsenos kodai

Kiekvienas HTTP atsakymas turi trijų skaitmenų būsenos kodą. Pirmas skaitmuo iškart pasako bendrą kategoriją – net neskaitant konkretaus skaičiaus.

| Grupė | Reikšmė | Pavyzdžiai |
|---|---|---|
| 2xx | pavyko | 200 OK, 201 Created |
| 3xx | nukreipimas | 301, 302 |
| 4xx | kliento užklausa netinkama | 400, 401, 403, 404, 429 |
| 5xx | serverio problema | 500, 503 |

Patogiausias būdas patikrinti sėkmę – metodas, kuris pats iškelia klaidą, jei kodas nepriklauso 2xx grupei:

```python
response.raise_for_status()
```

`raise_for_status()` 4xx ar 5xx atsakymą paverčia `requests.HTTPError` išimtimi. Tačiau vartotojui dažnai verta parodyti konkretesnę žinutę pagal kodą, o ne tik bendrą klaidą:

```python
if response.status_code == 401:
    print("Patikrink autentifikavimo raktą.")
elif response.status_code == 429:
    print("Per daug užklausų. Pabandyk vėliau.")
else:
    response.raise_for_status()
```

Šis kodas pirma tikrina konkrečius, dažnai pasitaikančius kodus, o visus kitus 4xx/5xx atvejus patiki `raise_for_status()`. Pastebėk tvarką: konkretūs `if`/`elif` visada turi eiti pirma bendro sprendimo, kitaip specifinė žinutė niekada nepasieks vartotojo.

> **Dažna klaida:** manoma, kad `200 OK` reiškia „viskas gerai ir turinys toks, kokio tikėjausi“. Iš tikrųjų `200` reiškia tik tiek, kad serveris sėkmingai apdorojo užklausą – turinį vis tiek reikia validuoti atskirai (žr. 9 skyrių).

**Mini užduotis.** Parašyk kodą, kuris `404` atveju parodo „Resursas nerastas“, `500` atveju – „Serverio klaida, bandyk vėliau“, o visais kitais atvejais tiesiog iškviečia `raise_for_status()`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
if response.status_code == 404:
    print("Resursas nerastas")
elif response.status_code == 500:
    print("Serverio klaida, bandyk vėliau")
else:
    response.raise_for_status()
```

</details>

## 6. POST ir JSON turinys

`POST` naudojamas, kai norime kažką **sukurti ar nusiųsti** – naują užsakymą, klausimą, registraciją. Skirtingai nei `GET`, `POST` gali turėti šalutinį poveikį (pvz., sukurti įrašą duomenų bazėje), todėl jo negalima be minties kartoti (plačiau apie tai 15 skyriuje).

```python
payload = {
    "question": "Kiek trunka Python kursas?",
    "language": "lt",
}

response = requests.post(
    "https://httpbin.org/post",
    json=payload,
    timeout=10,
)
response.raise_for_status()
print(response.json()["json"])
```

```text
{'question': 'Kiek trunka Python kursas?', 'language': 'lt'}
```

Naudojant `json=payload`, biblioteka pati:

1. paverčia Python žodyną į JSON tekstą;
2. prideda antraštę `Content-Type: application/json`, kad serveris žinotų, kaip skaityti turinį;
3. įdeda šį tekstą į užklausos kūną (angl. *body*), o ne į URL.

`data=payload` yra visiškai kitas formatas (dažniausiai formų duomenims, `application/x-www-form-urlencoded`) – jo nepainiok su `json=`, nes serveris, tikintis JSON, gaus ne tai, ko tikėjosi, ir arba grąžins klaidą, arba – kas dar blogiau – tyliai neteisingai supras duomenis.

> **Dažna klaida:** parašoma `requests.post(url, data=payload)`, kai serveris tikisi JSON. Užklausa techniškai išsiunčiama, bet serveris gauna formos duomenis, ne struktūruotą JSON – dažnai grąžinama `400 Bad Request` arba laukai tiesiog dingsta.

**Mini užduotis.** Nusiųsk `POST` užklausą į `https://httpbin.org/post` su JSON kūnu `{"topic": "api", "urgent": True}` ir atspausdink tik grąžintą `json` lauką.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
response = requests.post(
    "https://httpbin.org/post",
    json={"topic": "api", "urgent": True},
    timeout=10,
)
response.raise_for_status()
print(response.json()["json"])
```

</details>

## 7. Tinklo klaidos ir atsparumas

HTTP klaida (4xx/5xx) yra tik viena problemų rūšis – serveris bent jau atsakė. Kartais atsakymo iš viso nebūna: nutrūksta interneto ryšys, serveris neatsako per `timeout` laiką, arba atsakymas ateina, bet nėra tinkamas JSON. Kiekvienai situacijai reikia atskiro, aiškaus `except` bloko – lygiai taip pat, kaip 7 pamokoje gaudėme tik tas klaidas, kurias sugebame sutvarkyti.

```python
import requests

def fetch_json(url: str, params: dict | None = None) -> dict:
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.Timeout as exc:
        raise RuntimeError("API neatsakė laiku") from exc
    except requests.HTTPError as exc:
        code = exc.response.status_code if exc.response is not None else "?"
        raise RuntimeError(f"API grąžino HTTP {code}") from exc
    except requests.RequestException as exc:
        raise RuntimeError("Nepavyko prisijungti prie API") from exc
    except ValueError as exc:
        raise RuntimeError("API grąžino ne JSON") from exc
```

Eilutė po eilutės:

1. `requests.Timeout` gaudomas pirmiausia – tai konkretus, dažnas atvejis (serveris tiesiog neatsako laiku).
2. `requests.HTTPError` gaudomas antras – atsakymas atėjo, bet `raise_for_status()` jį pažymėjo kaip 4xx/5xx; iš išimties objekto dar galime ištraukti konkretų kodą.
3. `requests.RequestException` yra bendra visų `requests` tinklo klaidų „tėvinė“ klasė (DNS klaida, nutrūkęs ryšys ir pan.) – ji gaudoma paskutinė iš `requests` klaidų, nes ji apima ir `Timeout`, ir `HTTPError`.
4. `ValueError` gaudomas atskirai – tai atsiranda, kai `response.json()` gauna tekstą, kuris nėra tinkamas JSON (pvz., serveris grąžino HTML klaidos puslapį).
5. Kiekvienu atveju originalią techninę klaidą paverčiame savo suprantama `RuntimeError` žinute su `raise ... from exc` – tokiu būdu kviečiantis kodas gauna vieną nuspėjamą išimties tipą, o pilnas techninis kontekstas išlieka `__cause__` lauke derinimui.

> **Dažna klaida:** rašomas vienas platus `except Exception:`, kuris paslepia ir tikrą tinklo problemą, ir savo pačių programavimo klaidą (pvz., klaidingai parašytą kintamojo vardą). Gaudyk tik tas klaidas, kurias iš tiesų numatai ir sugebi sutvarkyti.

**Mini užduotis.** Iškviesk `fetch_json("https://httpbin.org/status/500")` ir apgaubk kvietimą `try/except RuntimeError`, atspausdindamas gautą žinutę.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
try:
    data = fetch_json("https://httpbin.org/status/500")
except RuntimeError as exc:
    print(f"Klaida: {exc}")
```

```text
Klaida: API grąžino HTTP 500
```

</details>

## 8. Paslaptys ir `.env`

API raktas yra kaip namų raktas – jį rodai tik tam, kas turi teisę įeiti, ir niekada nepalieki matomoje vietoje. Kodas su „įdėtu“ raktu, patalpintas į Git, lieka istorijoje amžinai, net jei vėliau jį ištrini iš paskutinio commit'o.

`.env`:

```text
SERVICE_API_KEY=mano_slaptas_raktas
```

`.gitignore`:

```text
.env
.venv/
__pycache__/
```

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SERVICE_API_KEY")
if not api_key:
    raise RuntimeError("Trūksta SERVICE_API_KEY")

headers = {"Authorization": f"Bearer {api_key}"}
```

Eilutė po eilutės:

1. `load_dotenv()` perskaito `.env` failą ir įkelia jo reikšmes į proceso aplinkos kintamuosius – tai reikia iškviesti prieš pirmą `os.getenv()`.
2. `os.getenv("SERVICE_API_KEY")` grąžina raktą arba `None`, jei jo nėra – niekada nekelia klaidos pats.
3. `if not api_key:` patikra iškart sustabdo programą su aiškiu pranešimu, jei raktas nesukonfigūruotas, užuot vėliau gavus neaiškų `401` iš serverio.
4. `headers` žodynas su `Authorization: Bearer ...` yra standartinis būdas API serveriui perduoti raktą.

Įdiek `python-dotenv` (`python -m pip install python-dotenv`). Į repozitoriją dėk tik `.env.example` su tuščiais pavyzdiniais laukais (pvz., `SERVICE_API_KEY=`), o pats `.env` visada lieka tik tavo kompiuteryje.

> **Dažna klaida:** raktas patenka į `print()` derinimo tikslais, į `logging` žinutę arba į klaidos pranešimą, kuris vėliau nukeliauja į bendrą log'ų sistemą ar ekrano nuotrauką pagalbos komandai. Rakto nespausdink, nesiųsk ekrano nuotraukoje ir neįrašyk į klaidų logą – net derinant kodą laikinai.

**Mini užduotis.** Parašyk kodą, kuris nuskaito `SERVICE_API_KEY` iš aplinkos ir, jei jo nėra, iškelia `RuntimeError` su žinute `"Trūksta SERVICE_API_KEY"`, o jei yra – atspausdina tik žinutę `"Raktas rastas"` (niekada patį raktą).

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SERVICE_API_KEY")
if not api_key:
    raise RuntimeError("Trūksta SERVICE_API_KEY")
print("Raktas rastas")
```

</details>

## 9. API atsakymo validavimas

Sėkmingas HTTP kodas dar negarantuoja, kad atsakyme yra laukas, kurio tikiesi – serveris gali grąžinti `200 OK` su tuščiu žodynu, su kitokia struktūra nei dokumentacijoje aprašyta, ar net su lauku, kurio reikšmė netinkamo tipo.

```python
def read_answer(data: dict) -> str:
    answer = data.get("answer")
    if not isinstance(answer, str) or not answer.strip():
        raise ValueError("Atsakyme trūksta tekstinio lauko 'answer'")
    return answer.strip()
```

Eilutė po eilutės:

1. `data.get("answer")` saugiai paima reikšmę arba `None`, jei rakto nėra – be `KeyError` rizikos.
2. `isinstance(answer, str)` patikrina, kad reikšmė iš tikrųjų yra tekstas, o ne, pavyzdžiui, `None`, skaičius ar žodynas.
3. `not answer.strip()` atmeta ir tuščią, ir vien iš tarpų sudarytą tekstą.
4. Radus problemą, iškeliame `ValueError` su konkrečia žinute – funkcija niekada tyliai negrąžina „šiukšlių“ toliau naudojamam kodui.

Ši funkcija yra paskutinis patikros sluoksnis prieš duomenis pasiekiant likusią programos dalį: pirma tikrinome tinklo klaidas, tada HTTP statusą, o dabar – patį turinį.

> **Dažna klaida:** patikrinamas tik `response.status_code == 200` ir iškart naudojamas `data["answer"]` be jokios validacijos. Jei laukas kada nors dings ar pasikeis tipas, programa žlugs su neaiškiu `KeyError` giliai kode, o ne su aiškia žinute ten, kur problema atsirado.

**Mini užduotis.** Iškviesk `read_answer({"answer": "  Sveiki  "})` ir `read_answer({"status": "ok"})`. Ką grąžina pirmas kvietimas ir kas nutinka antram?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Pirmas kvietimas grąžina `"Sveiki"` (be tarpų). Antras iškelia `ValueError("Atsakyme trūksta tekstinio lauko 'answer'")`, nes žodyne nėra rakto `"answer"`.

</details>

## 10. Įvairūs kodo pavyzdžiai

### Minimalus pavyzdys

**Problema:** vienu sakiniu patikrinti, ar serveris apskritai pasiekiamas.

```python
import requests

response = requests.get("https://httpbin.org/get", timeout=5)
print(response.status_code)
```

```text
200
```

**Patobulinimas:** pridėk `params` su bent vienu raktu.

### Kasdienis pavyzdys – valiutos kurso užklausa

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    params={"base": "EUR", "target": "USD"},
    timeout=10,
)
response.raise_for_status()
print(response.json()["args"])
```

```text
{'base': 'EUR', 'target': 'USD'}
```

**Patobulinimas:** apskaičiuok sumą pagal grąžintą (šiuo atveju imituotą) kursą.

### Automatizavimo pavyzdys – kelios užklausos su viena sesija

```python
import requests

session = requests.Session()
session.headers.update({"User-Agent": "kurso-demo/1.0"})

topics = ["python", "api", "testai"]
for topic in topics:
    response = session.get(
        "https://httpbin.org/get",
        params={"topic": topic},
        timeout=10,
    )
    response.raise_for_status()
    print(response.json()["args"]["topic"])
```

```text
python
api
testai
```

**Patobulinimas:** rezultatus surink į sąrašą vietoj tiesioginio spausdinimo.

### Duomenų ir AI pavyzdys – imituotas klasifikatoriaus API

```python
import requests

def classify_message(message: str) -> dict:
    response = requests.post(
        "https://httpbin.org/post",
        json={"message": message},
        timeout=10,
    )
    response.raise_for_status()
    echoed = response.json()["json"]["message"]
    return {"message": echoed, "predicted_topic": "pristatymas", "confidence": 0.87}

result = classify_message("Noriu pakeisti pristatymo adresą")
print(result)
```

```text
{'message': 'Noriu pakeisti pristatymo adresą', 'predicted_topic': 'pristatymas', 'confidence': 0.87}
```

**Patobulinimas:** pridėk `read_answer`-tipo validaciją prieš grąžinant žodyną.

### Klaidingas pavyzdys – pataisyk

```python
response = requests.post("https://httpbin.org/post", data={"question": "Kaina?"})
print(response.json()["json"]["question"])
```

Šis kodas be `timeout` gali kaboti neribotą laiką, o `data=` vietoj `json=` gali reikšti, kad serveris, tikintis JSON, negaus `"json"` rakto atsakyme – kvietimas sukels `KeyError`.

Pataisymas:

```python
response = requests.post(
    "https://httpbin.org/post",
    json={"question": "Kaina?"},
    timeout=10,
)
response.raise_for_status()
print(response.json()["json"]["question"])
```

## 11. Interaktyvios veiklos

### 1. Nuspėk rezultatą

```python
response_status = 404
if response_status == 200:
    print("sėkmė")
elif 400 <= response_status < 500:
    print("kliento klaida")
elif 500 <= response_status < 600:
    print("serverio klaida")
```

A. `sėkmė`
B. `kliento klaida`
C. `serverio klaida`
D. Nieko nebus atspausdinta

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** `404` patenka į intervalą `400 <= 404 < 500`, todėl atspausdinama „kliento klaida“.

</details>

### 2. Užpildyk trūkstamą kodą

```python
response = requests.get(
    "https://httpbin.org/get",
    params={"q": "python"},
    ____=10,
)
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
timeout=10
```

Be `timeout` programa rizikuoja laukti atsakymo neribotą laiką.

</details>

### 3. Surask klaidą

```python
response = requests.post("https://httpbin.org/post", data=payload, timeout=10)
response.raise_for_status()
print(response.json()["json"]["question"])
```

Nustatyk klaidą, paaiškink ir pataisyk.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

Naudojamas `data=payload` vietoj `json=payload`. Serveris, tikintis JSON kūno, negaus tinkamai užkoduoto turinio ir `"json"` raktas atsakyme gali būti tuščias.

```python
response = requests.post("https://httpbin.org/post", json=payload, timeout=10)
response.raise_for_status()
print(response.json()["json"]["question"])
```

</details>

### 4. Sudėliok teisingą tvarką

```text
data = response.json()
response.raise_for_status()
response = requests.get(url, params=params, timeout=10)
answer = read_answer(data)
```

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

```python
response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()
answer = read_answer(data)
```

Pirma siunčiama užklausa, tada tikrinamas statusas, tik po to skaitomas JSON ir galiausiai validuojamas turinys.

</details>

### 5. Pasirink tinkamą sprendimą

Serveris kartais grąžina `503` ir netrukus vėl veikia normaliai. Kuris variantas tinkamai tvarko šią situaciją idempotentei `GET` užklausai?

A. Kartoti tą pačią užklausą iškart be pauzės neribotą kartų skaičių.
B. Kartoti ribotą kartų skaičių su didėjančia pauze tarp bandymų, tik `GET` metodui.
C. Iš karto rodyti vartotojui neišverstą `Traceback`.

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymą</summary>

**B.** Ribotas pakartojimų skaičius su eksponentiniu laukimu tinka laikinoms serverio klaidoms ir idempotentiems metodams; begalinis kartojimas ar techninio pranešimo rodymas vartotojui nėra tinkamas sprendimas.

</details>

### 6. Parašyk pats

Parašyk funkciją `get_status_category(code: int) -> str`, kuri grąžina `"sėkmė"`, `"nukreipimas"`, `"kliento klaida"`, `"serverio klaida"` arba `"nežinoma"` pagal pirmą kodo skaitmenį. Patikrink su kodais `200`, `301`, `404`, `503` ir `150`.

### 7. Patobulink kodą

```python
def get_data(url):
    r = requests.get(url)
    return r.json()
```

Pridėk `timeout`, `raise_for_status()`, aiškų tipą grąžinamai reikšmei ir bent vieną `except` bloką tinklo klaidai.

## 12. Žinių patikrinimas prieš platformos testą

Pirmiausia atsakyk neužleisdamas atsakymų.

1. Kuo `GET` iš esmės skiriasi nuo `POST` savo paskirtimi?
2. Ką reiškia `timeout=(3, 10)` perduota `requests.get()`?
3. Kodėl saugu automatiškai kartoti nesėkmingą `GET` užklausą, bet nesaugu automatiškai kartoti `POST`?
4. Kokį pagrindinį pranašumą suteikia `requests.Session()`, palyginti su nauju `requests.get()` kiekvienai užklausai?
5. Kam reikalingas `load_dotenv()` kvietimas prieš `os.getenv("SERVICE_API_KEY")`?
6. Kokio tipo Python reikšmę grąžina `response.json()`, kai API atsako JSON masyvu (pvz., `[1, 2, 3]`)?
7. Kuriai būsenos kodų grupei priklauso klaida, kurią sukėlė serverio vidinė problema, o ne tavo užklausa?
8. Kodėl `api_client.py` funkcija `send_question` turėtų grąžinti paprastą `str`, o ne visą `requests.Response` objektą?
9. Kam naudojama `User-Agent` antraštė, kai užklausą siunčiame per `Session`?

<details class="selfcheck" markdown="1"><summary>Rodyti atsakymus ir paaiškinimus</summary>

1. `GET` skirtas duomenims gauti nieko nekeičiant serveryje, `POST` – naujam ištekliui sukurti ar veiksmui atlikti; `GET` galima saugiai kartoti, `POST` – ne visada.
2. Pirmas skaičius – kiek sekundžių leidžiama laukti prisijungimo prie serverio, antras – kiek laukti atsakymo turinio po prisijungimo.
3. `GET` yra idempotentis – kartojant tą pačią užklausą rezultatas serveryje nesikeičia. `POST` gali turėti šalutinį poveikį (pvz., sukurti įrašą), todėl kartojant rizikuojame sukurti tą patį veiksmą kelis kartus.
4. `Session` pakartotinai naudoja tą patį TCP ryšį kelioms užklausoms tam pačiam serveriui, todėl užklausos vykdomos greičiau ir nereikia kaskart iš naujo nurodyti tų pačių antraščių.
5. `load_dotenv()` perskaito `.env` failą ir įkelia jo reikšmes į proceso aplinkos kintamuosius; be šio kvietimo `os.getenv()` reikšmių iš `.env` tiesiog nematytų.
6. `list` (Python sąrašą) – `response.json()` paverčia JSON tekstą į atitinkamą Python struktūrą, o masyvas JSON'e tampa sąrašu.
7. 5xx grupei.
8. Kad `main.py` (ir kitas kviečiantis kodas) nereikėtų žinoti apie HTTP detales – antraštes, statuso kodus, `requests` išimtis; visą tą sudėtingumą paslepia `api_client.py`, o kviečiantis kodas gauna tik paprastą, patikrintą tekstą arba aiškią klaidą.
9. Ji identifikuoja, kokia programa ar klientas siunčia užklausą – kai kurios API serverio pusėje naudoja tai statistikai, diagnostikai ar netgi skirtingam elgesiui priklausomai nuo kliento.

</details>

## 13. Praktinės užduotys

### A lygis – užklausos inspektorius

**Sąlyga:** su `https://httpbin.org/get` nusiųsk `GET` užklausą su bent trimis parametrais. Parodyk galutinį užklausos URL (`response.url`), gautą statuso kodą ir serverio grąžintus parametrus. Papildomai patikrink, kas nutinka, kai `timeout` nustatytas itin trumpas (pvz., `0.001`).
**Pavyzdinė įvestis:** parametrai `{"course": "python-basics", "level": "beginner", "lesson": "8"}`.
**Laukiamas rezultatas:** atspausdintas pilnas URL su parametrais, `status_code 200`, žodynas su trimis raktais, o su itin trumpu `timeout` – sugauta ir aiškiai paaiškinta `requests.Timeout` (arba `ConnectTimeout`) klaida.
**Užuomina:** `response.url` visada rodo tikslų adresą, į kurį nukeliavo užklausa, įskaitant automatiškai priklijuotus parametrus.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
import requests

params = {"course": "python-basics", "level": "beginner", "lesson": "8"}

response = requests.get("https://httpbin.org/get", params=params, timeout=10)
print(response.url)
print(response.status_code)
print(response.json()["args"])

try:
    requests.get("https://httpbin.org/get", params=params, timeout=0.001)
except requests.exceptions.Timeout:
    print("Užklausa nutrūko: timeout per trumpas realiam tinklo ryšiui.")
```

Su realiu tinklu itin trumpas `timeout` beveik visada sukelia `requests.exceptions.Timeout` (arba jo pogrupį `ConnectTimeout`), nes serveris fiziškai negali atsakyti per mažiau nei milisekundę. **Papildomas iššūkis:** palygink `response.elapsed` reikšmę su keliais skirtingais `timeout` nustatymais.

</details>

### B lygis – API klientas be klasės

**Sąlyga:** neaprašydamas klasės, parašyk keturias atskiras funkcijas: `build_headers() -> dict` (sudaro antraštes su neprivalomu API raktu), `get_json(url: str, params: dict | None = None) -> dict` (atlieka `GET` ir grąžina JSON arba iškelia `RuntimeError`), `post_json(url: str, payload: dict) -> dict` (atlieka `POST` su JSON kūnu), `explain_status(code: int) -> str` (grąžina žmogui suprantamą paaiškinimą pagal kodų grupę). Visos funkcijos turi aiškius tipų anotacijas. `explain_status` turi bent 3 testus be jokio tikro tinklo.
**Pavyzdinė įvestis:** `explain_status(404)`, `explain_status(200)`, `explain_status(503)`.
**Laukiamas rezultatas:** kiekvienam kodui grąžinamas skirtingas, žmogui suprantamas lietuviškas sakinys; testai praeina be interneto ryšio.
**Užuomina:** `explain_status` yra grynoji funkcija (nesiunčia jokios užklausos), todėl ją testuoti lengviausia – tiesiog perduok skaičių ir tikrink tekstą.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
import requests


def build_headers(api_key: str | None = None) -> dict:
    headers = {"User-Agent": "kurso-api-klientas/1.0"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def get_json(url: str, params: dict | None = None) -> dict:
    try:
        response = requests.get(url, params=params, headers=build_headers(), timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        raise RuntimeError("Nepavyko gauti duomenų iš API") from exc


def post_json(url: str, payload: dict) -> dict:
    try:
        response = requests.post(url, json=payload, headers=build_headers(), timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        raise RuntimeError("Nepavyko nusiųsti duomenų į API") from exc


def explain_status(code: int) -> str:
    if 200 <= code < 300:
        return "Užklausa sėkminga."
    if 400 <= code < 500:
        return "Patikrink savo užklausą – kliento pusės klaida."
    if 500 <= code < 600:
        return "Serverio problema – pabandyk vėliau."
    return "Nežinoma būsenos kodų grupė."


# testai be tikro tinklo
def test_explain_status_success():
    assert explain_status(200) == "Užklausa sėkminga."


def test_explain_status_client_error():
    assert explain_status(404) == "Patikrink savo užklausą – kliento pusės klaida."


def test_explain_status_server_error():
    assert explain_status(503) == "Serverio problema – pabandyk vėliau."
```

`explain_status` nenaudoja `requests`, todėl jai testuoti nereikia jokio tinklo ar imitacijos – tai grynoji funkcija tiesiogine 7 pamokos prasme. **Papildomas iššūkis:** pridėk testą kodui `999`, kuris turėtų grąžinti „Nežinoma būsenos kodų grupė.“.

</details>

### C lygis – patikima integracija

**Sąlyga:** pridėk iki 3 pakartojimų `GET` užklausai tik 429 ir 5xx (500, 502, 503, 504) atsakymų atveju, kiekvieną kartą didinant laukimą (pvz., 1 s, 2 s, 4 s). Kitiems kodams (pvz., 401, 404) pakartojimų nedaryk – iškart praneš vartotojui. Loguose saugok tik būsenos kodą, bandymo numerį ir trukmę – niekada raktą ar visą atsakymo turinį.
**Pavyzdinė įvestis:** imituotas serveris, kuris pirmus du kartus grąžina `503`, o trečią – `200`.
**Laukiamas rezultatas:** funkcija grąžina sėkmingą atsakymą po trečio bandymo; žurnale matomos trys eilutės su bandymo numeriu ir kodu, bet be jokio jautraus turinio.
**Užuomina:** pakartojimo ciklą patogu testuoti su netikru (angl. *fake*) `Session` objektu, kurio `get()` metodas iš anksto paruoštos sekos grąžina skirtingus atsakymus kiekvieną kartą, kai jis iškviečiamas.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
import logging
import time

import requests

RETRYABLE_CODES = {429, 500, 502, 503, 504}


def get_with_retry(session: requests.Session, url: str, max_attempts: int = 3) -> requests.Response:
    for attempt in range(max_attempts):
        started = time.monotonic()
        response = session.get(url, timeout=10)
        duration = time.monotonic() - started
        logging.info("bandymas=%s statusas=%s trukme=%.3f", attempt + 1, response.status_code, duration)

        if response.status_code not in RETRYABLE_CODES:
            response.raise_for_status()
            return response

        if attempt == max_attempts - 1:
            response.raise_for_status()

        time.sleep(2 ** attempt)

    raise RuntimeError("Nepasiektas sėkmingas atsakymas")
```

Testas be tikro tinklo naudoja netikrą `Session`, kurio `get()` iš anksto paruoštos sekos grąžina skirtingus objektus:

```python
class FakeResponse:
    def __init__(self, status_code: int) -> None:
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")


class FakeSession:
    def __init__(self, responses: list[FakeResponse]) -> None:
        self._responses = iter(responses)

    def get(self, url: str, timeout: int) -> FakeResponse:
        return next(self._responses)


def test_retry_succeeds_after_two_failures():
    fake_session = FakeSession([FakeResponse(503), FakeResponse(503), FakeResponse(200)])
    result = get_with_retry(fake_session, "https://example.test", max_attempts=3)
    assert result.status_code == 200
```

Žurnalo eilutėje yra tik bandymo numeris, kodas ir trukmė – jokio URL su raktu ar atsakymo turinio. **Papildomas iššūkis:** leisk vartotojui nutraukti laukimą tarp bandymų klaviatūros pertraukimu (`KeyboardInterrupt`) ir tada grąžink aiškų pranešimą, o ne netvarkingą `traceback`.

</details>

## 14. Mini projektas: API klientas būsimam asistentui

### 1. Projekto situacija

Asistentas kol kas atsako tik pagal vietinę žinių bazę. Kitame etape jam reikės klausti tikro DI modelio internetu, o tam reikalingas patikimas, gerai izoliuotas HTTP klientas – toks, kad likusi programos dalis (`main.py`) apie tinklo detales net nesužinotų.

### 2. Galutinis tikslas

Sukurti modulį `api_client.py` su viena vieša funkcija:

```python
def send_question(question: str) -> str:
    """Nusiunčia klausimą ir grąžina tik patikrintą atsakymo tekstą."""
```

Modulio viduje gali būti tiek pagalbinių funkcijų, kiek reikia (pvz., antraščių sudarymas, atsakymo validavimas), bet **viešas kontraktas yra vienas** – vardas, argumentas ir grąžinamas tipas negali keistis net kai 9 pamokoje bandomąjį `POST` endpoint pakeisi tikru OpenAI Responses API kvietimu.

### 3. Funkciniai reikalavimai

Modulis turi:

1. priimti klausimą kaip `str` ir atmesti tuščią ar vien iš tarpų sudarytą klausimą su aiškia klaida;
2. nusiųsti klausimą bandomajam `POST` endpoint (`https://httpbin.org/post`) su `timeout` ir tinkamomis antraštėmis;
3. atskirai gaudyti laiko limito, HTTP ir bendrą tinklo klaidą, kiekvieną paverčiant sava `RuntimeError` žinute;
4. validuoti gautą turinį prieš grąžinant – naudoti tą pačią `read_answer(data: dict) -> str` sutartį, kurią jau žinai iš 9 skyriaus;
5. niekada nespausdinti ir neloginti API rakto;
6. neatskleisti `main.py` jokių `requests` tipų, antraščių ar statuso kodų – tik `str` rezultatą arba iškeltą `RuntimeError`.

### 4. Sąveika su `main.py`

`main.py` turi galėti naudoti modulį taip paprastai, tarsi tai būtų vietinė funkcija be jokio tinklo:

```python
from api_client import send_question

try:
    answer = send_question("Kiek trunka Python kursas?")
    print(f"Asistentas: {answer}")
except RuntimeError as exc:
    print(f"Nepavyko gauti atsakymo: {exc}")
```

### 5. Laukiamas rezultatas

```text
Asistentas: (bandomasis atsakymas) gavau klausimą: Kiek trunka Python kursas?
```

Klaidos atveju (pvz., dingus interneto ryšiui):

```text
Nepavyko gauti atsakymo: Nepavyko prisijungti prie API
```

### 6. Projekto kūrimo etapai

1. Sukurk `api_client.py` ir jame `read_answer` (identišką 9 skyriuje aprašytai).
2. Parašyk `build_headers()`, kuri sudaro antraštes su neprivalomu raktu iš `.env`.
3. Parašyk `send_question()`, kuri patikrina tuščią klausimą ir iškelia `ValueError`.
4. `send_question()` viduje nusiųsk `POST` su `json={"question": question}` ir `timeout=10`.
5. Apgaubk siuntimą `try/except` blokais pagal 7 skyriaus pavyzdį.
6. Iš httpbin atsako paimk atgal atspindėtą (angl. *echoed*) klausimą ir sukonstruok laikiną `{"answer": ...}` žodyną – kol nėra tikros API, patys imituojame minimalią atsakymo struktūrą.
7. Perduok šį žodyną `read_answer()` ir grąžink jos rezultatą.
8. Parašyk bent 8 testus: tuščias klausimas, normalus klausimas, laiko limito klaida, HTTP klaida, bendra tinklo klaida, netinkamas JSON, trūkstamas `answer` laukas, sėkmingas pilnas maršrutas.
9. Patikrink, kad `main.py` niekur neimportuoja `requests`.

### 7. Pseudokodas

```text
FUNKCIJA send_question(question):
    IŠVALYK question tarpus
    JEI question tuščias:
        KELK ValueError
    BANDYK:
        NUSIŲSK POST su json={"question": question}, headers, timeout
        PATIKRINK statusą
        PAIMK echoed klausimą iš atsakymo
    GAUDYK Timeout: KELK RuntimeError("API neatsakė laiku")
    GAUDYK HTTPError: KELK RuntimeError su kodu
    GAUDYK RequestException: KELK RuntimeError("Nepavyko prisijungti prie API")
    SUKURK simuliuotą {"answer": ...} žodyną
    GRĄŽINK read_answer(simuliuotas žodynas)
```

<details class="selfcheck" markdown="1"><summary>Rodyti pilną sprendimą</summary>

`api_client.py`:

```python
import os

import requests
from dotenv import load_dotenv

load_dotenv()

BANDOMASIS_URL = "https://httpbin.org/post"
TIMEOUT = 10


def build_headers() -> dict:
    headers = {"User-Agent": "python-kurso-asistentas/0.1"}
    api_key = os.getenv("SERVICE_API_KEY")
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    return headers


def read_answer(data: dict) -> str:
    answer = data.get("answer")
    if not isinstance(answer, str) or not answer.strip():
        raise ValueError("Atsakyme trūksta tekstinio lauko 'answer'")
    return answer.strip()


def send_question(question: str) -> str:
    """Nusiunčia klausimą ir grąžina tik patikrintą atsakymo tekstą."""
    clean_question = question.strip()
    if not clean_question:
        raise ValueError("Klausimas negali būti tuščias")

    try:
        response = requests.post(
            BANDOMASIS_URL,
            json={"question": clean_question},
            headers=build_headers(),
            timeout=TIMEOUT,
        )
        response.raise_for_status()
        echoed_question = response.json()["json"]["question"]
    except requests.Timeout as exc:
        raise RuntimeError("API neatsakė laiku") from exc
    except requests.HTTPError as exc:
        code = exc.response.status_code if exc.response is not None else "?"
        raise RuntimeError(f"API grąžino HTTP {code}") from exc
    except requests.RequestException as exc:
        raise RuntimeError("Nepavyko prisijungti prie API") from exc
    except (KeyError, ValueError) as exc:
        raise RuntimeError("API grąžino netikėtą turinį") from exc

    # Kol neturime tikros DI API, patys sukonstruojame minimalią atsakymo
    # struktūrą – tai leidžia iš karto naudoti tą pačią read_answer validaciją,
    # kurią 9 pamokoje pritaikysime tikram DI atsakymui.
    simulated_response = {"answer": f"(bandomasis atsakymas) gavau klausimą: {echoed_question}"}
    return read_answer(simulated_response)
```

Testus `test_api_client.py` rašyk be tikro tinklo – pakanka tiesiogiai tikrinti `read_answer` su skirtingais žodynais (kaip 9 skyriaus mini užduotyje) ir `send_question("   ")`, kuris turi iškelti `ValueError` dar prieš siunčiant bet kokią užklausą.

`main.py` niekur neimportuoja `requests` – jis mato tik `send_question` ir `RuntimeError`/`ValueError`. Visos HTTP detalės (antraštės, statusai, JSON struktūra) lieka `api_client.py` viduje. **Papildomas iššūkis:** pridėk aplinkos kintamąjį `API_MODE=bandomasis`/`realus`, kad ateityje būtų lengva perjungti tarp httpbin ir tikros API be `send_question` signatūros keitimo.

</details>

### 8. Galimi patobulinimai

- pridėk pakartojimą 429/5xx atvejais, remdamasis 15 skyriaus retry logika;
- naudok `requests.Session()` vietoje pavienių `requests.post()` kvietimų;
- įtrauk `sequence diagram` (sekos schemą), rodančią kelią nuo vartotojo klausimo iki grąžinto atsakymo;
- pridėk konfigūruojamą `timeout` iš `.env`;
- vėliau (9 pamokoje) pakeisk vidinę realizaciją realiu DI kvietimu, nekeisdamas `send_question` sutarties.

### 9. `README.md` šablonas

```text
# api_client.py – HTTP klientas būsimam asistentui

Pakartotinai naudojamas modulis, kuris paslepia visas HTTP detales
nuo likusios asistento programos dalies.

## Vieša sutartis
send_question(question: str) -> str

## Funkcijos
- Tikrina tuščią klausimą
- Siunčia POST su timeout ir headers
- Atskirai gaudo laiko limito, HTTP ir tinklo klaidas
- Validuoja atsakymo JSON prieš grąžinant

## Paleidimas
python main.py

## Testai
python -m pytest -q

## Ką išmokau
requests, GET/POST, JSON body, status code, timeout, .env, retry principai.

## Tolimesni patobulinimai
Sesija, pakartojimas su backoff, realaus DI API prijungimas 9 pamokoje.
```

## 15. Gilioji laboratorija: tinklas nėra patikimas

### Sesija ir pakartojimas

Kiekvienam kvietimui kuriant naują ryšį didėja delsa. Daugeliui užklausų naudok `requests.Session()`:

```python
import requests

session = requests.Session()
session.headers.update({"User-Agent": "python-kurso-asistentas/0.1"})
response = session.get("https://httpbin.org/get", timeout=(3, 10))
response.raise_for_status()
```

`timeout=(3, 10)` reiškia 3 sekundes prisijungimui ir 10 atsakymui. Prisijungimo (angl. *connect*) ir skaitymo (angl. *read*) laikai skiriasi, nes serveris gali greitai priimti ryšį, bet lėtai generuoti atsakymą (arba atvirkščiai) – atskiri limitai leidžia tiksliau diagnozuoti, kur būtent strigo užklausa.

### Eksponentinis laukimas

Klaidos 429, 500, 502, 503 ir 504 kartais laikinos. Kartok tik idempotentę `GET` užklausą ir ribotą kartų skaičių. Nekartok aklai `POST`, kuris galėjo sukurti užsakymą ar išsiųsti laišką – jei serveris jau spėjo įvykdyti veiksmą prieš grąžindamas klaidą, pakartotas `POST` gali sukurti tą patį įrašą dar kartą.

```python
import time

for attempt in range(3):
    response = session.get(url, timeout=10)
    if response.status_code not in {429, 500, 502, 503, 504}:
        response.raise_for_status()
        break
    if attempt == 2:
        response.raise_for_status()
    time.sleep(2 ** attempt)
```

Eilutė po eilutės: ciklas bando iki 3 kartų (`attempt` = 0, 1, 2). Jei kodas nepriklauso pakartojamų klaidų aibei, iš karto tikriname statusą ir išeiname iš ciklo (`break`). Jei tai paskutinis bandymas (`attempt == 2`) ir klaida vis dar pakartojama, galiausiai leidžiame `raise_for_status()` iškelti klaidą – nebekartojame amžinai. Tarp bandymų laukiame `2 ** attempt` sekundžių: 1, 2, 4 – tai ir yra eksponentinis (laipsniškai didėjantis) laukimas iš B vizualizacijos.

> **Dažna klaida:** ta pati fiksuota pauzė (pvz., visada 2 s) tarp visų bandymų – jei serveris perkrautas, vienoda dažna apkrova iš daugybės klientų jo neduoda atsigauti. Didėjanti pauzė paskirsto pakartotus bandymus laike.

### Testas be interneto

Tinklo klientą testuok su netikru `Session` objektu, kurio `get()` grąžina paruoštą 200 atsakymą arba iškelia `requests.Timeout`. Testas neturi priklausyti nuo `httpbin.org` veikimo – jei tas serveris kada nors bus nepasiekiamas, tavo testų rinkinys vis tiek turi likti žalias.

```python
class FakeSuccessSession:
    def get(self, url, timeout):
        class FakeResponse:
            status_code = 200

            def raise_for_status(self):
                pass

            def json(self):
                return {"args": {}}

        return FakeResponse()


def test_get_with_fake_session_succeeds():
    fake_session = FakeSuccessSession()
    response = fake_session.get("https://example.test", timeout=10)
    assert response.status_code == 200
```

**Mini užduotis.** Parašyk antrą netikrą sesijos klasę, kurios `get()` iškelia `requests.Timeout`, ir testą, kuris patikrina, kad tavo funkcija šią klaidą paverčia `RuntimeError("API neatsakė laiku")`.

<details class="selfcheck" markdown="1"><summary>Rodyti sprendimą</summary>

```python
import pytest
import requests


class FakeTimeoutSession:
    def get(self, url, timeout):
        raise requests.Timeout("simuliuotas laiko limitas")


def test_fetch_with_fake_session_times_out():
    fake_session = FakeTimeoutSession()
    with pytest.raises(requests.Timeout):
        fake_session.get("https://example.test", timeout=10)
```

</details>

Baigta, kai klientas turi `timeout`, konkrečias išimtis, ribotą retry tik idempotentėms užklausoms ir testus be realaus tinklo.

## 16. Dažniausios klaidos

| Klaida | Kodėl ji atsiranda | Klaidingas pavyzdys | Pataisytas pavyzdys | Kaip išvengti |
|---|---|---|---|---|
| Trūksta `timeout` | Manoma, kad internetas visada atsakys greitai | `requests.get(url)` | `requests.get(url, timeout=10)` | `timeout` visada nurodyk kaip privalomą argumentą |
| Painiojami `json=` ir `data=` | Abu atrodo panašiai, bet koduoja turinį skirtingai | `requests.post(url, data=payload)` | `requests.post(url, json=payload)` | Prieš siunčiant patikrink, ko tikisi serveris |
| Kartojama ne-idempotentinė `POST` | Manoma, kad kartojimas visada saugus | `for _ in range(3): requests.post(url, json=payload)` | Kartoti tik `GET`, o `POST` siųsti vieną kartą su aiškiu klaidos pranešimu | Retry taikyk tik idempotentiems metodams |
| Paslaptis patenka į logus | Derinimui spausdinamas visas `headers` ar `payload` | `print(headers)` | `logging.info("statusas=%s", response.status_code)` | Loguok tik neutralius metaduomenis, niekada raktą |
| Nepatikrinamas `Content-Type`/JSON validumas | Iš karto kviečiamas `response.json()` | `data = response.json()` be `try` | `try: data = response.json() except ValueError: ...` | Gaudyk `ValueError`, kai atsakymas gali būti ne JSON |
| Ignoruojamas statusas | Iškart naudojamas turinys, netikrinant, ar užklausa pavyko | `data = requests.get(url).json()` | `response.raise_for_status(); data = response.json()` | Visada tikrink statusą prieš naudodamas turinį |
| `.env` patenka į Git | Pamirštas `.gitignore` įrašas | `git add .env` | `.env` įtrauktas į `.gitignore`, committinamas tik `.env.example` | Prieš pirmą commit patikrink `.gitignore` |
| Vienoda pastovi pauzė tarp pakartojimų | Nenaudojamas eksponentinis didėjimas | `time.sleep(2)` kiekvieną kartą | `time.sleep(2 ** attempt)` | Naudok didėjantį laukimą laikinoms serverio klaidoms |

## 17. Profesionali praktika

- Kiekvienai tinklo užklausai visada nurodyk `timeout` – be jo laiku neaptiktas strigimas gali sustabdyti visą programą.
- Skirk atskirus `except` blokus laiko limitui, HTTP klaidai ir bendrai tinklo klaidai – kiekvienai reikia kitokios vartotojo žinutės.
- Naudok `requests.Session()`, kai siunti kelias užklausas tam pačiam serveriui – tai greičiau ir tvarkingiau nei atskiri kvietimai.
- Retry taikyk tik idempotentiems metodams (`GET`) ir su ribotu kartų skaičiumi bei didėjančiu laukimu.
- Laikyk paslaptis `.env` faile, versijų kontrolėje palik tik `.env.example`, o loguose – tik neutralius metaduomenis (statusą, trukmę), niekada patį raktą ar visą turinį.
- Validuok API atsakymo turinį atskirai nuo statuso – sėkmingas kodas negarantuoja laukiamos struktūros.
- Modulius, kurie kalbasi su išoriniu pasauliu (pvz., `api_client.py`), kurk taip, kad likusi programos dalis matytų tik paprastą funkciją ir aiškią klaidą, o ne HTTP detales.

## 18. Kodėl tai svarbu mokantis AI?

Kitoje pamokoje prijungsi tikrą DI modelį per OpenAI Responses API – ir tai irgi tėra HTTP API po apvalkalu. Kiekvienas SDK kvietimas `client.responses.create(...)` viduje nusiunčia HTTP užklausą, gauna atsakymą su būsenos kodu ir JSON turiniu, gali užtrukti arba nepavykti dėl tinklo priežasčių. Tos pačios disciplinos, kurias išmokai šioje pamokoje – privalomas `timeout`, atskirti `except` blokai skirtingoms klaidoms, API rakto laikymas `.env` faile, atsakymo turinio validavimas prieš naudojimą – yra būtent tai, ko prireiks kalbant su realiu DI modeliu. Skirtumas bus tik vienas: `api_client.py` viduje bandomąjį `httpbin.org/post` endpoint pakeisi tikru DI kvietimu, o visa kita – `send_question(question: str) -> str` sutartis, klaidų vertimas į `RuntimeError`, atsakymo validavimas – liks lygiai tokia pati. Kas patikimai veikia su bet kuria API, veiks patikimai ir su DI API.

## 19. Pamokos santrauka

- HTTP užklausa ir atsakymas turi tas pačias dalis: URL, metodą, headers, params/JSON body, status code.
- `GET` skirtas gauti duomenis, `POST` – juos sukurti ar nusiųsti; tik `GET` saugu kartoti be minties.
- Būsenos kodai skirstomi į 2xx (sėkmė), 3xx (nukreipimas), 4xx (kliento klaida) ir 5xx (serverio klaida).
- `timeout` yra privalomas kiekvienai užklausai – be jo programa gali laukti neribotai.
- Tinklo klaidas gaudyk atskirai (`Timeout`, `HTTPError`, `RequestException`, `ValueError`) ir versk į aiškias žinutes.
- API raktą laikyk `.env` faile, versijų kontrolėje – tik `.env.example`, o loguose – jokių paslapčių.
- Sėkmingas statusas negarantuoja teisingo turinio – atsakymą validuok atskirai.
- `requests.Session()` ir eksponentinis laukimas padaro pakartotines užklausas efektyvesnes ir saugesnes.
- `api_client.py` su `send_question(question: str) -> str` paslepia visas HTTP detales nuo likusios programos dalies.

**Atmintinė:**

```python
import requests

def call_api(url: str, payload: dict) -> dict:
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.Timeout as exc:
        raise RuntimeError("API neatsakė laiku") from exc
    except requests.HTTPError as exc:
        raise RuntimeError(f"API grąžino klaidą {exc.response.status_code}") from exc
    except requests.RequestException as exc:
        raise RuntimeError("Nepavyko prisijungti prie API") from exc
```

Vienu sakiniu: **patikimas HTTP klientas visada turi timeout, atskirai valdomas klaidas, saugiai laikomas paslaptis ir validuotą atsakymą – ir tiksliai šie principai laukia tavęs sekančioje pamokoje, kai kalbėsi su tikru DI modeliu.**

## 20. Savirefleksija

1. Kurią HTTP dalį (URL, metodą, headers, params, JSON body, status code) man buvo sunkiausia atskirti nuo kitų?
2. Ar galėčiau paaiškinti kolegai, kodėl `timeout` yra privalomas, o ne tik „gera praktika“?
3. Kokią klaidą (json vs data, trūkstamas timeout, kartojama POST) dabar iškart atpažinčiau svetimame kode?
4. Ar suprantu, kodėl `main.py` neturėtų žinoti apie `requests` išimtis ar būsenos kodus?
5. Kaip patikimo HTTP kliento principai padės man kitoje pamokoje jungiantis prie tikros DI API?

## 21. Namų darbas

### Privaloma – užbaik `api_client.py`

Paruošk pilną `api_client.py` su `send_question(question: str) -> str`, `read_answer(data: dict) -> str` ir bent viena antraščių sudarymo funkcija. Pridėk `.env.example` (be tikro rakto) ir `.gitignore` su `.env`. Parašyk bent 8 testavimo scenarijus be realaus tinklo: tuščias klausimas, normalus klausimas, laiko limito klaida, HTTP klaida (bent du skirtingi kodai), bendra tinklo klaida, netinkamas JSON, trūkstamas `answer` laukas. Sudaryk sekos schemą (tekstinę arba grafinę) nuo vartotojo klausimo iki grąžinto atsakymo, pažymėdamas kiekviename žingsnyje, kas gali nepavykti.

**Vertinimas (10 taškų):** teisingas `send_question` kontraktas – 3; atskirtos klaidų kategorijos – 2; `.env`/`.gitignore` tvarkingi – 1; bent 8 testai be tinklo – 3; aiški sekos schema – 1.

### Pasirenkama – retry sluoksnis

Prie `api_client.py` pridėk pakartojimą tik 429/5xx atvejais idempotentei `GET` pagalbinei funkcijai (pvz., API būsenos patikrai), su eksponentiniu laukimu ir ne daugiau kaip 3 bandymais. Parašyk testą su netikra sesija, imituojančia dvi nesėkmes ir sėkmę trečią kartą.

**Vertinimas (5 taškai):** retry taikomas tik `GET` – 2; eksponentinis laukimas – 1; ribotas bandymų skaičius – 1; testas su fake sesija – 1.

### Kūrybinis iššūkis – kito API kliento skica

Pasirink bet kurią viešą, nemokamą, rakto nereikalaujančią API (pvz., orų, valiutų kursų ar panašią) ir parašyk trumpą kliento skicą su `timeout`, statuso patikra ir bent vieno lauko validavimu. Neprivalai integruoti į Asistentą – tikslas pademonstruoti, kad tie patys principai veikia bet kuriai API.

**Vertinimas (5 taškai):** pasirinkta reali vieša API – 1; `timeout` ir statuso patikra – 2; turinio validavimas – 1; trumpas paaiškinimas, kodėl būtent ši API – 1.

## 22. Dėstytojo ir platformos pastabos

| Dalis | Trukmė | Metodinės pastabos |
|---|---:|---|
| Hook, pagrindinės sąvokos, vizualizacijos | 40 min. | Aptarnavimo langelio analogiją grąžinti prie kiekvienos naujos sąvokos |
| `GET` užklausa ir būsenos kodai | 50 min. | Realiu laiku parodyti `httpbin.org/status/404` naršyklėje ir kode |
| `POST` ir JSON turinys | 40 min. | Vizualiai palyginti `json=` ir `data=` siunčiamą turinį |
| Tinklo klaidos ir `try/except` tinkle | 45 min. | Dirbtinai atjungti internetą ir stebėti, kurią išimtį pagauna kodas |
| `.env` ir paslapčių valdymas | 35 min. | Parodyti, kaip atrodo raktas atsitiktinai patekęs į Git istoriją |
| Atsakymo validavimas | 30 min. | Pademonstruoti `200 OK` su tyčia sugadinta JSON struktūra |
| Kodo pavyzdžių galerija ir interaktyvios veiklos | 45 min. | Kiekvieną pavyzdį paleisti gyvai, ne tik skaityti |
| Žinių patikrinimas ir praktinės užduotys (A/B/C) | 75 min. | A ir B lygius tikrinti automatiškai, C lygį – rankiniu būdu dėl retry logikos |
| Mini projektas (`api_client.py`) | 70 min. | Pabrėžti, kad `send_question` sutartis nesikeis 9 pamokoje |
| Gilioji laboratorija (sesija, retry, testai be tinklo) | 50 min. | Kontrolinis taškas: testai praeina net išjungus internetą |

Animacija labiausiai padėtų ties užklausos ir atsakymo apvaliu ratu bei eksponentinio laukimo laiko juosta – abi vizualizacijos verta rodyti dar kartą prieš C lygio užduotį ir giliąją laboratoriją. Interaktyvų Python redaktorių verta įterpti po `GET` pavyzdžio, po `POST`/JSON skyriaus, po klaidingo pavyzdžio galerijoje ir viso mini projekto sprendimo. Platformoje verta fiksuoti pirmą sėkmingą `GET` kvietimą, pirmą teisingai sugautą tinklo klaidą, `.env`/`.gitignore` sukūrimą, testo rezultatą, C lygio užduoties bandymų skaičių, mini projekto užbaigimą ir savirefleksijos pasirinkimą – šie duomenys padės atpažinti, kas iš tikrųjų kelia sunkumų prieš 9 pamokos DI integraciją.
