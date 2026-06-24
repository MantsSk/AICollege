---
title: Promptų inžinerija
module: Promptų inžinerija
order: 2
---

# Promptų inžinerija

**Promptų inžinerija** yra gebėjimas rašyti instrukcijas, kurios iš LLM išgauna patikimus, kokybiškus atsakymus. Tai viena svarbiausių praktinio DI kompetencijų.

## Gero prompto anatomija

1. **Vaidmuo** — kuo modelis turėtų apsimesti ar kokią rolę atlikti.
2. **Užduotis** — ką konkrečiai padaryti.
3. **Kontekstas** — medžiaga, iš kurios dirbama.
4. **Formatas** — kaip turi atrodyti atsakymas.
5. **Apribojimai** — ko vengti.

```text
Esi patyręs Python mokytojas.        (vaidmuo)
Paaiškink list comprehensions         (užduotis)
visiškam pradedančiajam, kuris moka   (kontekstas)
tik for ciklus.
Naudok vieną trumpą pavyzdį, tada      (formatas)
2 eilučių santrauką. Venk žargono.     (apribojimai)
```

## Technikos, kurios patikimai padeda

- **Būk konkretus.** „Apibendrink 3 punktais“ veikia geriau nei „apibendrink“.
- **Parodyk pavyzdį** (one-shot / few-shot), kai svarbus formatas.
- **Paprašyk mąstyti žingsnis po žingsnio**, kai reikia samprotavimo.
- **Leisk pripažinti nežinojimą:** „Jei nesi tikras, taip ir pasakyk“ mažina haliucinacijas.

## Sistemos ir vartotojo žinutės

Dauguma API atskiria **sistemos** žinutę (pastovios instrukcijos / persona) nuo **vartotojo** žinučių (tikrasis prašymas). Mūsų DI mentorius naudoja sistemos promptą, kuris sako: *„pirmenybę teik kurso turiniui, aiškink paprastai, lik susitelkęs į mokymąsi.“*

## Iteruok

Į promptingą žiūrėk kaip į klaidų taisymą. Jei atsakymas blogas, dažniausiai reikia aiškesnio prompto, o ne kito modelio.

> **Mentoriaus patarimas:** įklijuok miglotą promptą ir paprašyk mentoriaus perrašyti jį pagal vaidmens/užduoties/konteksto/formato struktūrą.

Toliau: kaip mašinos supranta *prasmę* — **įterpiniai**.
