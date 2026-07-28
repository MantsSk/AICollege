# Python DI asistentas

Tai kurso baigiamasis projektas. Jis veikia vietiniu režimu be API rakto: klausimai apie kursą atsakomi iš `knowledge.json`. Įvedus `OPENAI_API_KEY`, nežinomi klausimai perduodami OpenAI Responses API, o kainos klausimui modelis gali paprašyti saugaus Python įrankio.

## Paleidimas

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
python assistant.py
```

`.env` faile įrašyk savo rakto reikšmę tik lokaliai. Jo nekelk į Git ir nespausdink ekrane. Jei raktas neįrašytas, vis tiek gali demonstruoti vietinę žinių bazę.

## Testai

```bash
python -m pytest -q
```

## Demonstracija

Išbandyk: `Kiek trunka kursas?`, `Kokios temos?`, `Kiek kainuoja 3 vietos po 20?`, `/history`, `/reset`, tuščią eilutę ir `/quit`. Studentas turi pridėti bent vieną temą, vieną testą ir vieną savo saugos taisyklę.
