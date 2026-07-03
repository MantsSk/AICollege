---
title: Atminties pridėjimas
module: Atmintis
order: 3
---

# Atminties pridėjimas

Pagal nutylėjimą kiekvienas API kvietimas yra be būsenos — modelis viską pamiršta. **Atmintis** reiškia ankstesnių žinučių padavimą atgal, kad pokalbis turėtų tęstinumą.

**Po šios pamokos galėsi:**

- kaupti pokalbio istoriją ir siųsti ją su kiekvienu kvietimu;
- suprojektuoti žinučių saugojimą duomenų bazėje;
- suvaldyti augančią istoriją trumpinimu arba apibendrinimu.

## Trumpalaikė atmintis: žinučių istorija

Laikyk sąrašą ir pridėk kiekvieną ėjimą:

```python
history = [{"role": "system", "content": "Esi mokymosi tutorius."}]

def ask(user_text):
    history.append({"role": "user", "content": user_text})
    reply = completion(model="claude-haiku-4-5-20251001", messages=history)\
        .choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply
```

Dabar „o paaiškink paprasčiau“ veikia, nes modelis mato, kas buvo prieš tai.

## Atminties saugojimas duomenų bazėje

Atmintyje laikomi sąrašai dingsta po perkrovimo. Saugok žinutes lentelėse — būtent taip daro ši platforma:

```text
chat_conversations  (id, user_id, lesson_id)
chat_messages       (id, conversation_id, role, content, created_at)
```

Kiekviename prašyme: įkelk pokalbio žinutes, nusiųsk jas LLM, tada išsaugok naujas vartotojo ir asistento žinutes.

## Stebėk konteksto langą

Ilgos istorijos kainuoja tokenus ir gali perpildyti konteksto langą. Strategijos:

- **Trumpinti** — laikyti tik paskutines N žinučių.
- **Apibendrinti** — senus ėjimus pakeisti trumpa santrauka.

```python
recent = history[-10:]   # laikyti paskutinius 10 ėjimų
```

## Pasitikrink save

**1. Kodėl „paaiškink paprasčiau“ neveikia be istorijos?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kiekvienas API kvietimas yra be būsenos: modelis mato tik tai, kas atsiųsta tame kvietime. Jei ankstesnių žinučių nėra sąraše, jis nežino, ką reikia paaiškinti paprasčiau.

</details>

**2. Kodėl žinutes verta saugoti duomenų bazėje, o ne Python sąraše?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Sąrašas gyvena procese ir dingsta perkrovus serverį. Duomenų bazėje pokalbiai išlieka, juos galima susieti su vartotoju ir pamoka.

</details>

**3. Kuo skiriasi istorijos trumpinimas nuo apibendrinimo?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Trumpinimas išmeta senas žinutes (paprasta, bet prarandami faktai). Apibendrinimas jas pakeičia santrauka — brangesnis (papildomas LLM kvietimas), bet išlaiko esmę.

</details>

## Mini užduotis

Papildyk savo terminalo chatą taip, kad jis siųstų tik paskutines 6 žinutes, bet sistemos žinutę — visada. Patikrink, kad ilgo pokalbio pradžia „pamirštama“, o asistento persona išlieka.

> **Užduoties patikra:** įklijuok savo kodą mentoriui ir paklausk: „Ar teisingai atskyriau sistemos žinutę nuo trumpinamos istorijos? Kaip pridėčiau santraukos strategiją?“

> **Mentoriaus patarimas:** paklausk „Kada turėčiau apibendrinti istoriją, o ne tiesiog ją trumpinti?“

Toliau: atsakymus pagrįsime tavo dokumentais — **žinių baze**.
