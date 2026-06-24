---
title: Deployment
module: Deployment
order: 5
---

# Deployment

Your assistant works locally — now ship it so real users can reach it. We'll use **Docker**, the same setup that runs this platform.

## Containerize it

A `Dockerfile` packages your app with everything it needs:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Run app + database together

`docker-compose.yml` defines the services:

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

## Secrets and keys

**Never** commit API keys. Use environment variables / a `.env` file that is git-ignored, and set real values in your host's dashboard.

## Where to deploy

| Platform | Best for |
|----------|----------|
| **Railway / Render** | fastest, push-to-deploy |
| **Fly.io** | global edge, generous free tier |
| **Hetzner VPS** | cheapest at scale, full control |

All of them run Docker, so the same image works everywhere.

## Production checklist

- ✅ Run database **migrations** on deploy (`alembic upgrade head`).
- ✅ HTTPS (the platform/proxy usually handles this).
- ✅ Set `temperature` and `max_tokens` to control cost.
- ✅ Add **usage limits** so a single user can't drain your budget.
- ✅ Monitor errors and token spend.

## You did it

You can now build, give memory and knowledge to, and deploy a real AI assistant — the exact stack behind AI College. Go build something and ship it.

> **Mentor tip:** Ask "Give me a step-by-step plan to deploy this on Railway."
