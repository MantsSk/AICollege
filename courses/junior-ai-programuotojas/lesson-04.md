---
title: Dokumentų klausimų įrankis
module: RAG projektas
order: 4
---

# Dokumentų klausimų įrankis

RAG reiškia, kad prieš atsakydamas modelis gauna aktualų tekstą iš dokumento. Junior projektui užtenka paprastos versijos: vartotojas įkelia tekstą, o programa atsako tik pagal jį.

**Po šios pamokos galėsi:**

- pagrįsti modelio atsakymą konkrečiu dokumentu;
- suformuluoti promptą, kuris draudžia atsakinėti be konteksto;
- paaiškinti, kuo šis įrankis skiriasi nuo pilno RAG.

## Projekto idėja

Sukurk įrankį:

```bash
python doc_qa.py notes.txt "Kokie yra svarbiausi punktai?"
```

Programa:

1. perskaito failą;
2. įdeda tekstą į promptą;
3. paprašo atsakyti tik pagal dokumentą.

## Paprastas promptas

```python
prompt = f"""
Atsakyk tik pagal pateiktą dokumentą.
Jei atsakymo nėra, parašyk: "Dokumente neradau atsakymo."

Dokumentas:
{document_text}

Klausimas:
{question}
"""
```

## Kodėl tai dar ne pilnas RAG?

Pilnas RAG skaidytų dokumentą į dalis, kurtų įterpinius ir ieškotų aktualiausių vietų. Bet šis mini projektas jau moko svarbiausio principo: modelis turi būti pagrįstas konkrečiu kontekstu.

## Pasitikrink save

**1. Kodėl prompte nurodoma tiksli frazė „Dokumente neradau atsakymo“?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Aiški instrukcija, ką sakyti neradus atsakymo, sumažina haliucinacijų riziką — modelis turi leidžiamą „išėjimą“ vietoj spėliojimo.

</details>

**2. Ko trūksta iki pilno RAG?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Dokumento skaidymo į dalis, įterpinių ir paieškos pagal prasmę. Čia visas dokumentas dedamas į promptą — veikia tik su mažais failais.

</details>

**3. Kada šis paprastas variantas nustos veikti?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kai dokumentas viršys konteksto langą arba taps per brangus siųsti su kiekvienu klausimu. Tada reikės skaidymo ir paieškos.

</details>

## Mini projektas

Sukurk `doc_qa.py`, kuris:

- priima failo kelią ir klausimą;
- atsako lietuviškai;
- neleidžia atsakyti, jei failas tuščias;
- pabaigoje parašo „Patikrinkite originalų dokumentą prieš priimdami sprendimą.“

> **Užduoties patikra:** išbandyk savo įrankį su klausimu, kurio atsakymo dokumente nėra, ir papasakok mentoriui rezultatą: „Štai kaip atsakė mano įrankis. Ar promptas pakankamai griežtas?“

> **Mentoriaus patarimas:** paklausk „Kaip šį paprastą dokumentų klausimų įrankį paversti tikru RAG projektu?“

Toliau: prijungsime įrankius ir sukursime mažą agentą.
