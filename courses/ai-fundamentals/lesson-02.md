---
title: Kaip veikia kalbos modeliai?
module: Kalbos modeliai
order: 2
---

# Kaip veikia kalbos modeliai?

Didysis kalbos modelis (LLM) yra DI sistema, išmokyta prognozuoti tekstą. Paprastai tariant, ji gauna žodžių ir jų dalių seką, tada spėja, kas turėtų eiti toliau. Kartojant šį procesą gaunamas atsakymas.

Tai nereiškia, kad modelis „mąsto“ kaip žmogus. Tačiau dideliame mastelyje toks prognozavimas sukuria gebėjimus, kurie atrodo labai protingi: aiškinimą, santraukas, vertimą, kodavimą, argumentų kūrimą.

**Po šios pamokos galėsi:**

- paprastai paaiškinti, kas yra tokenai ir konteksto langas;
- suprasti, kodėl tas pats klausimas gali gauti skirtingus atsakymus;
- atpažinti situacijas, kuriose haliucinacijos tikimybė didžiausia.

## Tokenai

Modelis neskaito teksto tiksliai taip, kaip žmogus. Tekstas suskaidomas į **tokenus** — žodžius, žodžių dalis arba simbolius.

```text
„Dirbtinis intelektas keičia mokymąsi“
gali tapti:
[„Dir“, „btinis“, „ intelektas“, „ keičia“, „ mokymąsi“]
```

Tokenai svarbūs todėl, kad nuo jų priklauso:

- kiek teksto modelis gali matyti vienu metu;
- kiek kainuoja API naudojimas;
- kada ilgas pokalbis pradeda prarasti ankstesnį kontekstą.

## Konteksto langas

**Konteksto langas** yra modelio trumpalaikė atmintis. Tai tekstas, kurį modelis mato atsakymo metu: tavo klausimas, ankstesnis pokalbis, dokumentai, instrukcijos.

Jei informacijos nėra kontekste, modelis gali:

- remtis bendromis žiniomis;
- spėti;
- pasakyti, kad nežino, jei taip paprašysi;
- sukurti įtikinamai skambantį, bet neteisingą atsakymą.

Todėl geras kontekstas dažnai svarbesnis už „tobulą“ promptą.

## Temperatūra

**Temperatūra** valdo atsitiktinumą:

- žema temperatūra tinka faktams, formatui, taisymui;
- aukštesnė temperatūra tinka idėjoms, kūrybai, alternatyvoms.

Kasdieniam vartotojui nebūtina reguliuoti temperatūros, bet verta suprasti principą: tas pats klausimas gali turėti skirtingus atsakymus, nes modelis nėra paprastas skaičiuotuvas.

## Kodėl modeliai klysta?

Kalbos modelis kuria tikėtiną tekstą, o ne tiesiogiai tikrina realybę. Jei jis nemato patikimo šaltinio, gali užpildyti spragas. Tai vadinama **haliucinacija**.

Haliucinacijos dažnesnės, kai:

- prašai labai naujų faktų;
- klausimas siauras arba nišinis;
- prašai citatų, teisinių ar medicininių atsakymų be šaltinių;
- spaudi modelį atsakyti, nors jis neturi pakankamai informacijos.

## Geras naudojimo principas

Duok modeliui tai, ko norėtum duoti žmogui bendradarbiui:

- tikslą;
- foną;
- pavyzdžius;
- pageidaujamą formatą;
- kriterijus, pagal kuriuos vertinsi rezultatą.

## Pasitikrink save

**1. Kas yra konteksto langas?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Modelio trumpalaikė atmintis — visas tekstas, kurį jis mato atsakydamas: klausimas, ankstesnis pokalbis, dokumentai, instrukcijos. Ko nėra kontekste, tuo modelis remtis negali.

</details>

**2. Kodėl ilgo pokalbio pabaigoje DI „pamiršta“, kas buvo pradžioje?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Konteksto langas ribotas: kai pokalbis viršija jo dydį (skaičiuojamą tokenais), seniausia dalis nebetelpa ir modelis jos nebemato.

</details>

**3. Kada haliucinacijos tikimybė didžiausia?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kai prašai labai naujų ar nišinių faktų, citatų ir šaltinių arba spaudi modelį atsakyti, nors jis neturi pakankamai informacijos. Modelis kuria tikėtiną tekstą, o ne tikrina realybę.

</details>

## Mini užduotis

Paimk ilgą tekstą, kurį turi perskaityti, ir paprašyk DI:

```text
Apibendrink šį tekstą 5 punktais.
Tada išskirk 3 dalykus, kuriuos turėčiau patikrinti pats.
Jei tekste nėra pakankamai informacijos, aiškiai tai pasakyk.
```

> **Užduoties patikra:** gautą santrauką įklijuok mentoriui ir paklausk: „Kurie šios santraukos teiginiai yra perfrazavimas, o kurie — modelio interpretacija, kurią turėčiau patikrinti pats?“

> **Mentoriaus patarimas:** paklausk „Paaiškink tokenus, konteksto langą ir haliucinacijas kaip žmogui, kuris niekada nenaudojo DI.“

Toliau: mokysimės rašyti promptus, kurie duoda geresnius atsakymus.
