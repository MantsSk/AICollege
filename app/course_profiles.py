"""Optional presentation metadata for mission-first courses.

Traditional courses need only ``course.yml`` and lesson markdown. Courses that
use the studio experience can additionally provide ``course.lab.json``. Keeping
this information beside the content lets future code, automation, and smart-home
labs share the same platform without adding a database column for every format.
"""
from __future__ import annotations

import json
from functools import lru_cache

from app.content import COURSES_DIR


@lru_cache(maxsize=None)
def get_course_profile(course_slug: str) -> dict:
    path = COURSES_DIR / course_slug / "course.lab.json"
    if not path.exists():
        return {}
    profile = json.loads(path.read_text(encoding="utf-8"))
    profile.setdefault("skills", [])
    profile.setdefault("outcomes", [])
    profile.setdefault("lessons", {})
    return profile


def get_lesson_profile(course_slug: str, lesson_slug: str) -> dict:
    return get_course_profile(course_slug).get("lessons", {}).get(lesson_slug, {})
