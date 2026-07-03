# AI College 🎓

A subscription-based, **text-first** learning platform for AI, Python, and automation — with an **AI Mentor in every lesson**.

Built with a Python-first stack: **FastAPI · Jinja2 · HTMX · TailwindCSS · PostgreSQL · SQLAlchemy 2.0 · Alembic · Stripe · LiteLLM · Docker**. No React, no SPA — just fast, server-rendered HTML with HTMX for the dynamic bits.

The UI is **Lithuanian-first** (default `lt`) with English (`en`) as a switchable secondary language.

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
- **Bilingual (LT/EN)** — UI strings and course content are translatable; visitors switch language via `/language/{lang}` (persisted in a cookie). Lithuanian is the default; English course content is layered on as file overlays with no schema changes.
- **Dark mode**, responsive, fast-loading.

---

## Quick start (Docker)

```bash
cp .env.example .env          # then edit values (see Configuration)
docker compose up --build
```

Visit **http://localhost:8000**. On startup the container runs migrations (`alembic upgrade head`) and seeds courses from the `courses/` markdown files.

## Quick start (local, without Docker)

The fastest path uses SQLite — no Postgres to run. `requirements-local.txt` is the same dependency set minus the Postgres drivers, and a `Makefile` wraps the common steps:

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
make install                                         # pip install -r requirements-local.txt
cp .env.example .env                                 # set DATABASE_URL=sqlite:///./local.sqlite3
make dev                                             # migrate + seed, then uvicorn --reload
```

`make` targets: `install`, `migrate` (`alembic upgrade head`), `seed` (`python -m app.seed`), and `dev` (migrate + seed + run). To target Postgres locally instead, `pip install -r requirements.txt` and point `DATABASE_URL` at your Postgres.

> The app targets PostgreSQL in production. Local dev and the test suite run on SQLite for speed — `app/database.py` detects a `sqlite://` URL and adjusts the engine automatically; the schema is written to work on both.

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

Run `python -m app.seed` (or `make seed`, or just restart) to sync files into the database. Seeding is idempotent: it upserts by slug and removes lessons whose files were deleted.

The three seeded courses: **Python Basics**, **AI Fundamentals**, **Build Your Own AI Assistant**.

### Translations

The Lithuanian content under `courses/` is canonical — it owns slugs, IDs, ordering, and seeds the database. Other languages are **display-only overlays** read from `courses_i18n/<lang>/`, matched to courses and lessons by slug:

```
courses_i18n/
  en/
    python-basics/
      course.yml
      lesson-01.md
      ...
```

`app/course_i18n.py` swaps in the overlay's title/body at render time when a non-default language is active; anything without an overlay falls back to the Lithuanian original, so translations can be partial. UI chrome (nav, buttons, landing copy) is translated separately via the `TRANSLATIONS` dict in `app/i18n.py`.

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
  i18n.py          # UI string translations + request language resolution
  course_i18n.py   # localized course-content overlays (display-only)
  templating.py    # shared Jinja2 env + helpers (i18n context processor)
  routers/         # pages (incl. /language), auth, courses, ai, billing
  templates/       # Jinja2 templates (+ HTMX partials)
  static/          # CSS (prose + code highlighting) and a little JS
alembic/           # migrations
courses/           # markdown content (Lithuanian, canonical)
courses_i18n/      # per-language display overlays (e.g. en/)
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
