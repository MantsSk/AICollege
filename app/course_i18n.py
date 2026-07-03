"""Localized course display overlays.

The database remains the canonical source for slugs, IDs, progress, and access
rules. English display content is read from file overlays so the schema does
not need language-specific columns.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from types import SimpleNamespace

from app.content import CourseDir, load_courses

COURSE_I18N_DIR = Path(__file__).resolve().parent.parent / "courses_i18n"


@lru_cache(maxsize=None)
def _localized_courses(lang: str) -> dict[str, CourseDir]:
    if lang == "lt":
        return {}
    return {course.slug: course for course in load_courses(COURSE_I18N_DIR / lang)}


def localize_course(course, lang: str):
    localized = _localized_courses(lang).get(course.slug)
    if localized is None:
        return course

    lesson_overlays = {lesson.slug: lesson for lesson in localized.lessons}
    lessons = []
    for lesson in course.lessons:
        overlay = lesson_overlays.get(lesson.slug)
        lessons.append(
            SimpleNamespace(
                id=lesson.id,
                slug=lesson.slug,
                course_id=lesson.course_id,
                title=overlay.title if overlay else lesson.title,
                module=overlay.module if overlay else lesson.module,
                content_md=overlay.content_md if overlay else lesson.content_md,
                order=lesson.order,
            )
        )

    return SimpleNamespace(
        id=course.id,
        slug=course.slug,
        title=localized.title,
        description=localized.description,
        order=course.order,
        lessons=lessons,
    )


def localize_courses(courses, lang: str):
    return [localize_course(course, lang) for course in courses]
