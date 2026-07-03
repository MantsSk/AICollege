---
title: Atminties pridėjimas
module: Atmintis
order: 3
---

# Atminties pridėjimas

Pagal nutylėjimą kiekvienas API kvietimas yra be būsenos — modelis viską pamiršta. **Atmintis** reiškia ankstesnių žinučių padavimą atgal, kad pokalbis turėtų tęstinumą.

## Trumpalaikė atmintis: žinučių istorija

Laikyk sąrašą ir pridėk kiekvieną ėjimą:

```python
history = [{"role": "system", "content": "Esi mokymosi tutorius."}]

def ask(user_text):
    history.append({"role": "user", "content": user_text})
    reply = completion(model="gpt-4o-mini", messages=history)\
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

> **Mentoriaus patarimas:** paklausk „Kada turėčiau apibendrinti istoriją, o ne tiesiog ją trumpinti?“

Toliau: atsakymus pagrįsime tavo dokumentais — **žinių baze**.
