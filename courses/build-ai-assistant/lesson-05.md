---
title: Diegimas
module: Diegimas
order: 5
---

# Diegimas

Tavo asistentas veikia lokaliai — dabar paleisk jį taip, kad pasiektų realūs vartotojai. Naudosime **Docker**, tą pačią sąranką, kuri paleidžia šią platformą.

**Po šios pamokos galėsi:**

- supakuoti programą į Docker konteinerį;
- paleisti programą ir duomenų bazę kartu su docker compose;
- pereiti produkcijos kontrolinį sąrašą prieš paleidimą.

## Sudėk į konteinerį

`Dockerfile` supakuoja programą su viskuo, ko jai reikia:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Paleisk programą ir duomenų bazę kartu

`docker-compose.yml` aprašo servisus:

```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    depends_on: [db]
  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: secret
```

```bash
docker compose up --build
```

## Paslaptys ir raktai

**Niekada** necommitink API raktų. Naudok aplinkos kintamuosius arba `.env` failą, kuris ignoruojamas git, o realias reikšmes nustatyk hostingo valdymo skydelyje.

## Kur diegti

| Platforma | Geriausia |
|----------|----------|
| **Railway / Render** | greičiausias push-to-deploy |
| **Fly.io** | globalus edge, dosnus nemokamas planas |
| **Hetzner VPS** | pigiausia masteliui, pilna kontrolė |

Visi jie paleidžia Docker, todėl tas pats image veikia visur.

## Produkcijos kontrolinis sąrašas

- ✅ Diegiant paleisk duomenų bazės **migracijas** (`alembic upgrade head`).
- ✅ HTTPS (platforma arba proxy dažniausiai tuo pasirūpina).
- ✅ Nustatyk `temperature` ir `max_tokens`, kad valdytum kainą.
- ✅ Pridėk **naudojimo limitus**, kad vienas vartotojas neišeikvotų biudžeto.
- ✅ Stebėk klaidas ir tokenų išlaidas.

## Pasitikrink save

**1. Ką duoda Dockerfile, ko neduoda paprastas `pip install`?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Atkuriamą aplinką: konteineryje užfiksuota Python versija, bibliotekos ir paleidimo komanda, todėl tas pats image identiškai veikia tavo kompiuteryje ir bet kuriame hostinge.

</details>

**2. Kur laikyti API raktus produkcijoje?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Aplinkos kintamuosiuose, nustatytuose hostingo valdymo skydelyje. `.env` failas tinka lokaliai, bet jis privalo būti `.gitignore` sąraše.

</details>

**3. Kodėl naudojimo limitai yra produkcijos būtinybė, o ne patogumas?**

<details class="selfcheck" markdown="1">
<summary>Rodyti atsakymą</summary>

Kiekvienas LLM kvietimas kainuoja. Be limitų vienas vartotojas (ar botas) gali per naktį išeikvoti visą biudžetą.

</details>

## Baigiamoji užduotis

Supakuok savo asistentą į Docker, paleisk lokaliai su `docker compose up` ir pereik visą produkcijos kontrolinį sąrašą, pažymėdamas, ką jau turi ir ko dar trūksta.

> **Užduoties patikra:** nusiųsk mentoriui savo kontrolinio sąrašo būseną ir paklausk: „Kurį trūkstamą punktą daryti pirmiausia ir kodėl?“

## Pavyko

Dabar gali sukurti realų DI asistentą, suteikti jam atmintį bei žinias ir paleisti viešai — tai tas pats technologijų rinkinys, ant kurio veikia AI College. Kurk ir paleisk.

> **Mentoriaus patarimas:** paklausk „Duok žingsnis po žingsnio planą, kaip tai paleisti Railway.“
