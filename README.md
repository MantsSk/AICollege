# AI College 🎓

A subscription-based, **text-first** learning platform for AI, Python, and automation — with an **AI Mentor in every lesson**.

Built with a Python-first stack: **FastAPI · Jinja2 · HTMX · TailwindCSS · PostgreSQL · SQLAlchemy 2.0 · Alembic · Stripe · LiteLLM · Docker**. No React, no SPA — just fast, server-rendered HTML with HTMX for the dynamic bits.

The UI is **Lithuanian-first** (default `lt`) with English (`en`) as a switchable secondary language.

---

## Features

- **Landing page** — focused Python course introduction, first-lesson preview, and FAQ.
- **Auth** — email register/login/password reset with server-side sessions.
- **Dashboard** — continue learning, per-course progress, manage subscription.
- **Course catalog & lessons** — clean markdown rendering with syntax-highlighted code, prev/next navigation, progress indicator.
- **Interactive learning workspace** — course outline, lesson/lab/check tabs, saved hands-on activities, completion gates, and a contextual mentor in one view.
- **Challenges & achievements** — randomized practice rounds, instant feedback, passed-check counts, and transparent skill points earned from completed lessons.
- **AI Mentor** — a chat panel inside every lesson, grounded in the lesson content via LiteLLM (works with Gemini, GPT, or Claude by config).
- **Free/testing tier** — anonymous users read the first lesson of each course; while payments are disabled, registered users can access all lessons and the AI Mentor (5 messages/day). With payments enabled, registered free users get the first 2 lessons and upgrade prompts appear at limits.
- **Paid tier (€9.99/mo)** — all lessons, all courses, higher AI limits, via Stripe Checkout + billing portal.
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
| `DEBUG` | Use `false` in production. Debug mode shows development details and relaxes secure cookies. |
| `BASE_URL` | Public `https://...` URL, used for Stripe redirects and reset links. |
| `ALLOWED_HOSTS` | Comma-separated public hostnames allowed to serve the app. |
| `SECURE_SSL_REDIRECT` | Redirect HTTP to HTTPS when your proxy/platform does not already do it. |
| `DATABASE_URL` | e.g. `postgresql+psycopg2://user:pass@host:5432/db` |
| `AI_MODEL` | LiteLLM model, e.g. `gemini/gemini-1.5-flash`, `gpt-4o-mini`, `claude-haiku-4-5-20251001` |
| `GEMINI_API_KEY` / `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` | Whichever your `AI_MODEL` needs. |
| `FREE_DAILY_AI_MESSAGES` / `PAID_DAILY_AI_MESSAGES` | AI Mentor daily limits. |
| `FREE_LESSONS_PER_COURSE` | Lessons unlocked for registered free users. |
| `PAYMENTS_ENABLED` | Keep `false` for free testing access. Set `true` only after Stripe is configured. |
| `STRIPE_SECRET_KEY` / `STRIPE_PRICE_ID` / `STRIPE_WEBHOOK_SECRET` | Subscription billing. |

**Switching AI providers** requires no code changes — just set `AI_MODEL` and the matching API key.

For production hosting, set `DEBUG=false`, use a strong `SECRET_KEY`, set `BASE_URL` to your public HTTPS domain, set `ALLOWED_HOSTS`, and keep Postgres private. The app refuses to start in production mode with the development secret or an HTTP `BASE_URL`.

---

## Managing course content

Courses are plain markdown files — **no admin panel**. The layout:

```
courses/
  python-basics/        # Python course for complete beginners
    course.yml           # title, description, order
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

The published courses are **Python nuo nulio** and **DI darbe: patikimas asistentas**. Each starts with one newly written introductory lesson; further lessons can be added incrementally. Published courses and their grouping are controlled by `app/course_paths.py`.

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

1. Create a recurring **€9.99/month** Price in Stripe; put its ID in `STRIPE_PRICE_ID`.
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
