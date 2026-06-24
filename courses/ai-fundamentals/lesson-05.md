---
title: DI agentai
module: DI agentai
order: 5
---

# DI agentai

**Agentas** yra LLM, kuris gali *spręsti* ir *veikti*, ne tik atsakyti. Duodi jam tikslą ir **įrankių** rinkinį, o jis kartoja ciklą: galvoja → pasirenka įrankį → stebi rezultatą → kartoja, kol tikslas pasiektas.

## Pokalbių robotas ir agentas

| | Pokalbių robotas | Agentas |
|--|---------|-------|
| Išvestis | tekstinis atsakymas | tekstas **ir veiksmai** |
| Įrankiai | nėra | paieška, kodas, API, DB |
| Žingsniai | vienas ėjimas | daug, savarankiškai |

## Įrankiai (funkcijų kvietimas)

Modeliui aprašai funkcijas; jis pasirenka, kurią kviesti ir su kokiais argumentais.

```python
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"],
        },
    },
}]
```

Modelis atsako „kviesk `get_weather(city='Vilnius')`“, tavo kodas tai paleidžia, o rezultatą paduodi atgal modeliui.

## Agento ciklas

```text
tikslas -> LLM galvoja -> kviečia įrankį -> gauna rezultatą
        -> LLM vėl galvoja -> ... -> galutinis atsakymas
```

## Kur agentai stiprūs ir kur reikia atsargumo

✅ Kelių žingsnių tyrimai, programavimo užduotys, darbo eigų automatizavimas.
⚠️ Pridėk **apsaugas**: žingsnių limitus, leidžiamus įrankius, žmogaus patvirtinimą rizikingiems veiksmams. Neriboti agentai gali užsiciklinti arba imtis netinkamų veiksmų.

## Ką išmokai

Dabar supranti visą šiuolaikinio DI rinkinį: modelius, promptingą, įterpinius, RAG ir agentus. Kitame kurse, **Sukurk savo DI asistentą**, visa tai sujungsi į realų produktą.

> **Mentoriaus patarimas:** paklausk „Koks paprasčiausias agentas, kurį galėčiau sukurti kaip pirmą projektą?“
