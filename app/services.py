"""Domain logic: markdown rendering, lesson access rules, progress, usage limits."""
from __future__ import annotations

from datetime import datetime, timezone

import markdown as md
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.config import settings
from app.models import (
    Course,
    DailyUsage,
    Lesson,
    LessonProgress,
    User,
)

# ---------------------------------------------------------------------------
# Markdown rendering (with syntax highlighting)
# ---------------------------------------------------------------------------

_MD_EXTENSIONS = [
    "fenced_code",
    "codehilite",
    "tables",
    "toc",
    "sane_lists",
    "nl2br",
    "md_in_html",
]
_MD_CONFIG = {
    "codehilite": {"guess_lang": False, "css_class": "codehilite"},
}


def render_markdown(text: str) -> str:
    return md.markdown(text, extensions=_MD_EXTENSIONS, extension_configs=_MD_CONFIG)


# ---------------------------------------------------------------------------
# Lesson access control
# ---------------------------------------------------------------------------


def lesson_index(lesson: Lesson, course: Course) -> int:
    """Zero-based position of the lesson within its course."""
    for i, lsn in enumerate(course.lessons):
        if lsn.id == lesson.id:
            return i
    return 0


def can_access_lesson(user: User | None, lesson: Lesson, course: Course) -> bool:
    """Free-tier gating.

    - Anonymous: first lesson only.
    - Registered free: first FREE_LESSONS_PER_COURSE lessons.
    - Subscribed: everything.
    """
    idx = lesson_index(lesson, course)
    if user and user.is_subscribed:
        return True
    if user is None:
        return idx == 0
    return idx < settings.free_lessons_per_course


def free_lessons_count(user: User | None) -> int:
    if user is None:
        return 1
    return settings.free_lessons_per_course


# ---------------------------------------------------------------------------
# Progress
# ---------------------------------------------------------------------------


def completed_lesson_ids(db: Session, user: User, course_id: int | None = None) -> set[int]:
    stmt = (
        select(LessonProgress.lesson_id)
        .join(Lesson, Lesson.id == LessonProgress.lesson_id)
        .where(LessonProgress.user_id == user.id, LessonProgress.completed.is_(True))
    )
    if course_id is not None:
        stmt = stmt.where(Lesson.course_id == course_id)
    return set(db.scalars(stmt).all())


def course_progress(db: Session, user: User | None, course: Course) -> tuple[int, int, int]:
    """Return (completed, total, percent) for a course."""
    total = len(course.lessons)
    if not user or total == 0:
        return 0, total, 0
    done = len(completed_lesson_ids(db, user, course.id))
    percent = round(done / total * 100)
    return done, total, percent


def mark_lesson_complete(db: Session, user: User, lesson: Lesson) -> None:
    existing = db.scalar(
        select(LessonProgress).where(
            LessonProgress.user_id == user.id, LessonProgress.lesson_id == lesson.id
        )
    )
    if existing is None:
        db.add(LessonProgress(user_id=user.id, lesson_id=lesson.id, completed=True))
        db.commit()


# ---------------------------------------------------------------------------
# Daily AI usage limits
# ---------------------------------------------------------------------------


def _today():
    return datetime.now(timezone.utc).date()


def daily_limit(user: User) -> int:
    return settings.paid_daily_ai_messages if user.is_subscribed else settings.free_daily_ai_messages


def get_usage(db: Session, user: User) -> DailyUsage:
    today = _today()
    usage = db.scalar(
        select(DailyUsage).where(DailyUsage.user_id == user.id, DailyUsage.day == today)
    )
    if usage is None:
        usage = DailyUsage(user_id=user.id, day=today, ai_messages=0)
        db.add(usage)
        db.commit()
        db.refresh(usage)
    return usage


def ai_messages_remaining(db: Session, user: User) -> int:
    usage = get_usage(db, user)
    return max(0, daily_limit(user) - usage.ai_messages)


def increment_ai_usage(db: Session, user: User) -> None:
    usage = get_usage(db, user)
    usage.ai_messages += 1
    db.commit()
