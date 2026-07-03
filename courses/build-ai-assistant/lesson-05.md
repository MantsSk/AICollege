---
title: Diegimas
module: Diegimas
order: 5
---

# Diegimas

Tavo asistentas veikia lokaliai — dabar paleisk jį taip, kad pasiektų realūs vartotojai. Naudosime **Docker**, tą pačią sąranką, kuri paleidžia šią platformą.

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

## Pavyko

Dabar gali sukurti realų DI asistentą, suteikti jam atmintį bei žinias ir paleisti viešai — tai tas pats technologijų rinkinys, ant kurio veikia AI College. Kurk ir paleisk.

> **Mentoriaus patarimas:** paklausk „Duok žingsnis po žingsnio planą, kaip tai paleisti Railway.“
