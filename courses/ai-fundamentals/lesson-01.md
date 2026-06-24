---
title: Kas yra didieji kalbos modeliai?
module: LLMs
order: 1
---

# Kas yra didieji kalbos modeliai?

**Didysis kalbos modelis (LLM)** yra programa, išmokyta prognozuoti kitą teksto dalį. Skamba paprastai, bet dideliu mastu tai duoda įspūdingų gebėjimų: rašyti, samprotauti, apibendrinti, versti ir programuoti.

## Kaip jie veikia intuityviai

1. Tekstas suskaidomas į **tokenus** (apytiksliai žodžių dalis).
2. Modelis perskaitė milžiniškus teksto kiekius ir išmoko statistinius dėsningumus.
3. Gavęs kelis tokenus, jis prognozuoja labiausiai tikėtiną kitą tokeną — po vieną.
4. Kartojant šį procesą gaunamos sklandžios pastraipos.

```text
Input:  "Lietuvos sostinė yra"
Output: " Vilnius."   ← labiausiai tikėtinas tęsinys
```

## Pagrindiniai terminai

- **Tokenas** — teksto gabaliukas. Anglų kalboje vidutiniškai apie 4 simboliai. Kaina skaičiuojama pagal tokenus.
- **Konteksto langas** — kiek teksto modelis gali „matyti“ vienu metu (pvz., 128k tokenų).
- **Temperatūra** — atsitiktinumas. `0` = kryptingas/deterministinis, `1`+ = kūrybiškesnis.
- **Parametrai** — išmokti svoriai. Daugiau ne visada reiškia geriau.

## Ką jie daro gerai ir kur klysta

✅ Juodraščiai, paaiškinimai, transformacijos, programavimas, idėjų generavimas.
⚠️ Tai ne duomenų bazė — jie gali **haliucinuoti** užtikrintai skambančius, bet klaidingus faktus.
⚠️ Nėra gyvų žinių, nebent jas pateiki (vėliau tai spręsime su **RAG**).

## Kodėl tai svarbu

Kiekvienas įrankis, kurį kursi šioje platformoje, įskaitant DI mentorių, yra LLM su geromis instrukcijomis ir tinkamu kontekstu. Supratęs modelį, magiją pakeisi kontrole.

> **Mentoriaus patarimas:** paklausk „Paaiškink tokenus ir konteksto langus paprasta analogija.“

Toliau: kaip iš tikrųjų *kalbėtis* su šiais modeliais — **promptų inžinerija**.
