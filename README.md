# AI College 🎓

A subscription-based, **text-first** learning platform for AI, Python, and automation — with an **AI Mentor in every lesson**.

Built with a Python-first stack: **FastAPI · Jinja2 · HTMX · TailwindCSS · PostgreSQL · SQLAlchemy 2.0 · Alembic · Stripe · LiteLLM · Docker**. No React, no SPA — just fast, server-rendered HTML with HTMX for the dynamic bits.

---

## Features

- **Landing page** — hero, course preview, benefits, pricing, FAQ, CTA.
- **Auth** — email register/login/password reset with server-side sessions.
- **Dashboard** — continue learning, per-course progress, manage subscription.
- **Course catalog & lessons** — clean markdown rendering with syntax-highlighted code, prev/next navigation, progress indicator.
- **AI Mentor** — a chat panel inside every lesson, grounded in the lesson content via LiteLLM (works with Gemini, GPT, or Claude by config).
- **Free tier** — anonymous users read the first lesson of each course; registered free users get the first 2 lessons + the AI Mentor (5 messages/day). Upgrade prompts appear at limits.
- **Paid tier (€20/mo)** — all lessons, all courses, higher AI limits, via Stripe Checkout + billing portal.
- **HTMX everywhere** — mentor chat, mark-complete, and progress updates with no page reloads and minimal JS.
- **Dark mode**, responsive, fast-loading.

---

## Quick start (Docker)

```bash
cp .env.example .env          # then edit values (see Configuration)
docker compose up --build
```

Visit **http://localhost:8000**. On startup the container runs migrations (`alembic upgrade head`) and seeds courses from the `courses/` markdown files.

## Quick start (local, without Docker)

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                 # point DATABASE_URL at your Postgres

alembic upgrade head
python -m app.seed
uvicorn app.main:app --reload
```

> The app targets PostgreSQL in production. The test suite runs on SQLite for speed; the schema is written to work on both.

---

## Configuration

All settings come from environment variables (see `.env.example`):

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Session signing key — set a long random value. |
| `DATABASE_URL` | e.g. `postgresql+psycopg2://user:pass@host:5432/db` |
| `AI_MODEL` | LiteLLM model, e.g. `gemini/gemini-1.5-flash`, `gpt-4o-mini`, `claude-haiku-4-5-20251001` |
| `GEMINI_API_KEY` / `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` | Whichever your `AI_MODEL` needs. |
| `FREE_DAILY_AI_MESSAGES` / `PAID_DAILY_AI_MESSAGES` | AI Mentor daily limits. |
| `FREE_LESSONS_PER_COURSE` | Lessons unlocked for registered free users. |
| `STRIPE_SECRET_KEY` / `STRIPE_PRICE_ID` / `STRIPE_WEBHOOK_SECRET` | Subscription billing. |
| `BASE_URL` | Public URL, used for Stripe redirects and reset links. |

**Switching AI providers** requires no code changes — just set `AI_MODEL` and the matching API key.

---

## Managing course content

Courses are plain markdown files — **no admin panel**. The layout:

```
courses/
  python-basics/
    course.yml          # title, description, order
    lesson-01.md
    lesson-02.md
  ai-fundamentals/
    ...
```

Each lesson has simple frontmatter:

```markdown
---
title: Variables and Types
module: Variables
order: 1
---

# Markdown body with code, tables, etc.
```

- **Add a lesson:** drop a `lesson-NN.md` file in the course folder.
- **Add a course:** create a new folder with a `course.yml` and lesson files.

Run `python -m app.seed` (or just restart) to sync files into the database. Seeding is idempotent: it upserts by slug and removes lessons whose files were deleted.

The three seeded courses: **Python Basics**, **AI Fundamentals**, **Build Your Own AI Assistant**.

---

## Stripe setup

1. Create a recurring **€20/month** Price in Stripe; put its ID in `STRIPE_PRICE_ID`.
2. Set `STRIPE_SECRET_KEY`.
3. Add a webhook endpoint pointing to `https://your-domain/billing/webhook` for events:
   `checkout.session.completed`, `customer.subscription.created/updated/deleted`. Put the signing secret in `STRIPE_WEBHOOK_SECRET`.
4. Locally, forward webhooks with the Stripe CLI:
   ```bash
   stripe listen --forward-to localhost:8000/billing/webhook
   ```

Checkout, the billing portal (upgrade / cancel / manage), and status sync are wired in `app/billing.py`.

---

## Architecture

```
app/
  main.py          # FastAPI app, session middleware, router registration
  config.py        # pydantic-settings
  database.py      # SQLAlchemy engine/session, Base
  models.py        # users, subscriptions, courses, lessons, lesson_progress,
                   # chat_conversations, chat_messages, daily_usage
  security.py      # password hashing, current-user resolution
  deps.py          # FastAPI dependencies (current_user / require_user)
  content.py       # load markdown course content from disk
  seed.py          # sync content -> database (idempotent)
  services.py      # markdown rendering, access control, progress, usage limits
  ai.py            # AI Mentor via LiteLLM (grounded in lesson content)
  billing.py       # Stripe checkout, portal, webhook handling
  templating.py    # shared Jinja2 env + helpers
  routers/         # pages, auth, courses, ai, billing
  templates/       # Jinja2 templates (+ HTMX partials)
  static/          # CSS (prose + code highlighting) and a little JS
alembic/           # migrations
courses/           # markdown content
tests/             # pytest suite
```

### Free-tier gating
`app/services.py:can_access_lesson` enforces: anonymous → lesson 1 only; free → first `FREE_LESSONS_PER_COURSE`; subscribed → all.

### AI Mentor
`app/ai.py` builds a system prompt containing the course/module/lesson titles and the **current lesson content**, instructing the model to prefer that content — a focused, single-document RAG. Conversation history is persisted per user per lesson; daily message counts are tracked in `daily_usage`.

---

## Tests

```bash
pytest
```

Covers public pages, lesson gating (anonymous & free), auth, password reset, mark-complete, billing guard, and the AI Mentor limit (with the LLM mocked).

---

## Deployment

The image is a standard Dockerfile and runs anywhere that supports Docker:

- **Railway / Render** — connect the repo, add a PostgreSQL plugin, set env vars.
- **Fly.io** — `fly launch` + a Postgres app.
- **Hetzner VPS** — `docker compose up -d` behind a reverse proxy (Caddy/Nginx) for HTTPS.

On boot, `scripts/start.sh` runs migrations, seeds content, then starts Uvicorn.

---

## License

Proprietary — © AI College.
