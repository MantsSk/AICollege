"""Load optional interactive lesson activities from JSON files."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from app.content import COURSES_DIR
from app.course_i18n import COURSE_I18N_DIR

ACTIVITY_TYPES = {
    "prompt_builder",
    "classify",
    "diagnose",
    "decision",
    "artifact_builder",
}


class ActivityError(ValueError):
    """Raised when an activity file is malformed."""


def _validate(payload: dict, source: Path) -> dict:
    activities = payload.get("activities")
    if not isinstance(activities, list) or not activities:
        raise ActivityError(f"{source}: 'activities' must be a non-empty list")

    seen: set[str] = set()
    for index, activity in enumerate(activities, start=1):
        where = f"{source}: activity {index}"
        activity_id = activity.get("id")
        if not isinstance(activity_id, str) or not activity_id:
            raise ActivityError(f"{where}: missing id")
        if activity_id in seen:
            raise ActivityError(f"{where}: duplicate id {activity_id!r}")
        seen.add(activity_id)
        if activity.get("type") not in ACTIVITY_TYPES:
            raise ActivityError(f"{where}: unsupported type {activity.get('type')!r}")
        if not activity.get("title") or not activity.get("instructions"):
            raise ActivityError(f"{where}: title and instructions are required")
        activity_type = activity.get("type")
        if activity_type == "decision":
            choices = activity.get("choices")
            if not isinstance(choices, list) or len(choices) < 2:
                raise ActivityError(f"{where}: decision requires at least two choices")
            if sum(bool(choice.get("correct")) for choice in choices) != 1:
                raise ActivityError(f"{where}: decision requires exactly one correct choice")
        if activity_type == "artifact_builder":
            fields = activity.get("fields")
            if not isinstance(fields, list) or not fields:
                raise ActivityError(f"{where}: artifact_builder requires fields")
            if any(not field.get("id") or not field.get("label") for field in fields):
                raise ActivityError(f"{where}: every artifact field requires id and label")

    payload.setdefault("version", 1)
    payload.setdefault("title", "Praktinė laboratorija")
    payload.setdefault("intro", "")
    payload.setdefault("references", [])
    return payload


@lru_cache(maxsize=None)
def _load(path: Path) -> dict | None:
    if not path.exists():
        return None
    return _validate(json.loads(path.read_text(encoding="utf-8")), path)


def get_activities(course_slug: str, lesson_slug: str, lang: str) -> dict | None:
    """Return localized activities when available, then fall back to Lithuanian."""
    filename = f"{lesson_slug}.activities.json"
    if lang != "lt":
        overlay = _load(COURSE_I18N_DIR / lang / course_slug / filename)
        if overlay is not None:
            return overlay
    return _load(COURSES_DIR / course_slug / filename)
