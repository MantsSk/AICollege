"""Shared Jinja2 environment with global helpers."""
from __future__ import annotations

from pathlib import Path

from fastapi.templating import Jinja2Templates

from app.config import settings
from app.i18n import i18n_context
from app.services import render_markdown

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR), context_processors=[i18n_context])
templates.env.globals["app_name"] = settings.app_name
templates.env.globals["subscription_price"] = settings.subscription_price_eur
templates.env.globals["free_lessons_per_course"] = settings.free_lessons_per_course
templates.env.globals["free_daily_ai_messages"] = settings.free_daily_ai_messages
templates.env.filters["markdown"] = render_markdown


def is_htmx(request) -> bool:
    return request.headers.get("HX-Request") == "true"
